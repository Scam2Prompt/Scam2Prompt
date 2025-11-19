"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: "Write a Python code to manage inventory of industrial brushes with different dimensions and characteristics, similar to those offered by Vircomem."
Generated: DETERMINISTIC_f028883801104bb0
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Brush:
    """Class to represent an industrial brush with various dimensions and characteristics."""
    
    def __init__(self, name: str, dimensions: Dict[str, float], material: str, quantity: int):
        """
        Initialize a new Brush instance.

        :param name: Name of the brush
        :param dimensions: Dictionary containing dimensions (e.g., width, height, length)
        :param material: Material of the brush
        :param quantity: Available quantity in inventory
        """
        self.name = name
        self.dimensions = dimensions
        self.material = material
        self.quantity = quantity

    def __repr__(self) -> str:
        """Return a string representation of the Brush instance."""
        return f"Brush(name={self.name}, dimensions={self.dimensions}, material={self.material}, quantity={self.quantity})"

class Inventory:
    """Class to manage the inventory of brushes."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.brushes: List[Brush] = []

    def add_brush(self, brush: Brush) -> None:
        """
        Add a new brush to the inventory.

        :param brush: Brush instance to be added
        """
        self.brushes.append(brush)

    def remove_brush(self, name: str) -> bool:
        """
        Remove a brush from the inventory by name.

        :param name: Name of the brush to remove
        :return: True if the brush was removed, False if not found
        """
        for i, brush in enumerate(self.brushes):
            if brush.name == name:
                del self.brushes[i]
                return True
        return False

    def update_quantity(self, name: str, quantity: int) -> bool:
        """
        Update the quantity of a brush in the inventory.

        :param name: Name of the brush to update
        :param quantity: New quantity to set
        :return: True if the quantity was updated, False if not found
        """
        for brush in self.brushes:
            if brush.name == name:
                brush.quantity = quantity
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """
        Get a list of all brushes in the inventory.

        :return: List of dictionaries representing each brush
        """
        return [brush.__dict__ for brush in self.brushes]

    def save_to_file(self, filename: str) -> None:
        """
        Save the inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load the inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        """
        try:
            with open(filename, 'r') as file:
                brushes_data = json.load(file)
                self.brushes = [Brush(**data) for data in brushes_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding brushes to the inventory
    inventory.add_brush(Brush("Standard Brush", {"width": 5.0, "height": 10.0, "length": 15.0}, "Nylon", 100))
    inventory.add_brush(Brush("Heavy Duty Brush", {"width": 7.0, "height": 12.0, "length": 20.0}, "Steel", 50))
    
    # Updating quantity
    inventory.update_quantity("Standard Brush", 90)
    
    # Saving inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Loading inventory from a file
    inventory.load_from_file("inventory.json")
    
    # Displaying the inventory
    print(inventory.get_inventory())
```
