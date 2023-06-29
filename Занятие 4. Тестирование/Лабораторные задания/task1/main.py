class Figure:
    def __init__(self, colour):
        self._colour = colour
        self._sketched = False

    @property
    def colour(self):
        return self._colour

    @property
    def sketched(self):
        return self._sketched


class Rectangle(Figure):
    def __init__(self, colour, width, height):
        super().__init__(colour)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._width = value
        else:
            raise ValueError("Значение ширины должно быть положительным числом")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._height = value
        else:
            raise ValueError("Значение высоты должно быть положительным числом")

    def rectangle_area(self):
        return self._width * self._height

    @staticmethod
    def is_square(width, height):
        return width == height

    @classmethod
    def create_square(cls, side_length):
        return cls("brown", side_length, side_length)


if __name__ == "__main__":
    figure = Figure("red")
    print(figure.colour)
    print(figure.sketched)

    rectangle = Rectangle("yellow", 6, 9)
    print(rectangle.width)
    print(rectangle.height)
    print(rectangle.colour)
    print(rectangle.sketched)
    print(rectangle.rectangle_area())

    rectangle.width = 8
    print(rectangle.rectangle_area())

    square = Rectangle.create_square(5)
    print(square.width)
    print(square.height)
    print(square.is_square(square.width, square.height))
    pass
