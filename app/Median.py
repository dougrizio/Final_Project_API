from Addition import addition
from Subtraction import subtraction
from Division import division



def median(data):
    #data.sort()

    numValues = len(data)
    indexValues = int(subtraction(1, numValues))

    midNum = int(division(2, indexValues))

    if numValues % 2 == 0:
        midNumTwo = int(addition(1, midNum))
        twoMids = addition(data[midNum], data[midNumTwo])
        return division(2, twoMids)
    else:
        return data[midNum]

