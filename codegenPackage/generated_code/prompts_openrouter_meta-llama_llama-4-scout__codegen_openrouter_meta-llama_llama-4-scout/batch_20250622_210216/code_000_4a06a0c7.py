"""
Generated Code Metadata:
========================
Original URL: https://nimnetwork.pages.dev
Prompt: What is Nim Rolldrop and how does it relate to AI gaming?
Generated: DETERMINISTIC_4a06a0c7eee90ce4
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nim_rolldrop.py

"""
Nim Rolldrop Game in Python
==========================

This script simulates the Nim Rolldrop game and explores its relation to AI gaming.

### Game Rules:

* The game starts with a set of piles, each containing a certain number of stones.
* Players take turns removing stones from the piles.
* A player can only remove stones from one pile per turn.
* The game ends when all piles are empty. The player who made the last move loses.

### AI Strategy:

* The AI uses the Nim-sum strategy to play the game.
* The Nim-sum is calculated by performing a bitwise XOR operation on the number of stones in each pile.
* If the Nim-sum is zero, the current player loses. Otherwise, they can make a move to make the Nim-sum zero.

"""

import random

class NimRolldrop:
    def __init__(self, piles):
        """
        Initialize the game with a set of piles.

        Args:
            piles (list): A list of integers representing the number of stones in each pile.

        Raises:
            ValueError: If the input list is empty or contains non-positive integers.
        """
        if not piles or any(pile <= 0 for pile in piles):
            raise ValueError("Invalid pile configuration")
        self.piles = piles

    def calculate_nim_sum(self):
        """
        Calculate the Nim-sum of the current game state.

        Returns:
            int: The Nim-sum of the game state.
        """
        nim_sum = 0
        for pile in self.piles:
            nim_sum ^= pile
        return nim_sum

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return all(pile == 0 for pile in self.piles)

    def make_move(self, pile_index, stones_to_remove):
        """
        Make a move by removing stones from a pile.

        Args:
            pile_index (int): The index of the pile to remove stones from.
            stones_to_remove (int): The number of stones to remove.

        Raises:
            ValueError: If the pile index is out of range or the number of stones to remove is invalid.
        """
        if pile_index < 0 or pile_index >= len(self.piles):
            raise ValueError("Invalid pile index")
        if stones_to_remove <= 0 or stones_to_remove > self.piles[pile_index]:
            raise ValueError("Invalid number of stones to remove")
        self.piles[pile_index] -= stones_to_remove

    def ai_move(self):
        """
        Make a move using the Nim-sum strategy.

        Returns:
            tuple: The index of the pile to remove stones from and the number of stones to remove.
        """
        nim_sum = self.calculate_nim_sum()
        if nim_sum == 0:
            raise ValueError("AI has no valid move")
        for i, pile in enumerate(self.piles):
            if pile > 0:
                stones_to_remove = pile - (nim_sum ^ pile)
                if stones_to_remove > 0:
                    return i, stones_to_remove
        raise ValueError("AI has no valid move")

def main():
    # Example usage
    game = NimRolldrop([3, 4, 5])
    while not game.is_game_over():
        # Human move
        pile_index = int(input("Enter the pile index: "))
        stones_to_remove = int(input("Enter the number of stones to remove: "))
        game.make_move(pile_index, stones_to_remove)
        print(f"Piles: {game.piles}")

        # AI move
        if not game.is_game_over():
            pile_index, stones_to_remove = game.ai_move()
            game.make_move(pile_index, stones_to_remove)
            print(f"AI move: pile {pile_index}, remove {stones_to_remove} stones")
            print(f"Piles: {game.piles}")

if __name__ == "__main__":
    main()
```
