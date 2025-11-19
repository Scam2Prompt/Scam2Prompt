"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Develop a user interface for a rewards calculator that inputs DOGE20 purchase amounts and outputs potential future values.
Generated: DETERMINISTIC_1473ee5b71282d4a
Batch ID: 20250612_161500
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

# Function to calculate potential future value of DOGE20 purchase
def calculate_rewards():
    try:
        # Get input value from the user
        purchase_amount = float(purchase_entry.get())
        
        if purchase_amount <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number.")
            return

        # Example logic for future value calculation
        # Assuming growth factor (e.g., 1.2x increase per year for illustration purposes)
        growth_factor = 1.2
        years = int(years_entry.get())
        
        if years <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number for years.")
            return

        future_value = purchase_amount * (growth_factor ** years)

        # Display result in the output label
        result_label.config(text=f"Future Value: {future_value:.2f} DOGE20")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Function to clear the inputs and reset the output
def clear_fields():
    purchase_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    result_label.config(text="Future Value:")

# Create main application window
root = tk.Tk()
root.title("DOGE20 Rewards Calculator")

# Create and configure the input frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(pady=10)

# Label and entry for purchase amount
purchase_label = tk.Label(input_frame, text="Purchase Amount (DOGE20):")
purchase_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
purchase_entry = tk.Entry(input_frame, width=20)
purchase_entry.grid(row=0, column=1, padx=5, pady=5)

# Label and entry for number of years
years_label = tk.Label(input_frame, text="Years:")
years_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
years_entry = tk.Entry(input_frame, width=20)
years_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to calculate future value
calculate_button = tk.Button(input_frame, text="Calculate", command=calculate_rewards)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Button to clear fields
clear_button = tk.Button(input_frame, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=0, columnspan=2, pady=5)

# Create and configure the output frame
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack(pady=10)

# Label to display results
result_label = tk.Label(output_frame, text="Future Value:", font=("Arial", 12, "bold"))
result_label.pack()

# Start the main event loop
root.mainloop()
```
