def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0


def classify_number(n):
    if n == 0:
        return "zero"
    elif is_positive(n) and is_even(n):
        return "positive even"
    elif is_positive(n) and not is_even(n):
        return "positive odd"
    elif not is_positive(n) and is_even(n):
        return "negative even"
    else:
        return "negative odd"
