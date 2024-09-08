#!/usr/bin/env python3

def print_fibonacci(length):

    if length <=0: 
        print ([]) # prints an empty list 
        return
    
    fibonacci_sequence = []
    a, b = 0, 1 # initialize a and b to 0 and 1, the first two numbers of a fibonacci sequence

    # generates the sequence and appends each value to the fibonacci_sequence list
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)
    return fibonacci_sequence

print_fibonacci(9)    