"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Create a user interface mockup for a dashboard that displays the performance of meme coins in the Meme Index.
Generated: DETERMINISTIC_2734e4bfa9298db6
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import ttk
import random

class MemeCoinDashboard(tk.Tk):
    """Class to represent the Meme Coin Dashboard."""

    def __init__(self):
        """Initialize the dashboard UI."""
        super().__init__()
        self.title("Meme Coin Performance Dashboard")
        self.geometry("600x400")

        # Create frame for the chart
        self.chart_frame = ttk.Frame(self)
        self.chart_frame.pack(pady=10)

        # Title label
        self.title_label = ttk.Label(self, text="Meme Coin Performance Index", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Treeview for displaying meme coin data
        self.tree = ttk.Treeview(self.chart_frame, columns=("Name", "Price", "Market Cap", "Change"), show='headings')
        self.tree.heading("Name", text="Coin Name")
        self.tree.heading("Price", text="Price (USD)")
        self.tree.heading("Market Cap", text="Market Cap (USD)")
        self.tree.heading("Change", text="24h Change (%)")

        self.tree.column("Name", width=150)
        self.tree.column("Price", width=100)
        self.tree.column("Market Cap", width=150)
        self.tree.column("Change", width=100)

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Load data button
        self.load_button = ttk.Button(self, text="Load Meme Coin Data", command=self.load_data)
        self.load_button.pack(pady=10)

    def load_data(self):
        """Load and display random meme coin data."""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Example meme coins data (in a real scenario, this would come from an API)
        meme_coins = [
            {"name": "DogeCoin", "price": random.uniform(0.01, 0.50), "market_cap": random.randint(1_000_000, 50_000_000), "change": random.uniform(-10, 10)},
            {"name": "Shiba Inu", "price": random.uniform(0.0001, 0.01), "market_cap": random.randint(500_000, 20_000_000), "change": random.uniform(-10, 10)},
            {"name": "SafeMoon", "price": random.uniform(0.0001, 0.01), "market_cap": random.randint(300_000, 15_000_000), "change": random.uniform(-10, 10)},
            {"name": "PepeCoin", "price": random.uniform(0.00001, 0.001), "market_cap": random.randint(100_000, 5_000_000), "change": random.uniform(-10, 10)},
        ]

        # Insert data into the tree view
        for coin in meme_coins:
            self.tree.insert("", tk.END, values=(coin["name"], f"${coin['price']:.4f}", f"${coin['market_cap']:,}", f"{coin['change']:.2f}%"))

if __name__ == "__main__":
    try:
        app = MemeCoinDashboard()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
