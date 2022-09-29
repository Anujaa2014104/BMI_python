name = input("Enter your Name :")
age = int(input("Enter your age :"))
weight = float(input("Enter your weight in Kg :"))
h1 = float(input("Enter your height in Cm :"))
h2 = h1 / 100
h3 = h2*h2
BMI = weight /h3
print("your Body Mass Index [BMI] is   ",BMI)
if(BMI<18):
    print("UNDER WEIGHT")
elif(BMI>=18 and BMI<=25):
    print("NORMAL and FIT ")
elif(BMI>25 and BMI<=30):
    print("FAT")
elif(BMI>30):
    print("OVER WEIGHT")
else:
    print("INVALID INPUT")
