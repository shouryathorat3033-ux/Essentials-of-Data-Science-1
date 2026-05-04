# Practical 01 - Lab Assignment 3
# Print different patterns

rows = int(input("Enter the number of rows: "))

print("\nPattern 1: Right triangle")
for i in range(1, rows + 1):
    print("* " * i)

print("\nPattern 2: Inverted triangle")
for i in range(rows, 0, -1):
    print("* " * i)

print("\nPattern 3: Pyramid")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("\nPattern 4: Number triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 5: Floyd's triangle")
number = 1
for i in range(1, rows + 1):
    for _ in range(i):
        print(number, end=" ")
        number += 1
    print()

print("\nPattern 6: Diamond")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
