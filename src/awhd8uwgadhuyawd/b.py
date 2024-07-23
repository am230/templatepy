from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .a import AType


def b_func(a: AType):
    print(a)
