# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class BigTableRowKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sha1Prefix = ... # type: typing___Text
    entityKey = ... # type: typing___Text
    reversedMillis = ... # type: typing___Text

    def __init__(self,
        *,
        sha1Prefix : typing___Optional[typing___Text] = None,
        entityKey : typing___Optional[typing___Text] = None,
        reversedMillis : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BigTableRowKey: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entityKey",u"reversedMillis",u"sha1Prefix"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entityKey",b"entityKey",u"reversedMillis",b"reversedMillis",u"sha1Prefix",b"sha1Prefix"]) -> None: ...