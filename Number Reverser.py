# number reverser 

num = int(input("enter your number:"))
reverse = 0
is_negative = num < 0
num = abs(num)
while num!= 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if is_negative:
    reverse = -reverse
print("reverse number:",reverse)

