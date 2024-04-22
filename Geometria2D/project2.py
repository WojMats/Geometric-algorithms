import matplotlib.pyplot as plt
from point import Point
from line import Line


def visualize_line(line, point=None):
    plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y], marker='o')
    if point:
        plt.plot(point.x, point.y, marker='o', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line Visualization')
    plt.grid()
    plt.show()

# Obliczanie punktu przecięcia dwóch prostych a) na podstawie współczynników równania w postaci ogólnej
def intersection_point_general_equation(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # są równoległe
    x = (b1 * c2 - b2 * c1) / determinant
    y = (a2 * c1 - a1 * c2) / determinant
    return Point(x, y)

# b) na podstawie dwóch linii o znanym początku i końcu (punkt przecięcia prostych przechodzących przez te linie),
def intersection_point_lines(line1, line2):
    a1 = line1.point2.y - line1.point1.y
    b1 = line1.point1.x - line1.point2.x
    c1 = a1 * line1.point1.x + b1 * line1.point1.y

    a2 = line2.point2.y - line2.point1.y
    b2 = line2.point1.x - line2.point2.x
    c2 = a2 * line2.point1.x + b2 * line2.point1.y

    return intersection_point_general_equation(a1, b1, c1, a2, b2, c2)


def distance_point_to_line(point, line):
    a = line.calculate_a()
    b = line.calculate_b(a)
    if a is None:
        return abs(point.x - line.point1.x)
    numerator = abs(a * point.x - point.y + b)
    denominator = (a ** 2 + 1) ** 0.5
    return numerator / denominator


class Triangle:
    def __init__(self, line_eq1, line_eq2, line_eq3):
        self.line_eq1 = line_eq1
        self.line_eq2 = line_eq2
        self.line_eq3 = line_eq3
        self.vertices = self.calculate_vertices()

    def calculate_vertices(self):
        point1 = intersection_point_general_equation(*self.line_eq1, *self.line_eq2)
        point2 = intersection_point_general_equation(*self.line_eq2, *self.line_eq3)
        point3 = intersection_point_general_equation(*self.line_eq3, *self.line_eq1)
        return [point1, point2, point3]


def visualize_triangle(triangle):
    plt.plot([triangle.vertices[0].x, triangle.vertices[1].x, triangle.vertices[2].x, triangle.vertices[0].x],
             [triangle.vertices[0].y, triangle.vertices[1].y, triangle.vertices[2].y, triangle.vertices[0].y],
             marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle Visualization')
    plt.grid()
    plt.show()


def main():
    point1 = Point(1, 1)
    point2 = Point(3, 3)
    line = Line(point1, point2)

    while True:
        print("Choose an operation:")
        print("1. Display Line Equation")
        print("2. Check if Point Lies on the Line")
        print("3. Check if Point is Below or Above the Line")
        print("4. Translate Line")
        print("5. Reflect Point")
        print("6. Check if Point Lies on the segment")
        print("7. Calculate Intersection Point of Two Lines (General Equation)")
        print("8. Calculate Intersection Point of Two Lines (Line Objects)")
        print("9. Calculate Distance Between Point and Line")
        print("10. Create Triangle")
        print("11. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Line equation:", line.line_equation())
            visualize_line(line)
        elif choice == 2:
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            print("Is point on line:", line.is_point_on_line(point))
            visualize_line(line, point)
        elif choice == 6:
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            print("Is point on segment:", line.is_point_on_segment(point))
            visualize_line(line, point)
        elif choice == 3:
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            line.point_below_above(point)
            visualize_line(line, point)
        elif choice == 4:
            x = float(input("Enter vector x coordinate: "))
            y = float(input("Enter vector y coordinate: "))
            vector = Point(x, y)
            line.translate_line(vector)
            print("Line translated.")
            visualize_line(line)
        elif choice == 5:
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            reflected_point = line.point_reflection(point)
            if reflected_point:
                print("Reflected point:", reflected_point.x, reflected_point.y)
                visualize_line(line, reflected_point)
            else:
                print("Line is vertical, reflection is not possible.")


        elif choice == 7:
            #a1 = float(input("Enter coefficient a1: "))
            #b1 = float(input("Enter coefficient b1: "))
            #c1 = float(input("Enter coefficient c1: "))
            #a2 = float(input("Enter coefficient a2: "))
            #b2 = float(input("Enter coefficient b2: "))
            #c2 = float(input("Enter coefficient c2: "))
            a1=3
            b1=-3
            c1=0
            a2=-4
            b2=-4
            c2=0
            intersection = intersection_point_general_equation(a1, b1, c1, a2, b2, c2)
            if intersection:
                print("Intersection point:", intersection.x, intersection.y)
                visualize_line(Line(intersection, intersection))
            else:
                print("Lines are parallel, no intersection point.")
        elif choice == 8:
            #point1_line1 = Point(float(input("Enter point1 x coordinate for line1: ")),
            #                     float(input("Enter point1 y coordinate for line1: ")))
            #point2_line1 = Point(float(input("Enter point2 x coordinate for line1: ")),
            #                    float(input("Enter point2 y coordinate for line1: ")))
            #point1_line2 = Point(float(input("Enter point1 x coordinate for line2: ")),
            #                    float(input("Enter point1 y coordinate for line2: ")))
            #point2_line2 = Point(float(input("Enter point2 x coordinate for line2: ")),
            #                    float(input("Enter point2 y coordinate for line2: ")))

            point1_line1 = Point(2, 2)
            point2_line1 = Point(5, 5)
            point1_line2 = Point(-2, 2)
            point2_line2 = Point(2, -2)

            line1 = Line(point1_line1, point2_line1)
            line2 = Line(point1_line2, point2_line2)
            intersection = intersection_point_lines(line1, line2)
            if intersection:
                print("Intersection point:", intersection.x, intersection.y)
                visualize_line(line1)
                visualize_line(line2)
                plt.plot(intersection.x, intersection.y, 'ro')
                plt.show()
            else:
                print("Lines are parallel, no intersection point.")

        elif choice == 9:
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            distance = distance_point_to_line(point, line)
            print("Distance between point and line:", distance)
            visualize_line(line, point)

        elif choice == 10:
            #a1 = float(input("Enter coefficient a1: "))
            #b1 = float(input("Enter coefficient b1: "))
            #c1 = float(input("Enter coefficient c1: "))
            #a2 = float(input("Enter coefficient a2: "))
            #b2 = float(input("Enter coefficient b2: "))
            #c2 = float(input("Enter coefficient c2: "))
            #a3 = float(input("Enter coefficient a3: "))
            #b3 = float(input("Enter coefficient b3: "))
            #c3 = float(input("Enter coefficient c3: "))
            a1 = 3
            b1 = -3
            c1 = 0
            a2 = -4
            b2 = -4
            c2 = 0
            a3 = 1
            b3 = -2
            c3 = 8
            triangle = Triangle((a1, b1, c1), (a2, b2, c2), (a3, b3, c3))
            print("Triangle vertices:")
            for vertex in triangle.vertices:
                print(vertex.x, vertex.y)
            visualize_triangle(triangle)
        elif choice == 11:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
