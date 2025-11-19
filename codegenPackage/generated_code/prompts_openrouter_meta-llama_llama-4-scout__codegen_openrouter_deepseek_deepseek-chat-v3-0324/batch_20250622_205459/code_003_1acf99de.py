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
import math
import random
from typing import List, Tuple

class AgarAICell:
    def __init__(self, x: float, y: float, radius: float):
        """
        Initialize an AI-controlled cell with position and size.
        
        Args:
            x: Initial x-coordinate
            y: Initial y-coordinate
            radius: Initial radius of the cell
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.target = None
        self.speed = 0
        self.update_speed()
    
    def update_speed(self) -> None:
        """Update movement speed based on current radius (larger cells move slower)."""
        self.speed = max(1, 10 - math.log(self.radius) * 2)
    
    def find_closest_prey(self, player_cells: List['AgarAICell']) -> None:
        """
        Find the closest player cell that is smaller than this AI cell.
        
        Args:
            player_cells: List of player-controlled cells
        """
        min_distance = float('inf')
        self.target = None
        
        for cell in player_cells:
            if cell.radius >= self.radius * 0.9:  # Don't target cells that are nearly our size
                continue
                
            distance = math.sqrt((self.x - cell.x)**2 + (self.y - cell.y)**2)
            if distance < min_distance:
                min_distance = distance
                self.target = cell
    
    def move_towards_target(self) -> None:
        """Move the AI cell towards its current target."""
        if not self.target:
            # Random movement if no target
            self.x += random.uniform(-self.speed, self.speed)
            self.y += random.uniform(-self.speed, self.speed)
            return
            
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            dx /= distance
            dy /= distance
            
        self.x += dx * self.speed
        self.y += dy * self.speed
    
    def check_collision(self, other_cell: 'AgarAICell') -> bool:
        """
        Check if this cell can consume another cell.
        
        Args:
            other_cell: The cell to check collision with
            
        Returns:
            bool: True if this cell can consume the other cell
        """
        distance = math.sqrt((self.x - other_cell.x)**2 + (self.y - other_cell.y)**2)
        return distance < self.radius and self.radius > other_cell.radius * 1.1
    
    def grow(self, amount: float) -> None:
        """
        Increase the cell's size.
        
        Args:
            amount: The amount to increase the radius by
        """
        self.radius += amount
        self.update_speed()
    
    def update(self, player_cells: List['AgarAICell']) -> None:
        """
        Main update method called each game tick.
        
        Args:
            player_cells: List of player-controlled cells
        """
        self.find_closest_prey(player_cells)
        self.move_towards_target()
        
        # Check for collisions with all player cells
        for cell in player_cells[:]:  # Create a copy for safe iteration
            if self.check_collision(cell):
                self.grow(cell.radius * 0.2)  # Grow by a fraction of the consumed cell's size
                player_cells.remove(cell)  # Remove consumed cell


class AgarGame:
    def __init__(self):
        """Initialize the game with AI and player cells."""
        self.ai_cell = AgarAICell(100, 100, 20)
        self.player_cells = [
            AgarAICell(random.randint(0, 800), random.randint(0, 600), random.randint(5, 15))
            for _ in range(5)
        ]
    
    def update(self) -> None:
        """Update game state."""
        self.ai_cell.update(self.player_cells)
        
        # Add new player cells if too few remain
        if len(self.player_cells) < 3:
            self.player_cells.append(
                AgarAICell(random.randint(0, 800), random.randint(0, 600), random.randint(5, 15))
            )


# Example usage
if __name__ == "__main__":
    game = AgarGame()
    for _ in range(100):  # Simulate 100 game ticks
        game.update()
```
