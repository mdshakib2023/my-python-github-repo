#Sum of Digits
num = int(input("enter your number:"))
sum = 0
num = abs(num)
while num!= 0:
    digit = num %10
    sum  += digit
    num //= 10
print("sum of digit",sum)

