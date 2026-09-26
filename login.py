import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# Correct username / password (you can change it)
VALID_USERNAME = "play"
VALID_PASSWORD = "1234"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Success", "Login successful!")

        # Run game.py
        # link the game.py------
        subprocess.Popen([sys.executable, "game.py"])

        root.destroy()  # close login window
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# ---------------- GUI Window ----------------
root = tk.Tk()
root.title("Memory Game Login")
root.geometry("350x250")

tk.Label(root, text="LOGIN", font=("Arial", 20)).pack(pady=10)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login, width=12).pack(pady=20)

root.mainloop()
