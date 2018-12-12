__author__ = 'Mrrrrr10'
__date__ = '2018/12/11 13:51'
__github__ = 'https://github.com/Mrrrrr10'


def sum(arr):
    """求和（版本版本）"""
    total = 0
    for x in arr:
        total += x
    return total


print(sum([1, 2, 3, 4]))


def sum(my_list):
    """求和（递归版本）"""
    if my_list == []:
        return 0
    return my_list[0] + sum(my_list[1:])


print(sum([2, 4, 6]))


def countlist(my_list):
    """计算列表包含的元素数：递归版本"""
    if my_list == []:
        return 0
    return 1 + countlist(my_list[1:])


print(countlist([2, 3, 4]))


def findmax(my_list):
    """找出列表中最大的数字"""
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]
    sub_max = max(my_list[1:])
    return my_list[0] if my_list[0] > sub_max else sub_max


print(findmax([5, 3, 7, 10]))

