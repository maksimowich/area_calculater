import math

from .Figure import Figure


class CircleFigure(Figure):
    def __init__(
            self,
            radius: float,
    ):
        if radius <= 0:
            raise ValueError("radius must be positive number")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2
