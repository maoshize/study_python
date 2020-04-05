# python基础语法

# 控制台输出, 打印语句逗号代表空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

# 控制台输入
# input = input('please enter your name: ')
# print("前缀", input)

print(r'\\t\\t')

print('''line1
line2jijjfdkfj
jdkfjskdf
line3''')

PI = 3.1415

print(10 // 3)
print(9 / 3)

# 格式化控制台输出
print('nihao: %d' % 12)

# list
list = [r'\\a', True, 123, 123, 123]
list1 = ['a', 123]
list = ['a', list1, 123]
list.append('234')
list.insert(1, 4555)
list.pop()
print(list)
print(len(list))

# tuple
tuple = (12, 'as', True, 12.22)
print(tuple.index(1, 2))

# dict
dict = {'aaa': 123, 'bbb': 1.23, 'ccc': r'\\t3', 'ddd': True}
dict['aaa'] = 234
dict.pop('aaa')
print('eee' in dict)
print(dict)

# set
s = set([r'\\a', True, 123, 123, 123])
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)


# 定义默认参数要牢记一点：默认参数必须指向不变对象！不能指向list，不过可以用None来做默认参数
def test(a, b=2):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("input typr error")
    return a + b, a * b


print(test(3))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def cal(*inputs):
    for i in inputs:
        print(i)


list = [1, 2, 3, 4]
cal(*list)


# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def guanjianzi(a, b, **c):
    print('a: ', a, 'b: ', b, 'c:', c)


extra = {'city': 'Beijing', 'job': 'Engineer'}
guanjianzi(1, 3, **extra)


# 命名关键字参数 要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(x, y, *, city, job):
    print(x, y, city, job)


# 使用命名关键字参数时，要特别注意，如果没有可变参数，
# 就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    print('second')
    pass

person(1, 2, city='a', job='b')


