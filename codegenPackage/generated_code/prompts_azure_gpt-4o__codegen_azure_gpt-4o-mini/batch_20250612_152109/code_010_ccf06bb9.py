"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Write a program to manage inventory for spare parts used in car repairs, such as batteries, brake pads, and spark plugs, with tracking for each car brand.
Generated: DETERMINISTIC_ccf06bb93cd7715d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class SparePart:
    """Class to represent a spare part in the inventory."""
    
    def __init__(self, name: str, brand: str, quantity: int):
        self.name = name
        self.brand = brand
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} ({self.brand}): {self.quantity} in stock"

class Inventory:
    """Class to manage the inventory of spare parts."""
    
    def __init__(self):
        self.parts: Dict[str, List[SparePart]] = {}

    def add_part(self, part: SparePart) -> None:
        """Add a spare part to the inventory."""
        if part.brand not in self.parts:
            self.parts[part.brand] = []
        self.parts[part.brand].append(part)

    def remove_part(self, name: str, brand: str, quantity: int) -> bool:
        """Remove a specified quantity of a spare part from the inventory."""
        if brand in self.parts:
            for part in self.parts[brand]:
                if part.name == name:
                    if part.quantity >= quantity:
                        part.quantity -= quantity
                        if part.quantity == 0:
                            self.parts[brand].remove(part)
                        return True
                    else:
                        print(f"Not enough {name} in stock.")
                        return False
        print(f"{name} ({brand}) not found in inventory.")
        return False

    def get_inventory(self) -> Dict[str, List[SparePart]]:
        """Return the current inventory."""
        return self.parts

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.parts, file, default=lambda o: o.__dict__, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.parts = json.load(file)
                # Convert dictionaries back to SparePart objects
                for brand, parts in self.parts.items():
                    self.parts[brand] = [SparePart(**part) for part in parts]
            print(f"Inventory loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding parts to the inventory
    inventory.add_part(SparePart("Battery", "Toyota", 10))
    inventory.add_part(SparePart("Brake Pad", "Honda", 5))
    inventory.add_part(SparePart("Spark Plug", "Ford", 20))

    # Display current inventory
    print("Current Inventory:")
    for brand, parts in inventory.get_inventory().items():
        for part in parts:
            print(part)

    # Remove parts from the inventory
    inventory.remove_part("Battery", "Toyota", 2)

    # Save inventory to a file
    inventory.save_inventory("inventory.json")

    # Load inventory from a file
    inventory.load_inventory("inventory.json")
```
