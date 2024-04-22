import matplotlib.pyplot as plt
from point import Point

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_a(self):
        if self.point1.x == self.point2.x:
            return None
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def calculate_b(self, a):
        if a is None:
            return None
        return self.point1.y - a * self.point1.x

    def line_equation(self):
        a = self.calculate_a()
        b = self.calculate_b(a)
        if a is None:
            return f"x = {self.point1.x}"
        return f"y = {a}x + {b}"

    def is_point_on_segment(self, punkt):
        a = self.calculate_a()
        if punkt.y == (a * punkt.x + self.calculate_b(a)):
            if (min(self.point1.x, self.point2.x) <= punkt.x <= max(self.point1.x, self.point2.x)) and \
                    (min(self.point1.y, self.point2.y) <= punkt.y <= max(self.point1.y, self.point2.y)):
                return True
        return False

    def is_point_on_line(self, point):
        a = self.calculate_a()
        if a is None:
            return point.x == self.point1.x
        return point.y == a * point.x + self.calculate_b(a)

    def point_below_above(self, point):
        a = self.calculate_a()
        c = self.calculate_b(a)
        equation = a * point.x - point.y + c
        if equation > point.y:
            print(f"Point {point.x}, {point.y} is below the line {self.line_equation()}")
        elif equation == 0:
            print(f"Point {point.x}, {point.y} is on the line {self.line_equation()}")
        else:
            print(f"Point {point.x}, {point.y} is above the line {self.line_equation()}")

    def translate_line(self, vector):
        self.point1.x += vector.x
        self.point1.y += vector.y
        self.point2.x += vector.x
        self.point2.y += vector.y

    def point_reflection(self, point):
        a = self.calculate_a()
        if a is None:
            return None
        b = self.calculate_b(a)
        a_prost = -1 / a
        b_prost = point.y - a_prost * point.x  # Oblicza wyraz wolny prostopadłej prostej przechodzącej przez punkt
        x_inter = (b_prost - b) / (a - a_prost)  # Oblicza współrzędną x punktu przecięcia linii i prostopadłej do niej.
        y_inter = a_prost * x_inter + b_prost  # Oblicza współrzędną y punktu przecięcia.
        x_reflected = 2 * x_inter - point.x
        y_reflected = 2 * y_inter - point.y
        return Point(x_reflected, y_reflected)
