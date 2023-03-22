import math
import random


# gpt 能秒出结果的时候，我手搓却要很久, 啊...难受
def merge_soft(array, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_soft(array, p, q)
        merge_soft(array, q + 1, r)
        # the merge operation
        merge_array = []
        i = p
        j = q + 1
        for k in range(r-p+1):
            array1_value = 100000 if i > q else array[i]
            array2_value = 100000 if j > r else array[j]
            if array1_value <= array2_value:
                merge_array.append(array1_value)
                i += 1

            else:
                merge_array.append(array2_value)
                j += 1
        m = p
        for n in range(len(merge_array)):
            array[m] = merge_array[n]
            m += 1


if __name__ == '__main__':
    # generate a random list of length 10
    random_list = [random.randint(1, 100) for i in range(10)]
    print(random_list)
    merge_soft(random_list, 0, len(random_list) - 1)
    print(random_list)
