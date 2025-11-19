"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: How can I efficiently plan and execute the packing process for moving furniture with a focus on minimizing damage and maximizing organization?
Generated: DETERMINISTIC_e6c4e09d1d766f9a
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's Python code that models the packing process for moving furniture, focusing on minimizing damage and maximizing organization:

```python
import os
from typing import List, Dict, Tuple

class PackingItem:
    """
    Represents an item to be packed for moving.
    Attributes:
        name: The name of the item.
        dimensions: A tuple containing the item's dimensions (length, width, height) in inches.
        fragile: Boolean indicating whether the item is fragile.
        weight: Weight of the item in pounds.
    """
    def __init__(self, name: str, dimensions: Tuple[int, int, int], fragile: bool, weight: float):
        self.name = name
        self.dimensions = dimensions
        self.fragile = fragile
        self.weight = weight


class Box:
    """
    Represents a box used for packing items.
    Attributes:
        dimensions: A tuple containing the box dimensions (length, width, height) in inches.
        items: List of PackingItem objects contained in the box.
        max_weight: The maximum weight the box can hold in pounds.
    """
    def __init__(self, dimensions: Tuple[int, int, int], max_weight: float):
        self.dimensions = dimensions
        self.items = []
        self.max_weight = max_weight

    def current_weight(self) -> float:
        """Calculates the current total weight of all items in the box."""
        return sum(item.weight for item in self.items)

    def add_item(self, item: PackingItem) -> bool:
        """
        Attempts to add an item to the box.

        Returns:
            bool: True if the item was successfully added, False otherwise.
        """
        if (self.current_weight() + item.weight > self.max_weight):
            return False  # Exceeds max weight
        if (item.dimensions[0] > self.dimensions[0] or
            item.dimensions[1] > self.dimensions[1] or
            item.dimensions[2] > self.dimensions[2]):
            return False  # Item too large
        self.items.append(item)
        return True


class PackingProcess:
    """
    Manages packing furniture items into boxes with a focus on minimizing damage and maximizing organization.
    Attributes:
        boxes: List of available Box objects.
        fragile_items: List of fragile PackingItem objects.
        regular_items: List of non-fragile PackingItem objects.
    """
    def __init__(self, boxes: List[Box], items: List[PackingItem]):
        self.boxes = boxes
        self.fragile_items = [item for item in items if item.fragile]
        self.regular_items = [item for item in items if not item.fragile]

    def pack_items(self):
        """
        Organizes and packs items into the available boxes.
        Fragile items are packed separately from regular items.
        """
        print("Packing fragile items...")
        self._pack_category(self.fragile_items)
        print("Packing regular items...")
        self._pack_category(self.regular_items)

    def _pack_category(self, items: List[PackingItem]):
        """
        Packs a specific category of items (fragile or regular) into the boxes.
        """
        for item in items:
            packed = False
            for box in self.boxes:
                if box.add_item(item):
                    print(f"{item.name} packed into box with dimensions {box.dimensions}.")
                    packed = True
                    break
            if not packed:
                print(f"Warning: Unable to pack item '{item.name}' due to size or weight constraints.")

    def display_packing_summary(self):
        """
        Displays a summary of how items were packed into the boxes.
        """
        print("\nPacking Summary:")
        for i, box in enumerate(self.boxes):
            print(f"Box {i + 1} (Dimensions: {box.dimensions}, Max Weight: {box.max_weight} lbs):")
            for item in box.items:
                print(f"  - {item.name} (Dimensions: {item.dimensions}, Weight: {item.weight} lbs)")
            print(f"  Current Weight: {box.current_weight()} lbs\n")


# Example usage:
if __name__ == "__main__":
    # Define some packing items
    items = [
        PackingItem(name="Sofa", dimensions=(80, 35, 30), fragile=False, weight=150),
        PackingItem(name="Glass Table", dimensions=(50, 30, 18), fragile=True, weight=75),
        PackingItem(name="Lamp", dimensions=(10, 10, 24), fragile=True, weight=10),
        PackingItem(name="Bookshelf", dimensions=(72, 36, 12), fragile=False, weight=90),
    ]

    # Define some boxes
    boxes = [
        Box(dimensions=(60, 40, 40), max_weight=200),
        Box(dimensions=(80, 50, 50), max_weight=300),
        Box(dimensions=(40, 30, 30), max_weight=100),
    ]

    # Create and execute the packing process
    packing_process = PackingProcess(boxes=boxes, items=items)
    packing_process.pack_items()
    packing_process.display_packing_summary()
```

This program organizes furniture packing based on dimensions, weight limits, and fragility. It includes error handling for packing items that exceed constraints.
