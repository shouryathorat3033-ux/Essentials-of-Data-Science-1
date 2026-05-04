# Practical 02 - Lab Assignment 1
# Find the position of a number in a list using linear search


def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i

    return -1


values = input("Enter numbers separated by space: ")
numbers = list(map(int, values.split()))

key = int(input("Enter number to search: "))
position = linear_search(numbers, key)

if position == -1:
    print(key, "is not present in the list.")
else:
    print(key, "is present at index", position)
    print("Position number is", position + 1)
