"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Write Python code to create a registration form for a basketball training camp, including fields for skill level (beginner/advanced), camp dates, and payment options, as described in the L-Zero basketball camp details.
Generated: DETERMINISTIC_84727eb93af4a18d
Batch ID: 20250612_145626
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
from datetime import datetime

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Basketball Training Camp Registration")

        # Initialize fields
        self.skill_level = tk.StringVar()
        self.camp_dates = tk.StringVar()
        self.payment_option = tk.StringVar()

        # Skill Level Label and Dropdown
        self.skill_level_label = tk.Label(master, text="Select Skill Level:")
        self.skill_level_label.grid(row=0, column=0)
        self.skill_level_dropdown = tk.OptionMenu(master, self.skill_level, "Beginner", "Advanced")
        self.skill_level_dropdown.grid(row=0, column=1)

        # Camp Dates Label and Entry
        self.camp_dates_label = tk.Label(master, text="Enter Camp Dates (YYYY-MM-DD):")
        self.camp_dates_label.grid(row=1, column=0)
        self.camp_dates_entry = tk.Entry(master, textvariable=self.camp_dates)
        self.camp_dates_entry.grid(row=1, column=1)

        # Payment Options Label and Dropdown
        self.payment_options_label = tk.Label(master, text="Select Payment Option:")
        self.payment_options_label.grid(row=2, column=0)
        self.payment_option_dropdown = tk.OptionMenu(master, self.payment_option, "Credit Card", "PayPal", "Bank Transfer")
        self.payment_option_dropdown.grid(row=2, column=1)

        # Submit Button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, columnspan=2)

    def submit_form(self):
        """Handle form submission, validate input, and display confirmation."""
        skill_level = self.skill_level.get()
        camp_dates = self.camp_dates.get()
        payment_option = self.payment_option.get()

        # Validate inputs
        if not skill_level:
            messagebox.showerror("Input Error", "Please select a skill level.")
            return

        if not camp_dates or not self.validate_date(camp_dates):
            messagebox.showerror("Input Error", "Please enter valid camp dates (YYYY-MM-DD).")
            return

        if not payment_option:
            messagebox.showerror("Input Error", "Please select a payment option.")
            return

        # Display confirmation message
        messagebox.showinfo("Registration Successful", 
                            f"Registration Details:\n"
                            f"Skill Level: {skill_level}\n"
                            f"Camp Dates: {camp_dates}\n"
                            f"Payment Option: {payment_option}")

    @staticmethod
    def validate_date(date_text):
        """Validate the date format."""
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    registration_form = RegistrationForm(root)
    root.mainloop()
```
