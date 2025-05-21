#Sum of Digits
num = 608732
digit = 0
while num!=0:
    num //=10
    print(num)
    digit+=1
    print(digit)
print("sum of digit:",digit)   