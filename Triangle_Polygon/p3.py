import matplotlib.pyplot as plt
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


class Polygon:
    def __init__(self, lines):
        self.lines = lines

    def visualize_polygon(self):
        for line in self.lines:
            plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y], color='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Polygon Visualization')
        plt.grid()
        plt.show()

    def is_point_inside(self, point):
        count = 0
        for line in self.lines:
            if (line.point1.y > point.y) != (line.point2.y > point.y) and \
                    point.x < (line.point2.x - line.point1.x) * (point.y - line.point1.y) / (
                    line.point2.y - line.point1.y) + line.point1.x:
                count += 1
        return count % 2 == 1


def main():
    # Wielokąt na podstawie współrzędnych
    point1 = Point(1, 1)
    point2 = Point(4, 5)
    point3 = Point(7, 3)
    point4 = Point(5, 1)
    point5 = Point(2, 2)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point5)
    line5 = Line(point5, point1)

    polygon = Polygon([line1, line2, line3, line4, line5])

    # Menu
    while True:
        print("Choose an option:")
        print("1. Visualize Polygon")
        print("2. Check if Point belongs to Polygon")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            polygon.visualize_polygon()
        elif choice == "2":
            x = float(input("Enter point x coordinate: "))
            y = float(input("Enter point y coordinate: "))
            point = Point(x, y)
            inside = polygon.is_point_inside(point)
            print("Is point inside polygon:", inside)
            if inside:
                plt.plot(point.x, point.y, 'ro')
                plt.show()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
