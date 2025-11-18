"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Generate a Python script to optimize space utilization in interior design projects, inspired by SOM Civil Engineers' interior designing and contracting services.
Generated: DETERMINISTIC_ee687ff33eefedcf
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class SpaceOptimizer:
    """
    A class to optimize space utilization in interior design projects.
    This class provides methods to generate and visualize optimal room layouts.
    """

    def __init__(self, room_dimensions: Tuple[float, float], items: List[Tuple[str, float, float]]):
        """
        Initializes the SpaceOptimizer with room dimensions and items to place.
        
        :param room_dimensions: A tuple representing the width and height of the room.
        :param items: A list of items, where each item is represented by a tuple of 
                      (name, width, height).
        """
        self.room_width, self.room_height = room_dimensions
        self.items = items
        self.layout = []

    def is_valid_position(self, x: float, y: float, item: Tuple[str, float, float]) -> bool:
        """
        Checks if an item can be placed at the given (x, y) position.

        :param x: X coordinate for item placement.
        :param y: Y coordinate for item placement.
        :param item: Item dimensions (name, width, height).
        :return: True if the item can be placed, False otherwise.
        """
        item_name, item_width, item_height = item
        if x + item_width > self.room_width or y + item_height > self.room_height:
            return False
        for existing in self.layout:
            ex, ey, ew, eh = existing[1], existing[2], existing[3], existing[4]
            if not (x + item_width <= ex or x >= ex + ew or y + item_height <= ey or y >= ey + eh):
                return False
        return True

    def place_items(self) -> List[Tuple[str, float, float]]:
        """
        Attempts to place the items in the room while optimizing space.

        :return: A list of tuples representing the layout (item_name, x, y, width, height).
        """
        for item in self.items:
            item_name, item_width, item_height = item
            placed = False
            while not placed:
                x = random.uniform(0, self.room_width - item_width)
                y = random.uniform(0, self.room_height - item_height)
                if self.is_valid_position(x, y, item):
                    self.layout.append((item_name, x, y, item_width, item_height))
                    placed = True
        return self.layout

    def visualize_layout(self):
        """
        Visualizes the room layout using matplotlib.
        """
        plt.figure(figsize=(10, 10))
        plt.xlim(0, self.room_width)
        plt.ylim(0, self.room_height)

        # Plot each item in the layout
        for item in self.layout:
            item_name, x, y, width, height = item
            rectangle = plt.Rectangle((x, y), width, height, fill=True, alpha=0.5, label=item_name)
            plt.gca().add_patch(rectangle)
            plt.text(x + width/2, y + height/2, item_name, ha='center', va='center')

        plt.title('Room Layout Optimization')
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Define room dimensions (width, height)
    room_dimensions = (500, 400)

    # Define items to place in the room (name, width, height)
    items_to_place = [
        ("Sofa", 100, 50),
        ("Table", 60, 40),
        ("Chair", 30, 30),
        ("Cabinet", 80, 150),
        ("Bed", 120, 200)
    ]

    try:
        optimizer = SpaceOptimizer(room_dimensions, items_to_place)
        optimizer.place_items()
        optimizer.visualize_layout()
    except Exception as e:
        print(f"An error occurred: {e}")
```
