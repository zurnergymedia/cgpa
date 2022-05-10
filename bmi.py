name = input('Please, enter your name: ')
print('Hello, ' + name + ". Let's calculate your BMI.")

height = float(input("Please, enter your height: "))

weight = int(input("Please, enter your weight: "))
bmi = (weight / (height ** 2))

print('Hello, ' + name + '. Your BMI is ' + str(round(bmi,1)))

if (bmi >= 30):
    print('You appear to be obese.')
    print('You should see a doctor.')
elif (bmi < 30 and bmi >= 25):
    print('You appear to be overweight.')
    print('You should see a doctor.')
elif (bmi < 25 and bmi >= 18.5):
    print('You weight appears to be normal.')
else:
    print('You appear to be underweight.')
    print('You should see a doctor.')
