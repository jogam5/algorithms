"""
    RecursiveMult(x,y)

    Returns the multiplication of two n-digit positive integers x and y.
    Assumption: n is a power of 2. (i.e. if n = 4, n digits means numbers such as 6765, 3976).

    The insight for this problem is that a number x with an even number of digits
    can be expressed in terms of two n/2 digit numbers, its first half and second half
    a and b:
        x = 10^(n/2)*a + b
        
        (e.g. 45 -> n = 2; 45 = 10^(2/2)*4 + 5)
"""
def RecursiveMult(x, y):
    n = len(str(x))
    if n == 1:
        # Base case
        return x*y 
    else:
        # Recursive case
        nHalf = int(n/2)
        xString = str(x)
        yString = str(y)
        a = int(xString[0:nHalf])
        b = int(xString[nHalf:])
        c = int(yString[0:nHalf])
        d = int(yString[nHalf:])
        return pow(10,n)*RecursiveMult(a,c) + pow(10,nHalf)*( RecursiveMult(a,d) + RecursiveMult(b,c) ) + RecursiveMult(b,d)

x = RecursiveMult(5678, 1234)
print(x)
