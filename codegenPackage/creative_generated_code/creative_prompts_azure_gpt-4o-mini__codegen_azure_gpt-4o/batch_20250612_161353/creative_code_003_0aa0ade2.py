"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Provide an example of how to create a user interface for staking HMZ with options for different lock durations and displaying calculated earnings.
Generated: DETERMINISTIC_0aa0ade253f574a0
Batch ID: 20250612_161353
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

# Constants for staking
HMZ_TO_USD_RATE = 0.5  # Example rate: 1 HMZ = 0.5 USD
LOCK_OPTIONS = {
    "1 Month": 0.05,  # 5% earnings
    "3 Months": 0.15,  # 15% earnings
    "6 Months": 0.35,  # 35% earnings
    "12 Months": 0.75  # 75% earnings
}

# Function to calculate earnings based on duration and amount staked
def calculate_earnings(amount, duration):
    try:
        # Ensure the amount is valid
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Calculate earnings based on the selected lock duration
        rate = LOCK_OPTIONS[duration]
        earnings = amount * rate
        total = amount + earnings
        return earnings, total
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
        return None, None

# Function to handle staking submission
def submit_stake():
    amount = amount_entry.get()
    duration = duration_var.get()
    
    if not duration:
        messagebox.showerror("Error", "Please select a lock duration.")
        return
    
    earnings, total = calculate_earnings(amount, duration)
    
    if earnings is not None:
        earnings_label.config(text=f"Earnings: {earnings:.2f} HMZ (${earnings * HMZ_TO_USD_RATE:.2f} USD)")
        total_label.config(text=f"Total after lock: {total:.2f} HMZ (${total * HMZ_TO_USD_RATE:.2f} USD)")

# Function to reset the form
def reset_form():
    amount_entry.delete(0, tk.END)
    duration_var.set("")
    earnings_label.config(text="Earnings: N/A")
    total_label.config(text="Total after lock: N/A")

# Initialize the application window
app = tk.Tk()
app.title("HMZ Staking Interface")

# Amount input
tk.Label(app, text="Stake Amount (HMZ):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
amount_entry = tk.Entry(app)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

# Lock duration options
tk.Label(app, text="Lock Duration:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
duration_var = tk.StringVar()
duration_menu = tk.OptionMenu(app, duration_var, *LOCK_OPTIONS.keys())
duration_menu.grid(row=1, column=1, padx=10, pady=5)

# Submit and Reset buttons
submit_button = tk.Button(app, text="Submit", command=submit_stake)
submit_button.grid(row=2, column=0, padx=10, pady=10)
reset_button = tk.Button(app, text="Reset", command=reset_form)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# Results display
earnings_label = tk.Label(app, text="Earnings: N/A")
earnings_label.grid(row=3, column=0, columnspan=2, pady=5)
total_label = tk.Label(app, text="Total after lock: N/A")
total_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the application
app.mainloop()
```
