from typing import Any

from sympy.core.relational import Eq, Ne, Relational

allhints = ...

def pdsolve(eq, func=..., hint=..., dict=..., solvefun=..., **kwargs) -> dict[Any, Any] | Any: ...
def classify_pde(eq, func=..., dict=..., *, prep=..., **kwargs): ...
def checkpdesol(pde, sol, func=..., solve_for_func=...) -> Any | tuple[bool, Any]: ...
def pde_1st_linear_constant_coeff_homogeneous(eq, func, order, match, solvefun) -> Eq | Relational | Ne: ...
def pde_1st_linear_constant_coeff(eq, func, order, match, solvefun) -> Eq | Relational | Ne: ...
def pde_1st_linear_variable_coeff(eq, func, order, match, solvefun) -> Eq | Relational | Ne: ...
def pde_separate(eq, fun, sep, strategy=...) -> list[Any] | None: ...
def pde_separate_add(eq, fun, sep) -> list[Any] | None: ...
def pde_separate_mul(eq, fun, sep) -> list[Any] | None: ...
