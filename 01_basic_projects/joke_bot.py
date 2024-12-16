# Write a simple joke bot.
# The bot starts by asking the user what they want.
# However, your program will only respond to one response: Joke.

joke = """Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12.
Sophia returns with 13 liters of milk.
The programmer asks why and Sophia replies: 'because they had eggs'"""

user = input("What do you want? ").lower()
# if user == 'joke':
#     print(joke)
# else:
#     print("Sorry! I only tell jokes")

# --- OR ---

user_input = user.strip().lower()

if "joke" in user_input:
    print(joke)
else:
    print("SORRY")

