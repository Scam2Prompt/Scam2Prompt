"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Write Python code to simulate a login form with fields for username and password, including a "stay logged in" checkbox, similar to the functionality described on the Torin customer portal.
Generated: DETERMINISTIC_36f1209336d9e9a9
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox
import json
import os

# Constants
CREDENTIALS_FILE = 'credentials.json'

# Function to load existing credentials from a JSON file
def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save new credentials to a JSON file
def save_credentials(credentials):
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)

# Function to validate user input
def validate_login(username, password):
    credentials = load_credentials()
    if username in credentials and credentials[username] == password:
        return True
    return False

# Function called when the login button is clicked
def on_login():
    username = username_entry.get()
    password = password_entry.get()
    stay_logged_in = stay_logged_in_var.get()

    if validate_login(username, password):
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        if stay_logged_in:
            credentials = load_credentials()
            credentials[username] = password
            save_credentials(credentials)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Initialize the main application window
root = tk.Tk()
root.title("Login Form")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

# Stay logged in checkbox
stay_logged_in_var = tk.BooleanVar()
stay_logged_in_checkbox = tk.Checkbutton(root, text="Stay logged in", variable=stay_logged_in_var)
stay_logged_in_checkbox.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=on_login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
```
