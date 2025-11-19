"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: Write a Python script that simulates the coin accumulation process in the Hamster Kombat game, allowing users to click and earn coins at a specified rate.
Generated: DETERMINISTIC_6ab79f8b5784532c
Batch ID: 20250612_160940
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
import time
import threading

class HamsterKombatCoinSimulator:
    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()
        self.root.title("Hamster Kombat Coin Simulator")
        self.root.geometry("400x300")
        
        # Initialize coin-related variables
        self.coins = 0
        self.coin_rate = 1  # Coins earned per click
        self.auto_click_rate = 0  # Coins earned automatically per second
        self.running = True  # Flag to control the auto-click thread
        
        # Create UI elements
        self.create_widgets()
        
        # Start the auto-click thread
        self.start_auto_click_thread()

    def create_widgets(self):
        """Create and place UI elements in the application window."""
        # Label to display the current coin count
        self.coin_label = tk.Label(self.root, text=f"Coins: {self.coins}", font=("Arial", 16))
        self.coin_label.pack(pady=20)
        
        # Button to simulate clicking and earning coins
        self.click_button = tk.Button(self.root, text="Click to Earn Coins", font=("Arial", 14), command=self.earn_coins)
        self.click_button.pack(pady=10)
        
        # Entry to set the auto-click rate
        self.auto_click_entry = tk.Entry(self.root, font=("Arial", 12))
        self.auto_click_entry.pack(pady=10)
        self.auto_click_entry.insert(0, "Enter auto-click rate (coins/sec)")
        
        # Button to update the auto-click rate
        self.update_rate_button = tk.Button(self.root, text="Update Auto-Click Rate", font=("Arial", 12), command=self.update_auto_click_rate)
        self.update_rate_button.pack(pady=10)
        
        # Button to exit the application
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 12), command=self.exit_application)
        self.exit_button.pack(pady=10)

    def earn_coins(self):
        """Simulate earning coins by clicking."""
        self.coins += self.coin_rate
        self.update_coin_label()

    def update_coin_label(self):
        """Update the coin count label."""
        self.coin_label.config(text=f"Coins: {self.coins}")

    def update_auto_click_rate(self):
        """Update the auto-click rate based on user input."""
        try:
            # Validate and update the auto-click rate
            new_rate = float(self.auto_click_entry.get())
            if new_rate < 0:
                raise ValueError("Auto-click rate must be non-negative.")
            self.auto_click_rate = new_rate
            messagebox.showinfo("Success", f"Auto-click rate updated to {self.auto_click_rate} coins/sec.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def auto_click(self):
        """Simulate earning coins automatically at the specified rate."""
        while self.running:
            if self.auto_click_rate > 0:
                self.coins += self.auto_click_rate
                self.update_coin_label()
            time.sleep(1)

    def start_auto_click_thread(self):
        """Start a separate thread for the auto-click functionality."""
        auto_click_thread = threading.Thread(target=self.auto_click, daemon=True)
        auto_click_thread.start()

    def exit_application(self):
        """Exit the application gracefully."""
        self.running = False  # Stop the auto-click thread
        self.root.destroy()

    def run(self):
        """Run the main application loop."""
        self.root.mainloop()


# Entry point for the script
if __name__ == "__main__":
    simulator = HamsterKombatCoinSimulator()
    simulator.run()
```
