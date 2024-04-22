import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

class Triangle:
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def calculate_area(self):
        a = self.line1.length()
        b = self.line2.length()
        c = self.line3.length()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def is_point_inside_heron(self, point):

        a = self.line1.length()
        b = self.line2.length()
        c = self.line3.length()


        s1 = Triangle(self.line1, Line(point, self.line1.point1), Line(point, self.line1.point2)).calculate_area()
        s2 = Triangle(self.line2, Line(point, self.line2.point1), Line(point, self.line2.point2)).calculate_area()
        s3 = Triangle(self.line3, Line(point, self.line3.point1), Line(point, self.line3.point2)).calculate_area()


        s = (a + b + c) / 2
        triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        print("Area s1:", s1)
        print("Area s2:", s2)
        print("Area s3:", s3)

        return triangle_area >= s1 + s2 + s3


    def calculate_angle(self):
        # Oblicz kąty między liniami
        angles = []
        lines = [self.line1, self.line2, self.line3]
        for i in range(3):
            j = (i + 1) % 3
            k = (i + 2) % 3

            vector1 = (lines[j].point1.x - lines[i].point1.x, lines[j].point1.y - lines[i].point1.y)
            vector2 = (lines[k].point1.x - lines[i].point1.x, lines[k].point1.y - lines[i].point1.y)

            #długości wektorów
            magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
            magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

            # iloczyn skalarny
            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

            # cos
            cos_angle = dot_product / (magnitude1 * magnitude2)
            angle = math.degrees(math.acos(cos_angle))

            angles.append(angle)

        return angles


def visualize_triangle(triangle):
    plt.plot([triangle.line1.point1.x, triangle.line1.point2.x], [triangle.line1.point1.y, triangle.line1.point2.y], 'r-')
    plt.plot([triangle.line2.point1.x, triangle.line2.point2.x], [triangle.line2.point1.y, triangle.line2.point2.y], 'g-')
    plt.plot([triangle.line3.point1.x, triangle.line3.point2.x], [triangle.line3.point1.y, triangle.line3.point2.y], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle Visualization')
    plt.grid()
    plt.show()

def visualize_triangle_with_point(triangle, point):
    plt.plot([triangle.line1.point1.x, triangle.line1.point2.x], [triangle.line1.point1.y, triangle.line1.point2.y], 'r-')
    plt.plot([triangle.line2.point1.x, triangle.line2.point2.x], [triangle.line2.point1.y, triangle.line2.point2.y], 'g-')
    plt.plot([triangle.line3.point1.x, triangle.line3.point2.x], [triangle.line3.point1.y, triangle.line3.point2.y], 'b-')
    plt.plot(point.x, point.y, marker='o', color='black')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle with Point Visualization')
    plt.grid()
    plt.show()

def main():

    point1 = Point(0, 0)
    point2 = Point(0, 3)
    point3 = Point(6, 0)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point1)

    # Utworzenie trójkąta
    triangle = Triangle(line1, line2, line3)


    while True:
        print("Choose an option:")
        print("1. Visualize Triangle")
        print("2. Check if Point belongs to Triangle (Heron)")
        print("3. Calculate Triangle Area")
        print("4. Calculate Angles of Triangle")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            visualize_triangle(triangle)
        elif choice == "2":
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            inside = triangle.is_point_inside_heron(point)
            print("Is point inside triangle (Heron):", inside)
            visualize_triangle_with_point(triangle, point)
        # elif choice == "3":
        #     x = float(input("Enter point x coordinate: "))
        #     y = float(input("Enter point y coordinate: "))
        #     point = Point(x, y)
        #     inside = triangle.is_point_inside_cross_product(point)
        #     print("Is point inside triangle (Cross Product):", inside)
        #     visualize_triangle_with_point(triangle, point)
        elif choice == "3":
            area = triangle.calculate_area()
            print("Triangle area:", area)
        elif choice == "4":
            angles = triangle.calculate_angle()
            if angles is not None:
                for i, angle in enumerate(angles, start=1):
                    print(f"Angle at vertex {i}: {angle} degrees")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


