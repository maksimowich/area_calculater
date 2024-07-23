import unittest

from area_calculater import CircleFigure, TriangleFigure


class TestShapeCalculator(unittest.TestCase):

    def test_circle_area(self):
        radius = 5
        expected_area = 78.54
        self.assertAlmostEqual(
            first=CircleFigure(radius).get_area(),
            second=expected_area,
            places=2,
        )

        with self.assertRaises(ValueError):
            CircleFigure(-1)

        with self.assertRaises(ValueError):
            CircleFigure(0)

    def test_triangle_area(self):
        side1, side2, side3 = 3, 4, 5
        expected_area = 6.0
        expected_is_right_triangle = True

        triangle_figure = TriangleFigure(side1, side2, side3)
        area = triangle_figure.get_area()
        is_right_triangle = triangle_figure.is_right_triangle()
        self.assertAlmostEqual(area, expected_area, places=2)
        self.assertEqual(is_right_triangle, expected_is_right_triangle)

        with self.assertRaises(ValueError):
            TriangleFigure(-1, 2, 3)

        with self.assertRaises(ValueError):
            TriangleFigure(1, 1, 10)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            TriangleFigure(1, 1, 10)
