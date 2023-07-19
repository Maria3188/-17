element = int(input())
array = [2, 4, 6, 9, 1, 3, 8, 5]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

def binary_search(array, element, left, right):

    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(array)
print(binary_search(array, element, 0, 8))