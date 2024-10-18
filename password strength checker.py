import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    errors = []


    if len(password) < 12:
        errors.append("Password should be at least  12 characters long.")
    else:
        strength += 1


    if not any(char.isdigit() for char in password):
        errors.append("Password should contain at least one digit.")
    else:
        strength += 1


    if not any(char.isupper() for char in password):
        errors.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1


    if not any(char.islower() for char in password):
        errors.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1


    if not any(not char.isalnum() for char in password):
        errors.append("Password should contain at least one special character.")
    else:
        strength += 1

    return strength, errors

def check_password():
    password = password_entry.get()
    strength, errors = check_password_strength(password)

    if strength == 5:
        result_label.config(text="Password strength: Strong", fg="green")
    elif strength >= 3:
        result_label.config(text="Password strength: Medium", fg="purple")
    else:
        result_label.config(text="Password strength: Weak", fg="red")

    error_text.delete(1.0, tk.END)
    for error in errors:
        error_text.insert(tk.END, error + "\n")

root = (tk.Tk)()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.Button(root, text="Check password", command=check_password)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

error_text = tk.Text(root, height=5, width=40)
error_text.pack()

root.mainloop()

