from collections import Counter



def mode(data):
    mostOften = Counter(data)
    get_mode = dict(mostOften)
    modeResult = [x for x, y in get_mode.items() if y == max(list(mostOften.values()))]

    numValues = len(data)
    numModes = len(modeResult)

    if numModes == numValues:
        return "No mode found"
    elif numModes != 1:
        return "Multiple modes found"
    else:
        return float(modeResult[0])

