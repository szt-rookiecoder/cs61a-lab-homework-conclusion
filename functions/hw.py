def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
       positive numbers x, y, and z.

       >>> two_of_three(1, 2, 3)
       5
       >>> two_of_three(5, 3, 1)
       10
       >>> two_of_three(10, 2, 8)
       68
       >>> two_of_three(5, 5, 5)
       50"""
    return min(x*x +y*y ,x*x+ z*z, y*y+ z*z )

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

       >>> largest_factor(15) # factors are 1, 3, 5
       5
       >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
       40
       >>> largest_factor(13) # factor is 1 since 13 is prime
       1
       """
    assert n > 1
    factor = n - 1
    while n % factor != 0:
        factor -= 1
    return factor

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.
    hailstone sequence:
    Pick a positive integer n as the start.
    If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
    Continue this process until n is 1.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            print(n)
            length += 1
        else:
            n = 3*n +1
            print(n)
            length += 1
    return length




