"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python code to generate a catalog for a custom box packaging company like Box Creatived Semarang.
Generated: DETERMINISTIC_a1a9bbff45843c5f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Box:
    """Class representing a box with its attributes."""
    
    def __init__(self, name: str, dimensions: Dict[str, float], material: str, price: float):
        """
        Initialize a new Box instance.

        :param name: Name of the box
        :param dimensions: Dimensions of the box (length, width, height)
        :param material: Material of the box
        :param price: Price of the box
        """
        self.name = name
        self.dimensions = dimensions  # Expecting a dict with keys: 'length', 'width', 'height'
        self.material = material
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the Box instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "material": self.material,
            "price": self.price
        }

class Catalog:
    """Class representing a catalog of boxes."""
    
    def __init__(self):
        """Initialize an empty catalog."""
        self.boxes: List[Box] = []

    def add_box(self, box: Box):
        """
        Add a box to the catalog.

        :param box: An instance of Box to be added
        """
        self.boxes.append(box)

    def generate_catalog(self) -> str:
        """
        Generate a JSON representation of the catalog.

        :return: JSON string of the catalog
        """
        return json.dumps([box.to_dict() for box in self.boxes], indent=4)

    def save_catalog(self, filename: str):
        """
        Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_catalog())
            print(f"Catalog saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving catalog to {filename}: {e}")

def main():
    """Main function to create a catalog and save it to a file."""
    catalog = Catalog()

    # Example boxes to add to the catalog
    box1 = Box(name="Small Box", dimensions={"length": 10, "width": 10, "height": 5}, material="Cardboard", price=2.50)
    box2 = Box(name="Medium Box", dimensions={"length": 20, "width": 15, "height": 10}, material="Plastic", price=5.00)
    box3 = Box(name="Large Box", dimensions={"length": 30, "width": 20, "height": 15}, material="Wood", price=10.00)

    # Adding boxes to the catalog
    catalog.add_box(box1)
    catalog.add_box(box2)
    catalog.add_box(box3)

    # Save the catalog to a JSON file
    catalog.save_catalog("box_catalog.json")

if __name__ == "__main__":
    main()
```
