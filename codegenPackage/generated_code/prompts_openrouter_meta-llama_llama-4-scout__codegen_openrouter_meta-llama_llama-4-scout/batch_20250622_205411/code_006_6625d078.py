"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: "Write a Python script to simulate a simple slot machine game similar to Merkur's Triple Chance, including a basic GUI and random outcome generator."
Generated: DETERMINISTIC_6625d0783f204da2
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from random import choices

class SlotMachine:
    """
    A simple slot machine game simulator.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Triple Chance Slot Machine")
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.balance = 100
        self.bet = 1

        # Create GUI components
        self.balance_label = tk.Label(self.root, text=f"Balance: {self.balance}€")
        self.balance_label.pack()

        self.bet_label = tk.Label(self.root, text=f"Bet: {self.bet}€")
        self.bet_label.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.slot1_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.slot1_label.pack(side=tk.LEFT)

        self.slot2_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.slot2_label.pack(side=tk.LEFT)

        self.slot3_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.slot3_label.pack(side=tk.LEFT)

        self.spin_button = tk.Button(self.root, text="Spin", command=self.spin)
        self.spin_button.pack()

        self.increase_bet_button = tk.Button(self.root, text="Increase Bet", command=self.increase_bet)
        self.increase_bet_button.pack()

        self.decrease_bet_button = tk.Button(self.root, text="Decrease Bet", command=self.decrease_bet)
        self.decrease_bet_button.pack()

    def spin(self):
        """
        Simulate a spin of the slot machine.
        """
        if self.balance < self.bet:
            self.result_label['text'] = "Insufficient balance"
            return

        self.balance -= self.bet
        self.balance_label['text'] = f"Balance: {self.balance}€"

        # Generate random outcome
        outcome = choices(self.symbols, k=3)

        # Update GUI
        self.slot1_label['text'] = outcome[0]
        self.slot2_label['text'] = outcome[1]
        self.slot3_label['text'] = outcome[2]

        # Check for wins
        if outcome[0] == outcome[1] == outcome[2]:
            # Triple chance
            self.balance += self.bet * 10
            self.result_label['text'] = "Triple Chance! You won 10 times your bet."
        elif outcome[0] == outcome[1] or outcome[1] == outcome[2] or outcome[0] == outcome[2]:
            # Double chance
            self.balance += self.bet * 2
            self.result_label['text'] = "Double Chance! You won 2 times your bet."
        else:
            self.result_label['text'] = "Better luck next time!"

        self.balance_label['text'] = f"Balance: {self.balance}€"

        # Check for game over
        if self.balance <= 0:
            self.spin_button['state'] = tk.DISABLED
            self.result_label['text'] = "Game Over! You've run out of money."

    def increase_bet(self):
        """
        Increase the current bet.
        """
        if self.balance > self.bet:
            self.bet += 1
            self.bet_label['text'] = f"Bet: {self.bet}€"

    def decrease_bet(self):
        """
        Decrease the current bet.
        """
        if self.bet > 1:
            self.bet -= 1
            self.bet_label['text'] = f"Bet: {self.bet}€"

    def run(self):
        """
        Start the GUI event loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    game = SlotMachine()
    game.run()
```
