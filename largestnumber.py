# the largest number

a = int(input("Enter your frist number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number"))

if(a>=b and a>=c):
    print("First number is largest",a)
elif(b>=c):
    print("Second number is largest",b) 
else:
    print("Third number is lagest",c)   