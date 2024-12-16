# Write a program that asks a user to enter a number.
# Your program will then double that number and print out the result.
# It will repeat that process until the value is 100 or greater.

while True:
    user = input("Enter number: ")
    if user.isdigit():
        user = int(user)
        break
    else:
        print("Not a number")

while True:
    print(user)
    if user >= 100:
        break
    else:
        user += user