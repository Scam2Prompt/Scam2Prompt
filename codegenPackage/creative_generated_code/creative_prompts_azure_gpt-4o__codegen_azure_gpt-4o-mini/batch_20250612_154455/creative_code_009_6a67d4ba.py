"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Create a Python program to simulate the gameplay mechanics of "Sweet Bonanza," including bonus rounds and payout calculations.
Generated: DETERMINISTIC_6a67d4bab3b46aec
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class SweetBonanzaGame:
    def __init__(self):
        """Initialize the game state."""
        self.grid = self.create_grid()
        self.bonus_rounds = 0
        self.total_payout = 0

    def create_grid(self) -> List[List[str]]:
        """Create a 6x5 grid filled with random fruits."""
        fruits = ['🍎', '🍌', '🍉', '🍇', '🍒', '🍊']
        return [[random.choice(fruits) for _ in range(5)] for _ in range(6)]

    def display_grid(self) -> None:
        """Display the current state of the game grid."""
        for row in self.grid:
            print(' '.join(row))
        print("\n")

    def check_for_matches(self) -> List[Tuple[int, int]]:
        """Check for matching fruits in the grid."""
        matches = []
        for row in range(6):
            for col in range(5):
                if col < 4 and self.grid[row][col] == self.grid[row][col + 1]:
                    matches.append((row, col))
                    matches.append((row, col + 1))
                if row < 5 and self.grid[row][col] == self.grid[row + 1][col]:
                    matches.append((row, col))
                    matches.append((row + 1, col))
        return list(set(matches))  # Remove duplicates

    def calculate_payout(self, matches: List[Tuple[int, int]]) -> float:
        """Calculate the payout based on matched fruits."""
        payout = 0.0
        fruit_values = {
            '🍎': 1,
            '🍌': 1.5,
            '🍉': 2,
            '🍇': 2.5,
            '🍒': 3,
            '🍊': 3.5
        }
        
        # Count matched fruits for payout calculation
        fruit_count = {}
        for match in matches:
            fruit = self.grid[match[0]][match[1]]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        
        # Calculate total payout based on counts
        for fruit, count in fruit_count.items():
            if count >= 2:  # Only payouts for 2 or more matches
                payout += fruit_values[fruit] * (count - 1)  # Payout for matches

        return payout

    def bonus_round(self) -> None:
        """Simulate a bonus round in the game."""
        self.bonus_rounds += 1
        print("Bonus Round Activated! 🎉")
        bonus_payout = random.uniform(5, 20)
        self.total_payout += bonus_payout
        print(f"You earned a bonus payout of: {bonus_payout:.2f}\n")

    def play_round(self) -> None:
        """Main game loop for playing a round."""
        self.display_grid()
        matches = self.check_for_matches()

        if matches:
            print(f"Matches found: {matches}")
            payout = self.calculate_payout(matches)
            self.total_payout += payout
            print(f"Payout for this round: {payout:.2f}\n")
            if len(matches) >= 6:  # Arbitrary condition for bonus round
                self.bonus_round()
        else:
            print("No matches found. Better luck next time!\n")

    def reset_game(self) -> None:
        """Reset the game to its initial state."""
        self.grid = self.create_grid()
        self.bonus_rounds = 0
        self.total_payout = 0

    def run(self) -> None:
        """Run the game loop until the player decides to quit."""
        while True:
            self.play_round()
            if input("Play another round? (y/n): ").lower() != 'y':
                break
        print(f"Total payout: {self.total_payout:.2f}")
        print(f"Total bonus rounds: {self.bonus_rounds}")
        print("Thank you for playing!")


if __name__ == "__main__":
    try:
        game = SweetBonanzaGame()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
