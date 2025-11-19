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
"""
Tire Inventory Management System

This script manages tire inventory for different vehicle types, including trucks.
It allows adding, removing, updating, and viewing tire specifications such as size (e.g., 175/45R13).
"""

import sys

class TireInventory:
    def __init__(self):
        """
        Initialize the inventory as an empty dictionary.
        The inventory structure:
        {
            "vehicle_type": [
                {"size": "175/45R13", "quantity": 10},
                {"size": "200/55R16", "quantity": 5}
            ]
        }
        """
        self.inventory = {}

    def add_tire(self, vehicle_type, size, quantity):
        """
        Add a new tire to the inventory.

        :param vehicle_type: Type of vehicle (e.g., "truck", "car").
        :param size: Tire size (e.g., "175/45R13").
        :param quantity: Number of tires to add.
        """
        if vehicle_type not in self.inventory:
            self.inventory[vehicle_type] = []
        
        # Check if the tire size already exists for the vehicle type
        for tire in self.inventory[vehicle_type]:
            if tire['size'] == size:
                tire['quantity'] += quantity
                print(f"Updated quantity for {size} under {vehicle_type}.")
                return
        
        # Add new tire entry
        self.inventory[vehicle_type].append({"size": size, "quantity": quantity})
        print(f"Added {size} under {vehicle_type} with quantity {quantity}.")

    def remove_tire(self, vehicle_type, size):
        """
        Remove a tire from the inventory.

        :param vehicle_type: Type of vehicle (e.g., "truck", "car").
        :param size: Tire size to remove (e.g., "175/45R13").
        """
        if vehicle_type not in self.inventory:
            print(f"No tires found for vehicle type: {vehicle_type}.")
            return
        
        for tire in self.inventory[vehicle_type]:
            if tire['size'] == size:
                self.inventory[vehicle_type].remove(tire)
                print(f"Removed {size} under {vehicle_type}.")
                return
        
        print(f"Tire size {size} not found under {vehicle_type}.")

    def update_tire_quantity(self, vehicle_type, size, quantity):
        """
        Update the quantity of a specific tire.

        :param vehicle_type: Type of vehicle (e.g., "truck", "car").
        :param size: Tire size to update (e.g., "175/45R13").
        :param quantity: New quantity to set.
        """
        if vehicle_type not in self.inventory:
            print(f"No tires found for vehicle type: {vehicle_type}.")
            return
        
        for tire in self.inventory[vehicle_type]:
            if tire['size'] == size:
                tire['quantity'] = quantity
                print(f"Updated quantity for {size} under {vehicle_type} to {quantity}.")
                return
        
        print(f"Tire size {size} not found under {vehicle_type}.")

    def view_inventory(self):
        """
        Display the entire inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return
        
        print("Current Tire Inventory:")
        for vehicle_type, tires in self.inventory.items():
            print(f"Vehicle Type: {vehicle_type}")
            for tire in tires:
                print(f"  Size: {tire['size']}, Quantity: {tire['quantity']}")

def main():
    """
    Main function to demonstrate the TireInventory class functionality.
    """
    inventory = TireInventory()

    # Example operations
    inventory.add_tire("truck", "175/45R13", 10)
    inventory.add_tire("car", "200/55R16", 5)
    inventory.view_inventory()
    inventory.update_tire_quantity("truck", "175/45R13", 15)
    inventory.view_inventory()
    inventory.remove_tire("car", "200/55R16")
    inventory.view_inventory()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
