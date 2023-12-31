# -*- coding: utf-8 -*-
"""E.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155S4CAV4IgSEFh3fiYn9tfljPNoiN2NE

We have four functions, func1, func2, func3, and complex_call, all of which take no parameters and only show text. The first three functions all print their function name and then might call zero or more of the other functions. The complex_call function does not print its name, but is the first function called and might call one or more of the other function. None of the functions are recursive.

1.a
Using what you know about the call stack, implement all four functions so that your implementation displays the same text as above.
"""

def func1():
    print("func1")

def func2():
    print("func2")
    func1()
    func1()

def func3():
    print("func3")
    func1()
    func2()
    func2()

def complex_func():
    func2()
    func3()
    func1()
    func2()

def main():
    complex_func()

if __name__ == '__main__':
    main()

"""1.b
In a comment labeled "1.b" in your complex_call function, explain what function or functions are called at the deepest stack level.
Function 1 called by function 2 so function 1 is at the deepest stack level,function 3 calls function 2 which calls function 1 so function 1 is deepest.

In the notes on binary search, a recursive algorithm was provided that searches for a positive integer from a sorted list. Modify bsearch so that it prints out when it recurses, if it is in the upper or lower portion of the list, and if the result was found or not found.

For example, for the input list [1,4,6,7,8,12,15,27,28,29]:
"""

def bsearch(lst, q, start, stop):
    if start > stop:
        print("Not found")
        return -1

    pivot = start + (stop - start) // 2

    if lst[pivot] == q:
        print("Found")
        return pivot
    elif lst[pivot] < q:
        print("Recursing Upper")
        return bsearch(lst, q, pivot + 1, stop)
    else:
        print("Recursing Lower")
        return bsearch(lst, q, start, pivot - 1)

def main():
    lst = [1, 4, 6, 7, 8, 12, 15, 27, 28, 29]
    i = bsearch(lst, 5, 0, len(lst) - 1)

if __name__ == '__main__':
    main()

"""When n is less than or equal to zero, the value is one
Otherwise when n is even, the value is the result of "n + harmonic(n-5)"
Otherwise when n is odd, the value is the result of "harmonic(n+1)/harmonic(n-1)"
Our function must use recursion to calculate the value of harmonic, display that value, and report the number of recursive calls that were made. Remember, recursion is only happening with the non-base cases.
"""

def harmonic(n):
  value = harmonic_helper(n)[0]
  num_recurse = harmonic_helper(n)[1]
  print("Value", value)
  print("Recursions:", num_recurse)


def harmonic_helper(n):
  if (n<= 0):
    return [1.0, 0]
  if (n% 2 ==0):
    even_n = n+ harmonic_helper(n-5)[0]
    count = harmonic_helper(n-5)[1]+1
    return (even_n, count)
  else:
    odd_n_number = harmonic_helper(n+1)[0]
    odd_n_denom = harmonic_helper(n-1)[0]
    odd_n = odd_n_number/odd_n_denom
    count = harmonic_helper(n+1)[1]+1
    count += harmonic_helper(n-1)[1]+1
    return [odd_n, count]


def main():
    harmonic(6.0)
    harmonic(5.0)
    harmonic(-1.0)

if __name__ == '__main__':
    main()