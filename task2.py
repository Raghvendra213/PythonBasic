# Check if a year is a leap year or not.

year = eval(input("Enter the number:-"))

if (year % 400 == 0) or (year%4==0 and year%100!=0):
    print(year,"Its a leap year")
else:
    print(year,"Its not a leap year")