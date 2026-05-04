# Practical 01 - Lab Assignment 1
# Accept marks of five courses and calculate result

PASS_MARK = 40
TOTAL_SUBJECTS = 5

marks = []

print("Enter marks for five courses out of 100")

for i in range(1, TOTAL_SUBJECTS + 1):
    mark = float(input(f"Course {i} marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / TOTAL_SUBJECTS
is_pass = True

for mark in marks:
    if mark < PASS_MARK:
        is_pass = False

print("\nResult")
print("Marks      :", marks)
print("Total      :", total)
print(f"Percentage : {percentage:.2f}%")

if not is_pass:
    print("Status     : Fail")
else:
    print("Status     : Pass")

    if percentage > 75:
        grade = "Distinction"
    elif percentage >= 60:
        grade = "First Division"
    elif percentage >= 50:
        grade = "Second Division"
    else:
        grade = "Third Division"

    print("Grade      :", grade)
