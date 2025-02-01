class sampleClass(): #Class 1
    def findAgeCategory(): #Procedure 1
        age=int(input("Enter your age:"))
        # Function body/task/procedure/formula
        if(age<18):
            category="Minor"
        elif(age<35):
            category="Adult"
        elif(age<55):
            category="Citizen"
        else:
            category="Senior Citizen"
        return category

    def multiplication(number1,number2): #Procedure 2
        result=number1*number2
        print(result)

class bmiClass(): #Class 2
    def calculateBMI(): #Procedure 1
        weight=float(input("Enter your weight in kg"))
        heightInCM=float(input("Enter your height in cm"))
        #convert the height from cm to meter
        heightInMeter=(heightInCM/100)
        #calculate the BMI
        bmi=(weight/(heightInMeter*heightInMeter))
        roundedBMI=round(bmi,2)
        #round of bmi with 2 decimal value
        print("Your weight(in Kg):",weight)
        print("Your Height(in cm):",heightInCM)
        print("Your BMI index is:",roundedBMI)
        return roundedBMI

    def classifyBMI(bmiIndex): # parameterized function defintion/Function with argument(s) #Procedure 2
        print("Your BMI classification based on your BMI index is as below:-")
        #check the bmi classification
        if (bmiIndex < 18.5): #Condition 1
            classification="Underweight"
        elif (18.5 <= bmiIndex < 24.9): #Condition 2
            classification="Normal weight"
        elif (25 <= bmiIndex < 29.9): #Condition 3
            classification="Overweight"
        elif (30 <= bmiIndex < 34.9): #Condition 4
            classification="Obesity: Mild (Class 1)"
        elif (35 <= bmiIndex < 39.9): #Condition 5
            classification="Obesity: Moderate (Class 2)"
        else:
            classification="Obesity: Morbid (Class 2)" # >=40
        return classification