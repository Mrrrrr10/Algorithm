__author__ = 'Mrrrrr10'
__date__ = '2019/1/6 11:28'
__github__ = 'https://github.com/Mrrrrr10'

# 1.不是装饰器的装饰器
# import time
#
#
# def decorator(func):
#     start = time.time()
#     func()
#     end = time.time()
#     used_time = end - start
#     print("耗时: {used_time}".format(used_time=used_time))
#
#
# def do_something():
#     for i in range(10000):
#         pass
#     print("play game")
#
#
# decorator(do_something)


# 2.最简单的装饰器
# import time
#
#
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         used_time = end - start
#         print("耗时: {used_time}".format(used_time=used_time))
#
#     return wrapper
#
#
# @decorator
# def do_something():
#     for i in range(10000):
#         pass
#     print("play game")
#
#
# do_something()

# 3.目标函数带固定参数的装饰器
# import time
#
#
# def decorator(func):
#     def wrapper(name):
#         start = time.time()
#         func(name)
#         end = time.time()
#         used_time = end - start
#         print("耗时: {used_time}".format(used_time=used_time))
#
#     return wrapper
#
#
# @decorator
# def do_something(name):
#     for i in range(10000):
#         pass
#     print("play game" + name)
#
#
# do_something("Mrrrrr10")

# 4.目标函数带不固定参数的装饰器
# import time
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         used_time = end - start
#         print("耗时: {used_time}".format(used_time=used_time))
#
#     return wrapper
#
#
# @decorator
# def do_something(name):
#     for i in range(10000):
#         pass
#     print("play game" + name)
#
#
# @decorator
# def do_something2(user, name):
#     for i in range(10000):
#         pass
#     print(user + "play game" + name)
#
#
# do_something("Mrrrrr10")
# do_something2("Mrrrrr10", "Mrrrrr10")

# 5. 让装饰器带参数
# import time
#
#
# def decorator(max):
#     def _decoractor(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             for i in range(max):
#                 func(*args, **kwargs)
#             end = time.time()
#             used_time = end - start
#             print("耗时: {used_time}".format(used_time=used_time))
#
#         return wrapper
#
#     return _decoractor
#
#
# @decorator(2)
# def do_something(name):
#     for i in range(10000):
#         pass
#     print("play game" + name)
#
#
# do_something("Mrrrrr10")

# 6.被装饰过的函数的函数名
# import functools
#
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         func()
#
#     return wrapper
#
#
# @decorator
# def do_something():
#     for i in range(10000):
#         pass
#
#
# print(do_something.__name__)

# 7.让函数只能运行指定的次数
class Decorator(object):
    def __init__(self, max):
        self.max = max
        self.count = 0

    def __call__(self, func):
        self.func = func
        return self.call_func

    def call_func(self, *args, **kwargs):
        self.count += 1
        if self.count == self.max:
            print("%s run more than %d times" % (self.func.__name__, self.max))
        elif self.count < self.max:
            self.func(*args, **kwargs)
        else:
            pass


@Decorator(10)
def do_something():
    print("play game")


@Decorator(15)
def do_something1():
    print("play game 1")


for i in range(10):
    do_something()
    do_something1()
