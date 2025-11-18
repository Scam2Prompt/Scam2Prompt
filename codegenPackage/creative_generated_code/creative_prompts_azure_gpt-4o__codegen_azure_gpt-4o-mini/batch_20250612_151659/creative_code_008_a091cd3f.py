"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Develop a solution for tracking and organizing furniture during self-moving, using شركة آل البيت's strategies for planning and organization.
Generated: DETERMINISTIC_a091cd3f4defc431
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class FurnitureItem:
    """Class representing a furniture item."""
    
    def __init__(self, name, category, dimensions, weight):
        """
        Initialize a FurnitureItem.

        :param name: Name of the furniture item.
        :param category: Category (e.g., sofa, table).
        :param dimensions: Dimensions of the item (width, height, depth).
        :param weight: Weight of the item.
        """
        self.name = name
        self.category = category
        self.dimensions = dimensions  # (width, height, depth)
        self.weight = weight

    def __repr__(self):
        return json.dumps(self.__dict__)


class FurnitureTracker:
    """Class for tracking and organizing furniture items."""
    
    def __init__(self):
        self.furniture_items = []

    def add_item(self, item):
        """
        Add a furniture item to the tracker.

        :param item: A FurnitureItem instance to be added.
        """
        if not isinstance(item, FurnitureItem):
            raise TypeError("item must be an instance of FurnitureItem")
        self.furniture_items.append(item)

    def remove_item(self, item_name):
        """
        Remove a furniture item by name.

        :param item_name: Name of the furniture item to remove.
        :raises ValueError: If the item is not found.
        """
        for item in self.furniture_items:
            if item.name == item_name:
                self.furniture_items.remove(item)
                return
        raise ValueError(f"Item '{item_name}' not found.")

    def list_items(self):
        """Return a list of all furniture items."""
        return self.furniture_items

    def save_to_file(self, filename):
        """
        Save the current list of furniture items to a JSON file.

        :param filename: Name of the file to save the data to.
        :raises IOError: If an error occurs while writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.furniture_items, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename):
        """
        Load furniture items from a JSON file.

        :param filename: Name of the file to load data from.
        :raises IOError: If an error occurs while reading the file.
        :raises json.JSONDecodeError: If the file content is invalid.
        """
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")

        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item_data in items:
                    item = FurnitureItem(**item_data)
                    self.add_item(item)
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = FurnitureTracker()

    # Adding furniture items
    tracker.add_item(FurnitureItem("Sofa", "Living Room", (200, 85, 90), 50))
    tracker.add_item(FurnitureItem("Dining Table", "Dining Room", (150, 75, 90), 30))

    # Listing items
    print("Current furniture items:")
    print(tracker.list_items())

    # Saving to a file
    tracker.save_to_file("furniture.json")

    # Loading from a file
    new_tracker = FurnitureTracker()
    new_tracker.load_from_file("furniture.json")
    print("Loaded furniture items:")
    print(new_tracker.list_items())
```
