"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-xi-wine.vercel.app
Prompt: Generate code to create a user interface for securing whitelist spots, inspired by "Secret Base Society."
Generated: DETERMINISTIC_6775783c6914e3bf
Batch ID: 20250612_153606
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

class WhitelistApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Whitelist Management")
        self.master.geometry("400x300")

        # Label for user instructions
        self.label = tk.Label(master, text="Enter your email to secure a whitelist spot:")
        self.label.pack(pady=10)

        # Entry field for email input
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.pack(pady=10)

        # Button to submit the email
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_email)
        self.submit_button.pack(pady=10)

        # Status label to show the result
        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=10)

    def submit_email(self):
        """Handle email submission and check validity."""
        email = self.email_entry.get()
        
        if self.validate_email(email):
            self.status_label.config(text="Email submitted successfully!", fg="green")
            # Further processing can be done here, like saving the email to a database
        else:
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            self.status_label.config(text="")

    def validate_email(self, email):
        """Validate the provided email format."""
        # Simple email validation pattern
        if "@" in email and "." in email:
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    
    # Create and run the whitelist application
    app = WhitelistApp(master=root)
    root.mainloop()
```
