import random


# insertion sort in increasing order
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1], array[i] = array[i], array[i+1]
            i = i - 1
        array[i+1] = key


# insertion sort in decrease order
def insertion_sort_dec(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i+1], array[i] = array[i], array[i+1]
            i = i - 1
        array[i+1] = key


# 递归方式 recursive insertion sort (increasing order)
# we recursively sort A[1. n-1] and then insert A[n] into the sorted array A[1..n-1].
def insertion_sort_recursive(array):   # 这个函数有问题
    if len(array) == 0: # 问题1：不需要检查数组长度是否为0
        return None
    insertion_sort_recursive(array[:-1])  # 问题2：使用array[:-1]创建了一个新的子数组
    if len(array[:-1]) == 0:  # 问题1（续）：这里的检查是不必
        return None
    else:
        for i in range(len(array[:-1])):
            if array[i] > array[-1]:
                array[i], array[-1] = array[-1], array[i]
        return array


# 递归方式 recursive insertion sort (increasing order)
# we recursively sort A[1. n-1] and then insert A[n] into the sorted array A[1..n-1].
def insertion_sort_recursive2(array, index=None):
    if index is None:
        index = len(array) - 1
    if index == 0:
        return
    insertion_sort_recursive2(array, index - 1)
    while index > 0 and array[index - 1] > array[index]:
        array[index - 1], array[index] = array[index], array[index - 1]
        index -= 1
    return array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate a random list of length 10
    random_list = [random.randint(1, 100) for i in range(10)]

    # print the random list
    print(random_list)
    insertion_sort(random_list)
    print(random_list)
    insertion_sort_dec(random_list)
    print(random_list)

    # new_random_list = [random.randint(1, 100) for i in range(10)]
    new_random_list = [44, 61, 66, 97, 90, 74, 90, 35, 89, 57]
    # new_random_list = [44, 97, 90, 57]
    print(new_random_list)
    print(insertion_sort_recursive2(new_random_list))

