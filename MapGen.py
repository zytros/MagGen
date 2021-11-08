import random
from random import randint
import cv2
import numpy as np
import time

points = []
hull = []
numPoints = 30
xDim = 200
yDim = 200
LAND = 1
WATER = -1

imgG = np.zeros((yDim, xDim, 3), np.uint8)

regInfo = np.zeros((xDim, yDim), np.uint8)


class HelperPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x & self.y == other.y:
            print("true")
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __hash__(self):
        p = HelperPoint(self.x, self.y)
        return p.__hash__()


class Region:
    def __init__(self, point):
        pList = [point]
        self.point = point



def Left_index(points):
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convexHull(pList, n):
    # There must be at least 3 pList
    if n < 3:
        return

    # Find the leftmost point
    l = Left_index(pList)

    p = l
    q = 0
    while (True):

        # Add current point to result
        hull.append(p)

        q = (p + 1) % n

        for i in range(n):

            # If i is more counterclockwise
            # than current q, then update q
            if (orientation(pList[p],
                            pList[i], pList[q]) == 2):
                q = i

        p = q

        # While we don't come to first point
        if (p == l):
            break


def doLandmasses():
    for i in range(1, 1000):
        print("Iteration:", i)
        p = 0.2
        for j in range(1, xDim - 1):
            for k in range(1, yDim - 1):
                if regInfo[j][k] == 1:
                    if random.random() < p:
                        if regInfo[j][k - 1] == 0:
                            regInfo[j][k - 1] = 11
                    if random.random() < p:
                        if regInfo[j][k + 1] == 0:
                            regInfo[j][k + 1] = 11
                    if random.random() < p:
                        if regInfo[j+1][k] == 0:
                            regInfo[j + 1][k] = 11
                    if random.random() < p:
                        if regInfo[j-1][k] == 0:
                            regInfo[j - 1][k] = 11

                elif regInfo[j][k] == 2:
                    if random.random() < p:
                        if regInfo[j][k - 1] == 0:
                            regInfo[j][k - 1] = 12
                    if random.random() < p:
                        if regInfo[j][k + 1] == 0:
                            regInfo[j][k + 1] = 12
                    if random.random() < p:
                        if regInfo[j+1][k] == 0:
                            regInfo[j + 1][k] = 12
                    if random.random() < p:
                        if regInfo[j-1][k] == 0:
                            regInfo[j - 1][k] = 12
        printImg()


def paintSea():
    i=0


def funcMain():
    for i in range(numPoints):
        x = random.randint(1, xDim - 1)
        y = random.randint(1, yDim - 1)
        points.append(Point(x, y))
        rnd = 0
        if random.random() < 0.3:
            rnd = 2
        else:
            rnd = 1
        regInfo[y][x] = rnd

    convexHull(points, numPoints)

    img = imgG

    for p in points:
        cv2.circle(img, (p.x, p.y), 5, (255, 255, 255, cv2.FILLED))
    for i in range(len(hull)):
        pos = (points[hull[i]].x, points[hull[i]].y)
        cv2.circle(img, pos, 10, (255, 0, 255, cv2.FILLED))
        startPoint = pos
        endPoint = (points[hull[(i + 1) % len(hull)]].x, points[hull[(i + 1) % len(hull)]].y)
        cv2.line(img, startPoint, endPoint, (255, 255, 255), 3)

    cv2.imshow("lel", img)
    cv2.waitKey(1)

    doLandmasses()


def printImg():
    for i in range(xDim):
        for j in range(yDim):
            if regInfo[i][j] == 11:
                regInfo[i][j] = 1
            elif regInfo[i][j] == 12:
                regInfo[i][j] = 2
            if regInfo[i][j] == 1:
                cv2.circle(imgG, (j, i), 1, (255, 0, 255))
            elif regInfo[i][j] == 2:
                cv2.circle(imgG, (j, i), 1, (255, 0, 0))
    cv2.imshow("asd", imgG)
    cv2.waitKey(1)





def testDoLandmasses():
    # def startpoints
    for i in range(xDim):
        for j in range(yDim):
            if random.random() < 0.001:
                regInfo[i][j] = randint(1,2);

    doLandmasses()


if __name__ == '__main__':
    #testDoLandmasses()

    funcMain()
    points = []
    hull = []
