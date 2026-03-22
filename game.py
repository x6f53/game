#I acknowledge the use of
#Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/)
#to create the code in this file
import random

number = random.randint(1, 5)

while True:
    guess = int(input("Guess a number between 1 and 5: "))
    
    if guess == number:
        print("Correct!")
        break
    else:
        print("Try again")
