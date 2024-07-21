from math import inf

def divide(first, second):
    if second ==0:
        try:
            div = first / second
        except ZeroDivisionError:
            return inf
    else:
        div = first / second
        return div

