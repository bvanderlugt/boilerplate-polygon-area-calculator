class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2) **.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        m = [["*" for x in range(self.width)] for i in range(self.height)]
        m1 = ["".join(k) for k in m]
        m2 = "\n".join(m1)
        m2 += "\n"
        return m2

    def get_amount_inside(self, shape):
        if self.get_area() < shape.get_area():
            return 0
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.height})"

    def __str__(self):
        return self.__repr__()
