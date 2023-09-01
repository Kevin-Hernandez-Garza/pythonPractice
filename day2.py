# In this project I create a tip calculator

# This program takes in the bill amount, tip percentage, and the number of people being split

# This total amount is the printed out on the console
# which calculates the amount owed by each individual.
bill_amount = float(input("How much is the bill? "))

tip = int(input("How much would you like to tip? (12%, 20%, or 25%) "))

people_share = int(input(
    "Among how many people would you like to split the bill with? "))

calculation = (bill_amount / people_share *
               (tip / 100)) + (bill_amount / people_share)

total = "{:.2f}".format(calculation)

print(f"Each person should pay the following amount: ${total}")
