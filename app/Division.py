
def division(a, b):
    div_result = 0

    try:
        div_result = float(b) / float(a)

    except ZeroDivisionError:
        print("It is not possible to divide by 0.")

    return div_result

