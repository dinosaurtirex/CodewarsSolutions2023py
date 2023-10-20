def all_permuted(array_length: int) -> int:
    if array_length == 0:
        return 1
    if array_length == 1:
        return 0

    derange = [0] * (array_length + 1)
    derange[0], derange[1] = 1, 0

    for i in range(2, array_length + 1):
        derange[i] = (i - 1) * (derange[i - 1] + derange[i - 2])

    return derange[array_length]

if __name__ == "__main__":
    res = all_permuted(4)
    print(res)