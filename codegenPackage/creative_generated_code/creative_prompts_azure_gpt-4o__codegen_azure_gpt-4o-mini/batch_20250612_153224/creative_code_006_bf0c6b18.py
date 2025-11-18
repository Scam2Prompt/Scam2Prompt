"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Develop a sample user interface for an enterprise software system that aligns with MetaCode's focus on simplicity and usability.
Generated: DETERMINISTIC_bf0c6b1861b73443
Batch ID: 20250612_153224
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

class EnterpriseApp(tk.Tk):
    """Main application class for the enterprise software system."""

    def __init__(self):
        """Initialize the main application window."""
        super().__init__()
        self.title("Enterprise Software System")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        """Create and place widgets in the application window."""
        
        # Title Label
        title_label = tk.Label(self, text="Welcome to MetaCode", font=("Arial", 16), bg="#f0f0f0")
        title_label.pack(pady=20)

        # User Input Section
        self.username_label = tk.Label(self, text="Username:", bg="#f0f0f0")
        self.username_label.pack(pady=(10, 0))
        
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:", bg="#f0f0f0")
        self.password_label.pack(pady=(10, 0))
        
        self.password_entry = tk.Entry(self, show='*', width=30)
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=5)

    def login(self):
        """Handle user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Basic validation for empty fields
        if not username or not password:
            messagebox.showerror("Input Error", "Please enter both username and password.")
            return

        # Here you could add authentication logic
        # For demonstration, we'll assume successful login if both fields are filled
        messagebox.showinfo("Login Success", f"Welcome, {username}!")

    def exit_app(self):
        """Exit the application."""
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.destroy()

if __name__ == "__main__":
    try:
        app = EnterpriseApp()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
```
