from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any

class OrderedDict(dict[Any, Any]):
    def __init__(self, *args, **kwds) -> None: ...
    def __setitem__(self, key, value, dict_setitem=...) -> None: ...
    def __delitem__(self, key, dict_delitem=...) -> None: ...
    def __iter__(self): ...
    def __reversed__(self) -> Generator[Any, None, None]: ...
    def clear(self) -> None: ...
    def popitem(self, last: bool = ...): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def iterkeys(self): ...
    def itervalues(self) -> Generator[Any, None, None]: ...
    def iteritems(self) -> Generator[Any, None, None]: ...
    def update(*args, **kwds) -> None: ...  # type: ignore[override]
    def pop(self, key, default=...): ...
    def setdefault(self, key, default: Incomplete | None = ...): ...
    def __reduce__(self): ...
    def copy(self): ...
    @classmethod
    def fromkeys(cls, iterable, value: Incomplete | None = ...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
