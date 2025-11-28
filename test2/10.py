'''
时间复杂度分析统计的不是算法运行的时间,而是算法运行时间随着
数据量变大时的增长趋势'''

#常数阶
def algorithm_A(n: int):
    print(0)

#线性阶
def algorithm_B(n: int):
    for _ in range(n):
        print(0)

#常数阶
def algorithm_C(n: int):
    for _ in range(1000000):
        print(0)