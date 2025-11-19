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


class DeltaFlightManager:
    """
    A class to manage Delta Airlines flight changes and calculate service fees.
    """

    def __init__(self, root):
        """
        Initialize the application UI and set default values.
        """
        self.root = root
        self.root.title("Delta Airlines Flight Manager")
        self.root.geometry("400x300")
        
        # Initialize UI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange user interface components.
        """
        # Title label
        title_label = tk.Label(self.root, text="Flight Change Manager", font=("Arial", 16))
        title_label.pack(pady=10)

        # Flight change reason dropdown
        tk.Label(self.root, text="Reason for Change:", font=("Arial", 12)).pack(pady=5)
        self.reason_var = tk.StringVar(value="Select")
        self.reason_dropdown = tk.OptionMenu(self.root, self.reason_var, "Schedule Conflict", "Personal", "Other")
        self.reason_dropdown.pack()

        # Service fee entry
        tk.Label(self.root, text="Base Service Fee ($):", font=("Arial", 12)).pack(pady=5)
        self.service_fee_entry = tk.Entry(self.root)
        self.service_fee_entry.pack()

        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate Total Fee", command=self.calculate_fee)
        calculate_button.pack(pady=10)

        # Output label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

    def calculate_fee(self):
        """
        Calculate the total service fee based on the reason for the change.
        """
        try:
            # Retrieve and validate base service fee
            base_fee = float(self.service_fee_entry.get())
            if base_fee < 0:
                raise ValueError("Base service fee cannot be negative.")

            # Determine additional fees based on reason for change
            reason = self.reason_var.get()
            additional_fee = 0

            if reason == "Schedule Conflict":
                additional_fee = 0  # No extra fee
            elif reason == "Personal":
                additional_fee = 50  # $50 extra fee
            elif reason == "Other":
                additional_fee = 30  # $30 extra fee
            else:
                messagebox.showerror("Invalid Input", "Please select a valid reason for change.")
                return

            # Calculate total fee
            total_fee = base_fee + additional_fee
            self.result_label.config(text=f"Total Service Fee: ${total_fee:.2f}")

        except ValueError as ve:
            messagebox.showerror("Invalid Input", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Create application window
    root = tk.Tk()
    app = DeltaFlightManager(root)
    root.mainloop()
```
