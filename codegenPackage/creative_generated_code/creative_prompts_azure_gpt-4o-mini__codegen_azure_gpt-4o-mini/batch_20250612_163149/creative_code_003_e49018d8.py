"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risesparksolution.com
Prompt: Develop a user-friendly dashboard interface that incorporates customizable features and portfolio management tools as described on RiseSparkSolution.
Generated: DETERMINISTIC_e49018d86cbc6cd5
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar, DoubleVar
from typing import List

class PortfolioManager:
    """A class to manage a user's portfolio."""

    def __init__(self):
        self.portfolio = {}

    def add_asset(self, name: str, value: float) -> None:
        """Add an asset to the portfolio."""
        if name in self.portfolio:
            messagebox.showwarning("Warning", f"Asset '{name}' already exists.")
        else:
            self.portfolio[name] = value
            messagebox.showinfo("Success", f"Asset '{name}' added with value {value}.")

    def remove_asset(self, name: str) -> None:
        """Remove an asset from the portfolio."""
        if name in self.portfolio:
            del self.portfolio[name]
            messagebox.showinfo("Success", f"Asset '{name}' removed.")
        else:
            messagebox.showwarning("Warning", f"Asset '{name}' does not exist.")

    def get_portfolio(self) -> List[str]:
        """Return a list of assets in the portfolio."""
        return [f"{name}: ${value:.2f}" for name, value in self.portfolio.items()]


class Dashboard(tk.Tk):
    """Main dashboard interface for the user."""

    def __init__(self):
        super().__init__()

        self.title("Portfolio Management Dashboard")
        self.geometry("400x400")

        # Initialize portfolio manager
        self.portfolio_manager = PortfolioManager()

        # String variables for input
        self.asset_name = StringVar()
        self.asset_value = DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange widgets in the dashboard."""
        ttk.Label(self, text="Asset Name:").pack(pady=5)
        asset_name_entry = ttk.Entry(self, textvariable=self.asset_name)
        asset_name_entry.pack(pady=5)

        ttk.Label(self, text="Asset Value:").pack(pady=5)
        asset_value_entry = ttk.Entry(self, textvariable=self.asset_value)
        asset_value_entry.pack(pady=5)

        add_button = ttk.Button(self, text="Add Asset", command=self.add_asset)
        add_button.pack(pady=5)

        remove_button = ttk.Button(self, text="Remove Asset", command=self.remove_asset)
        remove_button.pack(pady=5)

        view_button = ttk.Button(self, text="View Portfolio", command=self.view_portfolio)
        view_button.pack(pady=20)

    def add_asset(self):
        """Add asset to portfolio from user input."""
        name = self.asset_name.get()
        value = self.asset_value.get()
        
        if name and value >= 0:
            self.portfolio_manager.add_asset(name, value)
            self.asset_name.set("")
            self.asset_value.set(0.0)
        else:
            messagebox.showerror("Error", "Please enter a valid asset name and value.")

    def remove_asset(self):
        """Remove asset from portfolio based on user input."""
        name = self.asset_name.get()
        
        if name:
            self.portfolio_manager.remove_asset(name)
            self.asset_name.set("")
        else:
            messagebox.showerror("Error", "Please enter a valid asset name to remove.")

    def view_portfolio(self):
        """Display current portfolio in a message box."""
        portfolio = self.portfolio_manager.get_portfolio()
        if portfolio:
            messagebox.showinfo("Current Portfolio", "\n".join(portfolio))
        else:
            messagebox.showinfo("Current Portfolio", "Your portfolio is empty.")


if __name__ == "__main__":
    try:
        app = Dashboard()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
```
