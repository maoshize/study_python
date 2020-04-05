# python高级特性

# 切片 针对list tuple str
from collections.abc import Iterable

list = list(range(100))
print('list[0:2]', list[0:2])
print('list[:2]', list[:2])
print('list[-2:]', list[-2:])
print('list[-2:-1]', list[-2:-1])

print('list[:10:2]', list[:10:2])  # 前10个数，每两个取一个
print('list[::5]', list[::5])  # 所有数，每5个取一个
print('list[:]', list[:])  # copy

# 迭代 针对 str list tuple dict

# 默认dict迭代key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('key:', key)

# dict迭代value
for value in d.values():
    print('value:', value)

# dict迭代entry
for k, v in d.items():
    print('key:', k, 'value:', v)

# 迭代str
for ch in 'ABC':
    print(ch)

# 判断是否可迭代
print(isinstance('abc', Iterable))  # str是否可迭代

print(isinstance([1, 2, 3], Iterable))  # list是否可迭代

print(isinstance(123, Iterable))  # 整数是否可迭代

# 对list实现类似Java那样的下标循环
for i, value in enumerate(list):
    # print(i, value)
    pass

# for循环里，同时引用多个变量
for x, y in [(1, 2), (2, 3), (3, 4)]:
    print(x, y)
    pass

# 列表生成式list
print([x * x for x in range(1, 11) if x % 2 == 0])

print([x + y for x in range(1, 11) if x % 2 == 0 for y in range(2, 12) if y % 2 == 1])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 和if-else联用
print([x if x % 2 == 0 else -x for x in range(1, 11)])

# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
for n in g:
    print(n)
