# # This is a small program calculating your BMI.

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese!")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese!")


# # This program determines whether a year is a leap year
# year = int(input("What year were you born? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("It is a leap year! ")
#         else:
#             print("Not a leap year!")
#     else:
#         print("It is a leap year! ")
# else:
#     print("Not a leap year! ")


# The following program calculates the user's pizza order price
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S' or size == 's':
    pizza_prize = 15
    if add_pepperoni == 'y' or add_pepperoni == 'Y':
        pizza_prize += 2
if size == 'M' or size == 'm':
    pizza_prize = 20
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        pizza_prize += 3
if size == 'L' or size == 'l':
    pizza_prize = 25
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        pizza_prize += 3
if extra_cheese == 'y' or extra_cheese == 'Y':
    pizza_prize += 1

print(f"Your final bill is: ${pizza_prize}")
