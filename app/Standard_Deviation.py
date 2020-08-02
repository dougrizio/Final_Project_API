from Squarerooting import squarerooting
from Variance import variance

def standard_deviation(data):
    var = variance(data)
    return squarerooting(var)