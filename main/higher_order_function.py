# 高阶函数

# map/reduce

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
from functools import reduce


def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(f, L)))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
def f(x, y):
    return x * 10 + y;


print(type(int(reduce(f, L))))


# filter过滤
def fi(x):
   return x % 2 == 1;
print(list(filter(fi, L)))

# sort排序
sorted([36, 5, -12, 9, -21], key=abs)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)