"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a Python script to create a form for customers to register for a test drive of MG cars, including fields for name, email, phone number, and preferred car model (e.g., MG5, MG ZS, MG RX5).
Generated: DETERMINISTIC_51972ed441bf48e4
Batch ID: 20250612_153517
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
import re

class TestDriveForm:
    def __init__(self, master):
        """Initialize the Test Drive Form application."""
        self.master = master
        self.master.title("MG Cars Test Drive Registration")

        # Create and place labels and entry fields for the form
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the form widgets."""
        # Name Field
        tk.Label(self.master, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email Field
        tk.Label(self.master, text="Email:").grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Phone Number Field
        tk.Label(self.master, text="Phone Number:").grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)

        # Preferred Car Model Field
        tk.Label(self.master, text="Preferred Car Model:").grid(row=3, column=0, padx=10, pady=10)
        self.car_model_entry = tk.Entry(self.master)
        self.car_model_entry.grid(row=3, column=1, padx=10, pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.master, text="Register", command=self.submit_form)
        self.submit_button.grid(row=4, columnspan=2, pady=20)

    def submit_form(self):
        """Handle the form submission, validate input, and display messages."""
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        car_model = self.car_model_entry.get()

        # Validate the inputs
        if not self.validate_input(name, email, phone, car_model):
            return

        # Simulate form submission (could be an API call in real application)
        messagebox.showinfo("Success", "Thank you for registering for a test drive!")

        # Clear the form
        self.clear_form()

    def validate_input(self, name, email, phone, car_model):
        """Validate user input data and show error messages if any."""
        if not name:
            messagebox.showerror("Input Error", "Name is required.")
            return False

        if not self.validate_email(email):
            messagebox.showerror("Input Error", "Invalid email address.")
            return False

        if not self.validate_phone(phone):
            messagebox.showerror("Input Error", "Invalid phone number.")
            return False

        if not car_model:
            messagebox.showerror("Input Error", "Preferred car model is required.")
            return False

        return True

    @staticmethod
    def validate_email(email):
        """Validate the email format."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_phone(phone):
        """Validate the phone number format."""
        phone_regex = r'^\+?[0-9]{10,15}$'
        return re.match(phone_regex, phone) is not None

    def clear_form(self):
        """Clear the input fields in the form."""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.car_model_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TestDriveForm(master=root)
    root.mainloop()
```
