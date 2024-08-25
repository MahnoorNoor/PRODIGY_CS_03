import tkinter as tk
from tkinter import messagebox

# Functions for checking password criteria
def check_length(password):
    return len(password) >= 8

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_numbers(password):
    return any(char.isdigit() for char in password)

def has_special_chars(password):
    special_characters = "!@#$%^&*()-_+=<>?/.,"
    return any(char in special_characters for char in password)

def assess_password(password):
    length = check_length(password)
    uppercase = has_uppercase(password)
    lowercase = has_lowercase(password)
    numbers = has_numbers(password)
    special_chars = has_special_chars(password)
    
    if all([length, uppercase, lowercase, numbers, special_chars]):
        return "Strong Password"
    elif length and (uppercase or lowercase) and (numbers or special_chars):
        return "Moderate Password"
    else:
        return "Weak Password"

def detailed_feedback(password):
    feedback = []
    
    if not check_length(password):
        feedback.append("Password should be at least 8 characters long.")
    if not has_uppercase(password):
        feedback.append("Password should include uppercase letters.")
    if not has_lowercase(password):
        feedback.append("Password should include lowercase letters.")
    if not has_numbers(password):
        feedback.append("Password should include numbers.")
    if not has_special_chars(password):
        feedback.append("Password should include special characters.")
    
    return feedback if feedback else ["Your password is strong!"]

# Function to check password strength when the button is clicked
def check_password_strength():
    password = password_entry.get()
    password_strength = assess_password(password)
    feedback = detailed_feedback(password)
    feedback_message = "\n".join(feedback)
    messagebox.showinfo("Password Strength", f"Password Strength: {password_strength}\n\n{feedback_message}")

# Set up the GUI window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("500x300")

# Add a label and entry for the password
tk.Label(root, text="Enter your password:").pack(pady=10)
password_entry = tk.Entry(root, show='*', width=40)
password_entry.pack(pady=10)

# Add a button to check the password strength
tk.Button(root, text="Check Password Strength", command=check_password_strength).pack(pady=20)

# Start the GUI loop
root.mainloop()
