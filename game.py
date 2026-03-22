import random

number = random.randint(1, 5)
attempts = 0
while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    
    if guess == number:
        print("Correct! Attempts:", attempts)
        break