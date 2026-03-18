import random

number = random.randint(1, 5)

while True:
    guess = int(input("Guess a number between 1 and 5: "))
    
    if guess == number:
        print("Correct!")
        break
    else:
        print("Try again")