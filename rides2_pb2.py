# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rides2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0crides2.proto\"a\n\x0cStartRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12\x11\n\tdriver_id\x18\x02 \x01(\t\x12\x15\n\rpassenger_ids\x18\x03 \x03(\t\x12\x17\n\x04type\x18\x04 \x01(\x0e\x32\t.RideType*!\n\x08RideType\x12\x0b\n\x07REGULAR\x10\x00\x12\x08\n\x04POOL\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rides2_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RIDETYPE']._serialized_start=115
  _globals['_RIDETYPE']._serialized_end=148
  _globals['_STARTREQUEST']._serialized_start=16
  _globals['_STARTREQUEST']._serialized_end=113
# @@protoc_insertion_point(module_scope)