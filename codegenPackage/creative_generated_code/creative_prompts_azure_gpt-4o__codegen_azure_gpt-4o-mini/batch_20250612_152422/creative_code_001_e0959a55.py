"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molly-4uy.pages.dev
Prompt: Generate code to calculate daily fees for Angel and Private transactions using the fee percentages provided on the Molly Gateway site. Include functionality to display the results dynamically.
Generated: DETERMINISTIC_e0959a55fd931f1e
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox

# Constants for fee percentages (example values, please verify with actual rates)
ANGEL_FEE_PERCENTAGE = 0.05  # 5% for Angel transactions
PRIVATE_FEE_PERCENTAGE = 0.03  # 3% for Private transactions

def calculate_fees(transaction_amount, fee_percentage):
    """
    Calculate the fees based on the transaction amount and fee percentage.
    
    Args:
        transaction_amount (float): The total transaction amount.
        fee_percentage (float): The fee percentage as a decimal.

    Returns:
        float: The calculated fee.
    """
    if transaction_amount < 0:
        raise ValueError("Transaction amount must be non-negative.")
    return transaction_amount * fee_percentage

def on_calculate():
    """
    Event handler for the Calculate button. Gathers input, calculates fees,
    and updates the result in the UI.
    """
    try:
        # Get the transaction amount from the entry field
        amount = float(amount_entry.get())
        
        # Calculate fees for Angel and Private transactions
        angel_fee = calculate_fees(amount, ANGEL_FEE_PERCENTAGE)
        private_fee = calculate_fees(amount, PRIVATE_FEE_PERCENTAGE)
        
        # Update the result labels
        angel_fee_label.config(text=f"Angel Transaction Fee: ${angel_fee:.2f}")
        private_fee_label.config(text=f"Private Transaction Fee: ${private_fee:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Transaction Fee Calculator")

# Create and place the input field and button
tk.Label(root, text="Enter Transaction Amount:").pack(pady=10)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate Fees", command=on_calculate)
calculate_button.pack(pady=10)

# Labels to display results
angel_fee_label = tk.Label(root, text="Angel Transaction Fee: $0.00")
angel_fee_label.pack(pady=10)

private_fee_label = tk.Label(root, text="Private Transaction Fee: $0.00")
private_fee_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
```
