"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flights-ticketbooking.com
Prompt: How can I use Python to create a user-friendly interface for managing Delta Airlines flight changes, including service fee calculations?
Generated: DETERMINISTIC_9a6ee9c972b20f97
Batch ID: 20250612_162502
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

class FlightChangeManager:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("Delta Airlines Flight Change Manager")

        # User input fields
        self.flight_number_label = tk.Label(master, text="Flight Number:")
        self.flight_number_label.pack()
        self.flight_number_entry = tk.Entry(master)
        self.flight_number_entry.pack()

        self.change_date_label = tk.Label(master, text="Change Date (YYYY-MM-DD):")
        self.change_date_label.pack()
        self.change_date_entry = tk.Entry(master)
        self.change_date_entry.pack()

        self.service_fee_label = tk.Label(master, text="Service Fee ($):")
        self.service_fee_label.pack()
        self.service_fee_entry = tk.Entry(master)
        self.service_fee_entry.pack()

        # Action buttons
        self.calculate_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        self.change_flight_button = tk.Button(master, text="Change Flight", command=self.change_flight)
        self.change_flight_button.pack()

        # Result display
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_total(self):
        """Calculate the total cost including service fees."""
        try:
            fee = float(self.service_fee_entry.get())
            total = fee + self.get_base_fare()
            self.result_label.config(text=f"Total Cost: ${total:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid service fee.")

    def change_flight(self):
        """Handle the flight change process."""
        flight_number = self.flight_number_entry.get()
        change_date = self.change_date_entry.get()

        if not flight_number or not change_date:
            messagebox.showwarning("Input Warning", "Please fill in all fields.")
            return

        # Simulate flight change confirmation
        messagebox.showinfo("Success", f"Flight {flight_number} changed successfully to {change_date}.")

    def get_base_fare(self):
        """A placeholder function to simulate base fare retrieval."""
        # In a real-world application, this should interact with a database or an API
        return 200.00  # Static base fare for demonstration

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightChangeManager(root)
    root.mainloop()
```
