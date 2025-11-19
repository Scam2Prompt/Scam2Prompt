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
# Import required modules
import tkinter as tk
from tkinter import messagebox

# Define the TradingInterface class
class TradingInterface:
    def __init__(self, root):
        """
        Initialize the trading interface, supporting both Simple and Pro modes.
        :param root: Tk object, the root window for the application.
        """
        self.root = root
        self.root.title("Aster DEX - Trading Interface")
        self.mode = tk.StringVar(value="Simple")  # Default mode

        # Set up the UI
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for the trading application."""
        # Create a mode selector
        mode_frame = tk.Frame(self.root)
        mode_frame.pack(pady=10)

        tk.Label(mode_frame, text="Select Mode:").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(mode_frame, text="Simple", variable=self.mode, value="Simple",
                       command=self.switch_mode).pack(side=tk.LEFT)
        tk.Radiobutton(mode_frame, text="Pro", variable=self.mode, value="Pro",
                       command=self.switch_mode).pack(side=tk.LEFT)

        # Create a frame for Simple mode
        self.simple_frame = tk.Frame(self.root)
        self.pro_frame = tk.Frame(self.root)  # Create a frame for Pro mode
        self.setup_simple_mode_ui()  # Initialize Simple mode UI
        self.setup_pro_mode_ui()  # Initialize Pro mode UI

        # Display the default mode
        self.switch_mode()

    def setup_simple_mode_ui(self):
        """Set up UI elements for Simple mode."""
        tk.Label(self.simple_frame, text="Simple Mode Trading", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.simple_frame, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(self.simple_frame)
        amount_entry.pack(pady=5)

        submit_button = tk.Button(self.simple_frame, text="Submit Trade", command=lambda: self.handle_trade(amount_entry.get()))
        submit_button.pack(pady=10)

    def setup_pro_mode_ui(self):
        """Set up UI elements for Pro mode."""
        tk.Label(self.pro_frame, text="Pro Mode Trading", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.pro_frame, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(self.pro_frame)
        amount_entry.pack(pady=5)

        tk.Label(self.pro_frame, text="Price:").pack(pady=5)
        price_entry = tk.Entry(self.pro_frame)
        price_entry.pack(pady=5)

        submit_button = tk.Button(self.pro_frame, text="Submit Trade",
                                  command=lambda: self.handle_trade(amount_entry.get(), price_entry.get()))
        submit_button.pack(pady=10)

    def switch_mode(self):
        """Switch between Simple and Pro modes based on user selection."""
        # Hide both frames and show the selected mode
        self.simple_frame.pack_forget()
        self.pro_frame.pack_forget()

        if self.mode.get() == "Simple":
            self.simple_frame.pack(pady=20)
        elif self.mode.get() == "Pro":
            self.pro_frame.pack(pady=20)

    def handle_trade(self, amount, price=None):
        """
        Handle trade submission for both Simple and Pro modes.
        :param amount: str, the amount to trade.
        :param price: str, the price for the trade (only applicable in Pro mode).
        """
        try:
            # Validate and process trade
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            if self.mode.get() == "Pro":
                if price is None:
                    raise ValueError("Price is required in Pro mode.")
                price = float(price)
                if price <= 0:
                    raise ValueError("Price must be greater than zero.")
                messagebox.showinfo("Trade Submitted", f"Pro Trade Submitted\nAmount: {amount}\nPrice: {price}")
            else:
                messagebox.showinfo("Trade Submitted", f"Simple Trade Submitted\nAmount: {amount}")

        except ValueError as e:
            # Handle validation errors
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            # Handle unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TradingInterface(root)
    root.mainloop()
```
