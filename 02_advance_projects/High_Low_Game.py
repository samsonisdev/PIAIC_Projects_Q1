# Two numbers are generated from 1 to 100 (inclusive on both ends):
# one for you and one for a computer, who will be your opponent.
# You can see your number, but not the computer's!
# You make a guess, saying your number is either higher than or lower than the computer's number
# If your guess matches the truth
# (ex. you guess your number is higher, and then your number is actually higher than the computer's)
# you get a point!
# These steps make up one round of the game.
# The game is over after all rounds have been played.
# E.g:
# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
# Your score is now 1

import random

user_no = random.randint(0, 99)
score = 0
rounds = 5

def high_low_game(score):
    print("============================")
    print("Welcome To The High-Low Game")
    print("============================")

    print("Your number is: ", user_no)
    for i in range(rounds):
        comp_no = random.randint(0, 99)
        print("------------------------")
        print(f"-Round {i+1}:")
        guess = input("Is your number lower or higher than the computer's? ").lower()
        if guess == 'lower':
            if user_no < comp_no:
                print("Correct! Computer number was: ", comp_no)
                score += 1
            elif user_no > comp_no:
                print("Wrong! Computer number was: ", comp_no)
        elif guess == 'higher':
            if user_no > comp_no:
                print("Correct! Computer number was: ", comp_no)
                score += 1
            elif user_no < comp_no:
                print("Wrong! Computer number was: ", comp_no)
        else:
            print("Invalid!")

    print(f"Your score is: {score}/{rounds}")

high_low_game(score)
