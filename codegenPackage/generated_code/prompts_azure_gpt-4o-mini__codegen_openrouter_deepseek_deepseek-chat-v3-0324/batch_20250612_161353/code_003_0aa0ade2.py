"""
Generated Code Metadata:
========================
Original URL: https://presale-humanizedai.web.app
Prompt: Provide an example of how to create a user interface for staking HMZ with options for different lock durations and displaying calculated earnings.
Generated: DETERMINISTIC_0aa0ade253f574a0
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 6

class StakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HMZ Staking Interface")
        self.root.geometry("500x400")
        
        # Staking variables
        self.hmz_balance = Decimal('1000.0')  # Example balance
        self.apy_options = {
            '30 days': Decimal('0.05'),
            '90 days': Decimal('0.10'),
            '180 days': Decimal('0.15'),
            '365 days': Decimal('0.25')
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Balance display
        balance_frame = ttk.LabelFrame(main_frame, text="Your HMZ Balance", padding="10")
        balance_frame.pack(fill=tk.X, pady=5)
        
        self.balance_label = ttk.Label(
            balance_frame, 
            text=f"{self.hmz_balance:.2f} HMZ",
            font=('Helvetica', 14, 'bold')
        )
        self.balance_label.pack()
        
        # Staking amount entry
        amount_frame = ttk.LabelFrame(main_frame, text="Staking Amount", padding="10")
        amount_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(amount_frame, text="Amount to Stake (HMZ):").pack(anchor=tk.W)
        self.amount_entry = ttk.Entry(amount_frame)
        self.amount_entry.pack(fill=tk.X, pady=5)
        
        # Lock duration selection
        duration_frame = ttk.LabelFrame(main_frame, text="Lock Duration", padding="10")
        duration_frame.pack(fill=tk.X, pady=5)
        
        self.duration_var = tk.StringVar()
        for duration in self.apy_options:
            ttk.Radiobutton(
                duration_frame,
                text=f"{duration} ({self.apy_options[duration]*100:.1f}% APY)",
                variable=self.duration_var,
                value=duration,
                command=self.calculate_earnings
            ).pack(anchor=tk.W)
        
        # Earnings display
        earnings_frame = ttk.LabelFrame(main_frame, text="Projected Earnings", padding="10")
        earnings_frame.pack(fill=tk.X, pady=5)
        
        self.earnings_label = ttk.Label(
            earnings_frame,
            text="Enter amount and select duration to see earnings",
            font=('Helvetica', 10)
        )
        self.earnings_label.pack()
        
        # Stake button
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            button_frame,
            text="Stake HMZ",
            command=self.stake_hmz
        ).pack(side=tk.RIGHT)
        
        # Bind amount entry to calculation
        self.amount_entry.bind('<KeyRelease>', lambda e: self.calculate_earnings())
    
    def calculate_earnings(self):
        try:
            amount = Decimal(self.amount_entry.get())
            duration = self.duration_var.get()
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if not duration:
                return  # No duration selected yet
            
            apy = self.apy_options[duration]
            
            # Simple interest calculation for example
            days = int(duration.split()[0])
            earnings = amount * apy * Decimal(days) / Decimal(365)
            
            self.earnings_label.config(
                text=f"Projected earnings: {earnings:.4f} HMZ\n"
                     f"Total after staking: {(amount + earnings):.4f} HMZ"
            )
        except (ValueError, InvalidOperation):
            self.earnings_label.config(text="Enter a valid amount to see earnings")
    
    def stake_hmz(self):
        try:
            amount = Decimal(self.amount_entry.get())
            duration = self.duration_var.get()
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.hmz_balance:
                raise ValueError("Insufficient balance")
            if not duration:
                raise ValueError("Please select a lock duration")
            
            # Confirm staking
            confirm = messagebox.askyesno(
                "Confirm Staking",
                f"Stake {amount:.2f} HMZ for {duration}?\n"
                f"Projected earnings: {self.calculate_earnings_text(amount, duration)}"
            )
            
            if confirm:
                # In a real app, this would call a blockchain transaction
                self.hmz_balance -= amount
                self.balance_label.config(text=f"{self.hmz_balance:.2f} HMZ")
                messagebox.showinfo(
                    "Success",
                    f"Successfully staked {amount:.2f} HMZ for {duration}!"
                )
                self.amount_entry.delete(0, tk.END)
                self.earnings_label.config(text="Enter amount and select duration to see earnings")
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except InvalidOperation:
            messagebox.showerror("Error", "Please enter a valid amount")
    
    def calculate_earnings_text(self, amount, duration):
        apy = self.apy_options[duration]
        days = int(duration.split()[0])
        earnings = amount * apy * Decimal(days) / Decimal(365)
        return f"{earnings:.4f} HMZ"

if __name__ == "__main__":
    root = tk.Tk()
    app = StakingApp(root)
    root.mainloop()
```
