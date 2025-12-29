# Men-Driven Calculator (using if - elif - else)
print(''' 
    + Add
    - Sub
    * Mul
    / Div

''')

num1 = eval(input('Enter the value1:-'))  
num2 = eval(input('Enter the value2:-'))
userCh = input('Enter the user choice:- ') # +,-,*,/

if userCh=="+":
    print(num1+num2)
elif userCh=="-":
    print(num1-num2)
elif userCh=="*":
    print(num1*num2)
elif userCh=="/":
    print(num1/num2)
else:
    print("Invalid Operation")