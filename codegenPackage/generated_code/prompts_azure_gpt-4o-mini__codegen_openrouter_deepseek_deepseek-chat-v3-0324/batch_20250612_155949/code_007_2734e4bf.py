"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: Create a user interface mockup for a dashboard that displays the performance of meme coins in the Meme Index.
Generated: DETERMINISTIC_2734e4bfa9298db6
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class MemeCoinDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Index Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        # Sample meme coin data
        self.meme_coins = [
            {"name": "Dogecoin", "symbol": "DOGE", "price": 0.15, "change": 2.5, "volume": 500000000},
            {"name": "Shiba Inu", "symbol": "SHIB", "price": 0.000008, "change": -1.2, "volume": 300000000},
            {"name": "Pepe", "symbol": "PEPE", "price": 0.0000012, "change": 5.7, "volume": 150000000},
            {"name": "Floki", "symbol": "FLOKI", "price": 0.00002, "change": -3.4, "volume": 80000000},
            {"name": "Bonk", "symbol": "BONK", "price": 0.000015, "change": 10.2, "volume": 120000000},
        ]
        
        self.setup_ui()
        self.update_data()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", padx=10, pady=10)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame,
            text="Meme Index Dashboard",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 20, "bold")
        )
        title_label.pack(side=tk.LEFT)
        
        time_label = tk.Label(
            header_frame,
            text="",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 12)
        )
        time_label.pack(side=tk.RIGHT)
        self.time_label = time_label
        
        # Summary cards
        summary_frame = tk.Frame(self.root, bg="#f0f0f0", padx=10, pady=10)
        summary_frame.pack(fill=tk.X)
        
        metrics = [
            ("Total Market Cap", "$1.2B"),
            ("24h Volume", "$450M"),
            ("Top Gainer", "BONK (+10.2%)"),
            ("Top Loser", "FLOKI (-3.4%)")
        ]
        
        for i, (label, value) in enumerate(metrics):
            card = tk.Frame(summary_frame, bg="white", padx=15, pady=10, relief=tk.RAISED, borderwidth=1)
            card.grid(row=0, column=i, padx=5, sticky="nsew")
            
            tk.Label(card, text=label, bg="white", font=("Arial", 10)).pack()
            tk.Label(card, text=value, bg="white", font=("Arial", 14, "bold")).pack()
            
            summary_frame.columnconfigure(i, weight=1)
        
        # Main table
        table_frame = tk.Frame(self.root, bg="#f0f0f0", padx=10, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("#", "Name", "Symbol", "Price", "24h Change", "24h Volume")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)
        
        self.tree.column("#", width=50)
        self.tree.column("Name", width=200)
        self.tree.column("24h Volume", width=200)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Chart placeholder
        chart_frame = tk.Frame(self.root, bg="white", padx=10, pady=10, height=200)
        chart_frame.pack(fill=tk.X, padx=10, pady=10)
        
        chart_label = tk.Label(
            chart_frame,
            text="Price Performance Chart (Last 7 Days)",
            bg="white",
            font=("Arial", 12, "bold")
        )
        chart_label.pack()
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#2c3e50", padx=10, pady=5)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        tk.Label(
            footer_frame,
            text="Data updates every 60 seconds | Last updated: ",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 8)
        ).pack(side=tk.LEFT)
        
        self.last_updated_label = tk.Label(
            footer_frame,
            text="",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 8)
        )
        self.last_updated_label.pack(side=tk.LEFT)
    
    def update_data(self):
        # Update time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=now)
        self.last_updated_label.config(text=now)
        
        # Update table data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, coin in enumerate(self.meme_coins):
            # Simulate small price changes
            coin["price"] *= (1 + random.uniform(-0.01, 0.01))
            coin["change"] += random.uniform(-0.5, 0.5)
            coin["volume"] *= (1 + random.uniform(-0.05, 0.05))
            
            # Format values
            price = f"${coin['price']:,.8f}".rstrip('0').rstrip('.') if coin['price'] < 0.01 else f"${coin['price']:,.4f}"
            change = f"{coin['change']:+.2f}%"
            volume = f"${coin['volume']/1000000:,.1f}M"
            
            # Determine row color based on change
            tag = "up" if coin["change"] >= 0 else "down"
            
            self.tree.insert("", tk.END, values=(
                i+1,
                coin["name"],
                coin["symbol"],
                price,
                change,
                volume
            ), tags=(tag,))
        
        # Configure tag colors
        self.tree.tag_configure("up", foreground="green")
        self.tree.tag_configure("down", foreground="red")
        
        # Schedule next update
        self.root.after(60000, self.update_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeCoinDashboard(root)
    root.mainloop()
```
