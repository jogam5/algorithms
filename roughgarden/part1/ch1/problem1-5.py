"""
    Problem 1.5: Given as input an unsorted array of N distinct numbers, where N is a power of
    2. Provide an algorithm that identifies the second largest element with no more than 
    N + logN - 2 comparisons.
"""

"""
    The number of comparisons is equal to N.

    Assuming log of base 2, 
    if N = 2, the maximum time is: 2 + log(2) - 2 = 2 + 1 - 2 = 1.
    if N = 4, the maximum time is: 4 + log(4) - 2 = 4 + 2 - 2 = 4.
"""
def secondLargest(A):
  maximum = A[0];
  secondmax = 0;
  if ( len(A) == 2 ):
    print("comparison # 1")
    return A[1] if A[0] > A[1] else A[0]
  for i in range(len(A)):
    print("comparison #"+str(i+1))
    if A[i] >= maximum:
      secondmax = maximum
      maximum = A[i]
    elif A[i] >= secondmax:
      secondmax = A[i]
  return secondmax

if __name__ == '__main__':
    A = [5, 10, 3, 8]
    x = secondLargest(A)
    print(A)
    print("Number of elements: "+str(len(A)))
    print("Second largest element: "+str(x))
