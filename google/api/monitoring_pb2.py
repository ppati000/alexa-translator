# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/monitoring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/monitoring.proto',
  package='google.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1bgoogle/api/monitoring.proto\x12\ngoogle.api\x1a\x1cgoogle/api/annotations.proto\"\xec\x01\n\nMonitoring\x12K\n\x15producer_destinations\x18\x01 \x03(\x0b\x32,.google.api.Monitoring.MonitoringDestination\x12K\n\x15\x63onsumer_destinations\x18\x02 \x03(\x0b\x32,.google.api.Monitoring.MonitoringDestination\x1a\x44\n\x15MonitoringDestination\x12\x1a\n\x12monitored_resource\x18\x01 \x01(\t\x12\x0f\n\x07metrics\x18\x02 \x03(\tB*\n\x0e\x63om.google.apiB\x0fMonitoringProtoP\x01\xa2\x02\x04GAPIb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MONITORING_MONITORINGDESTINATION = _descriptor.Descriptor(
  name='MonitoringDestination',
  full_name='google.api.Monitoring.MonitoringDestination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monitored_resource', full_name='google.api.Monitoring.MonitoringDestination.monitored_resource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='google.api.Monitoring.MonitoringDestination.metrics', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=310,
)

_MONITORING = _descriptor.Descriptor(
  name='Monitoring',
  full_name='google.api.Monitoring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='producer_destinations', full_name='google.api.Monitoring.producer_destinations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consumer_destinations', full_name='google.api.Monitoring.consumer_destinations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MONITORING_MONITORINGDESTINATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=310,
)

_MONITORING_MONITORINGDESTINATION.containing_type = _MONITORING
_MONITORING.fields_by_name['producer_destinations'].message_type = _MONITORING_MONITORINGDESTINATION
_MONITORING.fields_by_name['consumer_destinations'].message_type = _MONITORING_MONITORINGDESTINATION
DESCRIPTOR.message_types_by_name['Monitoring'] = _MONITORING

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), dict(

  MonitoringDestination = _reflection.GeneratedProtocolMessageType('MonitoringDestination', (_message.Message,), dict(
    DESCRIPTOR = _MONITORING_MONITORINGDESTINATION,
    __module__ = 'google.api.monitoring_pb2'
    # @@protoc_insertion_point(class_scope:google.api.Monitoring.MonitoringDestination)
    ))
  ,
  DESCRIPTOR = _MONITORING,
  __module__ = 'google.api.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Monitoring)
  ))
_sym_db.RegisterMessage(Monitoring)
_sym_db.RegisterMessage(Monitoring.MonitoringDestination)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.google.apiB\017MonitoringProtoP\001\242\002\004GAPI'))
# @@protoc_insertion_point(module_scope)
