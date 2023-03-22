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
