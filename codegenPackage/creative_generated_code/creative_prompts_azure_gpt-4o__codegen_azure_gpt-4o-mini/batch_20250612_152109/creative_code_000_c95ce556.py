"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Write Python code to calculate the optimal layout for a retail store using UDIZINE's Vertik system, ensuring maximum wall space utilization for shelving and hanging displays.
Generated: DETERMINISTIC_c95ce556df46650e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from typing import List, Tuple

class RetailStoreLayout:
    def __init__(self, store_width: float, store_length: float):
        """
        Initializes the RetailStoreLayout with dimensions of the store.

        :param store_width: Width of the store in meters.
        :param store_length: Length of the store in meters.
        """
        self.store_width = store_width
        self.store_length = store_length
        self.wall_space = self.calculate_wall_space()

    def calculate_wall_space(self) -> float:
        """
        Calculates the total wall space available for shelving and hanging displays.

        :return: Total wall space in square meters.
        """
        # The store has 2 lengths and 2 widths contributing to the wall space
        return 2 * (self.store_width + self.store_length)

    def optimal_layout(self, shelf_width: float, shelf_height: float, num_shelves: int) -> List[Tuple[float, float]]:
        """
        Calculates the optimal layout for shelving based on wall space utilization.

        :param shelf_width: Width of each shelf in meters.
        :param shelf_height: Height of each shelf in meters.
        :param num_shelves: Number of shelves to be placed.
        :return: List of tuples representing the positions of each shelf.
        :raises ValueError: If the number of shelves exceeds the available wall space.
        """
        total_shelf_space = num_shelves * shelf_width
        if total_shelf_space > self.wall_space:
            raise ValueError("Not enough wall space for the specified number of shelves.")
        
        # Calculate positions for each shelf
        shelf_positions = []
        current_position = 0.0

        while num_shelves > 0:
            shelf_positions.append((current_position, shelf_height))
            current_position += shelf_width
            num_shelves -= 1

        return shelf_positions

# Example usage
if __name__ == "__main__":
    try:
        store = RetailStoreLayout(store_width=10.0, store_length=15.0)
        # Assuming each shelf is 0.5 meters wide and 2 meters tall, and we want to install 10 shelves
        layout = store.optimal_layout(shelf_width=0.5, shelf_height=2.0, num_shelves=10)
        print("Optimal Shelf Positions:", layout)
    except ValueError as e:
        print("Error:", e)
```
