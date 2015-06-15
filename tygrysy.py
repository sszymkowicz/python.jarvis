__author__ = 'Slawek'
import random as rand
import matplotlib.pyplot as plt
from math import sqrt, acos


def max_angle(p1, p2, points):
    p_max = points[0]
    for p in points:
        if angle(p1, p2, p) > angle(p1, p2, p_max):
            p_max = p
    return p_max


def angle(p1, p2, p3):
    p12 = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    p13 = sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
    p23 = sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
    if p13 == 0:
        return 0
    return acos((p12**2 + p13**2 - p23**2) / (2*p12*p13))


def jarvis(points):
    hull = [0]
    hull.append(min(points, key=lambda t: t[1]))
    hull[0] = (0, hull[1][1])
    i = 1
    while True:
        n = max_angle(hull[i], hull[i-1], points)
        hull.append(n)
        if n == hull[1]:
            break
        i += 1
    return hull


def deadband(points, r=5):
    bands = []
    for p in points:
        bands.append((p[0]-r, p[1]))
        bands.append((p[0]+r, p[1]))
        bands.append((p[0], p[1]-r))
        bands.append((p[0], p[1]+r))
        bands.append((p[0]+r-1, p[1]+r-1))
        bands.append((p[0]+r-1, p[1]-r+1))
        bands.append((p[0]-r+1, p[1]+r-1))
        bands.append((p[0]-r+1, p[1]-r+1))
    return bands


def main():
    points = [(rand.randint(0, 100), rand.randint(0, 100)) for _ in range(15)]
    ot = deadband(points, r=5)
    hull = jarvis(ot)
    hull.pop(0)

    x_points = [x[0] for x in points]
    y_points = [y[1] for y in points]
    x_hull = [x[0] for x in hull]
    y_hull = [y[1] for y in hull]
    x_ot = [x[0] for x in ot]
    y_ot = [y[1] for y in ot]

    plt.plot(x_points, y_points, 'bo')
    plt.plot(x_hull, y_hull, 'r')
    plt.plot(x_ot, y_ot, 'y.')
    plt.xlim([-10, 110])
    plt.ylim([-10, 110])
    plt.show()

if __name__ == "__main__":
    import sys
    sys.exit(main())