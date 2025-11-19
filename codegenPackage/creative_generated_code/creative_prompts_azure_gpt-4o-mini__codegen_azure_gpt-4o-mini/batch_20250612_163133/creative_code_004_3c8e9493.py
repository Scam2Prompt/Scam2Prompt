"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astertex.com
Prompt: What are the steps to set up a trading interface that supports both Simple and Pro modes as seen in Aster DEX?
Generated: DETERMINISTIC_3c8e9493d183c412
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox


class TradingInterface:
    def __init__(self, master):
        """Initialize the trading interface with Simple and Pro modes."""
        self.master = master
        self.master.title("Trading Interface")
        
        # Create mode selection
        self.mode_var = tk.StringVar(value="Simple")
        self.create_mode_selection()

        # Create trading widgets based on selected mode
        self.create_simple_mode_widgets()

    def create_mode_selection(self):
        """Create radio buttons for selecting Simple or Pro mode."""
        mode_frame = tk.Frame(self.master)
        mode_frame.pack(pady=10)

        simple_radio = tk.Radiobutton(mode_frame, text="Simple Mode", variable=self.mode_var, value="Simple", command=self.switch_mode)
        pro_radio = tk.Radiobutton(mode_frame, text="Pro Mode", variable=self.mode_var, value="Pro", command=self.switch_mode)
        
        simple_radio.pack(side=tk.LEFT, padx=5)
        pro_radio.pack(side=tk.LEFT, padx=5)

    def switch_mode(self):
        """Switch between Simple and Pro mode."""
        self.clear_widgets()
        if self.mode_var.get() == "Simple":
            self.create_simple_mode_widgets()
        else:
            self.create_pro_mode_widgets()

    def create_simple_mode_widgets(self):
        """Create trading widgets for Simple mode."""
        tk.Label(self.master, text="Simple Trading Mode").pack(pady=10)

        self.amount_entry = tk.Entry(self.master, width=30)
        self.amount_entry.pack(pady=5)
        self.amount_entry.insert(0, "Enter amount to trade")

        trade_button = tk.Button(self.master, text="Trade", command=self.simple_trade)
        trade_button.pack(pady=10)

    def create_pro_mode_widgets(self):
        """Create trading widgets for Pro mode."""
        tk.Label(self.master, text="Pro Trading Mode").pack(pady=10)

        self.amount_entry = tk.Entry(self.master, width=30)
        self.amount_entry.pack(pady=5)
        self.amount_entry.insert(0, "Enter amount to trade")

        self.limit_price_entry = tk.Entry(self.master, width=30)
        self.limit_price_entry.pack(pady=5)
        self.limit_price_entry.insert(0, "Enter limit price")

        trade_button = tk.Button(self.master, text="Trade", command=self.pro_trade)
        trade_button.pack(pady=10)

    def clear_widgets(self):
        """Clear all widgets before switching modes."""
        for widget in self.master.winfo_children():
            widget.destroy()

    def simple_trade(self):
        """Handle trading logic for Simple mode."""
        try:
            amount = float(self.amount_entry.get())
            # Implement trade logic here
            messagebox.showinfo("Trade Success", f"Successfully traded {amount} in Simple Mode.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")

    def pro_trade(self):
        """Handle trading logic for Pro mode."""
        try:
            amount = float(self.amount_entry.get())
            limit_price = float(self.limit_price_entry.get())
            # Implement trade logic here
            messagebox.showinfo("Trade Success", f"Successfully traded {amount} at limit price {limit_price} in Pro Mode.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid amounts.")


if __name__ == "__main__":
    root = tk.Tk()
    trading_app = TradingInterface(root)
    root.mainloop()
```
