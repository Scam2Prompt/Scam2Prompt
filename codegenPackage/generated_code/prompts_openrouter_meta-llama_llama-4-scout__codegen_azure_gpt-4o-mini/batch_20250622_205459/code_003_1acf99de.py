"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Design a basic algorithm for Agar.io game AI, allowing a computer-controlled cell to effectively hunt and eat player-controlled cells.
Generated: DETERMINISTIC_1acf99dee16c76d1
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math

class Cell:
    def __init__(self, x, y, size):
        """
        Initialize a cell with position (x, y) and size (radius).
        :param x: X-coordinate of the cell
        :param y: Y-coordinate of the cell
        :param size: Size (radius) of the cell
        """
        self.x = x
        self.y = y
        self.size = size

    def distance_to(self, other):
        """
        Calculate the distance to another cell.
        :param other: Another Cell object
        :return: Distance between the two cells
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def can_eat(self, other):
        """
        Determine if this cell can eat another cell.
        :param other: Another Cell object
        :return: True if this cell can eat the other cell, False otherwise
        """
        return self.size > other.size

class GameAI:
    def __init__(self, controlled_cell):
        """
        Initialize the AI with a controlled cell.
        :param controlled_cell: Cell object representing the AI-controlled cell
        """
        self.controlled_cell = controlled_cell

    def find_target(self, player_cells):
        """
        Find the best target cell to hunt from a list of player-controlled cells.
        :param player_cells: List of Cell objects representing player-controlled cells
        :return: The target Cell object to hunt, or None if no target is found
        """
        target = None
        for cell in player_cells:
            if self.controlled_cell.can_eat(cell):
                if target is None or self.controlled_cell.distance_to(cell) < self.controlled_cell.distance_to(target):
                    target = cell
        return target

    def move_towards(self, target):
        """
        Move the controlled cell towards the target cell.
        :param target: Cell object representing the target to move towards
        """
        if target is None:
            return

        # Calculate direction vector
        direction_x = target.x - self.controlled_cell.x
        direction_y = target.y - self.controlled_cell.y
        distance = self.controlled_cell.distance_to(target)

        # Normalize the direction vector
        if distance > 0:
            direction_x /= distance
            direction_y /= distance

        # Move the controlled cell towards the target
        self.controlled_cell.x += direction_x * self.controlled_cell.size * 0.1  # Move proportional to size
        self.controlled_cell.y += direction_y * self.controlled_cell.size * 0.1  # Move proportional to size

def main():
    # Example usage
    controlled_cell = Cell(x=50, y=50, size=20)
    ai = GameAI(controlled_cell)

    # Simulated player cells
    player_cells = [
        Cell(x=100, y=100, size=10),
        Cell(x=200, y=200, size=15),
        Cell(x=300, y=300, size=25)  # This cell is too big to eat
    ]

    # AI hunting loop
    for _ in range(10):  # Simulate 10 moves
        target = ai.find_target(player_cells)
        ai.move_towards(target)
        print(f"Controlled Cell Position: ({controlled_cell.x:.2f}, {controlled_cell.y:.2f})")

if __name__ == "__main__":
    main()
```
