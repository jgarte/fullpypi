# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dep_extraction/dep_meta.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dep_extraction/dep_meta.proto',
  package='',
  serialized_pb='\n\x1d\x64\x65p_extraction/dep_meta.proto\"\xd2\x01\n\x07\x44\x65pMeta\x12\x10\n\x08provides\x18\x01 \x03(\t\x12\x14\n\x0c\x64\x65pends_full\x18\x02 \x03(\t\x12!\n\x19\x64\x65pends_remove_py2_stdlib\x18\x03 \x03(\t\x12!\n\x19\x64\x65pends_remove_py3_stdlib\x18\x04 \x03(\t\x12\x14\n\x0crequires_txt\x18\x05 \x03(\t\x12\x18\n\x10requirements_txt\x18\x08 \x03(\t\x12\x1c\n\x14heuristic_setup_deps\x18\x06 \x03(\t\x12\x0b\n\x03log\x18\x07 \x03(\t\"8\n\x05SDist\x12\x11\n\tpypi_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\x1b\n\nKnownNames\x12\r\n\x05names\x18\x01 \x03(\t')




_DEPMETA = _descriptor.Descriptor(
  name='DepMeta',
  full_name='DepMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provides', full_name='DepMeta.provides', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depends_full', full_name='DepMeta.depends_full', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depends_remove_py2_stdlib', full_name='DepMeta.depends_remove_py2_stdlib', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depends_remove_py3_stdlib', full_name='DepMeta.depends_remove_py3_stdlib', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requires_txt', full_name='DepMeta.requires_txt', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requirements_txt', full_name='DepMeta.requirements_txt', index=5,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heuristic_setup_deps', full_name='DepMeta.heuristic_setup_deps', index=6,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log', full_name='DepMeta.log', index=7,
      number=7, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=34,
  serialized_end=244,
)


_SDIST = _descriptor.Descriptor(
  name='SDist',
  full_name='SDist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pypi_name', full_name='SDist.pypi_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='SDist.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SDist.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=246,
  serialized_end=302,
)


_KNOWNNAMES = _descriptor.Descriptor(
  name='KnownNames',
  full_name='KnownNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='KnownNames.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=304,
  serialized_end=331,
)

DESCRIPTOR.message_types_by_name['DepMeta'] = _DEPMETA
DESCRIPTOR.message_types_by_name['SDist'] = _SDIST
DESCRIPTOR.message_types_by_name['KnownNames'] = _KNOWNNAMES

class DepMeta(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEPMETA

  # @@protoc_insertion_point(class_scope:DepMeta)

class SDist(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SDIST

  # @@protoc_insertion_point(class_scope:SDist)

class KnownNames(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KNOWNNAMES

  # @@protoc_insertion_point(class_scope:KnownNames)


# @@protoc_insertion_point(module_scope)
