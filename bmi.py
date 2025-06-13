# bmi calculator 

height = float(input("Enter your height meters:"))
weight = float(input("Enter your weight kg:"))

bmi = weight / (height ** 2)
print("Your BMI is:",bmi)
if bmi <= 18.5:
    print("Your BMI is underweight.")
elif bmi <= 18.5 and bmi <= 24.9:
    print("Your BMI is normaleight.") 
elif bmi <=25 and bmi <= 29.9:
    print("Your BMI is overweight. ") 
else:
    print("Your BMI is obese.")