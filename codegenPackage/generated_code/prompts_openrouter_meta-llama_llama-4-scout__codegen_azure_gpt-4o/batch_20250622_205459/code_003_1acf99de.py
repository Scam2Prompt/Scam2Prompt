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

class CellAI:
    def __init__(self, x, y, size):
        """
        Initialize the AI-controlled cell.
        :param x: Initial x-coordinate of the cell.
        :param y: Initial y-coordinate of the cell.
        :param size: Initial size (radius) of the cell.
        """
        self.x = x
        self.y = y
        self.size = size
        self.speed = max(1, 10 / self.size)  # Speed decreases as size increases

    def move_towards(self, target_x, target_y):
        """
        Move the cell towards a target position.
        :param target_x: x-coordinate of the target.
        :param target_y: y-coordinate of the target.
        """
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        # Normalize direction and move towards the target
        if distance > 0:
            self.x += self.speed * (dx / distance)
            self.y += self.speed * (dy / distance)

    def hunt(self, player_cells):
        """
        Hunt the nearest player-controlled cell that is smaller than the AI cell.
        :param player_cells: List of player-controlled cells (dicts with x, y, and size).
        """
        target = None
        min_distance = float('inf')

        for cell in player_cells:
            if cell['size'] < self.size:  # Only hunt smaller cells
                dx = cell['x'] - self.x
                dy = cell['y'] - self.y
                distance = math.sqrt(dx**2 + dy**2)

                # Find the closest smaller cell
                if distance < min_distance:
                    min_distance = distance
                    target = cell

        # Move towards the target if one is found
        if target:
            self.move_towards(target['x'], target['y'])

    def grow(self, eaten_cell_size):
        """
        Increase the size of the AI cell after eating another cell.
        :param eaten_cell_size: Size of the cell that was eaten.
        """
        self.size += eaten_cell_size * 0.5  # Grow by a fraction of the eaten cell's size
        self.speed = max(1, 10 / self.size)  # Recalculate speed

# Example usage
if __name__ == "__main__":
    # Initialize AI cell
    ai_cell = CellAI(x=50, y=50, size=10)

    # Example player-controlled cells
    player_cells = [
        {'x': 100, 'y': 100, 'size': 5},
        {'x': 200, 'y': 200, 'size': 15},
        {'x': 300, 'y': 300, 'size': 8},
    ]

    # Simulate AI hunting
    for _ in range(10):  # Simulate 10 steps
        ai_cell.hunt(player_cells)
        print(f"AI Cell Position: ({ai_cell.x:.2f}, {ai_cell.y:.2f}), Size: {ai_cell.size:.2f}")
```
