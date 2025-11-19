"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Generate a Python script to simulate an ice cream truck inventory management system for a snow cone truck.
Generated: DETERMINISTIC_d5396b59319004f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class IceCreamTruckInventory:
    def __init__(self):
        """Initialize the inventory with an empty dictionary."""
        self.inventory: Dict[str, int] = {}

    def add_item(self, flavor: str, quantity: int) -> None:
        """
        Add a specified quantity of a flavor to the inventory.

        :param flavor: The flavor of the ice cream/snow cone.
        :param quantity: The quantity to add to the inventory.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.inventory[flavor] = self.inventory.get(flavor, 0) + quantity
        print(f"Added {quantity} of {flavor}. Current stock: {self.inventory[flavor]}")

    def remove_item(self, flavor: str, quantity: int) -> None:
        """
        Remove a specified quantity of a flavor from the inventory.

        :param flavor: The flavor of the ice cream/snow cone.
        :param quantity: The quantity to remove from the inventory.
        :raises ValueError: If quantity is less than 1 or exceeds available stock.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if flavor not in self.inventory or self.inventory[flavor] < quantity:
            raise ValueError("Not enough stock to remove.")
        self.inventory[flavor] -= quantity
        print(f"Removed {quantity} of {flavor}. Current stock: {self.inventory[flavor]}")

    def get_inventory(self) -> Dict[str, int]:
        """Return the current inventory as a dictionary."""
        return self.inventory

    def save_inventory(self, filename: str) -> None:
        """
        Save the current inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        with open(filename, 'w') as file:
            json.dump(self.inventory, file)
        print(f"Inventory saved to {filename}.")

    def load_inventory(self, filename: str) -> None:
        """
        Load inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {filename} contains invalid JSON.")

def main():
    """Main function to demonstrate the inventory management system."""
    truck_inventory = IceCreamTruckInventory()

    # Example usage
    try:
        truck_inventory.add_item("Blue Raspberry", 10)
        truck_inventory.add_item("Cherry", 5)
        truck_inventory.remove_item("Blue Raspberry", 3)
        print("Current Inventory:", truck_inventory.get_inventory())
        
        # Save and load inventory
        truck_inventory.save_inventory("inventory.json")
        truck_inventory.load_inventory("inventory.json")
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()
```
