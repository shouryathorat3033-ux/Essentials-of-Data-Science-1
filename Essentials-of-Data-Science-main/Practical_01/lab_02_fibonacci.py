# Practical 01 - Lab Assignment 2
# Fibonacci sequence using recursive function


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("How many Fibonacci numbers to display? "))

print("\nFibonacci sequence:")

for i in range(terms):
    print(fibonacci(i), end=" ")

print()
