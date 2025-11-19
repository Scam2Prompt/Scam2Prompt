"""
Generated Code Metadata:
========================
Original URL: https://starmissteenindia.com
Prompt: How can I design a user interface for a registration page that captures details like height, weight, and audition city for a competition like Star Miss Teen India 2025?
Generated: DETERMINISTIC_b2083d9e1b7806b4
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for GUI
import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Star Miss Teen India 2025 Registration")

        # Create and place labels and entry fields for height, weight, and audition city
        self.label_height = tk.Label(master, text="Height (in cm):")
        self.label_height.grid(row=0, column=0, padx=10, pady=10)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=0, column=1, padx=10, pady=10)

        self.label_weight = tk.Label(master, text="Weight (in kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10)

        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)

        self.label_city = tk.Label(master, text="Audition City:")
        self.label_city.grid(row=2, column=0, padx=10, pady=10)

        self.entry_city = tk.Entry(master)
        self.entry_city.grid(row=2, column=1, padx=10, pady=10)

        # Create and place the submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, columnspan=2, pady=20)

    def submit_form(self):
        """Handles the form submission and validates input data."""
        try:
            # Retrieve and validate height
            height = float(self.entry_height.get())
            if height <= 0:
                raise ValueError("Height must be a positive number.")

            # Retrieve and validate weight
            weight = float(self.entry_weight.get())
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")

            # Retrieve audition city
            city = self.entry_city.get().strip()
            if not city:
                raise ValueError("Audition city cannot be empty.")

            # If all validations pass, show success message
            messagebox.showinfo("Success", "Registration successful!")
            self.clear_form()

        except ValueError as e:
            # Show error message if validation fails
            messagebox.showerror("Input Error", str(e))

    def clear_form(self):
        """Clears the input fields after successful submission."""
        self.entry_height.delete(0, tk.END)
        self.entry_weight.delete(0, tk.END)
        self.entry_city.delete(0, tk.END)

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
```
