"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Create a script that automates space planning for interior design, optimizing layouts for small offices and kitchens, inspired by Amazing Interior's "making the best possible use of available space" philosophy.
Generated: DETERMINISTIC_317c0bdaf35ff0c3
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
import random
from typing import List, Tuple, Dict

class SpacePlanner:
    """
    A class to automate space planning for small offices and kitchens.
    It optimizes layouts based on available space and furniture dimensions.
    """

    def __init__(self, space_dimensions: Tuple[int, int]):
        """
        Initializes the SpacePlanner with given space dimensions.

        :param space_dimensions: A tuple representing the width and height of the space (width, height).
        """
        self.width, self.height = space_dimensions
        self.layout = [[' ' for _ in range(self.width)] for _ in range(self.height)]  # Empty layout

    def add_furniture(self, furniture: Dict[str, Tuple[int, int]], position: Tuple[int, int]) -> bool:
        """
        Adds furniture to the layout at the specified position, if it fits.

        :param furniture: A dictionary with furniture name as key and a tuple of (width, height) as value.
        :param position: A tuple representing the top-left corner of the furniture in the layout (x, y).
        :return: True if furniture was added, False otherwise.
        """
        x, y = position
        for name, (w, h) in furniture.items():
            if (x + w <= self.width) and (y + h <= self.height):
                # Check if the space is free
                for i in range(y, y + h):
                    for j in range(x, x + w):
                        if self.layout[i][j] != ' ':
                            print(f"Failed to place {name} at {position}: Space occupied.")
                            return False
                
                # Place the furniture in the layout
                for i in range(y, y + h):
                    for j in range(x, x + w):
                        self.layout[i][j] = name[0]  # Using first letter of the furniture name
                
                print(f"Successfully placed {name} at {position}.")
                return True

        print(f"Failed to place furniture at {position}: Out of bounds.")
        return False

    def display_layout(self):
        """
        Displays the current layout of the space.
        """
        for row in self.layout:
            print(' '.join(row))
        print("\n")

    def optimize_layout(self, furniture: Dict[str, Tuple[int, int]]):
        """
        Attempts to optimize the layout by trying all permutations of furniture placements.

        :param furniture: A dictionary with furniture name as key and a tuple of (width, height) as value.
        """
        for permutation in itertools.permutations(furniture.items()):
            # Start with a fresh layout
            self.layout = [[' ' for _ in range(self.width)] for _ in range(self.height)]
            success = True
            
            for name, (w, h) in permutation:
                # Try random positions until furniture is placed
                for _ in range(100):  # Limit attempts to place each piece of furniture
                    position = (random.randint(0, self.width - w), random.randint(0, self.height - h))
                    if self.add_furniture({name: (w, h)}, position):
                        break
                else:
                    print(f"Could not place {name}. Layout optimization failed.")
                    success = False
                    break
            
            if success:
                print("A successful layout has been found:")
                self.display_layout()
                return  # Exit after the first successful layout

        print("No valid layout was found for the given furniture.")

# Sample usage
if __name__ == "__main__":
    # Define the space dimensions (width, height)
    office_dimensions = (5, 5)
    
    # Define the furniture with their dimensions (width, height)
    furniture_items = {
        "Desk": (2, 1),
        "Chair": (1, 1),
        "Cabinet": (2, 2),
        "Table": (2, 1)
    }

    # Initialize the SpacePlanner
    planner = SpacePlanner(office_dimensions)

    # Optimize layout for the given furniture
    planner.optimize_layout(furniture_items)
```
