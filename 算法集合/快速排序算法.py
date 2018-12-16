__author__ = 'Mrrrrr10'
__date__ = '2018/12/13 13:20'
__github__ = 'https://github.com/Mrrrrr10'


def qsort(my_list):
    """快速排序算法"""
    if len(my_list) < 2:
        return my_list
    base = my_list[0]
    gt = []
    lt = []
    for x in my_list[1:]:
        if x > base:
            gt.append(x)
        else:
            lt.append(x)
    return qsort(lt) + [base] + qsort(gt)


print(qsort([3, 2, 6, 9, 7]))


def quicksort(array):
    """快速排序算法"""
    if len(array) < 2:
        return array  # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]  # 递归条件
        less = [i for i in array[1:] if i <= pivot]  # 由所有小于基准值的元素组成的子数组

        greater = [i for i in array[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([5, 3, 6, 2, 7, 8, 10, 1, 9, 4]))


