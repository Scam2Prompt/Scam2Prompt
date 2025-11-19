"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.co
Prompt: How can I use the VGA/glass technology to enhance the user interface of a banking app focused on savings?
Generated: DETERMINISTIC_89f57765a840ebcd
Batch ID: 20250612_140107
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

class BankingApp:
    def __init__(self, master):
        """Initialize the banking app with a user-friendly interface."""
        self.master = master
        master.title("Savings Banking App")
        
        # Set the window size and background color to enhance user experience
        master.geometry("400x300")
        master.configure(bg="lightblue")

        # Create label for the title
        self.label_title = tk.Label(master, text="Savings Banking App", font=("Arial", 24), bg="lightblue")
        self.label_title.pack(pady=10)

        # Create input field for the user to enter their savings amount
        self.label_amount = tk.Label(master, text="Enter Savings Amount:", bg="lightblue")
        self.label_amount.pack(pady=5)

        self.amount_entry = tk.Entry(master, width=20)
        self.amount_entry.pack(pady=5)

        # Create a button to submit the savings amount
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_savings)
        self.submit_button.pack(pady=20)

    def submit_savings(self):
        """Handle the submission of savings amount."""
        amount_str = self.amount_entry.get()
        
        try:
            # Attempt to convert input to a float
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("Amount must be non-negative.")
            
            # Display success message
            messagebox.showinfo("Success", f"You have saved: ${amount:.2f}")
            self.amount_entry.delete(0, tk.END)  # Clear the entry field
        except ValueError as e:
            # Handle invalid input (non-numeric or negative values)
            messagebox.showerror("Invalid Input", str(e))

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
```
