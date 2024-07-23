from google.protobuf import any_pb2 as _any_pb2
from github.com.openconfig.gnmi.proto.gnmi import gnmi_pb2 as _gnmi_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOPPED: _ClassVar[State]
    INIT: _ClassVar[State]
    RUNNING: _ClassVar[State]
STOPPED: State
INIT: State
RUNNING: State

class Configuration(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _containers.RepeatedCompositeFieldContainer[Config]
    def __init__(self, config: _Optional[_Iterable[_Union[Config, _Mapping]]] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ("target", "port", "seed", "values", "disable_sync", "client_type", "disable_eof", "credentials", "cert", "enable_delay", "custom", "random", "fixed", "tunnel_addr", "tunnel_crt")
    class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRPC: _ClassVar[Config.ClientType]
        STUBBY: _ClassVar[Config.ClientType]
        GRPC_GNMI: _ClassVar[Config.ClientType]
        GRPC_GNMI_PROD: _ClassVar[Config.ClientType]
    GRPC: Config.ClientType
    STUBBY: Config.ClientType
    GRPC_GNMI: Config.ClientType
    GRPC_GNMI_PROD: Config.ClientType
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SYNC_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EOF_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DELAY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_ADDR_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_CRT_FIELD_NUMBER: _ClassVar[int]
    target: str
    port: int
    seed: int
    values: _containers.RepeatedCompositeFieldContainer[Value]
    disable_sync: bool
    client_type: Config.ClientType
    disable_eof: bool
    credentials: Credentials
    cert: bytes
    enable_delay: bool
    custom: _any_pb2.Any
    random: RandomGenerator
    fixed: FixedGenerator
    tunnel_addr: str
    tunnel_crt: str
    def __init__(self, target: _Optional[str] = ..., port: _Optional[int] = ..., seed: _Optional[int] = ..., values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ..., disable_sync: bool = ..., client_type: _Optional[_Union[Config.ClientType, str]] = ..., disable_eof: bool = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ..., cert: _Optional[bytes] = ..., enable_delay: bool = ..., custom: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., random: _Optional[_Union[RandomGenerator, _Mapping]] = ..., fixed: _Optional[_Union[FixedGenerator, _Mapping]] = ..., tunnel_addr: _Optional[str] = ..., tunnel_crt: _Optional[str] = ...) -> None: ...

class FixedGenerator(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[_gnmi_pb2.SubscribeResponse]
    def __init__(self, responses: _Optional[_Iterable[_Union[_gnmi_pb2.SubscribeResponse, _Mapping]]] = ...) -> None: ...

class RandomGenerator(_message.Message):
    __slots__ = ("seed", "values")
    SEED_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    seed: int
    values: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, seed: _Optional[int] = ..., values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class DeleteValue(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Value(_message.Message):
    __slots__ = ("path", "timestamp", "repeat", "seed", "int_value", "double_value", "string_value", "sync", "delete", "bool_value", "uint_value", "string_list_value")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    SYNC_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedScalarFieldContainer[str]
    timestamp: Timestamp
    repeat: int
    seed: int
    int_value: IntValue
    double_value: DoubleValue
    string_value: StringValue
    sync: int
    delete: DeleteValue
    bool_value: BoolValue
    uint_value: UintValue
    string_list_value: StringListValue
    def __init__(self, path: _Optional[_Iterable[str]] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ..., repeat: _Optional[int] = ..., seed: _Optional[int] = ..., int_value: _Optional[_Union[IntValue, _Mapping]] = ..., double_value: _Optional[_Union[DoubleValue, _Mapping]] = ..., string_value: _Optional[_Union[StringValue, _Mapping]] = ..., sync: _Optional[int] = ..., delete: _Optional[_Union[DeleteValue, _Mapping]] = ..., bool_value: _Optional[_Union[BoolValue, _Mapping]] = ..., uint_value: _Optional[_Union[UintValue, _Mapping]] = ..., string_list_value: _Optional[_Union[StringListValue, _Mapping]] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("timestamp", "delta_min", "delta_max")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    delta_min: int
    delta_max: int
    def __init__(self, timestamp: _Optional[int] = ..., delta_min: _Optional[int] = ..., delta_max: _Optional[int] = ...) -> None: ...

class IntValue(_message.Message):
    __slots__ = ("value", "range", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: int
    range: IntRange
    list: IntList
    def __init__(self, value: _Optional[int] = ..., range: _Optional[_Union[IntRange, _Mapping]] = ..., list: _Optional[_Union[IntList, _Mapping]] = ...) -> None: ...

class IntRange(_message.Message):
    __slots__ = ("minimum", "maximum", "delta_min", "delta_max")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    minimum: int
    maximum: int
    delta_min: int
    delta_max: int
    def __init__(self, minimum: _Optional[int] = ..., maximum: _Optional[int] = ..., delta_min: _Optional[int] = ..., delta_max: _Optional[int] = ...) -> None: ...

class IntList(_message.Message):
    __slots__ = ("options", "random")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[int]
    random: bool
    def __init__(self, options: _Optional[_Iterable[int]] = ..., random: bool = ...) -> None: ...

class DoubleValue(_message.Message):
    __slots__ = ("value", "range", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: float
    range: DoubleRange
    list: DoubleList
    def __init__(self, value: _Optional[float] = ..., range: _Optional[_Union[DoubleRange, _Mapping]] = ..., list: _Optional[_Union[DoubleList, _Mapping]] = ...) -> None: ...

class DoubleRange(_message.Message):
    __slots__ = ("minimum", "maximum", "delta_min", "delta_max")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    minimum: float
    maximum: float
    delta_min: float
    delta_max: float
    def __init__(self, minimum: _Optional[float] = ..., maximum: _Optional[float] = ..., delta_min: _Optional[float] = ..., delta_max: _Optional[float] = ...) -> None: ...

class DoubleList(_message.Message):
    __slots__ = ("options", "random")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[float]
    random: bool
    def __init__(self, options: _Optional[_Iterable[float]] = ..., random: bool = ...) -> None: ...

class StringValue(_message.Message):
    __slots__ = ("value", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: str
    list: StringList
    def __init__(self, value: _Optional[str] = ..., list: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("options", "random")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[str]
    random: bool
    def __init__(self, options: _Optional[_Iterable[str]] = ..., random: bool = ...) -> None: ...

class StringListValue(_message.Message):
    __slots__ = ("value", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    list: StringList
    def __init__(self, value: _Optional[_Iterable[str]] = ..., list: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: bool
    list: BoolList
    def __init__(self, value: bool = ..., list: _Optional[_Union[BoolList, _Mapping]] = ...) -> None: ...

class BoolList(_message.Message):
    __slots__ = ("options", "random")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[bool]
    random: bool
    def __init__(self, options: _Optional[_Iterable[bool]] = ..., random: bool = ...) -> None: ...

class UintValue(_message.Message):
    __slots__ = ("value", "range", "list")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    value: int
    range: UintRange
    list: UintList
    def __init__(self, value: _Optional[int] = ..., range: _Optional[_Union[UintRange, _Mapping]] = ..., list: _Optional[_Union[UintList, _Mapping]] = ...) -> None: ...

class UintRange(_message.Message):
    __slots__ = ("minimum", "maximum", "delta_min", "delta_max")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    minimum: int
    maximum: int
    delta_min: int
    delta_max: int
    def __init__(self, minimum: _Optional[int] = ..., maximum: _Optional[int] = ..., delta_min: _Optional[int] = ..., delta_max: _Optional[int] = ...) -> None: ...

class UintList(_message.Message):
    __slots__ = ("options", "random")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[int]
    random: bool
    def __init__(self, options: _Optional[_Iterable[int]] = ..., random: bool = ...) -> None: ...
