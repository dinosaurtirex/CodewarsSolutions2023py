def zeros(n: int):
    count = 0
    i = 1
    while n // i > 1:
        i *= 5
        count += n // i
    return count