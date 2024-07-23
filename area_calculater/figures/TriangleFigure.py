import math

from .Figure import Figure


class TriangleFigure(Figure):
    def __init__(
            self,
            side1: float,
            side2: float,
            side3: float,
    ):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("lengths of triangle sides must be positive numbers")
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("triangle with such sides cannot exist")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
