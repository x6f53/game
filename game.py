#I acknowledge the use of
#Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/)
#to create the code in this file
import random

number = random.randint(1, 5)
attempts = 0
while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    
    if guess == number:
        print("Correct! Attempts:", attempts)
        break
