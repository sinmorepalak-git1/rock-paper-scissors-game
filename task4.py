import tkinter as tk
import random


choices = ['Rock', 'Paper', 'Scissors']


def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")
root.configure(bg="lightblue")


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)


rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play('Scissors'))
scissors_button.pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=20)


root.mainloop()