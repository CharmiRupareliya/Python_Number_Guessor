import random

top_of_range = input("Enter top range you want to go: ")
print()

# Checking if the input provided by the user is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Converting the input string to an integer

    if top_of_range <= 0:
        print("Please type a number larger than zero.")

else:
    print("Please type a number.")

random_num = random.randint(0,top_of_range)  # Generate a random number between 0 and the user-defined top range (inclusive)
guesses = 0

while True:   # Start an infinite loop for the user to keep guessing
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():    # Check if the user guess is a digit
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue

    if user_guess == random_num:    # Check if the user's guess matches the randomly generated number
        print("You got it !!!")
        break

    elif user_guess > random_num:  # Provide feedback if the user's guess is higher than the random number
        print("You were above the number !")

    else:    # Provide feedback if the user's guess is lower than the random number
        print("Yo were below the number ! ")

    print()

print("You got it in", guesses, "guesses")