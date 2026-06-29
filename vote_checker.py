import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    nationality = nationality_entry.get().strip().lower()

    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Please enter a valid age.")
        return

    age = int(age)

    if age >= 18 and nationality == "indian":
        result = f"✅ Hello {name}, you are Eligible to Vote."
        result_label.config(text=result, fg="green")
    else:
        result = f"❌ Hello {name}, you are Not Eligible to Vote."
        result_label.config(text=result, fg="red")


# Create Window
root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Voting Eligibility Checker",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Name
tk.Label(root, text="Name:", font=("Arial", 11)).pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Age
tk.Label(root, text="Age:", font=("Arial", 11)).pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

# Nationality
tk.Label(root, text="Nationality:", font=("Arial", 11)).pack()
nationality_entry = tk.Entry(root, width=30)
nationality_entry.pack(pady=5)

# Button
check_button = tk.Button(
    root,
    text="Check Eligibility",
    command=check_eligibility,
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold")
)
check_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()