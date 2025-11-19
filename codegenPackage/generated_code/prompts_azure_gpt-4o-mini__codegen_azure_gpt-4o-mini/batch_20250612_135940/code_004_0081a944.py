"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: What are the best practices for creating a user-friendly interface for a local prepayment discount platform based on the features of 단골가게?
Generated: DETERMINISTIC_0081a9448328ebcd
Batch ID: 20250612_135940
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

class PrepaymentDiscountApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("Prepayment Discount Platform")

        # Create and place labels and entry fields
        self.label = tk.Label(master, text="Enter Amount:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.discount_label = tk.Label(master, text="Discount Percentage:")
        self.discount_label.grid(row=1, column=0, padx=10, pady=10)

        self.discount_entry = tk.Entry(master)
        self.discount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create and place buttons
        self.calculate_button = tk.Button(master, text="Calculate Discount", command=self.calculate_discount)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_discount(self):
        """Calculate the discount based on user input and display the result."""
        try:
            # Get user input
            amount = float(self.amount_entry.get())
            discount_percentage = float(self.discount_entry.get())

            # Validate input values
            if amount < 0 or discount_percentage < 0:
                raise ValueError("Amount and discount percentage must be non-negative.")

            # Calculate discount
            discount = (discount_percentage / 100) * amount
            final_amount = amount - discount

            # Display the result
            self.result_label.config(text=f"Final Amount after Discount: {final_amount:.2f}")

        except ValueError as e:
            # Handle invalid input
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PrepaymentDiscountApp(root)
    root.mainloop()
```
