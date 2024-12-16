# Guess My Number
# I am thinking of a number between 0 and 99...
# Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

import random

num = random.randint(0, 99)

print("---GUESS THE NUMBER IN 6 GUESSES---")

for i in range(6, 0, -1):
    guess = input(f"{i}. Guess the number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Not a number!")
        continue

    if guess == num:
        print(f"Congrats! The number was: {num}")
        break
    elif guess < num:
        print("Your guess is lower")
    elif guess > num:
        print("Your guess is higher")

else:
    print(f"Oh! Sorry! The number was {num}")

# -- OR --

# secret_number: int = random.randint(1, 99)
#
# print("I am thinking of a number between 1 and 99...")
#
# guess = int(input("Enter a guess: "))
#
# while guess != secret_number:
#     if guess < secret_number:
#         print("Your guess is too low")
#     else:
#         print("Your guess is too high")
#
#     print()
#     guess: int = int(input("Enter a new guess: "))
#
# print("Congrats! The number was: " + str(secret_number))