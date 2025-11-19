"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Develop a Python script to simulate a creative puzzle where the solution requires unconventional thinking, as highlighted in Braindom's gameplay.
Generated: DETERMINISTIC_13df155149ebccc5
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Braindom Puzzle Simulator
==========================

This script simulates a creative puzzle similar to Braindom's gameplay.
The puzzle requires unconventional thinking to solve.

Puzzle Description:
--------------------

You are given a set of candles and a set of blocks with different heights.
The goal is to make all candles have the same height by placing blocks
underneath them.

Gameplay:
---------

1. The game starts with a set of candles and blocks.
2. The player can place blocks under candles to increase their height.
3. The game ends when all candles have the same height or when there
   are no more blocks available.

Code:
------
"""

import random

class Candle:
    """Represents a candle with a height."""
    def __init__(self, height):
        self.height = height

class Block:
    """Represents a block with a height."""
    def __init__(self, height):
        self.height = height

class Puzzle:
    """Simulates the Braindom puzzle."""
    def __init__(self, candles, blocks):
        self.candles = [Candle(height) for height in candles]
        self.blocks = [Block(height) for height in blocks]

    def display_status(self):
        """Displays the current status of the puzzle."""
        print("Candles:")
        for i, candle in enumerate(self.candles):
            print(f"Candle {i+1}: {candle.height} units")
        print(f"Blocks remaining: {len(self.blocks)}")

    def place_block(self, candle_index, block_index):
        """Places a block under a candle."""
        if candle_index < 0 or candle_index >= len(self.candles):
            raise ValueError("Invalid candle index")
        if block_index < 0 or block_index >= len(self.blocks):
            raise ValueError("Invalid block index")
        self.candles[candle_index].height += self.blocks[block_index].height
        del self.blocks[block_index]

    def check_win(self):
        """Checks if all candles have the same height."""
        return len(set(candle.height for candle in self.candles)) == 1

def main():
    # Initialize puzzle with random candle and block heights
    candles = [random.randint(1, 10) for _ in range(3)]
    blocks = [random.randint(1, 5) for _ in range(5)]
    puzzle = Puzzle(candles, blocks)

    while True:
        puzzle.display_status()
        if puzzle.check_win():
            print("Congratulations! All candles have the same height.")
            break
        if not puzzle.blocks:
            print("Game over! No more blocks available.")
            break

        # Get user input
        try:
            candle_index = int(input("Enter the candle number to place a block under: ")) - 1
            block_index = int(input("Enter the block number to place: ")) - 1
            puzzle.place_block(candle_index, block_index)
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
```
