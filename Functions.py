"""1. Write a function that will double any integer (n) and return the result"""

def double(n):
    n = 2 * n
    return n
print(double(5))



"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""

def Double(a):
    print("Enter number")
    a = int(input())
    a = a * 2
    return a
print (Double(2))    
