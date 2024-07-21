def divide(first, second):
    if second ==0:
        try:
            div = first / second
        except ZeroDivisionError:
            return "Ошибка"
    else:
        div = first / second
        return div
