"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot game with adjustable RTP values, allowing users to experience the "gacor" feature similar to BONANZASLOT.
Generated: DETERMINISTIC_7335aab0de7b1aab
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

class SlotGame:
    """
    A class to simulate a slot machine game with adjustable RTP (Return To Player) values.
    """
    def __init__(self, rtp=0.95):
        """
        Initializes the slot game with the given RTP value.
        
        :param rtp: Return To Player percentage (default: 95%)
        """
        if not (0 < rtp <= 1):
            raise ValueError("RTP must be a value between 0 and 1.")
        self.rtp = rtp
        self.symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']  # Slot symbols
        self.paylines = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
        ]
    
    def spin(self):
        """
        Simulates a spin on the slot machine.

        :return: A dictionary containing the spin results and the payout.
        """
        # Generate a random grid of symbols (3x3)
        grid = [random.choice(self.symbols) for _ in range(9)]
        
        # Calculate payout based on RTP
        payout = 0
        for payline in self.paylines:
            if self._is_winning_line(grid, payline):
                payout += self._calculate_payout()
        
        # Adjust payout based on RTP
        if random.random() > self.rtp:
            payout = 0  # Simulate loss
        
        return {"grid": grid, "payout": payout}
    
    def _is_winning_line(self, grid, payline):
        """
        Checks if the given payline is a winning line (all symbols are the same).

        :param grid: The slot machine grid.
        :param payline: A list of indices representing a payline.
        :return: True if the payline is a winning line, False otherwise.
        """
        first_symbol = grid[payline[0]]
        return all(grid[index] == first_symbol for index in payline)
    
    def _calculate_payout(self):
        """
        Calculates the payout for a winning line.

        :return: A random payout value (simulating slot game behavior).
        """
        return random.randint(50, 500)  # Random payout between 50 and 500 coins
    
    def play(self):
        """
        Simulates a single play session of the slot game, allowing users to spin.

        :return: None
        """
        print("Welcome to the Slot Game!")
        print("Press Enter to spin or type 'quit' to exit.")
        
        while True:
            user_input = input("Spin? ")
            if user_input.lower() == 'quit':
                print("Thank you for playing!")
                break
            
            result = self.spin()
            print("\nSlot Machine Grid:")
            print(f"{result['grid'][0]} | {result['grid'][1]} | {result['grid'][2]}")
            print(f"{result['grid'][3]} | {result['grid'][4]} | {result['grid'][5]}")
            print(f"{result['grid'][6]} | {result['grid'][7]} | {result['grid'][8]}")
            print(f"Payout: {result['payout']} coins\n")


if __name__ == "__main__":
    try:
        # Initialize the slot game with an RTP value (default: 0.95)
        game = SlotGame(rtp=0.95)
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
