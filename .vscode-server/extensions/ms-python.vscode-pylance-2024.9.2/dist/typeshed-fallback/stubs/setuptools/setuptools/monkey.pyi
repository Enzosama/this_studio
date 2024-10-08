from typing import TypeVar

_T = TypeVar("_T")

__all__: list[str] = []

def get_unpatched(item: _T) -> _T: ...
def get_unpatched_class(cls): ...
def patch_all() -> None: ...
def patch_func(replacement, target_mod, func_name) -> None: ...
def get_unpatched_function(candidate): ...
def patch_for_msvc_specialized_compiler(): ...
