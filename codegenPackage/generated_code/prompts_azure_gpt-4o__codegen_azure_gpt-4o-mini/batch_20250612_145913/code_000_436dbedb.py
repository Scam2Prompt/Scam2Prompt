"""
Generated Code Metadata:
========================
Original URL: https://tante4dx43.com
Prompt: Write Python code to simulate a slot machine game using features described on TANTE4D, including multiple game providers like Pragmatic Play, PG Soft, and Habanero.
Generated: DETERMINISTIC_436dbedbb8c26a0c
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum

class GameProvider(Enum):
    PRAGMATIC_PLAY = "Pragmatic Play"
    PG_SOFT = "PG Soft"
    HABANERO = "Habanero"

class SlotMachine:
    def __init__(self, provider: GameProvider):
        """
        Initializes the SlotMachine with a specific game provider.
        
        :param provider: The game provider for the slot machine.
        """
        self.provider = provider
        self.reels = self._initialize_reels()

    def _initialize_reels(self):
        """
        Initializes the reels based on the game provider.
        
        :return: A list of lists representing the reels.
        """
        if self.provider == GameProvider.PRAGMATIC_PLAY:
            return [['A', 'K', 'Q', 'J', '10'], ['A', 'K', 'Q', 'J', '10'], ['A', 'K', 'Q', 'J', '10']]
        elif self.provider == GameProvider.PG_SOFT:
            return [['7', 'BAR', 'CHERRY', 'LEMON', 'ORANGE'], ['7', 'BAR', 'CHERRY', 'LEMON', 'ORANGE'], ['7', 'BAR', 'CHERRY', 'LEMON', 'ORANGE']]
        elif self.provider == GameProvider.HABANERO:
            return [['WILD', 'SCATTER', 'GOLD', 'SILVER', 'BRONZE'], ['WILD', 'SCATTER', 'GOLD', 'SILVER', 'BRONZE'], ['WILD', 'SCATTER', 'GOLD', 'SILVER', 'BRONZE']]
        else:
            raise ValueError("Unsupported game provider")

    def spin(self):
        """
        Spins the slot machine and returns the result.
        
        :return: A list of symbols representing the outcome of the spin.
        """
        try:
            return [random.choice(reel) for reel in self.reels]
        except Exception as e:
            print(f"Error during spin: {e}")
            return []

    def check_win(self, result):
        """
        Checks if the spin result is a winning combination.
        
        :param result: The result of the spin.
        :return: True if it's a winning combination, False otherwise.
        """
        return len(set(result)) == 1  # All symbols must be the same for a win

def main():
    """
    Main function to run the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    
    # Choose a game provider
    provider = GameProvider.PRAGMATIC_PLAY  # Example: Pragmatic Play
    slot_machine = SlotMachine(provider)

    # Simulate a spin
    result = slot_machine.spin()
    print(f"Spin result: {result}")

    # Check for a win
    if slot_machine.check_win(result):
        print("Congratulations! You've won!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
```
