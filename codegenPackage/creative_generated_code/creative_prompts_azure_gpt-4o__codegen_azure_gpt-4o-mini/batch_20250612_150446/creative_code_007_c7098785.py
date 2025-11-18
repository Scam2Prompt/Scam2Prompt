"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Create a dashboard to display hourly interest earnings, total deposits, and withdrawal history for an investment platform, inspired by Digitalwealthtraders' user interface.
Generated: DETERMINISTIC_c7098785c61f0edd
Batch ID: 20250612_150446
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
from datetime import datetime
import random

class InvestmentDashboard:
    def __init__(self, root):
        """Initialize the main application window and its components."""
        self.root = root
        self.root.title("Investment Dashboard")
        self.root.geometry("600x400")

        # Sample data
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.hourly_interest_earnings = 0.00

        # Create UI components
        self.create_widgets()
        self.update_dashboard()

    def create_widgets(self):
        """Create and layout the UI components."""
        self.deposit_label = tk.Label(self.root, text="Total Deposits: $0.00", font=("Arial", 14))
        self.deposit_label.pack(pady=10)

        self.withdrawal_label = tk.Label(self.root, text="Total Withdrawals: $0.00", font=("Arial", 14))
        self.withdrawal_label.pack(pady=10)

        self.interest_label = tk.Label(self.root, text="Hourly Interest Earnings: $0.00", font=("Arial", 14))
        self.interest_label.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Funds", command=self.withdraw_funds)
        self.withdraw_button.pack(pady=20)

        self.deposit_button = tk.Button(self.root, text="Deposit Funds", command=self.deposit_funds)
        self.deposit_button.pack(pady=20)

        self.history_button = tk.Button(self.root, text="Show Withdrawal History", command=self.show_withdrawal_history)
        self.history_button.pack(pady=20)

    def update_dashboard(self):
        """Update the dashboard display with the current data."""
        self.deposit_label.config(text=f"Total Deposits: ${self.total_deposits:.2f}")
        self.withdrawal_label.config(text=f"Total Withdrawals: ${self.total_withdrawals:.2f}")
        self.interest_label.config(text=f"Hourly Interest Earnings: ${self.hourly_interest_earnings:.2f}")

    def deposit_funds(self):
        """Simulate depositing funds into the account."""
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0.")
            self.total_deposits += amount
            self.hourly_interest_earnings += amount * 0.01  # Simulated interest earning
            self.update_dashboard()
            messagebox.showinfo("Success", f"Deposited: ${amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def withdraw_funds(self):
        """Simulate withdrawing funds from the account."""
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0.")
            if amount > self.total_deposits:
                raise ValueError("Insufficient funds for withdrawal.")
            self.total_deposits -= amount
            self.total_withdrawals += amount
            self.update_dashboard()
            messagebox.showinfo("Success", f"Withdrew: ${amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def show_withdrawal_history(self):
        """Display a simple withdrawal history simulation."""
        # In a real application, this data should come from a database.
        withdrawal_history = [
            (random.uniform(50, 500), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            for _ in range(5)
        ]
        history_str = "\n".join([f"${amount:.2f} on {date}" for amount, date in withdrawal_history])
        messagebox.showinfo("Withdrawal History", history_str if history_str else "No withdrawals made yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentDashboard(root)
    root.mainloop()
```
