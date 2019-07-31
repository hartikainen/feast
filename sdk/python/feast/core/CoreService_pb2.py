# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/CoreService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.specs import EntitySpec_pb2 as feast_dot_specs_dot_EntitySpec__pb2
from feast.specs import FeatureGroupSpec_pb2 as feast_dot_specs_dot_FeatureGroupSpec__pb2
from feast.specs import FeatureSpec_pb2 as feast_dot_specs_dot_FeatureSpec__pb2
from feast.specs import StorageSpec_pb2 as feast_dot_specs_dot_StorageSpec__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/CoreService.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=_b('\n\nfeast.coreB\020CoreServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/core'),
  serialized_pb=_b('\n\x1c\x66\x65\x61st/core/CoreService.proto\x12\nfeast.core\x1a\x1c\x66\x65\x61st/specs/EntitySpec.proto\x1a\"feast/specs/FeatureGroupSpec.proto\x1a\x1d\x66\x65\x61st/specs/FeatureSpec.proto\x1a\x1d\x66\x65\x61st/specs/StorageSpec.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcc\t\n\x10\x43oreServiceTypes\x1a!\n\x12GetEntitiesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a@\n\x13GetEntitiesResponse\x12)\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x17.feast.specs.EntitySpec\x1a\x41\n\x14ListEntitiesResponse\x12)\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x17.feast.specs.EntitySpec\x1a!\n\x12GetFeaturesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x41\n\x13GetFeaturesResponse\x12*\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x18.feast.specs.FeatureSpec\x1a\x42\n\x14ListFeaturesResponse\x12*\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x18.feast.specs.FeatureSpec\x1a \n\x11GetStorageRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x44\n\x12GetStorageResponse\x12.\n\x0cstorageSpecs\x18\x01 \x03(\x0b\x32\x18.feast.specs.StorageSpec\x1a\x45\n\x13ListStorageResponse\x12.\n\x0cstorageSpecs\x18\x01 \x03(\x0b\x32\x18.feast.specs.StorageSpec\x1a)\n\x13\x41pplyEntityResponse\x12\x12\n\nentityName\x18\x01 \x01(\t\x1a)\n\x14\x41pplyFeatureResponse\x12\x11\n\tfeatureId\x18\x01 \x01(\t\x1a\x33\n\x19\x41pplyFeatureGroupResponse\x12\x16\n\x0e\x66\x65\x61tureGroupId\x18\x01 \x01(\t\x1a\x81\x01\n\x13GetUploadUrlRequest\x12K\n\x08\x66ileType\x18\x01 \x01(\x0e\x32\x39.feast.core.CoreServiceTypes.GetUploadUrlRequest.FileType\"\x1d\n\x08\x46ileType\x12\x07\n\x03\x43SV\x10\x00\x12\x08\n\x04JSON\x10\x01\x1a\xca\x01\n\x14GetUploadUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12P\n\nhttpMethod\x18\x02 \x01(\x0e\x32<.feast.core.CoreServiceTypes.GetUploadUrlResponse.HttpMethod\x12.\n\nexpiration\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04path\x18\x04 \x01(\t\"\x15\n\nHttpMethod\x12\x07\n\x03PUT\x10\x00\x1a\x46\n\x14\x41pplyFeaturesRequest\x12.\n\x0c\x66\x65\x61tureSpecs\x18\x01 \x03(\x0b\x32\x18.feast.specs.FeatureSpec\x1a+\n\x15\x41pplyFeaturesResponse\x12\x12\n\nfeatureIds\x18\x01 \x03(\t\x1a%\n\x0fGetTopicRequest\x12\x12\n\nentityName\x18\x01 \x01(\t\x1a?\n\x10GetTopicResponse\x12\x18\n\x10messageBrokerURI\x18\x01 \x01(\t\x12\x11\n\ttopicName\x18\x02 \x01(\t2\xf2\t\n\x0b\x43oreService\x12p\n\x0bGetEntities\x12/.feast.core.CoreServiceTypes.GetEntitiesRequest\x1a\x30.feast.core.CoreServiceTypes.GetEntitiesResponse\x12Y\n\x0cListEntities\x12\x16.google.protobuf.Empty\x1a\x31.feast.core.CoreServiceTypes.ListEntitiesResponse\x12r\n\nGetStorage\x12..feast.core.CoreServiceTypes.GetStorageRequest\x1a/.feast.core.CoreServiceTypes.GetStorageResponse\"\x03\x88\x02\x01\x12\\\n\x0bListStorage\x12\x16.google.protobuf.Empty\x1a\x30.feast.core.CoreServiceTypes.ListStorageResponse\"\x03\x88\x02\x01\x12p\n\x0bGetFeatures\x12/.feast.core.CoreServiceTypes.GetFeaturesRequest\x1a\x30.feast.core.CoreServiceTypes.GetFeaturesResponse\x12Y\n\x0cListFeatures\x12\x16.google.protobuf.Empty\x1a\x31.feast.core.CoreServiceTypes.ListFeaturesResponse\x12[\n\x0c\x41pplyFeature\x12\x18.feast.specs.FeatureSpec\x1a\x31.feast.core.CoreServiceTypes.ApplyFeatureResponse\x12v\n\rApplyFeatures\x12\x31.feast.core.CoreServiceTypes.ApplyFeaturesRequest\x1a\x32.feast.core.CoreServiceTypes.ApplyFeaturesResponse\x12j\n\x11\x41pplyFeatureGroup\x12\x1d.feast.specs.FeatureGroupSpec\x1a\x36.feast.core.CoreServiceTypes.ApplyFeatureGroupResponse\x12X\n\x0b\x41pplyEntity\x12\x17.feast.specs.EntitySpec\x1a\x30.feast.core.CoreServiceTypes.ApplyEntityResponse\x12g\n\x08GetTopic\x12,.feast.core.CoreServiceTypes.GetTopicRequest\x1a-.feast.core.CoreServiceTypes.GetTopicResponse\x12s\n\x0cGetUploadUrl\x12\x30.feast.core.CoreServiceTypes.GetUploadUrlRequest\x1a\x31.feast.core.CoreServiceTypes.GetUploadUrlResponseBU\n\nfeast.coreB\x10\x43oreServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/coreb\x06proto3')
  ,
  dependencies=[feast_dot_specs_dot_EntitySpec__pb2.DESCRIPTOR,feast_dot_specs_dot_FeatureGroupSpec__pb2.DESCRIPTOR,feast_dot_specs_dot_FeatureSpec__pb2.DESCRIPTOR,feast_dot_specs_dot_StorageSpec__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_CORESERVICETYPES_GETUPLOADURLREQUEST_FILETYPE = _descriptor.EnumDescriptor(
  name='FileType',
  full_name='feast.core.CoreServiceTypes.GetUploadUrlRequest.FileType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CSV', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1008,
  serialized_end=1037,
)
_sym_db.RegisterEnumDescriptor(_CORESERVICETYPES_GETUPLOADURLREQUEST_FILETYPE)

_CORESERVICETYPES_GETUPLOADURLRESPONSE_HTTPMETHOD = _descriptor.EnumDescriptor(
  name='HttpMethod',
  full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse.HttpMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUT', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1221,
  serialized_end=1242,
)
_sym_db.RegisterEnumDescriptor(_CORESERVICETYPES_GETUPLOADURLRESPONSE_HTTPMETHOD)


_CORESERVICETYPES_GETENTITIESREQUEST = _descriptor.Descriptor(
  name='GetEntitiesRequest',
  full_name='feast.core.CoreServiceTypes.GetEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetEntitiesRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=288,
)

_CORESERVICETYPES_GETENTITIESRESPONSE = _descriptor.Descriptor(
  name='GetEntitiesResponse',
  full_name='feast.core.CoreServiceTypes.GetEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.CoreServiceTypes.GetEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=354,
)

_CORESERVICETYPES_LISTENTITIESRESPONSE = _descriptor.Descriptor(
  name='ListEntitiesResponse',
  full_name='feast.core.CoreServiceTypes.ListEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.CoreServiceTypes.ListEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=421,
)

_CORESERVICETYPES_GETFEATURESREQUEST = _descriptor.Descriptor(
  name='GetFeaturesRequest',
  full_name='feast.core.CoreServiceTypes.GetFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetFeaturesRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=456,
)

_CORESERVICETYPES_GETFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetFeaturesResponse',
  full_name='feast.core.CoreServiceTypes.GetFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.CoreServiceTypes.GetFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=523,
)

_CORESERVICETYPES_LISTFEATURESRESPONSE = _descriptor.Descriptor(
  name='ListFeaturesResponse',
  full_name='feast.core.CoreServiceTypes.ListFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.CoreServiceTypes.ListFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=591,
)

_CORESERVICETYPES_GETSTORAGEREQUEST = _descriptor.Descriptor(
  name='GetStorageRequest',
  full_name='feast.core.CoreServiceTypes.GetStorageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetStorageRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=625,
)

_CORESERVICETYPES_GETSTORAGERESPONSE = _descriptor.Descriptor(
  name='GetStorageResponse',
  full_name='feast.core.CoreServiceTypes.GetStorageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storageSpecs', full_name='feast.core.CoreServiceTypes.GetStorageResponse.storageSpecs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=695,
)

_CORESERVICETYPES_LISTSTORAGERESPONSE = _descriptor.Descriptor(
  name='ListStorageResponse',
  full_name='feast.core.CoreServiceTypes.ListStorageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storageSpecs', full_name='feast.core.CoreServiceTypes.ListStorageResponse.storageSpecs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=766,
)

_CORESERVICETYPES_APPLYENTITYRESPONSE = _descriptor.Descriptor(
  name='ApplyEntityResponse',
  full_name='feast.core.CoreServiceTypes.ApplyEntityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityName', full_name='feast.core.CoreServiceTypes.ApplyEntityResponse.entityName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=809,
)

_CORESERVICETYPES_APPLYFEATURERESPONSE = _descriptor.Descriptor(
  name='ApplyFeatureResponse',
  full_name='feast.core.CoreServiceTypes.ApplyFeatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureId', full_name='feast.core.CoreServiceTypes.ApplyFeatureResponse.featureId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=811,
  serialized_end=852,
)

_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE = _descriptor.Descriptor(
  name='ApplyFeatureGroupResponse',
  full_name='feast.core.CoreServiceTypes.ApplyFeatureGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureGroupId', full_name='feast.core.CoreServiceTypes.ApplyFeatureGroupResponse.featureGroupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=905,
)

_CORESERVICETYPES_GETUPLOADURLREQUEST = _descriptor.Descriptor(
  name='GetUploadUrlRequest',
  full_name='feast.core.CoreServiceTypes.GetUploadUrlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileType', full_name='feast.core.CoreServiceTypes.GetUploadUrlRequest.fileType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CORESERVICETYPES_GETUPLOADURLREQUEST_FILETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=908,
  serialized_end=1037,
)

_CORESERVICETYPES_GETUPLOADURLRESPONSE = _descriptor.Descriptor(
  name='GetUploadUrlResponse',
  full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='httpMethod', full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse.httpMethod', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse.expiration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='feast.core.CoreServiceTypes.GetUploadUrlResponse.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CORESERVICETYPES_GETUPLOADURLRESPONSE_HTTPMETHOD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1242,
)

_CORESERVICETYPES_APPLYFEATURESREQUEST = _descriptor.Descriptor(
  name='ApplyFeaturesRequest',
  full_name='feast.core.CoreServiceTypes.ApplyFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureSpecs', full_name='feast.core.CoreServiceTypes.ApplyFeaturesRequest.featureSpecs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1244,
  serialized_end=1314,
)

_CORESERVICETYPES_APPLYFEATURESRESPONSE = _descriptor.Descriptor(
  name='ApplyFeaturesResponse',
  full_name='feast.core.CoreServiceTypes.ApplyFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureIds', full_name='feast.core.CoreServiceTypes.ApplyFeaturesResponse.featureIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1316,
  serialized_end=1359,
)

_CORESERVICETYPES_GETTOPICREQUEST = _descriptor.Descriptor(
  name='GetTopicRequest',
  full_name='feast.core.CoreServiceTypes.GetTopicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityName', full_name='feast.core.CoreServiceTypes.GetTopicRequest.entityName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1361,
  serialized_end=1398,
)

_CORESERVICETYPES_GETTOPICRESPONSE = _descriptor.Descriptor(
  name='GetTopicResponse',
  full_name='feast.core.CoreServiceTypes.GetTopicResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageBrokerURI', full_name='feast.core.CoreServiceTypes.GetTopicResponse.messageBrokerURI', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='feast.core.CoreServiceTypes.GetTopicResponse.topicName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1463,
)

_CORESERVICETYPES = _descriptor.Descriptor(
  name='CoreServiceTypes',
  full_name='feast.core.CoreServiceTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_CORESERVICETYPES_GETENTITIESREQUEST, _CORESERVICETYPES_GETENTITIESRESPONSE, _CORESERVICETYPES_LISTENTITIESRESPONSE, _CORESERVICETYPES_GETFEATURESREQUEST, _CORESERVICETYPES_GETFEATURESRESPONSE, _CORESERVICETYPES_LISTFEATURESRESPONSE, _CORESERVICETYPES_GETSTORAGEREQUEST, _CORESERVICETYPES_GETSTORAGERESPONSE, _CORESERVICETYPES_LISTSTORAGERESPONSE, _CORESERVICETYPES_APPLYENTITYRESPONSE, _CORESERVICETYPES_APPLYFEATURERESPONSE, _CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE, _CORESERVICETYPES_GETUPLOADURLREQUEST, _CORESERVICETYPES_GETUPLOADURLRESPONSE, _CORESERVICETYPES_APPLYFEATURESREQUEST, _CORESERVICETYPES_APPLYFEATURESRESPONSE, _CORESERVICETYPES_GETTOPICREQUEST, _CORESERVICETYPES_GETTOPICRESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=1463,
)

_CORESERVICETYPES_GETENTITIESREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETENTITIESRESPONSE.fields_by_name['entities'].message_type = feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC
_CORESERVICETYPES_GETENTITIESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTENTITIESRESPONSE.fields_by_name['entities'].message_type = feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC
_CORESERVICETYPES_LISTENTITIESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETFEATURESREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETFEATURESRESPONSE.fields_by_name['features'].message_type = feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC
_CORESERVICETYPES_GETFEATURESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTFEATURESRESPONSE.fields_by_name['features'].message_type = feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC
_CORESERVICETYPES_LISTFEATURESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETSTORAGEREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETSTORAGERESPONSE.fields_by_name['storageSpecs'].message_type = feast_dot_specs_dot_StorageSpec__pb2._STORAGESPEC
_CORESERVICETYPES_GETSTORAGERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTSTORAGERESPONSE.fields_by_name['storageSpecs'].message_type = feast_dot_specs_dot_StorageSpec__pb2._STORAGESPEC
_CORESERVICETYPES_LISTSTORAGERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYENTITYRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYFEATURERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETUPLOADURLREQUEST.fields_by_name['fileType'].enum_type = _CORESERVICETYPES_GETUPLOADURLREQUEST_FILETYPE
_CORESERVICETYPES_GETUPLOADURLREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETUPLOADURLREQUEST_FILETYPE.containing_type = _CORESERVICETYPES_GETUPLOADURLREQUEST
_CORESERVICETYPES_GETUPLOADURLRESPONSE.fields_by_name['httpMethod'].enum_type = _CORESERVICETYPES_GETUPLOADURLRESPONSE_HTTPMETHOD
_CORESERVICETYPES_GETUPLOADURLRESPONSE.fields_by_name['expiration'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CORESERVICETYPES_GETUPLOADURLRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETUPLOADURLRESPONSE_HTTPMETHOD.containing_type = _CORESERVICETYPES_GETUPLOADURLRESPONSE
_CORESERVICETYPES_APPLYFEATURESREQUEST.fields_by_name['featureSpecs'].message_type = feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC
_CORESERVICETYPES_APPLYFEATURESREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYFEATURESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETTOPICREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETTOPICRESPONSE.containing_type = _CORESERVICETYPES
DESCRIPTOR.message_types_by_name['CoreServiceTypes'] = _CORESERVICETYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoreServiceTypes = _reflection.GeneratedProtocolMessageType('CoreServiceTypes', (_message.Message,), {

  'GetEntitiesRequest' : _reflection.GeneratedProtocolMessageType('GetEntitiesRequest', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETENTITIESREQUEST,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetEntitiesRequest)
    })
  ,

  'GetEntitiesResponse' : _reflection.GeneratedProtocolMessageType('GetEntitiesResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETENTITIESRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetEntitiesResponse)
    })
  ,

  'ListEntitiesResponse' : _reflection.GeneratedProtocolMessageType('ListEntitiesResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_LISTENTITIESRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListEntitiesResponse)
    })
  ,

  'GetFeaturesRequest' : _reflection.GeneratedProtocolMessageType('GetFeaturesRequest', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETFEATURESREQUEST,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetFeaturesRequest)
    })
  ,

  'GetFeaturesResponse' : _reflection.GeneratedProtocolMessageType('GetFeaturesResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETFEATURESRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetFeaturesResponse)
    })
  ,

  'ListFeaturesResponse' : _reflection.GeneratedProtocolMessageType('ListFeaturesResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_LISTFEATURESRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListFeaturesResponse)
    })
  ,

  'GetStorageRequest' : _reflection.GeneratedProtocolMessageType('GetStorageRequest', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETSTORAGEREQUEST,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetStorageRequest)
    })
  ,

  'GetStorageResponse' : _reflection.GeneratedProtocolMessageType('GetStorageResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETSTORAGERESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetStorageResponse)
    })
  ,

  'ListStorageResponse' : _reflection.GeneratedProtocolMessageType('ListStorageResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_LISTSTORAGERESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListStorageResponse)
    })
  ,

  'ApplyEntityResponse' : _reflection.GeneratedProtocolMessageType('ApplyEntityResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_APPLYENTITYRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyEntityResponse)
    })
  ,

  'ApplyFeatureResponse' : _reflection.GeneratedProtocolMessageType('ApplyFeatureResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_APPLYFEATURERESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeatureResponse)
    })
  ,

  'ApplyFeatureGroupResponse' : _reflection.GeneratedProtocolMessageType('ApplyFeatureGroupResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeatureGroupResponse)
    })
  ,

  'GetUploadUrlRequest' : _reflection.GeneratedProtocolMessageType('GetUploadUrlRequest', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETUPLOADURLREQUEST,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetUploadUrlRequest)
    })
  ,

  'GetUploadUrlResponse' : _reflection.GeneratedProtocolMessageType('GetUploadUrlResponse', (_message.Message,), {
    'DESCRIPTOR' : _CORESERVICETYPES_GETUPLOADURLRESPONSE,
    '__module__' : 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetUploadUrlResponse)
    })
  ,

  ApplyFeaturesRequest = _reflection.GeneratedProtocolMessageType('ApplyFeaturesRequest', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYFEATURESREQUEST,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeaturesRequest)
    ))
  ,

  ApplyFeaturesResponse = _reflection.GeneratedProtocolMessageType('ApplyFeaturesResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYFEATURESRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeaturesResponse)
    ))
  ,

  GetTopicRequest = _reflection.GeneratedProtocolMessageType('GetTopicRequest', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETTOPICREQUEST,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetTopicRequest)
    ))
  ,

  GetTopicResponse = _reflection.GeneratedProtocolMessageType('GetTopicResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETTOPICRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetTopicResponse)
    ))
  ,
  DESCRIPTOR = _CORESERVICETYPES,
  __module__ = 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes)
  })
_sym_db.RegisterMessage(CoreServiceTypes)
_sym_db.RegisterMessage(CoreServiceTypes.GetEntitiesRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetEntitiesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListEntitiesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetFeaturesRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetFeaturesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListFeaturesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetStorageRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetStorageResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListStorageResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyEntityResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeatureResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeatureGroupResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetUploadUrlRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetUploadUrlResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeaturesRequest)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeaturesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetTopicRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetTopicResponse)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
  name='CoreService',
  full_name='feast.core.CoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1466,
  serialized_end=2732,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetEntities',
    full_name='feast.core.CoreService.GetEntities',
    index=0,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETENTITIESREQUEST,
    output_type=_CORESERVICETYPES_GETENTITIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListEntities',
    full_name='feast.core.CoreService.ListEntities',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTENTITIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStorage',
    full_name='feast.core.CoreService.GetStorage',
    index=2,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETSTORAGEREQUEST,
    output_type=_CORESERVICETYPES_GETSTORAGERESPONSE,
    serialized_options=_b('\210\002\001'),
  ),
  _descriptor.MethodDescriptor(
    name='ListStorage',
    full_name='feast.core.CoreService.ListStorage',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTSTORAGERESPONSE,
    serialized_options=_b('\210\002\001'),
  ),
  _descriptor.MethodDescriptor(
    name='GetFeatures',
    full_name='feast.core.CoreService.GetFeatures',
    index=4,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETFEATURESREQUEST,
    output_type=_CORESERVICETYPES_GETFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFeatures',
    full_name='feast.core.CoreService.ListFeatures',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeature',
    full_name='feast.core.CoreService.ApplyFeature',
    index=6,
    containing_service=None,
    input_type=feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC,
    output_type=_CORESERVICETYPES_APPLYFEATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeatures',
    full_name='feast.core.CoreService.ApplyFeatures',
    index=7,
    containing_service=None,
    input_type=_CORESERVICETYPES_APPLYFEATURESREQUEST,
    output_type=_CORESERVICETYPES_APPLYFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeatureGroup',
    full_name='feast.core.CoreService.ApplyFeatureGroup',
    index=8,
    containing_service=None,
    input_type=feast_dot_specs_dot_FeatureGroupSpec__pb2._FEATUREGROUPSPEC,
    output_type=_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyEntity',
    full_name='feast.core.CoreService.ApplyEntity',
    index=9,
    containing_service=None,
    input_type=feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC,
    output_type=_CORESERVICETYPES_APPLYENTITYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTopic',
    full_name='feast.core.CoreService.GetTopic',
    index=10,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETTOPICREQUEST,
    output_type=_CORESERVICETYPES_GETTOPICRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUploadUrl',
    full_name='feast.core.CoreService.GetUploadUrl',
    index=11,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETUPLOADURLREQUEST,
    output_type=_CORESERVICETYPES_GETUPLOADURLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name['CoreService'] = _CORESERVICE

# @@protoc_insertion_point(module_scope)
