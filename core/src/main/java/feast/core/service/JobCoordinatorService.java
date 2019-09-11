package feast.core.service;

import com.google.common.base.Strings;
import feast.core.FeatureSetProto;
import feast.core.FeatureSetProto.FeatureSetSpec;
import feast.core.SourceProto.SourceType;
import feast.core.StoreProto;
import feast.core.config.ImportJobDefaults;
import feast.core.dao.JobInfoRepository;
import feast.core.exception.JobExecutionException;
import feast.core.exception.RetrievalException;
import feast.core.job.JobManager;
import feast.core.log.Action;
import feast.core.log.AuditLogger;
import feast.core.log.Resource;
import feast.core.model.FeatureSet;
import feast.core.model.JobInfo;
import feast.core.model.JobStatus;
import feast.core.model.Store;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class JobCoordinatorService {

  private JobInfoRepository jobInfoRepository;
  private JobManager jobManager;
  private ImportJobDefaults defaults;

  @Autowired
  public JobCoordinatorService(
      JobInfoRepository jobInfoRepository,
      JobManager jobManager,
      ImportJobDefaults defaults) {
    this.jobInfoRepository = jobInfoRepository;
    this.jobManager = jobManager;
    this.defaults = defaults;
  }

  /**
   * Start or update a job given the list of FeatureSets to populate and the store to sink to. If
   * there has been no change in the
   */
  public JobInfo startOrUpdateJob(List<FeatureSetSpec> featureSetSpecs, StoreProto.Store store) {
    String featureSetName = featureSetSpecs.get(0).getName();
    Optional<JobInfo> job = getJob(featureSetName, store.getName());
    if (job.isPresent()) {
      Set<String> existingFeatureSetsPopulatedByJob = job.get()
          .getFeatureSets()
          .stream()
          .map(FeatureSet::getId)
          .collect(Collectors.toSet());
      Set<String> newFeatureSetsPopulatedByJob = featureSetSpecs.stream()
          .map(fs -> fs.getName() + ":" + fs.getVersion())
          .collect(Collectors.toSet());
      if (existingFeatureSetsPopulatedByJob.size() == newFeatureSetsPopulatedByJob.size()
          && existingFeatureSetsPopulatedByJob.containsAll(newFeatureSetsPopulatedByJob)) {
        return job.get();
      } else {
        return updateJob(job.get(), featureSetSpecs, store);
      }
    } else {
      return startJob(createJobId(featureSetName, store.getName()), featureSetSpecs,
          store);
    }
  }

  /**
   * Get the non-terminal job associated with the given featureSet name and store name, if any.
   */
  private Optional<JobInfo> getJob(String featureSetName, String storeName) {
    List<JobInfo> jobs = jobInfoRepository
        .findByFeatureSetsNameAndStoreName(featureSetName, storeName);
    switch (jobs.size()) {
      case 0:
        return Optional.empty();
      case 1:
        return Optional.of(jobs.get(0));
      default:
        return jobs.stream()
            .filter(job -> job.getStatus().equals(JobStatus.RUNNING))
            .findFirst();
    }
  }

  /**
   * Start or update the job to ingest data to the sink.
   */
  private JobInfo startJob(String jobId, List<FeatureSetSpec> featureSetSpecs,
      StoreProto.Store sinkSpec) {
    try {

      AuditLogger.log(
          Resource.JOB,
          jobId,
          Action.SUBMIT,
          "Building graph and submitting to %s",
          defaults.getRunner());

      String extId = jobManager.startJob(jobId, featureSetSpecs, sinkSpec);
      if (extId.isEmpty()) {
        throw new RuntimeException(
            String.format("Could not submit job: \n%s", "unable to retrieve job external id"));
      }

      AuditLogger.log(
          Resource.JOB,
          jobId,
          Action.STATUS_CHANGE,
          "Job submitted to runner %s with ext id %s.",
          defaults.getRunner(),
          extId);
      SourceType sourceType = featureSetSpecs.get(0).getSource().getType();
      List<FeatureSet> featureSets = new ArrayList<>();
      for (FeatureSetSpec featureSetSpec : featureSetSpecs) {
        FeatureSet featureSet = new FeatureSet();
        featureSet.setId(featureSetSpec.getName() + ":" + featureSetSpec.getVersion());
        featureSets.add(featureSet);
      }
      JobInfo jobInfo = new JobInfo(jobId, extId, sourceType, defaults.getRunner(),
          Store.fromProto(sinkSpec), featureSets, JobStatus.RUNNING);
      return jobInfoRepository.save(jobInfo);
    } catch (Exception e) {
      updateJobStatus(jobId, JobStatus.ERROR);
      AuditLogger.log(
          Resource.JOB,
          jobId,
          Action.STATUS_CHANGE,
          "Job failed to be submitted to runner %s. Job status changed to ERROR.",
          defaults.getRunner());
      throw new JobExecutionException(String.format("Error running ingestion job: %s", e), e);
    }
  }

  /**
   * Update the given job
   */
  private JobInfo updateJob(JobInfo jobInfo, List<FeatureSetSpec> featureSetSpecs,
      StoreProto.Store store) {
    jobInfo.setFeatureSets(featureSetSpecs.stream()
        .map(spec -> FeatureSet.fromProto(spec))
        .collect(Collectors.toList()));
    jobInfo.setStore(Store.fromProto(store));
    String extId = jobManager.updateJob(jobInfo);
    jobInfo.setExtId(extId);
    return jobInfoRepository.save(jobInfo);
  }

  /**
   * Drain the given job. If this is successful, the job will start the draining process. When the
   * draining process is complete, the job will be cleaned up and removed.
   *
   * <p>Batch jobs will be cancelled, as draining these jobs is not supported by beam.
   *
   * @param id feast-internal id of a job
   */
  public void abortJob(String id) {
    Optional<JobInfo> jobOptional = jobInfoRepository.findById(id);
    if (!jobOptional.isPresent()) {
      throw new RetrievalException(Strings.lenientFormat("Unable to retrieve job with id %s", id));
    }
    JobInfo job = jobOptional.get();
    if (JobStatus.getTerminalState().contains(job.getStatus())) {
      throw new IllegalStateException("Unable to stop job already in terminal state");
    }
    jobManager.abortJob(job.getExtId());
    job.setStatus(JobStatus.ABORTING);

    AuditLogger.log(Resource.JOB, id, Action.ABORT, "Triggering draining of job");
    jobInfoRepository.saveAndFlush(job);
  }

  /**
   * Update a given job's status
   */
  public void updateJobStatus(String jobId, JobStatus status) {
    Optional<JobInfo> jobRecordOptional = jobInfoRepository.findById(jobId);
    if (jobRecordOptional.isPresent()) {
      JobInfo jobRecord = jobRecordOptional.get();
      jobRecord.setStatus(status);
      jobInfoRepository.save(jobRecord);
    }
  }

  public String createJobId(String featureSetName, String storeName) {
    String dateSuffix = String.valueOf(Instant.now().toEpochMilli());
    return String.format("%s-to-%s", featureSetName, storeName) + dateSuffix;
  }
}