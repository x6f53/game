import tkinter as tk
import random

number = random.randint(1, 5)

def check_guess():
    guess = int(entry.get())
    if guess == number:
        result.config(text="Correct!")
    else:
        result.config(text="Try again")

root = tk.Tk()
root.title("Guessing Game")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=check_guess)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()