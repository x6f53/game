import random

number = random.randint(1, 5)

guess = int(input("Guess a number between 1 and 5: "))

if guess == number:
    print("Correct!")
else:
    print("Wrong! The number was", number)