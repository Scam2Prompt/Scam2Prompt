"""
Generated Code Metadata:
========================
Original URL: https://wavecall.io
Prompt: Create a pricing dashboard for an international calling platform like WaveCall, including cost calculations based on usage and underlying AI service costs.
Generated: DETERMINISTIC_e07b733bbdb02bb4
Batch ID: 20250622_211502
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

class PricingDashboard:
    def __init__(self, master):
        """Initialize the main window and its components."""
        self.master = master
        self.master.title("WaveCall Pricing Dashboard")
        
        # Set up the input fields
        self.create_widgets()
        
        # Initialize service costs (in USD)
        self.base_rate = 0.05  # Base rate per minute
        self.ai_service_cost = 0.02  # AI service cost per minute

    def create_widgets(self):
        """Create and place the widgets in the window."""
        # Label for usage input
        self.usage_label = tk.Label(self.master, text="Enter usage in minutes:")
        self.usage_label.grid(row=0, column=0, padx=10, pady=10)

        # Entry for usage input
        self.usage_entry = tk.Entry(self.master)
        self.usage_entry.grid(row=0, column=1, padx=10, pady=10)

        # Calculate button
        self.calculate_button = tk.Button(self.master, text="Calculate Cost", command=self.calculate_cost)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label for displaying the result
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_cost(self):
        """Calculate the total cost based on usage and display the result."""
        try:
            # Get the usage input
            usage_minutes = float(self.usage_entry.get())
            if usage_minutes < 0:
                raise ValueError("Usage cannot be negative.")

            # Calculate total cost
            total_cost = (self.base_rate + self.ai_service_cost) * usage_minutes
            
            # Display the result
            self.result_label.config(text=f"Total Cost: ${total_cost:.2f}")
        
        except ValueError as e:
            # Handle invalid input
            messagebox.showerror("Input Error", f"Invalid input: {e}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = PricingDashboard(root)
    root.mainloop()
```
