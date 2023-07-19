import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # List of usernames and passwords
    credentials = [
        {'username': 'user1', 'password': 'pass1'},
        {'username': 'user2', 'password': 'pass2'},
        {'username': 'user3', 'password': 'pass3'}
    ]

    for cred in credentials:
        if cred['username'] == username and cred['password'] == password:
            messagebox.showinfo("Login Successful", "Login Successful!")
            return

    messagebox.showerror("Invalid Credentials", "Invalid username or password.")

# Create a tkinter window
window = tk.Tk()
window.title("Login")

# Create username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(window, text="Submit", command=login)
submit_button.pack()

# Run the tkinter event loop
window.mainloop()
