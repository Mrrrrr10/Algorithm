__author__ = 'Mrrrrr10'
__date__ = '2018/12/7 15:07'
__github__ = 'https://github.com/Mrrrrr10'

import math


def binary_search(my_list, item):
    """
    二分查找算法
    :param my_list:元素列表
    :param item:需要查找的元素
    :return:要查找元素的索引
    """
    low = 0                                 # 最低位索引
    high = len(my_list) - 1                 # 最高位索引

    while low <= high:                      # 判断范围是否缩小到只有一个元素
        mid = math.ceil((low + high) / 2)   # 如果(low + high)不是偶数，将mid向下取整。
        guess = my_list[mid]                # 中间索引：猜测的数字

        if guess == item:
            # 猜的数对了
            return mid
        if guess > item:
            # 猜的数大了
            high = mid - 1                  # 最高位索引 = 中间索引 - 1
        else:
            # 猜的数小了
            low = mid + 1                   # 最低位索引 = 中间索引 + 1
    return None                             # 要查找的元素不在列表内


my_list = range(101)
my_num = 63
print("要查找的元素:%s，其索引:%s" % (my_num, binary_search(my_list, my_num)))





