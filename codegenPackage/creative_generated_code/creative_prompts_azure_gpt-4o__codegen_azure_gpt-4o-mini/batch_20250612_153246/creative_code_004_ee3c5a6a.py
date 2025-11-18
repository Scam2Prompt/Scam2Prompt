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
import tkinter as tk
from tkinter import messagebox

# Constants for item prices
ITEM_PRICES = {
    "GFRC": 50.0,  # Price per unit for Glass Fiber Reinforced Concrete
    "AR_Fiber": 30.0  # Price per unit for AR Fiber
}

class QuoteRequestForm:
    def __init__(self, root):
        self.root = root
        self.root.title("IDG Fiber Products Quote Request Form")
        
        # Labels and entries for each item
        self.create_widgets()
        
    def create_widgets(self):
        # Glass Fiber Reinforced Concrete (GFRC)
        tk.Label(self.root, text="Glass Fiber Reinforced Concrete (GFRC) Quantity:").grid(row=0, column=0)
        self.gfrc_entry = tk.Entry(self.root)
        self.gfrc_entry.grid(row=0, column=1)

        # AR Fiber
        tk.Label(self.root, text="AR Fiber Quantity:").grid(row=1, column=0)
        self.ar_fiber_entry = tk.Entry(self.root)
        self.ar_fiber_entry.grid(row=1, column=1)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.submit_button.grid(row=2, columnspan=2)

        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_total(self):
        """Calculate the total cost based on user input and display the result."""
        try:
            # Get quantities from entries and convert to integers
            gfrc_quantity = int(self.gfrc_entry.get()) if self.gfrc_entry.get() else 0
            ar_fiber_quantity = int(self.ar_fiber_entry.get()) if self.ar_fiber_entry.get() else 0

            # Calculate total cost
            total_cost = (gfrc_quantity * ITEM_PRICES["GFRC"]) + (ar_fiber_quantity * ITEM_PRICES["AR_Fiber"])
            
            # Display the total cost
            self.result_label.config(text=f"Total Cost: ${total_cost:.2f}")
        except ValueError:
            # Handle invalid input
            messagebox.showerror("Input Error", "Please enter valid quantities.")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = QuoteRequestForm(root)
    root.mainloop()
```
