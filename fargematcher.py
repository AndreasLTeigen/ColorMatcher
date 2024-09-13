import sys
import math

def removeNewlineChar(line):
    return line[:-1]

def extractColor(lineArray):
    red = int(lineArray[-3])
    green = int(lineArray[-2])
    blue = int(lineArray[-1])
    return red, green, blue

def extractName(lineArray):
    name =  " ".join(lineArray[0:-3])
    return name

def extractNameAndColor(lineArray):
    name = extractName(lineArray)
    r, g, b = extractColor(lineArray)
    return name, r, g, b

def loadFargekart(file):
    fargekart = {}
    for line in file:
        line = removeNewlineChar(line)
        line = line.split(' ')
        name, r, g, b = extractNameAndColor(line)
        fargekart[name] = [r, g, b]
    return fargekart

def parseQueryColor(colorString):
    return extractColor(colorString)

def euclideanDistance(v1, v2):
    assert(len(v1) == len(v2))
    cum = 0
    for i in range(len(v1)):
        temp = v1[i] - v2[i]
        cum += temp*temp
    return math.sqrt(cum)

def colorDistance(queryColor, referenceColor):
    return euclideanDistance(queryColor, referenceColor)

def findNearestColor(queryColor, fargekart):
    nearestColorName = None
    nearestDistance = float('inf')
    for name in fargekart:
        referenceColor = fargekart[name]
        dist = colorDistance(queryColor, referenceColor)
        if dist < nearestDistance:
            nearestColorName = name
            nearestDistance = dist
    return nearestColorName, fargekart[nearestColorName]

file = open('Fargekart.txt', 'r')
fargekart = loadFargekart(file)

colorString = sys.argv[1:4]

r, g, b = parseQueryColor(colorString)
queryColor = [r, g, b]
name, colorCode = findNearestColor(queryColor, fargekart)

print("Query color: ", queryColor)
print(name, ": " , colorCode)

file.close()