"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydrop.web.app
Prompt: Write code for a "Jelly Flip" game or utility, referencing the interactive tools mentioned on the JellyDrop site.
Generated: DETERMINISTIC_a77a6483a00cb879
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

class JellyFlipGame:
    """
    A Jelly Flip game inspired by interactive tools on the JellyDrop site.
    Players aim to flip jelly-like tiles to match them all to the same color.
    """

    def __init__(self, grid_size=4):
        """
        Initialize the game with a square grid of jelly tiles.
        :param grid_size: Size of the grid (default is 4x4).
        """
        self.grid_size = grid_size
        self.colors = ['red', 'blue']  # Available colors for the game
        self.grid = self._generate_grid()

    def _generate_grid(self):
        """
        Generates a random grid of jelly tiles.
        :return: A 2D list representing the grid.
        """
        return [[random.choice(self.colors) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def display_grid(self):
        """
        Displays the current state of the grid.
        """
        print("\nCurrent Grid:")
        for row in self.grid:
            print(" ".join(row))
        print()

    def flip_tile(self, row, col):
        """
        Flips the selected tile and its adjacent tiles.
        :param row: Row index of the tile to flip.
        :param col: Column index of the tile to flip.
        """
        if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
            print("Invalid position! Please try again.")
            return

        # Flip the selected tile
        self.grid[row][col] = self._flip_color(self.grid[row][col])

        # Flip the adjacent tiles
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dr, dc in directions:
            adj_row, adj_col = row + dr, col + dc
            if 0 <= adj_row < self.grid_size and 0 <= adj_col < self.grid_size:
                self.grid[adj_row][adj_col] = self._flip_color(self.grid[adj_row][adj_col])

    def _flip_color(self, color):
        """
        Flips a jelly tile's color to the other available color.
        :param color: Current color of the tile.
        :return: The flipped color.
        """
        return self.colors[1] if color == self.colors[0] else self.colors[0]

    def check_win(self):
        """
        Checks if all tiles in the grid are the same color.
        :return: True if all tiles are the same color, False otherwise.
        """
        first_color = self.grid[0][0]
        for row in self.grid:
            if any(tile != first_color for tile in row):
                return False
        return True

    def play(self):
        """
        Main function to run the game loop.
        """
        print("Welcome to Jelly Flip!")
        print("Match all tiles to the same color to win.\n")
        self.display_grid()

        while True:
            try:
                user_input = input("Enter the tile to flip (row,col) or 'quit' to exit: ").strip()
                if user_input.lower() == 'quit':
                    print("Thanks for playing!")
                    break

                row, col = map(int, user_input.split(','))
                self.flip_tile(row, col)
                self.display_grid()

                if self.check_win():
                    print("Congratulations! You've won the game!")
                    break

            except ValueError:
                print("Invalid input! Please enter the tile coordinates in the format 'row,col'.")

            except Exception as e:
                print(f"An error occurred: {e}")
                sys.exit(1)


if __name__ == "__main__":
    # Run the game
    game = JellyFlipGame(grid_size=4)
    game.play()
```
