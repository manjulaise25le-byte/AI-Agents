import tkinter as tk
from tkinter import messagebox
import time
import random
import threading

# -------------------- MEMORY GAME CODE --------------------

words_list = [
    "apple", "ball", "cat", "dog", "fish", "hat", "ice", "jug", "kite", "lion","Mango","Bus","Car"
]

def play_round(round_num, length=4):
    words = random.sample(words_list, length)
    print(f"Round {round_num}: Remember these words in order:")
    print(words)
    time.sleep(4)

    print("\n" * 100)

    correct = 0
    for i, word in enumerate(words):
        guess = input(f"Enter word {i + 1}: ").strip().lower()
        if guess == word:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong, the correct word was '{word}'.")

    print(f"\nYou remembered {correct} out of {length} words correctly.\n")

    return correct == length

def memory_game():
    name = input("Enter your name: ").strip()
    print(f"\nWelcome {name}! Let's start the memory game.\n")
    time.sleep(1)

    rounds = random.randint(5, 8)
    print(f"You will play {rounds} rounds of the memory game.\n")
    time.sleep(2)

    full_success = 0
    for round_num in range(1, rounds + 1):
        success = play_round(round_num)
        if success:
            print(f"Great job, {name}! You won round {round_num}!\n")
            full_success += 1
        else:
            print(f"Round {round_num} completed. Keep practicing!\n")
        time.sleep(2)

    print(f"Game over, {name}! You perfectly remembered {full_success} rounds out of {rounds}.")

# -------------------- LOGIN PAGE CODE --------------------

VALID_USERNAME = "player"
VALID_PASSWORD = "1234"

def start_game_thread():
    """Start the memory game in a separate thread after closing GUI"""
    root.destroy()
    threading.Thread(target=memory_game).start()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome to the Memory Game!")
        start_game_thread()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# -------------------- GUI WINDOW --------------------

root = tk.Tk()
root.title("Memory Game - Login")
root.geometry("330x260")

tk.Label(root, text="LOGIN", font=("Arial", 20)).pack(pady=10)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login, width=15).pack(pady=20)

root.mainloop()
