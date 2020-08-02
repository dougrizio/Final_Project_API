from Subtraction import subtraction
from Squaring import squaring
from Mean import mean

def variance(data):
    varMean = mean(data)

    listDiffs = []
    for eachNum in data:
        eachDiff = subtraction(eachNum, varMean)
        listDiffs.append(eachDiff)

    listSquares = []
    for eachDiff in listDiffs:
        eachSquare = squaring(eachDiff)
        listSquares.append(eachSquare)

    return mean(listSquares)