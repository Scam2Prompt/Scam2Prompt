"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Develop a solution for tracking and organizing furniture during self-moving, using شركة آل البيت's strategies for planning and organization.
Generated: DETERMINISTIC_a091cd3f4defc431
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class FurnitureItem:
    """Class to represent a furniture item."""
    
    def __init__(self, name: str, dimensions: Dict[str, float], weight: float):
        """
        Initialize a furniture item.

        :param name: Name of the furniture item.
        :param dimensions: Dimensions of the item (length, width, height).
        :param weight: Weight of the item in kilograms.
        """
        self.name = name
        self.dimensions = dimensions  # Expected to be a dict with keys: 'length', 'width', 'height'
        self.weight = weight

    def __repr__(self):
        return f"FurnitureItem(name={self.name}, dimensions={self.dimensions}, weight={self.weight})"


class FurnitureTracker:
    """Class to track and organize furniture items during self-moving."""
    
    def __init__(self):
        """Initialize the furniture tracker with an empty list of items."""
        self.items: List[FurnitureItem] = []

    def add_item(self, item: FurnitureItem):
        """
        Add a furniture item to the tracker.

        :param item: FurnitureItem instance to be added.
        """
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item_name: str):
        """
        Remove a furniture item from the tracker by name.

        :param item_name: Name of the furniture item to be removed.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed item: {item}")
                return
        print(f"Item with name '{item_name}' not found.")

    def list_items(self) -> List[FurnitureItem]:
        """
        List all furniture items currently tracked.

        :return: List of FurnitureItem instances.
        """
        return self.items

    def save_to_file(self, filename: str):
        """
        Save the current list of furniture items to a JSON file.

        :param filename: Name of the file to save the items to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([item.__dict__ for item in self.items], file, indent=4)
            print(f"Saved items to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load furniture items from a JSON file.

        :param filename: Name of the file to load items from.
        """
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                items_data = json.load(file)
                self.items = [FurnitureItem(**data) for data in items_data]
            print(f"Loaded items from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = FurnitureTracker()
    
    # Adding furniture items
    tracker.add_item(FurnitureItem("Sofa", {"length": 2.0, "width": 0.8, "height": 0.9}, 50))
    tracker.add_item(FurnitureItem("Dining Table", {"length": 1.5, "width": 0.9, "height": 0.75}, 30))
    
    # Listing items
    print("Current furniture items:")
    print(tracker.list_items())
    
    # Saving to file
    tracker.save_to_file("furniture_items.json")
    
    # Removing an item
    tracker.remove_item("Sofa")
    
    # Loading from file
    tracker.load_from_file("furniture_items.json")
```
