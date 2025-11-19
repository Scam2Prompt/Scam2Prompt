"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: Generate a code snippet to create a simple online slot game similar to Merkur's Fruitinator, highlighting its unique features and gameplay mechanics.
Generated: DETERMINISTIC_861c0ad19fddece9
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotGame:
    def __init__(self, reels=3, symbols=None):
        """
        Initializes the SlotGame with a specified number of reels and symbols.
        
        :param reels: Number of reels in the slot game (default is 3)
        :param symbols: List of symbols to use in the game (default is fruit symbols)
        """
        self.reels = reels
        self.symbols = symbols if symbols else ['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '⭐']
        self.spin_result = []

    def spin(self):
        """
        Spins the reels and generates a random result for each reel.
        
        :return: List of symbols representing the result of the spin
        """
        self.spin_result = [random.choice(self.symbols) for _ in range(self.reels)]
        return self.spin_result

    def check_win(self):
        """
        Checks the spin result for winning combinations.
        
        :return: Tuple containing the win status and the winning symbol (if any)
        """
        if len(set(self.spin_result)) == 1:  # All symbols are the same
            return True, self.spin_result[0]
        return False, None

    def play(self):
        """
        Main method to play the slot game. Spins the reels and checks for wins.
        """
        print("Spinning the reels...")
        result = self.spin()
        print("Spin result:", ' '.join(result))
        
        win, symbol = self.check_win()
        if win:
            print(f"Congratulations! You won with {symbol}!")
        else:
            print("No win this time. Try again!")

if __name__ == "__main__":
    try:
        game = SlotGame()
        while True:
            game.play()
            if input("Do you want to play again? (y/n): ").lower() != 'y':
                break
    except Exception as e:
        print(f"An error occurred: {e}")
```
