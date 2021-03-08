"""
    Insertion Sort
    
    This program contains the sorting algorithm Insertion Sort.

    Insight: a value is assigned as the Key, the element to its left
    is moved to the right if the Key is lower than this element.

    A loop is used from 1 up to the length of the array or list.
    A Key is assigned to the second element of the array.
    An auxiliary variable called 'j' is used to make a reference
    to the previous element before i.
    A while loop is used to check if the Key is lower than the previous
    element of the list. As long as this condition is fulfilled (and
    the auxiliary variable 'j' is greater or equal than zero, first we
    move to the right the element to the left of the Key and second we
    move to the left the Key. During this while loop, the 'j' variable is
    decreased.

    If 'j' is only greater than zero in the while loop, an error to swap the
    first and second element occurs.

"""
def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]  # j  = i - 1 (i.e. left to right)
            array[j] = key # j = i - 1 (i.e. right to left)
            j = j - 1
    return array

array = [31, 41, 59, 26, 41, 58]
print("Unsorted array: ")
print(array)
print("Sorted array: ")
print(insertionSort(array)) 
