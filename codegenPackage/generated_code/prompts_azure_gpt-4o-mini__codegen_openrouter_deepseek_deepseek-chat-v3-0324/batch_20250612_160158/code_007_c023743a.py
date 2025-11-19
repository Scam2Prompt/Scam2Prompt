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

class FinancialCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Loan Comparison Calculator")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and arrange all UI components"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header = ttk.Label(main_frame, text="Loan Comparison Calculator", style='Header.TLabel')
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Notebook for different loan types
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky='nsew')
        
        # Property Finance Tab
        self.create_property_finance_tab()
        
        # Asset Finance Tab
        self.create_asset_finance_tab()
        
        # Results Frame
        results_frame = ttk.LabelFrame(main_frame, text="Comparison Results")
        results_frame.grid(row=2, column=0, columnspan=2, sticky='nsew', pady=(20, 0))
        
        # Results Treeview
        self.results_tree = ttk.Treeview(results_frame, columns=('Type', 'Amount', 'Term', 'Rate', 'Monthly', 'Total'), show='headings')
        self.results_tree.heading('Type', text='Loan Type')
        self.results_tree.heading('Amount', text='Amount ($)')
        self.results_tree.heading('Term', text='Term (years)')
        self.results_tree.heading('Rate', text='Rate (%)')
        self.results_tree.heading('Monthly', text='Monthly Payment')
        self.results_tree.heading('Total', text='Total Cost')
        
        for col in ('Type', 'Amount', 'Term', 'Rate', 'Monthly', 'Total'):
            self.results_tree.column(col, width=120, anchor='center')
        
        self.results_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Calculate Button
        calculate_btn = ttk.Button(main_frame, text="Compare Loans", command=self.calculate_loans)
        calculate_btn.grid(row=3, column=0, columnspan=2, pady=(20, 0))
    
    def create_property_finance_tab(self):
        """Create the property finance tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Property Finance")
        
        # Input fields
        ttk.Label(tab, text="Loan Amount ($):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.prop_amount = ttk.Entry(tab)
        self.prop_amount.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Loan Term (years):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.prop_term = ttk.Entry(tab)
        self.prop_term.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Interest Rate (%):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.prop_rate = ttk.Entry(tab)
        self.prop_rate.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Property Type:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.prop_type = ttk.Combobox(tab, values=["Residential", "Commercial", "Investment"])
        self.prop_type.grid(row=3, column=1, padx=5, pady=5)
        self.prop_type.current(0)
    
    def create_asset_finance_tab(self):
        """Create the asset finance tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Asset Finance")
        
        # Input fields
        ttk.Label(tab, text="Asset Value ($):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.asset_amount = ttk.Entry(tab)
        self.asset_amount.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Loan Term (years):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.asset_term = ttk.Entry(tab)
        self.asset_term.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Interest Rate (%):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.asset_rate = ttk.Entry(tab)
        self.asset_rate.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(tab, text="Asset Type:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.asset_type = ttk.Combobox(tab, values=["Vehicle", "Equipment", "Machinery", "Other"])
        self.asset_type.grid(row=3, column=1, padx=5, pady=5)
        self.asset_type.current(0)
    
    def calculate_loan(self, amount, term, rate):
        """Calculate monthly payment and total cost of loan"""
        try:
            amount = float(amount)
            term = float(term)
            rate = float(rate) / 100  # Convert to decimal
            
            monthly_rate = rate / 12
            num_payments = term * 12
            
            # Monthly payment calculation
            if rate == 0:
                monthly_payment = amount / num_payments
            else:
                monthly_payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
            
            total_cost = monthly_payment * num_payments
            
            return round(monthly_payment, 2), round(total_cost, 2)
        
        except ValueError:
            return None
    
    def calculate_loans(self):
        """Calculate and compare both loan options"""
        # Clear previous results
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Property finance calculation
        prop_amount = self.prop_amount.get()
        prop_term = self.prop_term.get()
        prop_rate = self.prop_rate.get()
        
        prop_result = self.calculate_loan(prop_amount, prop_term, prop_rate)
        
        if prop_result:
            monthly, total = prop_result
            self.results_tree.insert('', 'end', values=(
                f"Property ({self.prop_type.get()})",
                f"${float(prop_amount):,.2f}",
                prop_term,
                f"{float(prop_rate):.2f}%",
                f"${monthly:,.2f}",
                f"${total:,.2f}"
            ))
        else:
            messagebox.showerror("Error", "Invalid property finance input values")
            return
        
        # Asset finance calculation
        asset_amount = self.asset_amount.get()
        asset_term = self.asset_term.get()
        asset_rate = self.asset_rate.get()
        
        asset_result = self.calculate_loan(asset_amount, asset_term, asset_rate)
        
        if asset_result:
            monthly, total = asset_result
            self.results_tree.insert('', 'end', values=(
                f"Asset ({self.asset_type.get()})",
                f"${float(asset_amount):,.2f}",
                asset_term,
                f"{float(asset_rate):.2f}%",
                f"${monthly:,.2f}",
                f"${total:,.2f}"
            ))
        else:
            messagebox.showerror("Error", "Invalid asset finance input values")

if __name__ == "__main__":
    root = tk.T
