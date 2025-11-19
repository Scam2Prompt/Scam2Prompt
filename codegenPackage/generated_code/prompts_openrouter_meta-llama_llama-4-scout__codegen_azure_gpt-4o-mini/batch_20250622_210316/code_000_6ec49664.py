"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Write a Python code to manage an inventory of gemstones, including their names, carat weights, and prices, similar to the catalog found on Bismillah Gems.
Generated: DETERMINISTIC_6ec49664128b6f5e
Batch ID: 20250622_210316
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

class Gemstone:
    """Class to represent a gemstone with its attributes."""
    
    def __init__(self, name: str, carat_weight: float, price: float):
        self.name = name
        self.carat_weight = carat_weight
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the gemstone object to a dictionary."""
        return {
            "name": self.name,
            "carat_weight": self.carat_weight,
            "price": self.price
        }

class Inventory:
    """Class to manage a collection of gemstones."""
    
    def __init__(self):
        self.gemstones: List[Gemstone] = []

    def add_gemstone(self, gemstone: Gemstone) -> None:
        """Add a gemstone to the inventory."""
        self.gemstones.append(gemstone)

    def remove_gemstone(self, name: str) -> bool:
        """Remove a gemstone from the inventory by name."""
        for gemstone in self.gemstones:
            if gemstone.name == name:
                self.gemstones.remove(gemstone)
                return True
        return False

    def find_gemstone(self, name: str) -> Gemstone:
        """Find a gemstone by name."""
        for gemstone in self.gemstones:
            if gemstone.name == name:
                return gemstone
        raise ValueError(f"Gemstone '{name}' not found in inventory.")

    def list_gemstones(self) -> List[Dict[str, Any]]:
        """List all gemstones in the inventory."""
        return [gemstone.to_dict() for gemstone in self.gemstones]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_gemstones(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                gemstones_data = json.load(file)
                self.gemstones = [Gemstone(**data) for data in gemstones_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding gemstones
    inventory.add_gemstone(Gemstone("Diamond", 1.0, 5000.0))
    inventory.add_gemstone(Gemstone("Ruby", 0.5, 3000.0))
    
    # Listing gemstones
    print("Current Inventory:")
    print(inventory.list_gemstones())
    
    # Saving to file
    inventory.save_to_file("gemstones_inventory.json")
    
    # Loading from file
    new_inventory = Inventory()
    new_inventory.load_from_file("gemstones_inventory.json")
    print("Loaded Inventory:")
    print(new_inventory.list_gemstones())
```
