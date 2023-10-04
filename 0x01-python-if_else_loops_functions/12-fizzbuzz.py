#!/usr/bin/python3
def fizzbuzz():
    """Write a function that prints the numbers
    from 1 to 100 separated by a space"""
    """for multiples of 3, fizz
    for multiples of 5, buzz"""
    """for multiples of both 3 & 5, fizzbuzz"""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
