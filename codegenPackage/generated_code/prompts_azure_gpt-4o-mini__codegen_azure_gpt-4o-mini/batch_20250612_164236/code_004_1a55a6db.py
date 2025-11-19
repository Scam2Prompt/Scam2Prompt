"""
Generated Code Metadata:
========================
Original URL: https://tomi.com.au
Prompt: Illustrate how to implement a user interface that allows customers to select their desired Tomi Broadband plan and check its availability.
Generated: DETERMINISTIC_1a55a6dbe5f65a46
Batch ID: 20250612_164236
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

class TomiBroadbandApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Tomi Broadband Plan Selector")
        
        # Available plans
        self.plans = {
            "Basic Plan": {"speed": "50 Mbps", "price": "$30", "available": True},
            "Standard Plan": {"speed": "100 Mbps", "price": "$50", "available": True},
            "Premium Plan": {"speed": "200 Mbps", "price": "$70", "available": False},
        }
        
        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the UI components."""
        # Label for plan selection
        self.label = tk.Label(self.master, text="Select Your Tomi Broadband Plan:")
        self.label.pack(pady=10)

        # Dropdown for plan selection
        self.plan_var = tk.StringVar(value=list(self.plans.keys())[0])
        self.plan_menu = tk.OptionMenu(self.master, self.plan_var, *self.plans.keys())
        self.plan_menu.pack(pady=10)

        # Check availability button
        self.check_button = tk.Button(self.master, text="Check Availability", command=self.check_availability)
        self.check_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def check_availability(self):
        """Check the availability of the selected plan and display the result."""
        selected_plan = self.plan_var.get()
        plan_info = self.plans[selected_plan]

        if plan_info["available"]:
            message = f"{selected_plan} is available!\nSpeed: {plan_info['speed']}\nPrice: {plan_info['price']}"
        else:
            message = f"Sorry, {selected_plan} is currently not available."

        # Display the result in a message box
        messagebox.showinfo("Plan Availability", message)

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = TomiBroadbandApp(root)
    root.mainloop()
```
