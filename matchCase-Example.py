print(''' 
    + Add
    - Sub
    * Mul
    / Div

''')

num1 = eval(input('Enter the value1:-'))  
num2 = eval(input('Enter the value2:-'))
userCh = input('Enter the user choice:- ') # +,-,*,/
# print(num1)
# print(num2)
# print(opr)

match userCh:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case _:
        print("Invalid Opr")