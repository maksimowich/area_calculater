from area_calculater import CircleFigure, TriangleFigure

radius = 5
circle_area = CircleFigure(radius).get_area()
print(f"Площадь круга с радиусом {radius} равна {circle_area:.2f}")

side1 = 3
side2 = 4
side3 = 5
triangle_area = TriangleFigure(side1, side2, side3).get_area()
print(f"Площадь треугольника со сторонами {side1}, {side2}, {side3} равна {triangle_area:.2f}")
