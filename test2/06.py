'''如果函数在返回前的最后一步才进行递归调用,则该函数
可以被编译器或解释器优化,使其在空间效率上与迭代相当'''

def tail_recur(n, res):
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)

n = 5
res = tail_recur(n, 0)
print(f'{res}')