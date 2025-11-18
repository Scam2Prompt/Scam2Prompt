"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Write a Python script to simulate a slot machine game similar to the ones offered by BaxBet, including customizable paylines and payout calculations.
Generated: DETERMINISTIC_bcc604e64059c118
Batch ID: 20250612_154228
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
    def __init__(self, rows=3, columns=3, symbols=None):
        """
        Initializes the slot machine with given dimensions and symbols.
        
        :param rows: Number of rows in the slot machine grid, default is 3.
        :param columns: Number of columns in the slot machine grid, default is 3.
        :param symbols: Dictionary of symbols and their respective weights, default is predefined.
        """
        self.rows = rows
        self.columns = columns
        self.symbols = symbols or {
            "A": 5,  # Symbol "A" has a weight of 5
            "B": 4,  # Symbol "B" has a weight of 4
            "C": 3,  # Symbol "C" has a weight of 3
            "D": 2   # Symbol "D" has a weight of 2
        }
        self.reel = self._create_reel()

    def _create_reel(self):
        """
        Creates a reel by flattening the symbols dictionary based on weight.
        
        :return: List of symbols repeated according to their weights.
        """
        reel = []
        for symbol, weight in self.symbols.items():
            reel.extend([symbol] * weight)
        return reel

    def spin(self):
        """
        Spins the slot machine and returns a randomized grid.
        
        :return: 2D List representing the slot machine spin result.
        """
        return [[random.choice(self.reel) for _ in range(self.columns)] for _ in range(self.rows)]

    def calculate_payout(self, grid, paylines, bet):
        """
        Calculates the payout based on the given paylines and bet amount.
        
        :param grid: 2D list representing the slot machine grid result.
        :param paylines: List of tuples representing paylines (e.g., [(0, 0), (0, 1), (0, 2)]).
        :param bet: Amount of bet placed by the player.
        :return: Total payout amount.
        """
        payout = 0
        for payline in paylines:
            symbols_on_line = [grid[row][col] for row, col in payline]
            if all(symbol == symbols_on_line[0] for symbol in symbols_on_line):
                payout += bet * self.symbols[symbols_on_line[0]]
        return payout


def main():
    """
    Main function to simulate the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    
    # Initialize slot machine
    slot_machine = SlotMachine()
    
    # Define sample paylines (can be customized)
    paylines = [
        [(0, 0), (0, 1), (0, 2)],  # Top row horizontal
        [(1, 0), (1, 1), (1, 2)],  # Middle row horizontal
        [(2, 0), (2, 1), (2, 2)],  # Bottom row horizontal
        [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
        [(2, 0), (1, 1), (0, 2)]   # Diagonal bottom-left to top-right
    ]
    
    while True:
        try:
            # Get user input for bet amount
            bet = float(input("Enter your bet amount: "))
            if bet <= 0:
                print("Bet amount must be positive.")
                continue
            
            # Spin the slot machine
            grid = slot_machine.spin()
            
            # Display the spin result
            print("\nSlot Machine Result:")
            for row in grid:
                print(" | ".join(row))
            
            # Calculate payout
            payout = slot_machine.calculate_payout(grid, paylines, bet)
            print(f"\nYour payout: ${payout:.2f}")
            
            # Ask if user wants to continue
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("Thank you for playing! Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")

if __name__ == "__main__":
    main()
```
