# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: utility_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='utility_update.proto',
  package='cilantro',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14utility_update.proto\x12\x08\x63ilantro\"\xc8\x01\n\x0eUtilityMessage\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x0c\n\x04load\x18\x02 \x01(\x02\x12\r\n\x05\x61lloc\x18\x03 \x01(\x02\x12\x0e\n\x06reward\x18\x04 \x01(\x02\x12\r\n\x05sigma\x18\x05 \x01(\x02\x12\x18\n\x10\x65vent_start_time\x18\x06 \x01(\x01\x12\x16\n\x0e\x65vent_end_time\x18\x07 \x01(\x01\x12\r\n\x05\x64\x65\x62ug\x18\x08 \x01(\t\x12\x12\n\nnum_events\x18\t \x01(\x05\x12\x15\n\rnum_successes\x18\n \x01(\x05\"\x1d\n\nUtilityAck\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x32V\n\x10UtilityMessaging\x12\x42\n\x0ePublishUtility\x12\x18.cilantro.UtilityMessage\x1a\x14.cilantro.UtilityAck\"\x00\x62\x06proto3'
)




_UTILITYMESSAGE = _descriptor.Descriptor(
  name='UtilityMessage',
  full_name='cilantro.UtilityMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='cilantro.UtilityMessage.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load', full_name='cilantro.UtilityMessage.load', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alloc', full_name='cilantro.UtilityMessage.alloc', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward', full_name='cilantro.UtilityMessage.reward', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigma', full_name='cilantro.UtilityMessage.sigma', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_start_time', full_name='cilantro.UtilityMessage.event_start_time', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_end_time', full_name='cilantro.UtilityMessage.event_end_time', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug', full_name='cilantro.UtilityMessage.debug', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_events', full_name='cilantro.UtilityMessage.num_events', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_successes', full_name='cilantro.UtilityMessage.num_successes', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=235,
)


_UTILITYACK = _descriptor.Descriptor(
  name='UtilityAck',
  full_name='cilantro.UtilityAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='cilantro.UtilityAck.retcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=237,
  serialized_end=266,
)

DESCRIPTOR.message_types_by_name['UtilityMessage'] = _UTILITYMESSAGE
DESCRIPTOR.message_types_by_name['UtilityAck'] = _UTILITYACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UtilityMessage = _reflection.GeneratedProtocolMessageType('UtilityMessage', (_message.Message,), {
  'DESCRIPTOR' : _UTILITYMESSAGE,
  '__module__' : 'utility_update_pb2'
  # @@protoc_insertion_point(class_scope:cilantro.UtilityMessage)
  })
_sym_db.RegisterMessage(UtilityMessage)

UtilityAck = _reflection.GeneratedProtocolMessageType('UtilityAck', (_message.Message,), {
  'DESCRIPTOR' : _UTILITYACK,
  '__module__' : 'utility_update_pb2'
  # @@protoc_insertion_point(class_scope:cilantro.UtilityAck)
  })
_sym_db.RegisterMessage(UtilityAck)



_UTILITYMESSAGING = _descriptor.ServiceDescriptor(
  name='UtilityMessaging',
  full_name='cilantro.UtilityMessaging',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=268,
  serialized_end=354,
  methods=[
  _descriptor.MethodDescriptor(
    name='PublishUtility',
    full_name='cilantro.UtilityMessaging.PublishUtility',
    index=0,
    containing_service=None,
    input_type=_UTILITYMESSAGE,
    output_type=_UTILITYACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UTILITYMESSAGING)

DESCRIPTOR.services_by_name['UtilityMessaging'] = _UTILITYMESSAGING

# @@protoc_insertion_point(module_scope)
