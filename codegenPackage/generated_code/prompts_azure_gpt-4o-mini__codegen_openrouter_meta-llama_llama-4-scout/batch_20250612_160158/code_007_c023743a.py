"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Design a user interface for a financial calculator that helps users compare different loan options, including terms for asset finance and property finance.
Generated: DETERMINISTIC_c023743a20825f0f
Batch ID: 20250612_160158
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

class FinancialCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Calculator")

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.asset_finance_tab = ttk.Frame(self.tab_control)
        self.property_finance_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.asset_finance_tab, text="Asset Finance")
        self.tab_control.add(self.property_finance_tab, text="Property Finance")
        self.tab_control.pack(expand=1, fill="both")

        # Asset finance tab
        self.asset_finance_widgets()

        # Property finance tab
        self.property_finance_widgets()

    def asset_finance_widgets(self):
        # Create asset finance widgets
        tk.Label(self.asset_finance_tab, text="Asset Price").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.asset_finance_tab, text="Deposit").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.asset_finance_tab, text="Term (years)").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.asset_finance_tab, text="Interest Rate").grid(row=3, column=0, padx=5, pady=5)

        self.asset_price_entry = tk.Entry(self.asset_finance_tab)
        self.deposit_entry = tk.Entry(self.asset_finance_tab)
        self.term_entry = tk.Entry(self.asset_finance_tab)
        self.interest_rate_entry = tk.Entry(self.asset_finance_tab)

        self.asset_price_entry.grid(row=0, column=1, padx=5, pady=5)
        self.deposit_entry.grid(row=1, column=1, padx=5, pady=5)
        self.term_entry.grid(row=2, column=1, padx=5, pady=5)
        self.interest_rate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.calculate_asset_finance_button = tk.Button(self.asset_finance_tab, text="Calculate", command=self.calculate_asset_finance)
        self.calculate_asset_finance_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.asset_finance_result_label = tk.Label(self.asset_finance_tab, text="")
        self.asset_finance_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def property_finance_widgets(self):
        # Create property finance widgets
        tk.Label(self.property_finance_tab, text="Property Price").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.property_finance_tab, text="Deposit").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.property_finance_tab, text="Term (years)").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.property_finance_tab, text="Interest Rate").grid(row=3, column=0, padx=5, pady=5)

        self.property_price_entry = tk.Entry(self.property_finance_tab)
        self.property_deposit_entry = tk.Entry(self.property_finance_tab)
        self.property_term_entry = tk.Entry(self.property_finance_tab)
        self.property_interest_rate_entry = tk.Entry(self.property_finance_tab)

        self.property_price_entry.grid(row=0, column=1, padx=5, pady=5)
        self.property_deposit_entry.grid(row=1, column=1, padx=5, pady=5)
        self.property_term_entry.grid(row=2, column=1, padx=5, pady=5)
        self.property_interest_rate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.calculate_property_finance_button = tk.Button(self.property_finance_tab, text="Calculate", command=self.calculate_property_finance)
        self.calculate_property_finance_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.property_finance_result_label = tk.Label(self.property_finance_tab, text="")
        self.property_finance_result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def calculate_asset_finance(self):
        try:
            asset_price = float(self.asset_price_entry.get())
            deposit = float(self.deposit_entry.get())
            term = float(self.term_entry.get())
            interest_rate = float(self.interest_rate_entry.get()) / 100 / 12

            loan_amount = asset_price - deposit
            monthly_payment = loan_amount * interest_rate * (1 + interest_rate) ** (term * 12) / ((1 + interest_rate) ** (term * 12) - 1)

            self.asset_finance_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def calculate_property_finance(self):
        try:
            property_price = float(self.property_price_entry.get())
            deposit = float(self.property_deposit_entry.get())
            term = float(self.property_term_entry.get())
            interest_rate = float(self.property_interest_rate_entry.get()) / 100 / 12

            loan_amount = property_price - deposit
            monthly_payment = loan_amount * interest_rate * (1 + interest_rate) ** (term * 12) / ((1 + interest_rate) ** (term * 12) - 1)

            self.property_finance_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialCalculator(root)
    root.mainloop()
```
