"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-usdt-trc20-payfor-00000017.pages.dev
Prompt: Generate code to display a numeric keypad for entering USDT transaction amounts, mimicking the interface design of OKX's payment system.
Generated: DETERMINISTIC_6db736123cecbde6
Batch ID: 20250612_154601
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

class NumericKeypad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("USDT Transaction Amount Keypad")
        self.geometry("300x400")
        self.resizable(False, False)

        self.amount_entry = tk.Entry(self, font=('Arial', 24), justify='right')
        self.amount_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Create keypad buttons
        self.create_keypad()

    def create_keypad(self):
        """Creates a numeric keypad with buttons from 0 to 9, a clear button, and an enter button."""
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('C', 4, 0), ('0', 4, 1), ('Enter', 4, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Configure grid weights for better resizing
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        """Handles button clicks to update the amount entry or perform actions like clear or enter."""
        if value == 'C':
            self.amount_entry.delete(0, tk.END)  # Clear the entry
        elif value == 'Enter':
            self.submit_amount()
        else:
            self.amount_entry.insert(tk.END, value)  # Append the clicked number

    def submit_amount(self):
        """Validates and submits the entered amount."""
        amount = self.amount_entry.get()
        if self.validate_amount(amount):
            messagebox.showinfo("Success", f"Submitting amount: {amount} USDT")
            self.amount_entry.delete(0, tk.END)  # Clear entry after submission
        else:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid USDT amount.")

    def validate_amount(self, amount):
        """Validates the entered amount to ensure it's a positive number."""
        try:
            value = float(amount)
            return value > 0  # Ensure amount is greater than zero
        except ValueError:
            return False  # Not a number

if __name__ == "__main__":
    try:
        keypad = NumericKeypad()
        keypad.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal Error", f"An unexpected error occurred: {str(e)}")
```
