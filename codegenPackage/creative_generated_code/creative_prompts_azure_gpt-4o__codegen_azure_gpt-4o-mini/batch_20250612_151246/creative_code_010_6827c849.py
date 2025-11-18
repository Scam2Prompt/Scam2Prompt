"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-gifts.pages.dev
Prompt: Generate a code snippet to display a cost calculator for Rewarble voucher redemption fees based on user input.
Generated: DETERMINISTIC_6827c8497d0eb5d8
Batch ID: 20250612_151246
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

class CostCalculator:
    def __init__(self, root):
        """Initialize the main window and components."""
        self.root = root
        self.root.title("Rewarble Voucher Redemption Fee Calculator")

        # Create input fields
        tk.Label(root, text="Enter Voucher Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create a button to calculate the fee
        self.calculate_button = tk.Button(root, text="Calculate Fee", command=self.calculate_fee)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_fee(self):
        """Calculate and display the redemption fee based on user input."""
        try:
            # Get the voucher amount from user input
            amount = float(self.amount_entry.get())

            # Validate that amount is non-negative
            if amount < 0:
                raise ValueError("Amount must be non-negative.")

            # Define a simple fee structure (for example, 5% fee)
            fee_percentage = 0.05
            fee = amount * fee_percentage

            # Display the result
            self.result_label.config(text=f"Redemption Fee: ${fee:.2f}")
        except ValueError as e:
            # Handle invalid inputs gracefully
            messagebox.showerror("Input Error", f"Invalid input: {e}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = CostCalculator(root)
    root.mainloop()
```
