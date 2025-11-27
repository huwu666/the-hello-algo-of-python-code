def while_loop_ii(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res

print(while_loop_ii(10))