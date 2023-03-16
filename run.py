# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import pyfiglet
from termcolor import colored


def Welcome():
    """
    Function to display home page
    """
    title = "Welcome  to  NUMBER  GUESSING  GAME "
    print(colored(pyfiglet.figlet_format(title), "green"))

Welcome()
name = input(" Please Enter your name :  ")
print("Welcome", name, "to this 'Number Guessing Game'")
playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("Okay! Let's start to  play game ! :")
top_of_range = input("Type a number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, 11)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You got it wrong!")

print("You got it in", guesses, "guesses")
