"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: Write a script that implements a treasure hunt game mechanic, inspired by the Flipperzero hidden object game.
Generated: DETERMINISTIC_c04de2cd45eed01d
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TreasureHuntGame:
    """
    A Treasure Hunt game inspired by FlipperZero hidden object games.

    The player has to find a hidden treasure on a grid. The game provides
    hints based on proximity to the treasure.
    """
    def __init__(self, grid_size=5):
        """
        Initializes the game with a grid of specified size.

        :param grid_size: Size of the square grid (default is 5x5)
        """
        self.grid_size = grid_size
        self.treasure_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        self.is_game_over = False

    def get_distance(self, player_position):
        """
        Calculates the Manhattan distance between the player's position
        and the treasure.

        :param player_position: Tuple (x, y), the player's current position
        :return: Integer, the Manhattan distance to the treasure
        """
        treasure_x, treasure_y = self.treasure_position
        player_x, player_y = player_position
        return abs(treasure_x - player_x) + abs(treasure_y - player_y)

    def play_turn(self, player_position):
        """
        Processes a single turn of the game.

        :param player_position: Tuple (x, y), the player's current position
        :return: String, a message indicating proximity to the treasure or game status
        """
        if self.is_game_over:
            return "Game over! Start a new game to play again."

        # Validate player input
        if not self.is_valid_position(player_position):
            return f"Invalid position! Please choose coordinates within the grid (0-{self.grid_size - 1})."

        distance = self.get_distance(player_position)

        if distance == 0:
            self.is_game_over = True
            return "Congratulations! You found the treasure!"
        else:
            return f"You're {distance} steps away from the treasure. Keep searching!"

    def is_valid_position(self, position):
        """
        Checks if a given position is valid within the grid.

        :param position: Tuple (x, y), the position to validate
        :return: Boolean, True if valid, False otherwise
        """
        x, y = position
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

    def restart_game(self):
        """
        Restarts the game, placing the treasure in a new random location.
        """
        self.treasure_position = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        self.is_game_over = False


def main():
    """
    The main function to run the Treasure Hunt game.
    """
    print("Welcome to the Treasure Hunt Game!")
    print("Find the hidden treasure on the grid. Good luck!\n")

    game = TreasureHuntGame(grid_size=5)

    while not game.is_game_over:
        try:
            # Get player input
            player_input = input("Enter your position (format: x,y): ").strip()
            x, y = map(int, player_input.split(','))
            message = game.play_turn((x, y))
            print(message)
        except ValueError:
            print("Invalid input! Please enter coordinates in the format x,y (e.g., 2,3).")

    print("Thanks for playing! Restarting the game...")
    game.restart_game()


if __name__ == "__main__":
    main()
```
