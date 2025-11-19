"""
Generated Code Metadata:
========================
Original URL: https://csmoney.org
Prompt: Develop a sorting algorithm in Python to categorize CS:GO skins into "Weapons," "Rare Weapons," and "Miscellaneous," mimicking CS Money's inventory management system.
Generated: DETERMINISTIC_1001788f86f4935e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class CSGOItemType(Enum):
    """Enum for CS:GO item types."""
    WEAPON = 1
    RARE_WEAPON = 2
    MISCELLANEOUS = 3

class CSGOItem:
    """Class representing a CS:GO item."""
    def __init__(self, name: str, item_type: CSGOItemType):
        """
        Initialize a CS:GO item.

        Args:
        - name (str): The name of the item.
        - item_type (CSGOItemType): The type of the item.
        """
        self.name = name
        self.item_type = item_type

class CSGOInventory:
    """Class representing a CS:GO inventory."""
    def __init__(self):
        """Initialize an empty CS:GO inventory."""
        self.items: Dict[CSGOItemType, List[CSGOItem]] = {
            CSGOItemType.WEAPON: [],
            CSGOItemType.RARE_WEAPON: [],
            CSGOItemType.MISCELLANEOUS: []
        }

    def add_item(self, item: CSGOItem):
        """
        Add an item to the inventory.

        Args:
        - item (CSGOItem): The item to add.

        Raises:
        - TypeError: If the item is not of a valid type.
        """
        if item.item_type not in self.items:
            raise TypeError("Invalid item type")
        self.items[item.item_type].append(item)

    def sort_items(self):
        """Sort items in the inventory by name."""
        for item_type in self.items:
            self.items[item_type] = sorted(self.items[item_type], key=lambda item: item.name)

    def print_inventory(self):
        """Print the current state of the inventory."""
        for item_type in self.items:
            print(f"{item_type.name}:")
            for item in self.items[item_type]:
                print(f"- {item.name}")
            print()

def main():
    # Create an inventory
    inventory = CSGOInventory()

    # Create some items
    items = [
        CSGOItem("M9 Bayonet | Black Pearl", CSGOItemType.RARE_WEAPON),
        CSGOItem("AK-47 | Gold Plated", CSGOItemType.RARE_WEAPON),
        CSGOItem("Glock-18 | Whiteout", CSGOItemType.WEAPON),
        CSGOItem("Knife", CSGOItemType.MISCELLANEOUS),
        CSGOItem("M4A4 | Shutter", CSGOItemType.WEAPON),
        CSGOItem("P90 | Red Spectre", CSGOItemType.WEAPON),
    ]

    # Add items to the inventory
    for item in items:
        try:
            inventory.add_item(item)
        except TypeError as e:
            print(f"Error adding item: {e}")

    # Sort items
    inventory.sort_items()

    # Print the inventory
    inventory.print_inventory()

if __name__ == "__main__":
    main()
```
