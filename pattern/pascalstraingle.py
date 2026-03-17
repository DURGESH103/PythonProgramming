n = 6
def pascals_row(row):
    result = [1]
    for i in range(1, row+ 1):
        result.append(result[-1] *
(row -i+1) // i)
    return result

for i in range(n):
    row = pascals_row(i)
    print(" " * (n - i), end="")
    print(" ".join(str(x) for x in row))