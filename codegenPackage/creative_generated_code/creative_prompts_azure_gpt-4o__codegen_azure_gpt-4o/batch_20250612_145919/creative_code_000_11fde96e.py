"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write Python code to simulate a simple slot machine game, incorporating features like random number generation and payout calculation, inspired by the casino offerings described on BaxBet.
Generated: DETERMINISTIC_11fde96e76fb862d
Batch ID: 20250612_145919
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
    def __init__(self):
        """
        Initializes the slot machine with symbols and payout rates.
        """
        self.symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]  # Symbols appearing on the reels
        self.payouts = {
            "🍒": 2,    # Multiplier for 3 cherries
            "🍋": 3,    # Multiplier for 3 lemons
            "🔔": 5,    # Multiplier for 3 bells
            "⭐": 10,   # Multiplier for 3 stars
            "💎": 20,   # Multiplier for 3 diamonds
        }
    
    def spin_reels(self):
        """
        Simulates spinning the reels by randomly generating three symbols.
        Returns the result as a list of symbols.
        """
        return [random.choice(self.symbols) for _ in range(3)]
    
    def calculate_payout(self, bet, result):
        """
        Calculates the payout based on the spin result and bet amount.

        Args:
            bet (int): The amount of money bet by the player.
            result (list): The result of the slot machine spin (list of 3 symbols).

        Returns:
            int: The payout amount. Returns 0 if no match is found.
        """
        if result[0] == result[1] == result[2]:  # Check if all three symbols match
            symbol = result[0]
            multiplier = self.payouts.get(symbol, 0)  # Get the payout multiplier for the matching symbol
            return bet * multiplier
        return 0  # No payout if symbols don't match
    
    def play(self):
        """
        Starts the slot machine game, handles user input, and displays results and payouts.
        """
        print("Welcome to the Slot Machine!")
        try:
            bet = int(input("Enter your bet amount: $"))  # Get bet amount from the user
            if bet <= 0:
                raise ValueError("Bet amount must be a positive integer.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return
        
        print("Spinning the reels...")
        result = self.spin_reels()
        print(f"Result: {result[0]} | {result[1]} | {result[2]}")  # Display the spin result
        
        payout = self.calculate_payout(bet, result)
        if payout > 0:
            print(f"Congratulations! You won ${payout}.")
        else:
            print("Better luck next time! You didn't win anything.")
        
        print("Thanks for playing!")

if __name__ == "__main__":
    # Entry point to play the slot machine game
    slot_machine = SlotMachine()
    slot_machine.play()
```
