"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Design a user interface for the EarthMeta Wallet app, allowing users to track their token performance and rewards in real-time, as well as manage their digital assets.
Generated: DETERMINISTIC_d6b3506731232fb3
Batch ID: 20250622_211557
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
from datetime import datetime
import json
import requests
from threading import Thread

class EarthMetaWalletApp:
    def __init__(self, root):
        """
        Initialize the EarthMeta Wallet application.
        
        Args:
            root (tk.Tk): The root window for the application.
        """
        self.root = root
        self.root.title("EarthMeta Wallet")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load user data
        self.user_data = self.load_user_data()
        
        # Initialize UI components
        self.setup_ui()
        
        # Start background data refresh
        self.refresh_data()
    
    def setup_ui(self):
        """Setup the main UI components."""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            self.header_frame,
            text="EarthMeta Wallet",
            font=("Helvetica", 16, "bold")
        ).pack(side=tk.LEFT)
        
        self.refresh_btn = ttk.Button(
            self.header_frame,
            text="Refresh",
            command=self.refresh_data
        )
        self.refresh_btn.pack(side=tk.RIGHT)
        
        # Balance display
        self.balance_frame = ttk.LabelFrame(
            self.main_frame,
            text="Token Balances",
            padding="10"
        )
        self.balance_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.balance_tree = ttk.Treeview(
            self.balance_frame,
            columns=("token", "balance", "value"),
            show="headings",
            height=5
        )
        self.balance_tree.heading("token", text="Token")
        self.balance_tree.heading("balance", text="Balance")
        self.balance_tree.heading("value", text="Value (USD)")
        self.balance_tree.pack(fill=tk.X)
        
        # Rewards display
        self.rewards_frame = ttk.LabelFrame(
            self.main_frame,
            text="Rewards",
            padding="10"
        )
        self.rewards_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.rewards_tree = ttk.Treeview(
            self.rewards_frame,
            columns=("date", "type", "amount", "value"),
            show="headings",
            height=5
        )
        self.rewards_tree.heading("date", text="Date")
        self.rewards_tree.heading("type", text="Type")
        self.rewards_tree.heading("amount", text="Amount")
        self.rewards_tree.heading("value", text="Value (USD)")
        self.rewards_tree.pack(fill=tk.X)
        
        # Transaction controls
        self.transaction_frame = ttk.Frame(self.main_frame)
        self.transaction_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            self.transaction_frame,
            text="Send Tokens",
            font=("Helvetica", 12)
        ).pack(anchor=tk.W)
        
        self.send_frame = ttk.Frame(self.transaction_frame)
        self.send_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(self.send_frame, text="Token:").pack(side=tk.LEFT, padx=(0, 5))
        self.token_var = tk.StringVar()
        self.token_combobox = ttk.Combobox(
            self.send_frame,
            textvariable=self.token_var,
            state="readonly"
        )
        self.token_combobox.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(self.send_frame, text="Amount:").pack(side=tk.LEFT, padx=(0, 5))
        self.amount_entry = ttk.Entry(self.send_frame, width=15)
        self.amount_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(self.send_frame, text="To:").pack(side=tk.LEFT, padx=(0, 5))
        self.recipient_entry = ttk.Entry(self.send_frame, width=30)
        self.recipient_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        self.send_btn = ttk.Button(
            self.send_frame,
            text="Send",
            command=self.send_tokens
        )
        self.send_btn.pack(side=tk.LEFT)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        
        # Initialize data
        self.update_ui()
    
    def load_user_data(self):
        """
        Load user data from file or API.
        
        Returns:
            dict: User data including balances and rewards.
        """
        try:
            # In a real app, this would fetch from an API
            # For demo, we'll use a sample data structure
            return {
                "balances": [
                    {"token": "EMT", "balance": 1000, "value": 5000},
                    {"token": "BTC", "balance": 0.5, "value": 20000},
                    {"token": "ETH", "balance": 5, "value": 10000}
                ],
                "rewards": [
                    {"date": "2023-01-01", "type": "Staking", "amount": 10, "value": 50},
                    {"date": "2023-01-02", "type": "Referral", "amount": 5, "value": 25}
                ]
            }
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load user data: {str(e)}")
            return {"balances": [], "rewards": []}
    
    def update_ui(self):
        """Update the UI with current data."""
        # Clear existing data
        for item in self.balance_tree.get_children():
            self.balance_tree.delete(item)
        
        for item in self.rewards_tree.get_children():
            self.rewards_tree.delete(item)
        
        # Update balances
        for balance in self.user_data.get("balances", []):
            self.balance_tree.insert("", tk.END, values=(
                balance["token"],
                balance["balance"],
                f"${balance['value']:,.2f}"
            ))
        
        # Update rewards
        for reward in self.user_data.get("rewards", []):
            self.rewards_tree.insert("", tk.END, values=(
                reward["date"],
                reward["type"],
                reward["amount"],
                f"${reward['value']:,.2f}"
            ))
        
        # Update token combobox
        tokens = [b["token"] for b in self.user_data.get("balances", [])]
        self.token_combobox["values"] = tokens
        if tokens:
            self.token_combobox.current(0)
    
    def refresh_data(self):
        """Refresh data from the server."""
        self.status_var.set("Refreshing data...")
        self.refresh_btn.config(state=tk.DISABLED)
        
        def fetch_data():
            try:
                # Simulate API call
                # In a real app, this would be an actual API request
                self.user_data = self.load_user_data()
                self.root.after(0, self.update_ui)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Failed to refresh data: {str(e)}"
                ))
            finally:
                self.root.after(0, lambda: self.status_var.set("Ready"))
                self.root.after(0, lambda: self.refresh_btn.config(state=tk.NORMAL))
        
        # Run in background thread to avoid UI freeze
        Thread(target=fetch_data, daemon=True).start()
    
    def send_tokens(self):
        """Handle token sending."""
        token = self.token_var.get()
        amount = self.amount_entry.get()
        recipient = self.recipient_entry.get()
        
        if not all([token, amount, recipient]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return
        
        # Check balance
        balance = next(
            (b for b in self.user_data["balances"] if b["token"]
