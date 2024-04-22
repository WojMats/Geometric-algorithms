import matplotlib.pyplot as plt
import math


def find_leftmost_point(x_coords, y_coords):
    min_x = min(x_coords)
    min_x_index = x_coords.index(min_x)
    return min_x_index

def orientation(x_coords, y_coords, p, q, r):
    val = (y_coords[q] - y_coords[p]) * (x_coords[r] - x_coords[q]) - (x_coords[q] - x_coords[p]) * (y_coords[r] - y_coords[q])
    if val == 0:
        return 0  # Punkty są współliniowe
    elif val > 0:
        return 1  # Zgodnie z ruchem wskazówek zegara
    else:
        return 2  # Przeciwnie do ruchu wskazówek zegara

def jarvis_convex_hull(x_coords, y_coords):
    n = len(x_coords)
    if n < 3:
        return x_coords, y_coords

    hull_indices = []
    leftmost_index = find_leftmost_point(x_coords, y_coords)
    p = leftmost_index
    while True:
        hull_indices.append(p)
        q = (p + 1) % n
        for r in range(n):
            if orientation(x_coords, y_coords, p, q, r) == 2:
                q = r
        p = q
        if p == leftmost_index:
            break

    hull_x = [x_coords[i] for i in hull_indices]
    hull_y = [y_coords[i] for i in hull_indices]
    return hull_x, hull_y

def graham_convex_hull(x_coords, y_coords):
    n = len(x_coords)
    if n < 3:
        return x_coords, y_coords

   #najnizsza
    min_y_index = min(range(n), key=lambda i: (y_coords[i], x_coords[i]))

    #zamianka z pierwszym pkt
    x_coords[0], x_coords[min_y_index] = x_coords[min_y_index], x_coords[0]
    y_coords[0], y_coords[min_y_index] = y_coords[min_y_index], y_coords[0]

    #kat pol.
    angles = [(math.atan2(y_coords[i] - y_coords[0], x_coords[i] - x_coords[0]), i) for i in range(1, n)]
    angles.sort()

    #stos
    stack = [0]

    # Dopóki stos zawiera więcej niż jeden punkt i kierunek z punktu na szczycie stosu, poprzedzającego punkt na szczycie stosu, i aktualnego punktu jest nieprawidłowy (nie tworzy skrętu w prawo), usuwa punkt ze stosu. Ten krok wykonuje operację zwana "poprawianiem otoczki", która eliminuje wklęsłe części otoczki wypukłej.
    for _, i in angles:
        while len(stack) > 1 and orientation(x_coords, y_coords, stack[-2], stack[-1], i) != 2:
            stack.pop()
        stack.append(i)

    # Zwrócenie współrzędnych punktów
    hull_x = [x_coords[i] for i in stack]
    hull_y = [y_coords[i] for i in stack]
    return hull_x, hull_y


def read_points_from_file(filename):
    x_coords = []
    y_coords = []
    with open(filename, 'r') as file:
        num_elements = int(file.readline())
        for line in file:
            x, y = map(int, line.split())
            x_coords.append(x)
            y_coords.append(y)
    return x_coords, y_coords


def plot_points_and_hulls(x_coords, y_coords, jarvis_hull_x, jarvis_hull_y, graham_hull_x, graham_hull_y):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(x_coords, y_coords)
    plt.plot(jarvis_hull_x + [jarvis_hull_x[0]], jarvis_hull_y + [jarvis_hull_y[0]], 'r-')
    plt.title("Algorytm Jarvisa")
    plt.xlabel("Współrzędna X")
    plt.ylabel("Współrzędna Y")

    plt.subplot(1, 2, 2)
    plt.scatter(x_coords, y_coords)
    plt.plot(graham_hull_x + [graham_hull_x[0]], graham_hull_y + [graham_hull_y[0]], 'g-')
    plt.title("Algorytm Grahama")
    plt.xlabel("Współrzędna X")
    plt.ylabel("Współrzędna Y")

    plt.tight_layout()
    plt.show()


def main():
    filename = '../ksztalt_3.txt'
    x_coords, y_coords = read_points_from_file(filename)
    jarvis_hull_x, jarvis_hull_y = jarvis_convex_hull(x_coords, y_coords)
    graham_hull_x, graham_hull_y = graham_convex_hull(x_coords, y_coords)
    plot_points_and_hulls(x_coords, y_coords, jarvis_hull_x, jarvis_hull_y, graham_hull_x, graham_hull_y)
main()