"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://situsgresiktoto.com
Prompt: How can I create a slot game using the features highlighted on GRESIKTOTO, specifically focusing on high win rates and game variety?
Generated: DETERMINISTIC_777665b4e6b9b168
Batch ID: 20250612_135929
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
    def __init__(self, reels, symbols, win_table):
        """
        Initializes the SlotGame with given parameters.
        
        :param reels: Number of reels in the slot game
        :param symbols: List of symbols available on the reels
        :param win_table: Dictionary mapping combinations of symbols to their win amounts
        """
        self.reels = reels
        self.symbols = symbols
        self.win_table = win_table

    def spin(self):
        """
        Simulates a spin of the slot machine, generating a random outcome on each reel.
        
        :return: List of symbols representing the outcome of the spin
        """
        return [random.choice(self.symbols) for _ in range(self.reels)]

    def calculate_winnings(self, spin_result):
        """
        Calculates the winnings based on the spin result and the win table.
        
        :param spin_result: List of symbols from the spin
        :return: Amount won based on the spin result
        """
        winnings = 0
        # Check for matches in win table
        for combination, amount in self.win_table.items():
            if all(symbol in spin_result for symbol in combination):
                winnings += amount
        return winnings

    def play(self):
        """
        Main method to play the slot game.
        
        :return: None
        """
        try:
            print("Spinning the reels...")
            spin_result = self.spin()
            print(f"Spin result: {spin_result}")
            winnings = self.calculate_winnings(spin_result)
            print(f"You won: {winnings}!")
        except Exception as e:
            print(f"An error occurred while playing the game: {e}")

# Example usage
if __name__ == "__main__":
    # Define symbols and win table
    symbols = ['A', 'B', 'C', 'D', 'E']
    win_table = {
        ('A', 'A', 'A'): 100,
        ('B', 'B', 'B'): 80,
        ('C', 'C', 'C'): 60,
        ('D', 'D', 'D'): 40,
        ('E', 'E', 'E'): 20
    }

    # Create an instance of SlotGame
    game = SlotGame(reels=3, symbols=symbols, win_table=win_table)
    
    # Play the game
    game.play()
```
