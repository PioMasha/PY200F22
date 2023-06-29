import unittest
from main import Rectangle  # импортируем то, что будем тестировать


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle = Rectangle("yellow", 6, 9)
        self.assertEqual(rectangle.rectangle_area(), 54)  # add assertion here

    def test_create_square(self):
        square = Rectangle.create_square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.is_square(square.width, square.height))


if __name__ == '__main__':
    unittest.main()
