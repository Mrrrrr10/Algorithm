__author__ = 'Mrrrrr10'
__date__ = '2018/12/10 17:53'
__github__ = 'https://github.com/Mrrrrr10'


def findSmallest(arr):
    """找出最小元素"""
    smallest = arr[0]               # 存储最小的值
    smallest_index = 0              # 存储最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            # 第二个元素 < 最小值
            # 那么这个元素就是当前的最小值
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """对数组进行排序"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)        # 数组中最小的元素的索引，并将其加入到新数组中
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
