#使用while循环实现迭代

def while_loop(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

print(while_loop(4))