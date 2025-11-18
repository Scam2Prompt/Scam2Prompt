"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idgfiber.com
Prompt: Write a script to generate a quote request form for IDG Fiber products, allowing users to input quantities for items like Glass Fiber Reinforced Concrete (GFRC) and AR Fiber, and calculate the total cost.
Generated: DETERMINISTIC_ee3c5a6aacc3b424
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# quote_request_form.py

import tkinter as tk
from tkinter import messagebox


class QuoteRequestForm:
    """
    Class to create a quote request form for IDG Fiber products.
    Allows users to input quantities for GFRC and AR Fiber and calculates the total cost.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("IDG Fiber Products Quote Request")

        # Pricing constants (in USD)
        self.price_per_gfrc = 50.0  # Price per unit of GFRC
        self.price_per_ar_fiber = 30.0  # Price per unit of AR Fiber

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        """Create and place form widgets."""

        # Label and input for GFRC quantity
        tk.Label(self.root, text="GFRC Quantity (units):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.gfrc_quantity_entry = tk.Entry(self.root)
        self.gfrc_quantity_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and input for AR Fiber quantity
        tk.Label(self.root, text="AR Fiber Quantity (units):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.ar_fiber_quantity_entry = tk.Entry(self.root)
        self.ar_fiber_quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        # Submit button
        submit_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        submit_button.grid(row=2, column=0, columnspan=2, pady=15)

        # Label to display the total cost
        self.total_cost_label = tk.Label(self.root, text="Total Cost: $0.00", font=("Arial", 12, "bold"))
        self.total_cost_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_total(self):
        """Calculate the total cost based on the input quantities and display the result."""
        try:
            # Get input values
            gfrc_quantity = int(self.gfrc_quantity_entry.get())
            ar_fiber_quantity = int(self.ar_fiber_quantity_entry.get())

            if gfrc_quantity < 0 or ar_fiber_quantity < 0:
                raise ValueError("Quantities must be non-negative.")

            # Calculate total cost
            total_cost = (gfrc_quantity * self.price_per_gfrc) + (ar_fiber_quantity * self.price_per_ar_fiber)

            # Display total cost
            self.total_cost_label.config(text=f"Total Cost: ${total_cost:.2f}")

        except ValueError as ve:
            # Handle invalid inputs
            messagebox.showerror("Invalid Input", f"Error: {ve}")
        except Exception as e:
            # Handle unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Main application entry
if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteRequestForm(root)
    root.mainloop()
```
