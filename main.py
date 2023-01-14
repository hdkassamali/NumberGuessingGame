# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_list = []
for number in range(1, 101):
    number_list.append(number)

random_number = random.choice(number_list)
print(f"Psst the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_lives = 10
else:
    number_of_lives = 5
game_over = False

while not game_over:
    print(f"You have {number_of_lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if random_number == user_guess:
        print(f"You got it! The answer was {user_guess}.")
        game_over = True
    else:
        if user_guess > random_number:
            print("Too high.")
            number_of_lives -= 1
        elif user_guess < random_number:
            print("Too low.")
            number_of_lives -= 1
    if number_of_lives > 0 and game_over is not True:
        print("Guess again.")
    elif number_of_lives < 1:
        print("You've run out of guesses, you lose.")
        game_over = True

