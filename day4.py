# importing the random module
# import random

# # random number from 1-10
# random_int = random.randint(1, 10)
# print(random_int)


# # random  number from 0.0-1.0
# random_float = random.random()
# print(random_float)

# random number number between 0.0-5.0
# random_float = random.random() * 5
# print(random_float)

# a heads or tails games, importing the random module
# import random

# coin_toss = random.randint(0, 1)
# if coin_toss == 1:
#     print('Heads')
# else:
#     print('Tails')

# Banker Roulette Program (below)
# Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma: ")
# names = names_string.split(", ")

# # storing the length of the list
# length = len(names)

# # getting a random number from the total length
# choice = random.randint(0, length)

# # printing out the index that was randomly chosen
# print(f'{names[choice]} is going to buy the meal today!')


# nested list
fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
