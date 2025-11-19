"""
Generated Code Metadata:
========================
Original URL: https://fixedfloatio.org
Prompt: Design a basic user interface for a crypto swap platform like FixedFloat, incorporating user-friendly features for beginners and experienced traders.
Generated: DETERMINISTIC_9e265a5e7b0eb135
Batch ID: 20250622_212248
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
from decimal import Decimal, InvalidOperation

class CryptoSwapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoSwap Platform")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('TLabel', background='#f5f5f5', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        # Header
        self.header_frame = ttk.Frame(self.root)
        self.header_label = ttk.Label(
            self.header_frame, 
            text="CryptoSwap Platform", 
            style='Header.TLabel'
        )
        
        # Swap Frame
        self.swap_frame = ttk.Frame(self.root, padding=10)
        
        # From Currency
        self.from_currency_frame = ttk.Frame(self.swap_frame)
        self.from_label = ttk.Label(self.from_currency_frame, text="From:")
        self.from_currency = ttk.Combobox(
            self.from_currency_frame, 
            values=["BTC", "ETH", "USDT", "BNB", "SOL"],
            state="readonly",
            width=10
        )
        self.from_currency.current(0)
        self.from_amount = ttk.Entry(self.from_currency_frame, width=20)
        self.from_amount.insert(0, "0.0")
        
        # To Currency
        self.to_currency_frame = ttk.Frame(self.swap_frame)
        self.to_label = ttk.Label(self.to_currency_frame, text="To:")
        self.to_currency = ttk.Combobox(
            self.to_currency_frame, 
            values=["BTC", "ETH", "USDT", "BNB", "SOL"],
            state="readonly",
            width=10
        )
        self.to_currency.current(1)
        self.to_amount = ttk.Label(self.to_currency_frame, text="0.0", width=20)
        
        # Swap Button
        self.swap_button = ttk.Button(
            self.swap_frame, 
            text="⇅", 
            width=3,
            command=self.swap_currencies
        )
        
        # Rate Info
        self.rate_frame = ttk.Frame(self.swap_frame)
        self.rate_label = ttk.Label(
            self.rate_frame, 
            text="Exchange Rate: 1 BTC = 15.5 ETH"
        )
        
        # Fees Info
        self.fees_frame = ttk.Frame(self.swap_frame)
        self.fees_label = ttk.Label(
            self.fees_frame, 
            text="Transaction Fee: 0.5%"
        )
        
        # Swap Button
        self.execute_button = ttk.Button(
            self.swap_frame, 
            text="Execute Swap", 
            command=self.execute_swap
        )
        
        # Advanced Options
        self.advanced_frame = ttk.Frame(self.root, padding=10)
        self.advanced_label = ttk.Label(
            self.advanced_frame, 
            text="Advanced Options",
            style='Header.TLabel'
        )
        
        # Slippage Tolerance
        self.slippage_frame = ttk.Frame(self.advanced_frame)
        self.slippage_label = ttk.Label(
            self.slippage_frame, 
            text="Slippage Tolerance:"
        )
        self.slippage = ttk.Combobox(
            self.slippage_frame, 
            values=["0.1%", "0.5%", "1.0%", "3.0%"],
            state="readonly",
            width=10
        )
        self.slippage.current(1)
        
        # Transaction Speed
        self.speed_frame = ttk.Frame(self.advanced_frame)
        self.speed_label = ttk.Label(
            self.speed_frame, 
            text="Transaction Speed:"
        )
        self.speed = ttk.Combobox(
            self.speed_frame, 
            values=["Slow", "Medium", "Fast"],
            state="readonly",
            width=10
        )
        self.speed.current(1)
        
        # Bind events
        self.from_amount.bind("<KeyRelease>", self.calculate_amount)
        self.from_currency.bind("<<ComboboxSelected>>", self.calculate_amount)
        self.to_currency.bind("<<ComboboxSelected>>", self.calculate_amount)
    
    def setup_layout(self):
        # Header layout
        self.header_frame.pack(fill=tk.X, padx=5, pady=5)
        self.header_label.pack(pady=10)
        
        # Swap frame layout
        self.swap_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # From currency layout
        self.from_currency_frame.pack(fill=tk.X, pady=5)
        self.from_label.pack(side=tk.LEFT, padx=5)
        self.from_currency.pack(side=tk.LEFT, padx=5)
        self.from_amount.pack(side=tk.LEFT, padx=5)
        
        # Swap button layout
        self.swap_button.pack(pady=5)
        
        # To currency layout
        self.to_currency_frame.pack(fill=tk.X, pady=5)
        self.to_label.pack(side=tk.LEFT, padx=5)
        self.to_currency.pack(side=tk.LEFT, padx=5)
        self.to_amount.pack(side=tk.LEFT, padx=5)
        
        # Rate and fees layout
        self.rate_frame.pack(fill=tk.X, pady=5)
        self.rate_label.pack()
        self.fees_frame.pack(fill=tk.X, pady=5)
        self.fees_label.pack()
        
        # Execute button layout
        self.execute_button.pack(pady=10)
        
        # Advanced options layout
        self.advanced_frame.pack(fill=tk.X, padx=5, pady=10)
        self.advanced_label.pack(anchor=tk.W, pady=5)
        
        # Slippage layout
        self.slippage_frame.pack(fill=tk.X, pady=5)
        self.slippage_label.pack(side=tk.LEFT, padx=5)
        self.slippage.pack(side=tk.LEFT, padx=5)
        
        # Speed layout
        self.speed_frame.pack(fill=tk.X, pady=5)
        self.speed_label.pack(side=tk.LEFT, padx=5)
        self.speed.pack(side=tk.LEFT, padx=5)
    
    def calculate_amount(self, event=None):
        try:
            from_amount = Decimal(self.from_amount.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            # Mock conversion rates (in a real app, this would come from an API)
            rates = {
                "BTC": {"ETH": Decimal('15.5'), "USDT": Decimal('50000'), "BNB": Decimal('1000'), "SOL": Decimal('2000')},
                "ETH": {"BTC": Decimal('0.0645'), "USDT": Decimal('3200'), "BNB": Decimal('64'), "SOL": Decimal('128')},
                "USDT": {"BTC": Decimal('0.00002'), "ETH": Decimal('0.0003125'), "BNB": Decimal('0.02'), "SOL": Decimal('0.04')},
                "BNB": {"BTC": Decimal('0.001'), "ETH": Decimal('0.0156'), "USDT": Decimal('50'), "SOL": Decimal('2')},
                "SOL": {"BTC": Decimal('0.0005'), "ETH": Decimal('0.0078'), "USDT": Decimal('25'), "BNB": Decimal('0.5')}
            }
            
            if from_curr == to_curr:
                to_amount = from_amount
            else:
                to_amount = from_amount * rates[from_curr][to_curr]
            
            self.to_amount.config(text=f"{to_amount:.8f}".rstrip('0').rstrip('.') if '.' in f"{to_amount:.8f}" else f"{to_amount:.8f}")
            
            # Update rate label
            self.rate_label.config(text=f"Exchange Rate: 1 {from_curr} = {rates[from_curr][to_curr]} {to_curr}")
            
        except InvalidOperation:
            self.to_amount.config(text="0.0")
    
    def swap_currencies
