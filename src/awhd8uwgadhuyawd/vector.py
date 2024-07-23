from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Vector:
    x: float
    y: float

    def __add__(self, other: Vector):
        return Vector(self.x + other.x, self.y + other.y)
