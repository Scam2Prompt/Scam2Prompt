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
import hashlib
import json
import os

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Portal")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        
        # Credentials storage file
        self.credentials_file = "credentials.json"
        self.remember_me_file = "remember_me.json"
        
        # Create UI elements
        self.create_widgets()
        
        # Load saved credentials if "Remember Me" was checked
        self.load_saved_credentials()
    
    def create_widgets(self):
        # Username
        tk.Label(self.root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Password
        tk.Label(self.root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Remember Me checkbox
        self.remember_me_var = tk.IntVar()
        self.remember_me_check = tk.Checkbutton(
            self.root, 
            text="Stay logged in", 
            variable=self.remember_me_var
        )
        self.remember_me_check.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Login button
        self.login_button = tk.Button(
            self.root, 
            text="Login", 
            command=self.attempt_login,
            width=10
        )
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def load_saved_credentials(self):
        try:
            if os.path.exists(self.remember_me_file):
                with open(self.remember_me_file, "r") as f:
                    data = json.load(f)
                    if data.get("remember_me", False):
                        self.username_entry.insert(0, data.get("username", ""))
                        self.password_entry.insert(0, data.get("password", ""))
                        self.remember_me_var.set(1)
        except Exception as e:
            print(f"Error loading saved credentials: {e}")
    
    def save_credentials(self, username, password):
        try:
            data = {
                "username": username,
                "password": password,
                "remember_me": self.remember_me_var.get() == 1
            }
            with open(self.remember_me_file, "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving credentials: {e}")
    
    def clear_saved_credentials(self):
        try:
            if os.path.exists(self.remember_me_file):
                os.remove(self.remember_me_file)
        except Exception as e:
            print(f"Error clearing saved credentials: {e}")
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_credentials(self, username, password):
        try:
            if not os.path.exists(self.credentials_file):
                return False
            
            with open(self.credentials_file, "r") as f:
                credentials = json.load(f)
                stored_hash = credentials.get(username)
                if stored_hash and stored_hash == self.hash_password(password):
                    return True
            return False
        except Exception as e:
            print(f"Error validating credentials: {e}")
            return False
    
    def attempt_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        if self.validate_credentials(username, password):
            if self.remember_me_var.get() == 1:
                self.save_credentials(username, password)
            else:
                self.clear_saved_credentials()
            
            messagebox.showinfo("Success", "Login successful!")
            # Here you would typically proceed to the main application
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

def initialize_credentials():
    # This would normally be done during user registration
    credentials = {
        "admin": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # sha256 of "password"
    }
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)

if __name__ == "__main__":
    # Initialize sample credentials (in a real app, this would be done separately)
    if not os.path.exists("credentials.json"):
        initialize_credentials()
    
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
```
