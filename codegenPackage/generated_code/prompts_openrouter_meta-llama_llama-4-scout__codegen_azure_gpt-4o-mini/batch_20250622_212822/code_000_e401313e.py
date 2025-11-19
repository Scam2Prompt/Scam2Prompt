"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Generate a Python script to manage tire inventory for different vehicle types, including trucks, with specifications like 175/45R13."
Generated: DETERMINISTIC_e401313e0026fde1
Batch ID: 20250622_212822
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

class Tire:
    """Class representing a tire with specifications."""
    
    def __init__(self, size: str, vehicle_type: str, quantity: int):
        """
        Initialize a Tire instance.

        :param size: The size of the tire (e.g., '175/45R13').
        :param vehicle_type: The type of vehicle the tire is suitable for (e.g., 'car', 'truck').
        :param quantity: The number of tires in inventory.
        """
        self.size = size
        self.vehicle_type = vehicle_type
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """Convert the Tire instance to a dictionary."""
        return {
            'size': self.size,
            'vehicle_type': self.vehicle_type,
            'quantity': self.quantity
        }

class TireInventory:
    """Class to manage tire inventory."""
    
    def __init__(self):
        """Initialize an empty tire inventory."""
        self.inventory: List[Tire] = []

    def add_tire(self, tire: Tire) -> None:
        """Add a tire to the inventory.

        :param tire: Tire instance to be added.
        """
        self.inventory.append(tire)

    def remove_tire(self, size: str, vehicle_type: str, quantity: int) -> bool:
        """Remove a specified quantity of tires from the inventory.

        :param size: The size of the tire to remove.
        :param vehicle_type: The type of vehicle the tire is suitable for.
        :param quantity: The number of tires to remove.
        :return: True if removal was successful, False otherwise.
        """
        for tire in self.inventory:
            if tire.size == size and tire.vehicle_type == vehicle_type:
                if tire.quantity >= quantity:
                    tire.quantity -= quantity
                    if tire.quantity == 0:
                        self.inventory.remove(tire)
                    return True
                else:
                    print(f"Not enough tires in inventory to remove {quantity}.")
                    return False
        print("Tire not found in inventory.")
        return False

    def get_inventory(self) -> List[Dict]:
        """Get the current inventory as a list of dictionaries.

        :return: List of tire specifications in dictionary format.
        """
        return [tire.to_dict() for tire in self.inventory]

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                tires_data = json.load(file)
                for tire_data in tires_data:
                    tire = Tire(tire_data['size'], tire_data['vehicle_type'], tire_data['quantity'])
                    self.add_tire(tire)
            print(f"Inventory loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    inventory = TireInventory()
    
    # Adding tires to inventory
    inventory.add_tire(Tire("175/45R13", "car", 10))
    inventory.add_tire(Tire("225/75R16", "truck", 5))
    
    # Display current inventory
    print("Current Inventory:", inventory.get_inventory())
    
    # Remove tires
    inventory.remove_tire("175/45R13", "car", 2)
    
    # Display updated inventory
    print("Updated Inventory:", inventory.get_inventory())
    
    # Save inventory to file
    inventory.save_inventory("tire_inventory.json")
    
    # Load inventory from file
    new_inventory = TireInventory()
    new_inventory.load_inventory("tire_inventory.json")
    print("Loaded Inventory:", new_inventory.get_inventory())
```
