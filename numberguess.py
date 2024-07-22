import random
answer = random.randint(1,20)
attempts = 0
print("Welcome to the game!")
print('The goal of the game is to guess a random number between 1 and 20.')

while True:
    try:    
        guess = int(input("What is your guess? "))
    except ValueError:
        print("Please enter an integer.")
        continue
    attempts += 1
    if answer < guess:
        print("Go lower and try again.")
    if answer > guess:
        print("Go higher and try again.")
    if answer == guess:
        print(f"Congratulations! It took you {attempts} attempts to guess the number.")
        break
    if guess > 20:
        print("Your guess must be under 20.")
    if answer == 1:
        print(f"Congratulations! It took you {attempts} attempt to guess the number.")
        break
    