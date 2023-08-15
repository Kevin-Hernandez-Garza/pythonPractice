# In this project I create a tip calculator

# This program takes in the bill amount, tip percentage, and the number of people being split

# This total amount is the printed out on the console 
# which calculates the amount owed by each individual. 

bill_amount = input("How much is the bill? ")

tip = input("How much would you like to tip? (12%, 20%, or 25%) ")

people_share = input(
    "Among how many people would you like to split the bill with? ")

total = ((float(bill_amount) / int(people_share)) *
         (int(tip) / 100)) + (float(bill_amount) / int(people_share))

print("{:.2f}".format(total))
