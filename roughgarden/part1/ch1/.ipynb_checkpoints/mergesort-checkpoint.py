"""
    Merge(list A, list B)
    --> return list C

    Input: sorted list A, sorted list B
    Output: sorted list C composed of the merge of A and B
    ---
    
    Returns a sorted list, which is a merge of list A and list B.

    The insight for this function lies in having two distinct
    indexes for 'A' and 'B'. Each index increases each time an element
    of 'A' or 'B' is stored in 'result'.

    When either 'A' or 'B' is empty, the other list should be appended
    to the result.

    Problems I encountered:
    1. I didn't know how to compute 'n', I did a lot of trial-error
    2. The order of the if-else conditions took me a while to frame

    Things I did well:
    1. Sketch things
    2. Identified insight of separate 'j' and 'k' and 'tested' them in my mind
    3. Used 'append' as a simpler tool than counting indexes 
    4. Tried a simple test case [1,5] and [3,6]
"""

def Merge(A, B):
    result = []
    k = 0 # A index
    j = 0 # B index
    n = len(A)+len(B) # length of result
    for i in range(n):
        if k == len(A):  
            # if A is empty, append the rest of B to 'result'
            result.append(B[j])
            j = j + 1
        elif j == len(B): 
            # if B is empty, append the rest of A to 'result'
            result.append(A[k])
            k = k + 1
        elif A[k] < B[j]: 
            result.append(A[k])
            k = k + 1
        elif A[k] > B[j]:
            result.append(B[j])
            j = j + 1
        #print(result)
    return result

"""
    MergeSort

    Input: array A of n distinct integers
    Output: array with the same integers, sorted from
        smallest to largest
    ---
    The algorithm is divided into three parts:

    FIRST: 
        Divide the array or list in two parts
    SECOND:
        Recursively sort each part, where the base case is
        simply returning the array when its length is 1
        C := recursively sort first half of A
        D := recursively sort second half of A
    THIRD:
        Merge both parts using the Merge() function described above. 

    Problems I encountered:
    1. Understanding how the recursive case had to be framed

    Things I did well:
    1. Identifying the base case in the recursive part of MergeSort
    2. Explicitly dividing the solution into three parts

    --> How many levels does this recursion tree have, as a function of
    the length N of the input array?
    Answer: log(N).
    Insight: the input size decreases by a factor of 2 with each level
    of the recursion. The number of levels of recursion required is 
    equivalent to the number of times needed to divide N by 2 before
    getting a number that is at most 1.
"""

def MergeSort(array):
    n = len(array)
    if n == 1:
        return array
    else:
        # Divide the array
        half = int(n/2)
        c = array[0:half]
        d = array[half:]
        # Recursive calls
        x = MergeSort(c)
        y = MergeSort(d)
        # Merge
        return Merge(x,y)

if __name__ == '__main__':
    A = [3,8,9,5,4]
    print( MergeSort(A) )
