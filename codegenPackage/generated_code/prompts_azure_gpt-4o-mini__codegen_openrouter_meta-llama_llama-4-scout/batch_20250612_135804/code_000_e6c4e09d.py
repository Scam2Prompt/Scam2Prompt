"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: How can I efficiently plan and execute the packing process for moving furniture with a focus on minimizing damage and maximizing organization?
Generated: DETERMINISTIC_e6c4e09d1d766f9a
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Furniture:
    """Represents a piece of furniture with its characteristics."""
    
    def __init__(self, name: str, width: int, height: int, depth: int, fragile: bool = False):
        """
        Initializes a Furniture object.

        Args:
        - name (str): The name of the furniture.
        - width (int): The width of the furniture.
        - height (int): The height of the furniture.
        - depth (int): The depth of the furniture.
        - fragile (bool): Whether the furniture is fragile. Defaults to False.
        """
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.fragile = fragile

class Box:
    """Represents a box with its characteristics."""
    
    def __init__(self, width: int, height: int, depth: int):
        """
        Initializes a Box object.

        Args:
        - width (int): The width of the box.
        - height (int): The height of the box.
        - depth (int): The depth of the box.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.furniture: List[Furniture] = []

    def add_furniture(self, furniture: Furniture):
        """
        Adds furniture to the box.

        Args:
        - furniture (Furniture): The furniture to add.
        """
        self.furniture.append(furniture)

class PackingPlan:
    """Represents a packing plan."""
    
    def __init__(self):
        self.boxes: List[Box] = []

    def add_box(self, box: Box):
        """
        Adds a box to the packing plan.

        Args:
        - box (Box): The box to add.
        """
        self.boxes.append(box)

    def pack_furniture(self, furniture_list: List[Furniture]):
        """
        Packs furniture into boxes efficiently.

        Args:
        - furniture_list (List[Furniture]): The list of furniture to pack.
        """
        # Sort furniture by volume in descending order
        furniture_list.sort(key=lambda f: f.width * f.height * f.depth, reverse=True)

        # Separate fragile and non-fragile furniture
        fragile_furniture = [f for f in furniture_list if f.fragile]
        non_fragile_furniture = [f for f in furniture_list if not f.fragile]

        # Pack fragile furniture first
        self._pack_furniture(fragile_furniture, True)

        # Pack non-fragile furniture
        self._pack_furniture(non_fragile_furniture, False)

    def _pack_furniture(self, furniture_list: List[Furniture], fragile: bool):
        """
        Packs furniture into boxes.

        Args:
        - furniture_list (List[Furniture]): The list of furniture to pack.
        - fragile (bool): Whether the furniture is fragile.
        """
        for furniture in furniture_list:
            # Find a suitable box
            box = self._find_suitable_box(furniture)
            if box:
                box.add_furniture(furniture)
            else:
                # Create a new box if no suitable box is found
                new_box = Box(furniture.width, furniture.height, furniture.depth)
                new_box.add_furniture(furniture)
                self.add_box(new_box)

    def _find_suitable_box(self, furniture: Furniture) -> Box:
        """
        Finds a suitable box for the furniture.

        Args:
        - furniture (Furniture): The furniture to find a box for.

        Returns:
        - Box: A suitable box, or None if no suitable box is found.
        """
        for box in self.boxes:
            if (box.width >= furniture.width and 
                box.height >= furniture.height and 
                box.depth >= furniture.depth):
                return box
        return None

    def print_packing_plan(self):
        """
        Prints the packing plan.
        """
        for i, box in enumerate(self.boxes):
            print(f"Box {i+1} ({box.width}x{box.height}x{box.depth}):")
            for furniture in box.furniture:
                print(f"- {furniture.name} ({furniture.width}x{furniture.height}x{furniture.depth}) - Fragile: {furniture.fragile}")
            print()

def main():
    # Create furniture
    furniture_list = [
        Furniture("Sofa", 200, 80, 60),
        Furniture("Chair", 50, 50, 50, fragile=True),
        Furniture("Table", 100, 70, 50),
        Furniture("Lamp", 30, 30, 30, fragile=True),
    ]

    # Create a packing plan
    packing_plan = PackingPlan()

    # Pack furniture
    packing_plan.pack_furniture(furniture_list)

    # Print packing plan
    packing_plan.print_packing_plan()

if __name__ == "__main__":
    main()
```
