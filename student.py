# Student Details Program

# Taking student details as input
name = input("Enter Student Name: ")
dob = input("Enter Date of Birth (DD/MM/YYYY): ")
usn = input("Enter USN Number: ")
department = input("Enter Department: ")


marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5


print("\n----- Student Details -----")
print("Name       :", name)
print("DOB        :", dob)
print("USN        :", usn)
print("Department :", department)

print("\nMarks in 5 Subjects:")
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")

print("\nTotal Marks :", total)
print("Percentage  :", percentage, "%")