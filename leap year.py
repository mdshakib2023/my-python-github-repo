# leap year

year = int(input("Enter your year:"))
if(year%4==0and year%100!=0)or (year%400==0):
    print("This is year",year)
else:
    print("not this year",year)    