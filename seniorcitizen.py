

from datetime import date   # import is correct


name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))


current_year = date.today().year

age = current_year - year_of_birth


print("\n----- Result -----")
print("Name:", name)
print("Age :", age)

if age >= 60:
    print("Status: Senior Citizen")
else:
    print("Status: Not a Senior Citizen")