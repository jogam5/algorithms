"""
    RecursiveMult(int x, int y)
    --> return (int) x*y 

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

"""
    isOdd(int x)
    --> return True or False

    Returns true if the given integer is odd, otherwise return False (i.e. the
    integer is even)
"""
def isOdd(x):
    if x % 2 == 0:
        return False
    else:
        return True

"""
    addZeros(int x, int y)
    --> return string x, string y

    Returns x and y with leading zeros, so that both x and y have the same even length.
"""
def addZeros(x, y):
    x = str(x)
    y = str(y)

    if len(x) == len(y):
        if isOdd(len(x)):
            x = "0"+x
        if isOdd(len(y)):
            y = "0"+y
        return x, y
    elif len(x) > len(y):
        #print("x > y")
        if isOdd(len(x)):
            # if odd add leading zero
            x = "0"+x
        delta = abs(len(x)-len(y))
        y = delta*"0"+y
    else:
        #print("y > x")
        if isOdd(len(y)):
            # if odd add leading zero
            y = "0"+y
        delta = abs(len(x)-len(y))
        x = delta*"0"+x
    return x, y

"""
    Karatsuba(int x, int y)
    --> return (int) x*y

    Computes the recursive multiplication of x*y using the Karatsuba 
    recursive strategy.

    Learnings:
        i. Divide the problem in submodules (i.e. isOdd or addZeros)
        ii. Debug using small values
"""
def Karatsuba(x, y):
    w = len(str(x))
    z = len(str(y))
    if w == 1 and z == 1:
        # Base case
        return x*y 
    else:
        # Recursive case
        xString, yString = addZeros(x,y)

        # n and n/2
        n = len(xString)
        nHalf = int(n/2)

        a = int(xString[0:nHalf])
        b = int(xString[nHalf:])
        c = int(yString[0:nHalf])
        d = int(yString[nHalf:])
        p = a + b
        q = c + d

        """
        Debugging:
        print("a: "+str(a))
        print("b: "+str(b))
        print("c: "+str(c))
        print("d: "+str(d))
        print("p: a + b -> "+str(p))
        print("q: c + d -> "+str(q))
        """
        firstTerm = Karatsuba(a,c)
        secondTerm = Karatsuba(p,q)
        thirdTerm = Karatsuba(b,d)

        return pow(10,n)*firstTerm + pow(10,nHalf)*(secondTerm - firstTerm - thirdTerm) + thirdTerm

if __name__ == '__main__':
    print(RecursiveMult(5678, 1234))
    print(Karatsuba(12345, 6789))
