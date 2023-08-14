import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return
    
    password = generate_password(length)
    password_label.config(text="Generated Password: " + password)

# Create the main GUI window
root = tk.Tk()
root.title("Password Generator")

# Change window background color
root.configure(bg='lightgray')

# Create and configure frames
input_frame = tk.Frame(root)
output_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)
output_frame.pack(padx=20, pady=(0, 20))

# Create widgets
length_label = tk.Label(input_frame, text="Enter password length:", bg='lightgray')
length_entry = tk.Entry(input_frame)
generate_button = tk.Button(input_frame, text="Generate Password", command=generate_button_click, bg='blue', fg='white')
password_label = tk.Label(output_frame, text="Generated Password: ", wraplength=300, justify='center', font=('Helvetica', 12, 'bold'), bg='lightgray')

# Place widgets using grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
password_label.grid(row=0, column=0, padx=10, pady=10)

# Configure grid weights for responsive layout
root.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
output_frame.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
root.mainloop()
