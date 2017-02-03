import math
import operator

class Point:
    def __init__(self, category, x, y):
        self.x = float(x)
        self.y = float(y)
        self.category = category


    def distanceTo(self, point2):
        return math.sqrt(((self.x - point2.x) ** 2) + ((self.y - point2.y) ** 2))

    def __str__(self):
        return self.category + " " + str(self.x) + " " + str(self.y) + " "

class Pair:

    def __init__(self, Point1, Point2, distance):
        self.Point1 = Point1
        self.Point2 = Point2
        self.distance = Point1.distanceTo(Point2)


#Define method for voting on category
def voteForCategory(listOfStrings):
    maxCount = 0
    maxString = ""
    knownStrings = []
    for i in listOfStrings:
        if not knownStrings.__contains__(i):
            count_i = 0
            knownStrings.append(i)
            for j in listOfStrings:
                if j == i:
                    count_i += 1
                    if count_i > maxCount:
                        maxCount = count_i
                        maxString = i

    return maxString

#Define method for average distance
def averageDistance(listOfPoints, Point):
    distanceCounter = 0.0
    for p in listOfPoints:
        distanceCounter += Point.distanceTo(p)
    ret = distanceCounter / len(listOfPoints)

    return str("Average Distance to " + listOfPoints[0].category + " items: " + str(ret))

#Define main method

if __name__ == '__main__':

    #read in and process the file
    fileName = input("Enter a data file: ")
    myFile = open(fileName,"r")
    lines = myFile.readlines()
    data_array = []

    iterator = 0
    while iterator < len(lines):
        temp = lines[iterator].split()
        data_point = Point(str(temp[0]), float(temp[1]), float(temp[2]))
        data_array.append(data_point)
        iterator+=1
    for i in data_array:
        print(i)

# Error handling for reading in values for k and m
    while True:
        try:
            k = int(input("Enter a value for k: "))
        except ValueError:
            print("That's not a number")
        else:
            if 0 < k <= len(data_array):
                break
            else:
                print("Out of range. Try again: ")
    while True:
        try:
            m = int(input("Enter a value for m: "))
        except ValueError:
            print("That's not a number")
        else:
            if 0 < m <= len(data_array):
                break
            else:
                print("Out of range. Try again: ")


    #Unidentified (X,Y) pairs
    loopBreak = True
    unID_points = []
    while(loopBreak):
        response = input("Enter an X Value and a Y Value, separated by a space: ")
        myPoint = Point("(unidentified)",float(response.split()[0]), float(response.split()[1]))
        if myPoint.x == 1.0 and myPoint.y == 1.0:
            loopBreak = False
        else:
            unID_points.append(myPoint)
    # loop for each unidentified point
    for p in unID_points:
        pairs = []
        categories = []
        cat1 = []
        cat2 = []
        for d in range (0, m):
            pairs.append(Pair(p, data_array[d], p.distanceTo(data_array[d])))
            if data_array[d].category == "cat1":
                cat1.append(data_array[d])
            if data_array[d].category == "cat2":
                cat2.append(data_array[d])
        pairs.sort(key=operator.attrgetter('distance'))
        for i in pairs:
            print(i.Point2)
            categories.append(i.Point2.category)
        pointCategory = voteForCategory(categories)
        p.category = pointCategory
        print("Data item (" + str(p.x) + "," + str(p.y) + ") assigned to: " + pointCategory)

        print(averageDistance(cat1, p))
        print(averageDistance(cat2, p))


