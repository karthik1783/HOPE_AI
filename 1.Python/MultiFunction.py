class SubfieldsInAI():
    def printSubList():
        print("Sub-fields in AI are:")
        subFieldList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for item in subFieldList:
            print(item)

class FindOddOrEven():
    def findOddOrEven(number):
        if((number%2)!=0):
            print(number,"is Odd number")
        else:
            print(number,"is Even number")

class FindMarriageEligibility():
    def checkMarriageEligibility(gender,age):
        if(gender=="Male"): # == operator checks with 'case sensitive'
            if(age>=21):
                print("Eligible...")
            else:
                print("Not Eligible...")
        elif(gender=="Female"):
            if(age>=18):
                print("Eligible...")
            else:
                print("Not Eligible...")
        else:
             print("Either Male nor Female marriage eligibility only system checks at this moment...")

class CalculatePercentage():
    def calculatePercentage(markList):
        summary=int(0)
        for mark in markList:
            summary=summary+int(mark)
        totalSubjects=len(markList)
        average=(summary/totalSubjects)
        return average
        