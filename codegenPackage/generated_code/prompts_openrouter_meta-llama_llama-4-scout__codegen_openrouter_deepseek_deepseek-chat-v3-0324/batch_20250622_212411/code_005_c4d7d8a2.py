"""
Generated Code Metadata:
========================
Original URL: https://usual-app.vercel.app
Prompt: "Design a basic UI for an alternative DeFi platform inspired by Usual's galaxy theme."
Generated: DETERMINISTIC_c4d7d8a2dfc9a87c
Batch ID: 20250622_212411
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
import webbrowser

class GalaxyDeFiUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Galaxy DeFi Platform")
        self.root.geometry("900x600")
        self.root.configure(bg="#0a0a1a")
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('TFrame', background='#0a0a1a')
        style.configure('TLabel', background='#0a0a1a', foreground='#6bd6ff', font=('Helvetica', 10))
        style.configure('TButton', background='#1a1a3a', foreground='#6bd6ff', font=('Helvetica', 10), borderwidth=1)
        style.configure('TEntry', fieldbackground='#1a1a3a', foreground='white', insertcolor='white')
        style.configure('TCombobox', fieldbackground='#1a1a3a', foreground='white')
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        logo_label = ttk.Label(header_frame, text="🌌 Galaxy DeFi", font=('Helvetica', 20, 'bold'))
        logo_label.pack(side=tk.LEFT)
        
        wallet_frame = ttk.Frame(header_frame)
        wallet_frame.pack(side=tk.RIGHT)
        
        ttk.Label(wallet_frame, text="Wallet Balance:").pack(side=tk.LEFT)
        self.balance_label = ttk.Label(wallet_frame, text="0.00 ETH", font=('Helvetica', 10, 'bold'))
        self.balance_label.pack(side=tk.LEFT, padx=5)
        
        # Main content area
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Navigation
        nav_frame = ttk.Frame(content_frame, width=200)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        
        nav_buttons = [
            ("Dashboard", self.show_dashboard),
            ("Swap", self.show_swap),
            ("Stake", self.show_stake),
            ("Governance", self.show_governance),
            ("Portfolio", self.show_portfolio)
        ]
        
        for text, command in nav_buttons:
            btn = ttk.Button(nav_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=5)
        
        # Right panel - Content
        self.content_area = ttk.Frame(content_frame)
        self.content_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Footer
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Label(footer_frame, text="© 2023 Galaxy DeFi").pack(side=tk.LEFT)
        
        docs_btn = ttk.Button(footer_frame, text="Documentation", command=self.open_docs)
        docs_btn.pack(side=tk.RIGHT)
        
        # Initialize with dashboard
        self.show_dashboard()
    
    def show_dashboard(self):
        self.clear_content()
        
        ttk.Label(self.content_area, text="Dashboard", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        stats_frame = ttk.Frame(self.content_area)
        stats_frame.pack(fill=tk.X, pady=10)
        
        stats = [
            ("Total Value Locked", "$12.5M"),
            ("Active Users", "3,245"),
            ("APY", "8.25%"),
            ("Transactions", "42,189")
        ]
        
        for i, (label, value) in enumerate(stats):
            frame = ttk.Frame(stats_frame)
            frame.grid(row=0, column=i, padx=10, sticky="nsew")
            
            ttk.Label(frame, text=label).pack()
            ttk.Label(frame, text=value, font=('Helvetica', 12, 'bold')).pack()
        
        # Recent transactions
        ttk.Label(self.content_area, text="Recent Transactions", font=('Helvetica', 14)).pack(pady=(20, 5), anchor=tk.W)
        
        transactions = [
            ("ETH → USDC", "0.5 ETH", "2 hours ago"),
            ("Staked GXY", "1000 GXY", "5 hours ago"),
            ("USDC → ETH", "1000 USDC", "1 day ago")
        ]
        
        for tx in transactions:
            frame = ttk.Frame(self.content_area)
            frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(frame, text=tx[0], width=20).pack(side=tk.LEFT)
            ttk.Label(frame, text=tx[1], width=15).pack(side=tk.LEFT)
            ttk.Label(frame, text=tx[2]).pack(side=tk.RIGHT)
    
    def show_swap(self):
        self.clear_content()
        
        ttk.Label(self.content_area, text="Swap Tokens", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        swap_frame = ttk.Frame(self.content_area)
        swap_frame.pack(fill=tk.X, pady=20)
        
        # From token
        from_frame = ttk.Frame(swap_frame)
        from_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(from_frame, text="From").pack(anchor=tk.W)
        from_entry = ttk.Entry(from_frame)
        from_entry.pack(fill=tk.X)
        
        from_token = ttk.Combobox(from_frame, values=["ETH", "USDC", "GXY", "WBTC"])
        from_token.pack(fill=tk.X, pady=5)
        from_token.set("ETH")
        
        # To token
        to_frame = ttk.Frame(swap_frame)
        to_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(to_frame, text="To").pack(anchor=tk.W)
        to_entry = ttk.Entry(to_frame)
        to_entry.pack(fill=tk.X)
        
        to_token = ttk.Combobox(to_frame, values=["ETH", "USDC", "GXY", "WBTC"])
        to_token.pack(fill=tk.X, pady=5)
        to_token.set("USDC")
        
        # Swap button
        swap_btn = ttk.Button(self.content_area, text="Swap", command=self.execute_swap)
        swap_btn.pack(pady=20)
        
        # Price info
        price_frame = ttk.Frame(self.content_area)
        price_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(price_frame, text="Exchange Rate: 1 ETH = 1,850 USDC").pack(side=tk.LEFT)
        ttk.Label(price_frame, text="Slippage: 0.5%").pack(side=tk.RIGHT)
    
    def show_stake(self):
        self.clear_content()
        
        ttk.Label(self.content_area, text="Stake Tokens", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        stake_frame = ttk.Frame(self.content_area)
        stake_frame.pack(fill=tk.X, pady=20)
        
        # Token selection
        ttk.Label(stake_frame, text="Token").pack(anchor=tk.W)
        token = ttk.Combobox(stake_frame, values=["GXY", "ETH", "USDC"])
        token.pack(fill=tk.X, pady=5)
        token.set("GXY")
        
        # Amount
        ttk.Label(stake_frame, text="Amount").pack(anchor=tk.W)
        amount_entry = ttk.Entry(stake_frame)
        amount_entry.pack(fill=tk.X, pady=5)
        
        # Stake button
        stake_btn = ttk.Button(self.content_area, text="Stake", command=self.execute_stake)
        stake_btn.pack(pady=20)
        
        # Info
        info_frame = ttk.Frame(self.content_area)
        info_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(info_frame, text="Current APY: 12.
