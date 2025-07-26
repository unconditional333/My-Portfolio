# Input student details
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

# Input marks for 5 subjects
print("\nEnter marks out of 100 for each subject:")
english = float(input("English: "))
maths = float(input("Maths: "))
science = float(input("Science: "))
social = float(input("Social Studies: "))
computer = float(input("Computer Science: "))

# Calculate total and percentage
total = english + maths + science + social + computer
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'Fail'

# Print the marksheet
print("\n========== MARKSHEET ==========")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("--------------------------------")
print("English        :", english)
print("Maths          :", maths)
print("Science        :", science)
print("Social Studies :", social)
print("Computer       :", computer)
print("--------------------------------")
print("Total Marks    :", total, "/ 500")
print("Percentage     :", percentage, "%")
print("Grade          :", grade)
print("================================")
