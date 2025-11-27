#在一个循环结构内嵌套另一个循环结构

def nested_for_loop(n: int) -> int:
    res = ''
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j}),"
    return res

print(nested_for_loop(5))