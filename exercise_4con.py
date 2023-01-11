import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"{abs(number1)} is greater than {abs(number2)}")
else:
    print(f"{abs(number2)} is greater than {abs(number1)}")