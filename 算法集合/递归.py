__author__ = 'Mrrrrr10'
__date__ = '2018/12/10 23:15'
__github__ = 'https://github.com/Mrrrrr10'


def countdown(i):
    """计时器"""
    print(i)
    if i <= 0:  # 基线条件
        return
    else:
        countdown(i - 1)  # 递归条件


countdown(10)


def greet2(name):
    print("how are you, " + name + "?")


def bye():
    print("ok bye!")


def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


greet("Mr10")


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))











