# 面向对象编程
from enum import Enum


class Student(object):
    name = '类变量'

    def __init__(self, score, name):
        self.__core = score
        self.__name = name

    def print(self):
        print('score', self.__core, 'name', self.__name)


std = Student(59, 'msz')
std.print()
print(std.name)


# 面向对象高级编程
# 限制实例的属性比如，只允许对Student实例添加name和age属性
# _slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, age, name):
        self.__age = age
        self.__name = name


# 把一个getter方法变成属性，只需要加上@property就可以了
class Test(object):
    __slots__ = ('name', 'age')

    @property
    def score(self):
        return self.__core

    score.setter

    def setScore(self, score):
        self.__score = score


t = Test
print(t.score)

# 枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Month.Jan)


