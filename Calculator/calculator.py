#Basic calculator project
import math

def cube(n):
    return n**3
    
def squareroot(n):
    if n < 0:
        return "NAN"
    else:
        return math.sqrt(n)


def negate(n):
    return -1 * n

def factorial(n):
    fact = 1
    return math.factorial(n)