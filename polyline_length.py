import numpy as np
import random
from sklearn.metrics.pairwise import euclidean_distances


def calculate_polyline_length():
    n = int(input("Enter the number of points on the plane: "))
    print()
    points = []
    result = 0

    for i in range(n):
        points.append([random.randint(0, 9), random.randint(0, 9)])

    print("Points: ", points)
    point_index = random.randint(0, n - 1)
    point = points[point_index]
    print("Initial point drawn: ", point)
    sequence_points = [point]

    while len(points) > 1:
        points.remove(point)
        distances = euclidean_distances([point], points)
        min_distance = min(distances[0])
        result = result + min_distance
        index = np.where(distances[0] == min_distance)
        point = points[index[0][0]]
        sequence_points.append(point)

    print("Sequence points:", sequence_points)
    print("Polyline length: ", round(result, 2))


if __name__ == '__main__':
    calculate_polyline_length()