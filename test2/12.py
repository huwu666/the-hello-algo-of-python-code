#常数阶
def constant(n: int) -> int:
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count

#线性阶
def linear(n: int) -> int:
    count = 0
    for _ in range(n):
        count += 1
    return count

#平方阶
def quadratic(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

#冒泡排序
def bubble_sort(nums: list[int]) -> int:
    cpunt = 0
    for i in range(len(nums) - 1, 0 , -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp: int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3
    return count

#指数阶
def exponential(n: int) -> int:
    count = 0
    base = 1
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    return count

#指数阶常出现在递归函数中
def exp_recur(n: int) -> int:
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1

#对数阶
def logarithmic(n: int) -> int:
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

#对数阶也常出现在递归函数中
def log_recur(n: int) -> int:
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1

#线性对数阶
def linear_log_recur(n: int) -> int:
    if n <= 1:
        return 1
    count = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count

#阶乘阶
def factorial_recur(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count

#最差,最佳,平均时间复杂度
import random

def random_numbers(n: int) -> list[int]:
    nums = [i for i in range(1, n + 1)]
    random.shuffle(nums)
    return nums

def fine_one(nums: list[int]) -> int:
    for i in range(len(nums)):
        if nums[i] == 1:
            return i
    return -1

random_numbers(4)
print(random_numbers(4))
print(fine_one(random_numbers(4)))