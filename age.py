# age

age = int(input("Enter your age:"))

if age >= 0 and age <=1:
    print("infant")
elif age >= 2 and age <=3:
    print("toddler")    
elif age >= 4 and age <=12:
    print("child")
elif age >= 13 and age <=19:
    print("teenager")   
elif age >= 20:
    print("adult")
else:
    print("ended")        
    