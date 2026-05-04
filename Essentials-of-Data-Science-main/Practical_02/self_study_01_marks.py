# Practical 02 - Self Study Assignment 1
# Find total marks and percentage using list

subjects = ["Maths", "Physics", "Chemistry", "Computer", "English"]
marks = []

print("Enter marks out of 100")

for subject in subjects:
    mark = float(input(subject + ": "))
    marks.append(mark)

total = sum(marks)
maximum_marks = len(subjects) * 100
percentage = (total / maximum_marks) * 100

print("\nStudent Marks")
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("\nTotal marks :", total, "/", maximum_marks)
print(f"Percentage  : {percentage:.2f}%")
