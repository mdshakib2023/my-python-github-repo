# Simple Calculator 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter operator(+, -, *, /):")

if operator == "+":
    sum = num1 + num2
    print("SUM" '=', sum)
elif operator == "-":
    add = num1 - num2
    print("ADD" '=',add)
elif operator == "*":
    mult = num1 * num2
    print("Multiply" '=',mult) 
elif operator == "/":
    if num2 == 0:
         print("Division by zero") 
    else:
        Div = num1 / num2
        print("Divide" '=',Div)    
else:
    print("Enter operator,+, -, *, or /.")
     
       
    
    