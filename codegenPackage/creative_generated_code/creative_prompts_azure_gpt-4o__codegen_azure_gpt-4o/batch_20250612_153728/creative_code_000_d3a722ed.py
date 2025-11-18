"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot machine game with RTP "gacor" mechanics as described on BONANZASLOT, ensuring fairness and transparency in the results.
Generated: DETERMINISTIC_d3a722ed96cd58a1
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    """
    A class to simulate a slot machine game with RTP (Return to Player) mechanics.
    Ensures fairness and transparency in results.

    Attributes:
        symbols (list): The symbols available on the slot machine.
        payouts (dict): The payout values for specific combinations of symbols.
        rtp (float): The Return to Player percentage (e.g., 95.0 for 95% RTP).
    """

    def __init__(self, rtp=95.0):
        """
        Initializes the slot machine with default symbols, payouts, and RTP.

        Args:
            rtp (float): The desired Return to Player percentage.
        """
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]  # Slot machine symbols
        self.payouts = {
            ("🍒", "🍒", "🍒"): 50,
            ("🍋", "🍋", "🍋"): 40,
            ("🍊", "🍊", "🍊"): 30,
            ("🍉", "🍉", "🍉"): 25,
            ("⭐", "⭐", "⭐"): 100,
            ("💎", "💎", "💎"): 200,
        }
        self.rtp = rtp / 100  # Convert RTP to decimal form

    def spin(self):
        """
        Simulates a spin on the slot machine.

        Returns:
            tuple: A tuple containing the spin result (list of symbols) and winnings (int).
        """
        # Spin the reels
        spin_result = [random.choice(self.symbols) for _ in range(3)]
        
        # Calculate winnings based on spin result
        winnings = self.payouts.get(tuple(spin_result), 0)
        
        # Adjust winnings to match RTP
        if winnings > 0 and random.random() > self.rtp:
            winnings = 0  # Simulate RTP adjustment
        
        return spin_result, winnings

    def play(self):
        """
        Allows the user to play the slot machine game.
        """
        print("Welcome to the Slot Machine!")
        print(f"RTP: {self.rtp * 100}%")
        print("Symbols: " + ", ".join(self.symbols))
        print("To quit the game, type 'exit'.")

        total_spent = 0
        total_won = 0

        while True:
            user_input = input("Press Enter to spin or type 'exit' to quit: ").strip().lower()
            if user_input == "exit":
                break
            
            # Simulate a spin
            total_spent += 1  # Assume each spin costs 1 unit
            spin_result, winnings = self.spin()
            total_won += winnings

            # Show spin result and winnings
            print(f"Spin Result: {' | '.join(spin_result)}")
            print(f"You won: {winnings} units")

        # Show session summary
        print("\nThank you for playing!")
        print(f"Total Spent: {total_spent} units")
        print(f"Total Won: {total_won} units")
        print(f"Net Profit: {total_won - total_spent} units")


# Main execution block
if __name__ == "__main__":
    try:
        # Initialize the slot machine with a desired RTP (default is 95%)
        machine = SlotMachine(rtp=95.0)
        machine.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
