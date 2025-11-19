"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Develop a sample user interface for an enterprise software system that aligns with MetaCode's focus on simplicity and usability.
Generated: DETERMINISTIC_bf0c6b1861b73443
Batch ID: 20250612_153224
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

class EnterpriseApp:
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Enterprise Software System")
        self.root.geometry("600x400")
        
        # Create a title label
        self.title_label = tk.Label(root, text="Welcome to MetaCode Enterprise System", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Create a frame for user input
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Create a label and entry for username
        self.username_label = tk.Label(self.input_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.input_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label and entry for password
        self.password_label = tk.Label(self.input_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.input_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create a login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        # Create a status label
        self.status_label = tk.Label(root, text="", fg="red")
        self.status_label.pack(pady=10)

    def login(self):
        """Handle the login process."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple validation
        if not username or not password:
            self.status_label.config(text="Username and password cannot be empty.")
            return

        # Simulate a login process (replace with actual authentication logic)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to the system!")
            self.status_label.config(text="", fg="green")
        else:
            self.status_label.config(text="Invalid username or password.")

if __name__ == "__main__":
    # Create the main application window
    try:
        root = tk.Tk()
        app = EnterpriseApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
```
