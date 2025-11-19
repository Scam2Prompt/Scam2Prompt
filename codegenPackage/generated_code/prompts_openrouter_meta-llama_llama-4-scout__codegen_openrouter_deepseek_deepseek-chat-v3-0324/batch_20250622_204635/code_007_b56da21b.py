"""
Generated Code Metadata:
========================
Original URL: https://qudefi-ai.pages.dev
Prompt: "Design a user interface for QuDefi's Revenue App, allowing users to monitor their earnings, rewards, and overall financial performance within the QuDefi ecosystem."
Generated: DETERMINISTIC_b56da21b7cca486e
Batch ID: 20250622_204635
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
import json
import requests
from datetime import datetime

class QuDefiRevenueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuDefi Revenue App")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 14, "bold"))
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TEntry", font=("Arial", 10))
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.header_label = ttk.Label(
            self.header_frame,
            text="QuDefi Revenue Dashboard",
            style="Header.TLabel"
        )
        self.header_label.pack(side=tk.LEFT)
        
        # Refresh button
        self.refresh_button = ttk.Button(
            self.header_frame,
            text="Refresh",
            command=self.refresh_data
        )
        self.refresh_button.pack(side=tk.RIGHT)
        
        # Stats frame
        self.stats_frame = ttk.Frame(self.main_frame)
        self.stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Stats widgets
        stats = [
            ("Total Earnings", "0 QDF"),
            ("Current Rewards", "0 QDF"),
            ("APY", "0%"),
            ("Last Updated", "Never")
        ]
        
        self.stat_widgets = []
        for i, (title, value) in enumerate(stats):
            frame = ttk.Frame(self.stats_frame)
            frame.grid(row=0, column=i, padx=10, sticky=tk.W)
            
            title_label = ttk.Label(frame, text=title)
            title_label.pack()
            
            value_label = ttk.Label(frame, text=value, font=("Arial", 12, "bold"))
            value_label.pack()
            
            self.stat_widgets.append(value_label)
        
        # Main content
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Earnings history
        self.history_frame = ttk.LabelFrame(
            self.content_frame,
            text="Earnings History",
            padding=10
        )
        self.history_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self.history_tree = ttk.Treeview(
            self.history_frame,
            columns=("date", "amount", "type", "tx_hash"),
            show="headings"
        )
        
        self.history_tree.heading("date", text="Date")
        self.history_tree.heading("amount", text="Amount (QDF)")
        self.history_tree.heading("type", text="Type")
        self.history_tree.heading("tx_hash", text="Transaction Hash")
        
        self.history_tree.column("date", width=120)
        self.history_tree.column("amount", width=100)
        self.history_tree.column("type", width=100)
        self.history_tree.column("tx_hash", width=200)
        
        scrollbar = ttk.Scrollbar(
            self.history_frame,
            orient=tk.VERTICAL,
            command=self.history_tree.yview
        )
        self.history_tree.configure(yscrollcommand=scrollbar.set)
        
        self.history_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Rewards breakdown
        self.rewards_frame = ttk.LabelFrame(
            self.content_frame,
            text="Rewards Breakdown",
            padding=10
        )
        self.rewards_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.rewards_tree = ttk.Treeview(
            self.rewards_frame,
            columns=("source", "amount", "percentage"),
            show="headings"
        )
        
        self.rewards_tree.heading("source", text="Source")
        self.rewards_tree.heading("amount", text="Amount (QDF)")
        self.rewards_tree.heading("percentage", text="Percentage")
        
        self.rewards_tree.column("source", width=150)
        self.rewards_tree.column("amount", width=100)
        self.rewards_tree.column("percentage", width=100)
        
        scrollbar = ttk.Scrollbar(
            self.rewards_frame,
            orient=tk.VERTICAL,
            command=self.rewards_tree.yview
        )
        self.rewards_tree.configure(yscrollcommand=scrollbar.set)
        
        self.rewards_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Footer
        self.footer_frame = ttk.Frame(self.main_frame)
        self.footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.status_label = ttk.Label(
            self.footer_frame,
            text="Ready",
            style="TLabel"
        )
        self.status_label.pack(side=tk.LEFT)
        
        self.version_label = ttk.Label(
            self.footer_frame,
            text="v1.0.0",
            style="TLabel"
        )
        self.version_label.pack(side=tk.RIGHT)
        
        # Initialize with sample data
        self.refresh_data()
    
    def refresh_data(self):
        """Refresh all data from the API"""
        try:
            # Simulate API call
            # In a real app, this would be replaced with actual API calls
            response = {
                "total_earnings": 1250.75,
                "current_rewards": 42.30,
                "apy": 12.5,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "history": [
                    {"date": "2023-05-01", "amount": 50.00, "type": "Staking", "tx_hash": "0x123...abc"},
                    {"date": "2023-05-02", "amount": 25.50, "type": "Liquidity", "tx_hash": "0x456...def"},
                    {"date": "2023-05-03", "amount": 12.25, "type": "Staking", "tx_hash": "0x789...ghi"},
                ],
                "rewards_breakdown": [
                    {"source": "Staking", "amount": 75.25, "percentage": 60},
                    {"source": "Liquidity Mining", "amount": 25.50, "percentage": 20},
                    {"source": "Governance", "amount": 12.50, "percentage": 10},
                    {"source": "Referrals", "amount": 12.50, "percentage": 10},
                ]
            }
            
            # Update stats
            self.stat_widgets[0].config(text=f"{response['total_earnings']} QDF")
            self.stat_widgets[1].config(text=f"{response['current_rewards']} QDF")
            self.stat_widgets[2].config(text=f"{response['apy']}%")
            self.stat_widgets[3].config(text=response['last_updated'])
            
            # Update history
            self.history_tree.delete(*self.history_tree.get_children())
            for item in response['history']:
                self.history_tree.insert("", tk.END, values=(
                    item['date'],
                    item['amount'],
                    item['type'],
                    item['tx_hash']
                ))
            
            # Update rewards breakdown
            self.rewards_tree.delete(*self.rewards_tree.get_children())
            for item in response['rewards_breakdown']:
                self.rewards_tree.insert("", tk.END, values=(
                    item['source'],
                    item['amount'],
                    f"{item['percentage']}%"
                ))
            
            self.status_label.config(text="Data refreshed successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh data: {str(e)}")
            self.status_label.config(text="Error refreshing data")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuDefiRevenueApp
