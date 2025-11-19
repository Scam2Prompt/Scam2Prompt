"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write a Python script to create a reservation form for horse riding tours, including fields for tour options like "Laguna Ride," "Cowboy Experience," and "Skiing & Riding Experience," as described on the Chile Horse Riding website.
Generated: DETERMINISTIC_c1e7cd5a928f69d8
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

class HorseRidingReservation:
    def __init__(self, master):
        self.master = master
        master.title("Horse Riding Tour Reservation Form")

        # Tour options
        self.tour_options = {
            "Laguna Ride": 100,
            "Cowboy Experience": 150,
            "Skiing & Riding Experience": 200
        }

        # Create and place labels and entry fields
        self.create_widgets()

    def create_widgets(self):
        # Name label and entry
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email label and entry
        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Tour option label and dropdown
        self.tour_label = tk.Label(self.master, text="Select Tour:")
        self.tour_label.grid(row=2, column=0, padx=10, pady=10)
        self.tour_var = tk.StringVar(value=list(self.tour_options.keys())[0])
        self.tour_menu = tk.OptionMenu(self.master, self.tour_var, *self.tour_options.keys())
        self.tour_menu.grid(row=2, column=1, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, columnspan=2, pady=20)

    def submit_form(self):
        """Handles form submission and validates input."""
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        tour = self.tour_var.get()

        # Validate input
        if not name or not email:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        if not self.validate_email(email):
            messagebox.showerror("Input Error", "Please enter a valid email address.")
            return

        # Process reservation (for demonstration, we just show a message)
        cost = self.tour_options[tour]
        messagebox.showinfo("Reservation Successful", f"Thank you, {name}! You have reserved the '{tour}' tour for ${cost}.")

        # Clear the form
        self.clear_form()

    @staticmethod
    def validate_email(email):
        """Validates the email format."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def clear_form(self):
        """Clears the form fields."""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.tour_var.set(list(self.tour_options.keys())[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = HorseRidingReservation(root)
    root.mainloop()
```
