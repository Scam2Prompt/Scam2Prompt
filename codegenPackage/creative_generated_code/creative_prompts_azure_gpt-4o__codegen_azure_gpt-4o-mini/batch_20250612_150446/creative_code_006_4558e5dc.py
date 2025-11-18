"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradingtrustltd.com
Prompt: Create a dashboard interface for managing investments, deposits, withdrawals, and referral statistics, similar to the account control panel described on Trading-Trust Ltd.
Generated: DETERMINISTIC_4558e5dcd6e817aa
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Dashboard Interface

import tkinter as tk
from tkinter import messagebox

class InvestmentDashboard:
    def __init__(self, master):
        """Initialize the Investment Dashboard interface."""
        self.master = master
        self.master.title("Investment Dashboard")

        # Initialize investment data
        self.investment_data = {
            'total_investment': 0.0,
            'total_withdrawals': 0.0,
            'total_deposits': 0.0,
            'referrals': 0
        }

        # Create layout
        self.create_widgets()

    def create_widgets(self):
        """Create and place widgets in the interface."""
        # Investment Overview
        self.investment_label = tk.Label(self.master, text="Investment Overview", font=("Arial", 16))
        self.investment_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Total Investment
        self.total_investment_label = tk.Label(self.master, text=f"Total Investment: ${self.investment_data['total_investment']:.2f}")
        self.total_investment_label.grid(row=1, column=0, padx=10, pady=5)

        # Total Withdrawals
        self.total_withdrawals_label = tk.Label(self.master, text=f"Total Withdrawals: ${self.investment_data['total_withdrawals']:.2f}")
        self.total_withdrawals_label.grid(row=2, column=0, padx=10, pady=5)

        # Total Deposits
        self.total_deposits_label = tk.Label(self.master, text=f"Total Deposits: ${self.investment_data['total_deposits']:.2f}")
        self.total_deposits_label.grid(row=3, column=0, padx=10, pady=5)

        # Total Referrals
        self.referrals_label = tk.Label(self.master, text=f"Total Referrals: {self.investment_data['referrals']}")
        self.referrals_label.grid(row=4, column=0, padx=10, pady=5)

        # Add Deposit Button
        self.deposit_button = tk.Button(self.master, text="Add Deposit", command=self.add_deposit)
        self.deposit_button.grid(row=5, column=0, padx=10, pady=10)

        # Add Withdrawal Button
        self.withdrawal_button = tk.Button(self.master, text="Add Withdrawal", command=self.add_withdrawal)
        self.withdrawal_button.grid(row=5, column=1, padx=10, pady=10)

        # Add Referral Button
        self.referral_button = tk.Button(self.master, text="Add Referral", command=self.add_referral)
        self.referral_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_deposit(self):
        """Prompt user for deposit amount and update the total."""
        amount = self.get_amount("Enter deposit amount:")
        if amount is not None:
            self.investment_data['total_deposits'] += amount
            self.investment_data['total_investment'] += amount
            self.update_labels()

    def add_withdrawal(self):
        """Prompt user for withdrawal amount and update the total."""
        amount = self.get_amount("Enter withdrawal amount:")
        if amount is not None:
            if amount > self.investment_data['total_investment']:
                messagebox.showerror("Error", "Withdrawal exceeds total investment amount.")
                return
            self.investment_data['total_withdrawals'] += amount
            self.investment_data['total_investment'] -= amount
            self.update_labels()

    def add_referral(self):
        """Increment the referral count."""
        self.investment_data['referrals'] += 1
        self.update_labels()

    def get_amount(self, prompt):
        """Get a valid amount input from the user."""
        try:
            amount_str = tk.simpledialog.askstring("Input", prompt)
            if amount_str is not None:
                amount = float(amount_str)
                if amount < 0:
                    raise ValueError("Amount must be non-negative.")
                return amount
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        return None

    def update_labels(self):
        """Update the displayed labels with the current investment data."""
        self.total_investment_label.config(text=f"Total Investment: ${self.investment_data['total_investment']:.2f}")
        self.total_withdrawals_label.config(text=f"Total Withdrawals: ${self.investment_data['total_withdrawals']:.2f}")
        self.total_deposits_label.config(text=f"Total Deposits: ${self.investment_data['total_deposits']:.2f}")
        self.referrals_label.config(text=f"Total Referrals: {self.investment_data['referrals']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentDashboard(master=root)
    root.mainloop()
```
