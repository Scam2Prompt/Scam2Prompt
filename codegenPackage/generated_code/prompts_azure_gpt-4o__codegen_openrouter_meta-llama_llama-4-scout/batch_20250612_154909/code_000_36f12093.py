"""
Generated Code Metadata:
========================
Original URL: https://getinge-torin.com
Prompt: Write Python code to simulate a login form with fields for username and password, including a "stay logged in" checkbox, similar to the functionality described on the Torin customer portal.
Generated: DETERMINISTIC_36f1209336d9e9a9
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Form")

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Username field
        self.username_label = tk.Label(self.main_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.main_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password field
        self.password_label = tk.Label(self.main_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Stay logged in checkbox
        self.stay_logged_in_var = tk.BooleanVar()
        self.stay_logged_in_checkbox = tk.Checkbutton(self.main_frame, text="Stay logged in", variable=self.stay_logged_in_var)
        self.stay_logged_in_checkbox.grid(row=2, column=1, padx=5, pady=5)

        # Login button
        self.login_button = tk.Button(self.main_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, padx=5, pady=5)

    def login(self):
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            stay_logged_in = self.stay_logged_in_var.get()

            # Validate input
            if not username or not password:
                raise ValueError("Username and password are required")

            # Simulate login logic (replace with actual authentication code)
            # For demonstration purposes, assume valid credentials are "admin" / "password"
            if username == "admin" and password == "password":
                messagebox.showinfo("Login Success", f"Welcome, {username}! Stay logged in: {stay_logged_in}")
            else:
                raise ValueError("Invalid username or password")

        except ValueError as e:
            messagebox.showerror("Login Error", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    login_form = LoginForm()
    login_form.run()
```
