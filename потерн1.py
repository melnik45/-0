# Abstraction
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


# Concrete Abstraction
class Circle(Shape):
    def draw(self):
        print(f"Drawing a Circle with {self.color} color")


class Square(Shape):
    def draw(self):
        print(f"Drawing a Square with {self.color} color")


# Implementation
class Color:
    def apply_color(self):
        pass


# Concrete Implementation
class RedColor(Color):
    def apply_color(self):
        return "Red"


class BlueColor(Color):
    def apply_color(self):
        return "Blue"


# Bridge
class ColoredShape(Shape):
    def __init__(self, shape, color):
        super().__init__(color)
        self.shape = shape

    def draw(self):
        print(f"{self.shape.__class__.__name__} colored with {self.color} color")


# Usage
if __name__ == "__main__":
    red = RedColor()
    blue = BlueColor()

    circle = Circle(red)
    square = Square(blue)

    colored_circle = ColoredShape(circle, red)
    colored_square = ColoredShape(square, blue)

    circle.draw()
    square.draw()

    colored_circle.draw()
    colored_square.draw()
