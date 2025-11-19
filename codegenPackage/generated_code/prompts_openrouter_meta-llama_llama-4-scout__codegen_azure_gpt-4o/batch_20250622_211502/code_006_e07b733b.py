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

# Constants for pricing
CALL_RATE_PER_MINUTE = 0.05  # USD per minute
AI_SERVICE_COST_PER_CALL = 0.10  # USD per call

class PricingDashboard:
    def __init__(self, root):
        """
        Initialize the pricing dashboard.
        :param root: Tkinter root window.
        """
        self.root = root
        self.root.title("WaveCall Pricing Dashboard")
        self.root.geometry("400x300")
        
        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Create and place widgets in the dashboard.
        """
        # Title Label
        title_label = tk.Label(self.root, text="WaveCall Pricing Dashboard", font=("Arial", 16))
        title_label.pack(pady=10)

        # Minutes Used Input
        tk.Label(self.root, text="Minutes Used:").pack()
        self.minutes_entry = tk.Entry(self.root)
        self.minutes_entry.pack(pady=5)

        # Number of Calls Input
        tk.Label(self.root, text="Number of Calls:").pack()
        self.calls_entry = tk.Entry(self.root)
        self.calls_entry.pack(pady=5)

        # Calculate Button
        calculate_button = tk.Button(self.root, text="Calculate Cost", command=self.calculate_cost)
        calculate_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def calculate_cost(self):
        """
        Calculate the total cost based on user input and display the result.
        """
        try:
            # Get user input
            minutes_used = float(self.minutes_entry.get())
            number_of_calls = int(self.calls_entry.get())

            # Validate input
            if minutes_used < 0 or number_of_calls < 0:
                raise ValueError("Minutes and calls must be non-negative.")

            # Calculate costs
            call_cost = minutes_used * CALL_RATE_PER_MINUTE
            ai_service_cost = number_of_calls * AI_SERVICE_COST_PER_CALL
            total_cost = call_cost + ai_service_cost

            # Display result
            self.result_label.config(text=f"Total Cost: ${total_cost:.2f}")
        except ValueError as ve:
            # Handle invalid input
            messagebox.showerror("Input Error", f"Invalid input: {ve}")
        except Exception as e:
            # Handle unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = PricingDashboard(root)
    root.mainloop()
```
