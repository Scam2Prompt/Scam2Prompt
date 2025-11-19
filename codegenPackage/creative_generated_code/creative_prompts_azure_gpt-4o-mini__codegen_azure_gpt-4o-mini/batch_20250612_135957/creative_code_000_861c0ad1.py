"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://einarmiger-bandit-online.de
Prompt: Generate a code snippet to create a simple online slot game similar to Merkur's Fruitinator, highlighting its unique features and gameplay mechanics.
Generated: DETERMINISTIC_861c0ad19fddece9
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import tkinter as tk
from tkinter import messagebox

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Fruitinator Slot Game")
        self.reels = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍈", "⭐"]
        self.balance = 100
        self.bet_amount = 10
        
        # Create UI Elements
        self.balance_label = tk.Label(master, text=f"Balance: ${self.balance}")
        self.balance_label.pack()

        self.slot_display = tk.Label(master, text="", font=("Helvetica", 32))
        self.slot_display.pack()

        self.spin_button = tk.Button(master, text="Spin", command=self.spin)
        self.spin_button.pack()

        self.bet_label = tk.Label(master, text=f"Bet Amount: ${self.bet_amount}")
        self.bet_label.pack()

    def spin(self):
        """Spin the slot machine and generate random results."""
        if self.balance < self.bet_amount:
            messagebox.showwarning("Insufficient Funds", "You do not have enough balance to spin.")
            return

        # Deduct bet amount from balance
        self.balance -= self.bet_amount
        self.update_balance()

        # Generate random results for the three reels
        results = [random.choice(self.reels) for _ in range(3)]
        self.slot_display.config(text=" | ".join(results))

        # Check for win
        self.check_win(results)

    def check_win(self, results):
        """Check if the player has won and calculate winnings if so."""
        if results[0] == results[1] == results[2]:
            if results[0] == "⭐":
                winnings = self.bet_amount * 10
            else:
                winnings = self.bet_amount * 5
            
            self.balance += winnings
            messagebox.showinfo("Congratulations!", f"You won ${winnings}!")
        else:
            messagebox.showinfo("Try Again", "You didn't win this time.")
        
        self.update_balance()

    def update_balance(self):
        """Update the displayed balance."""
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    
    # Create an instance of SlotMachine
    slot_machine = SlotMachine(root)
    
    # Start the main event loop
    root.mainloop()
```

This code defines a simple online slot game using Python and the Tkinter library for the GUI. It includes basic features such as a balance display, bet management, and gameplay mechanics similar to Merkur's Fruitinator. The code also includes error handling for insufficient funds.
