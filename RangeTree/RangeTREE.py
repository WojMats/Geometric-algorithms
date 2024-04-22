import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def build_range_tree_1d(points):
    if not points:
        return None

    points.sort()
    mid = len(points) // 2
    root = Node(points[mid])  #Tworzy nowy węzeł drzewa root z punktem, który jest środkowym punktem listy points
    root.left = build_range_tree_1d(points[:mid])  #Rekurencyjnie buduje lewe poddrzewo dla punktów znajdujących się przed środkowym punktem. W tym celu wywołuje funkcję build_range_tree_1d
    root.right = build_range_tree_1d(points[mid+1:])

    return root

def query_range_1d(root, start, end):
    if root is None:
        return []

    if root.point >= start and root.point <= end:  #prawdza, czy punkt w korzeniu drzewa root znajduje się wewnątrz zakresu od start do end. Jeśli tak, dodaje ten punkt do listy wynikowej result.
        result = [root.point]
        result.extend(query_range_1d(root.left, start, end))
        result.extend(query_range_1d(root.right, start, end))
        return result
    elif root.point < start:
        return query_range_1d(root.right, start, end)
    else:
        return query_range_1d(root.left, start, end)

def build_range_tree_2d(points):
    if not points:
        return None

    points.sort(key=lambda x: x[0]) #Punkty są sortowane względem ich współrzędnej x.
    mid = len(points) // 2
    root = Node(points[mid])

    left_points = points[:mid]
    right_points = points[mid+1:]

    left_points.sort(key=lambda x: x[1]) #wzgledm y
    right_points.sort(key=lambda x: x[1])

    root.left = build_range_tree_2d(left_points)
    root.right = build_range_tree_2d(right_points)

    return root

#Algorytm budowy drzewa przedziałowego 2D:
#Sortowanie listy punktów względem współrzędnej x: O(n log n)
#Sortowanie lewych i prawych poddrzew względem współrzędnej y: O(n log n)
#Budowa drzewa przedziałowego: O(n log^2 n) (sortowanie x dla każdego węzła, rekurencja, gdzie n to liczba punktów)
#Łączna złożoność czasowa: O(n log^2 n)

def query_range_2d(root, x_start, x_end, y_start, y_end):
    if root is None:
        return []

    x, y = root.point

    if x >= x_start and x <= x_end and y >= y_start and y <= y_end:
        result = [root.point]  #lista wynikowa
        result.extend(query_range_2d(root.left, x_start, x_end, y_start, y_end))
        result.extend(query_range_2d(root.right, x_start, x_end, y_start, y_end))
        return result
    elif x < x_start: #lewe poddrzewo nie zawiera punktów, ignorujemy lewe poddrzewo
        return query_range_2d(root.right, x_start, x_end, y_start, y_end)
    elif x > x_end:  #prawe poddrzewo nie zawiera punktów
        return query_range_2d(root.left, x_start, x_end, y_start, y_end)
    else:
        result = []
        result.extend(query_range_2d(root.left, x_start, x_end, y_start, y_end))
        result.extend(query_range_2d(root.right, x_start, x_end, y_start, y_end))
        return result




# Testy dla drzewa 1D
points_1d = [random.randint(1, 100) for _ in range(50)]
tree_1d = build_range_tree_1d(points_1d)
query_start_1d = 20
query_end_1d = 80
result_1d = query_range_1d(tree_1d, query_start_1d, query_end_1d)
print("Punkty 1D:", points_1d)
print("Wynik zapytania 1D (przedział [{}, {}]): {}".format(query_start_1d, query_end_1d, result_1d))

# Wizualizacja dla drzewa 1D
plt.figure(figsize=(10, 6))
plt.plot(points_1d, [0] * len(points_1d), 'bo', label='Punkty')
plt.axvspan(query_start_1d, query_end_1d, color='lightgreen', alpha=0.5, label='Przedział zapytania')
plt.xlabel('Wartość')
plt.ylabel('Indeks')
plt.title('Wizualizacja drzewa zakresowego 1D')
plt.legend()
plt.show()

#Testy dla drzewa 2D
points_2d = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(50)]
tree_2d = build_range_tree_2d(points_2d)
query_x_start_2d = 50
query_x_end_2d = 80
query_y_start_2d = 80
query_y_end_2d = 90
result_2d = query_range_2d(tree_2d, query_x_start_2d, query_x_end_2d, query_y_start_2d, query_y_end_2d)
print("Punkty 2D:", points_2d)
print("Wynik zapytania 2D (przedział x: [{}, {}], przedział y: [{}, {}]): {}".format(
query_x_start_2d, query_x_end_2d, query_y_start_2d, query_y_end_2d, result_2d))

#Wizualizacja dla drzewa 2D
plt.figure(figsize=(10, 6))
x_values = [point[0] for point in points_2d]
y_values = [point[1] for point in points_2d]
plt.plot(x_values, y_values, 'bo', label='Punkty')
plt.axvspan(query_x_start_2d, query_x_end_2d, color='lightgreen', alpha=0.5, label='Przedział zapytania X')
plt.axhspan(query_y_start_2d, query_y_end_2d, color='lightblue', alpha=0.5, label='Przedział zapytania Y')
plt.xlabel('Wartość X')
plt.ylabel('Wartość Y')
plt.title('Wizualizacja drzewa zakresowego 2D')
plt.legend()
plt.show()