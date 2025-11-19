"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: How can I design a feature that allows users to double their energy in a coin collection game, similar to the one described on minerswiss.com?
Generated: DETERMINISTIC_3acc85f7615ab34f
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CoinCollectionGame:
    """
    CoinCollectionGame simulates a coin collection game where users can double their energy.
    """
    def __init__(self, initial_energy=100):
        """
        Initialize the game with a given initial energy.
        :param initial_energy: Starting energy for the player (default: 100)
        """
        self.energy = initial_energy

    def double_energy(self):
        """
        Allows the user to attempt doubling their energy.
        Successful doubling is determined via a random chance (e.g., 50% success rate).
        """
        try:
            success_chance = random.random()  # Generate a random float between 0.0 and 1.0
            if success_chance <= 0.5:  # 50% chance to succeed
                self.energy *= 2
                print(f"Success! Your energy has been doubled to {self.energy}.")
            else:
                print("Failed to double energy. Better luck next time!")
        except Exception as e:
            print(f"An error occurred while attempting to double energy: {e}")

    def display_energy(self):
        """
        Displays the current energy level of the user.
        """
        print(f"Current energy: {self.energy}")

def main():
    """
    Main function to run the CoinCollectionGame.
    """
    print("Welcome to the Coin Collection Game!")
    game = CoinCollectionGame()

    while True:
        game.display_energy()
        user_input = input("Type 'double' to double your energy or 'quit' to exit: ").strip().lower()

        if user_input == 'double':
            game.double_energy()
        elif user_input == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'double' or 'quit'.")

if __name__ == "__main__":
    main()
```
