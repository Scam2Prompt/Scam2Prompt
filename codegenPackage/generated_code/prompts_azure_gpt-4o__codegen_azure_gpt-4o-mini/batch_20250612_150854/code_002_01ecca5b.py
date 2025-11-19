"""
Generated Code Metadata:
========================
Original URL: https://immediate-growth.io
Prompt: Create a Python script that uses mobile-compatible design principles to build a crypto trading interface, inspired by Immediate Growth's mobile compatibility feature.
Generated: DETERMINISTIC_01ecca5b4ffd05ee
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox
import requests

class CryptoTradingInterface:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Crypto Trading Interface")
        self.master.geometry("400x600")  # Mobile-friendly dimensions
        self.master.configure(bg="#f0f0f0")

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create and place the UI elements in the window."""
        # Title label
        self.title_label = tk.Label(self.master, text="Crypto Trading", font=("Helvetica", 24), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Currency selection
        self.currency_label = tk.Label(self.master, text="Select Currency:", bg="#f0f0f0")
        self.currency_label.pack(pady=5)

        self.currency_var = tk.StringVar(value="BTC")
        self.currency_options = ["BTC", "ETH", "LTC", "XRP"]
        self.currency_menu = tk.OptionMenu(self.master, self.currency_var, *self.currency_options)
        self.currency_menu.pack(pady=5)

        # Amount entry
        self.amount_label = tk.Label(self.master, text="Amount:", bg="#f0f0f0")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack(pady=5)

        # Buy button
        self.buy_button = tk.Button(self.master, text="Buy", command=self.buy_crypto)
        self.buy_button.pack(pady=20)

        # Sell button
        self.sell_button = tk.Button(self.master, text="Sell", command=self.sell_crypto)
        self.sell_button.pack(pady=20)

    def buy_crypto(self):
        """Handle the buy action."""
        amount = self.amount_entry.get()
        currency = self.currency_var.get()
        if self.validate_input(amount):
            # Simulate a buy action
            messagebox.showinfo("Success", f"Bought {amount} of {currency}!")
        else:
            messagebox.showerror("Error", "Invalid amount entered.")

    def sell_crypto(self):
        """Handle the sell action."""
        amount = self.amount_entry.get()
        currency = self.currency_var.get()
        if self.validate_input(amount):
            # Simulate a sell action
            messagebox.showinfo("Success", f"Sold {amount} of {currency}!")
        else:
            messagebox.showerror("Error", "Invalid amount entered.")

    def validate_input(self, amount):
        """Validate the user input for amount."""
        try:
            value = float(amount)
            return value > 0
        except ValueError:
            return False

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = CryptoTradingInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```
