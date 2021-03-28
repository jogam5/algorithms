"""
    Insertion Sort Non-increasing
    
    This program contains the sorting algorithm Insertion Sort in
    a non-increasing order (i.e. 59, 58, 41 ... ).

    Insight: similar to the regular non-decreasing Insertion Sort,
    the backbone of the algorithm is the same except for a little
    change in the while loop condition: 'key > array[j]'.

    Using this condition, instead of ordering in ascending order,
    the algorithm orders in a descending fashion.
"""
def nonincreasingInsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key > array[j]:
            array[j+1] = array[j]
            array[j] = key
            j = j - 1
    return array

array = [31, 41, 59, 26, 41, 58]
print("Unsorted array: ")
print(array)
print("Sorted array in non-increasing order: ")
print(nonincreasingInsertionSort(array)) 
