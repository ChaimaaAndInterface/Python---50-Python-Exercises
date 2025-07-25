"""
Fibonacci Sequence: Generate the first 'n' numbers of the Fibonacci sequence.
0, 1, 1, 2, 3, 5, 8
"""


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


fib_sequence = fibonacci(10)
print(fib_sequence)
