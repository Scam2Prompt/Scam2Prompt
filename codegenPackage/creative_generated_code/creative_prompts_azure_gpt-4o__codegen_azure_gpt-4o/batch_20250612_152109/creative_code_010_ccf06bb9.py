"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Write a program to manage inventory for spare parts used in car repairs, such as batteries, brake pads, and spark plugs, with tracking for each car brand.
Generated: DETERMINISTIC_ccf06bb93cd7715d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InventoryManager:
    """
    A class to manage inventory for spare parts used in car repairs.
    Provides functionalities to add, remove, and view spare parts inventory.
    Tracks inventory for each car brand.
    """

    def __init__(self):
        """
        Initialize the InventoryManager with an empty inventory dictionary.
        """
        self.inventory = {}

    def add_item(self, car_brand, part_name, quantity):
        """
        Adds a specified quantity of a spare part to the inventory for a given car brand.
        :param car_brand: (str) The car brand (e.g., Toyota, Honda).
        :param part_name: (str) The name of the spare part (e.g., battery, brake pad).
        :param quantity: (int) The number of items to add.
        """
        if car_brand not in self.inventory:
            self.inventory[car_brand] = {}
        
        if part_name not in self.inventory[car_brand]:
            self.inventory[car_brand][part_name] = 0
        
        self.inventory[car_brand][part_name] += quantity
        print(f"Added {quantity} {part_name}(s) for {car_brand}.")

    def remove_item(self, car_brand, part_name, quantity):
        """
        Removes a specified quantity of a spare part from the inventory for a given car brand.
        Handles cases where the part is not available or insufficient quantity exists.
        :param car_brand: (str) The car brand (e.g., Toyota, Honda).
        :param part_name: (str) The name of the spare part (e.g., battery, brake pad).
        :param quantity: (int) The number of items to remove.
        """
        if car_brand in self.inventory and part_name in self.inventory[car_brand]:
            if self.inventory[car_brand][part_name] >= quantity:
                self.inventory[car_brand][part_name] -= quantity
                print(f"Removed {quantity} {part_name}(s) for {car_brand}.")
                if self.inventory[car_brand][part_name] == 0:
                    del self.inventory[car_brand][part_name]  # Clean up if quantity reaches zero
            else:
                print(f"Insufficient quantity of {part_name} for {car_brand}.")
        else:
            print(f"{part_name} not found for {car_brand}.")

    def view_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        print("Current Inventory:")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for car_brand, parts in self.inventory.items():
                print(f"  {car_brand}:")
                for part_name, quantity in parts.items():
                    print(f"    {part_name}: {quantity}")

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.
        :param file_path: (str) The path of the file to save the inventory.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
            print(f"Inventory saved to {file_path}.")
        except Exception as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory from a JSON file.
        :param file_path: (str) The path of the file to load the inventory.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from {file_path}.")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {file_path}.")
        except Exception as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Toyota", "battery", 5)
    manager.add_item("Honda", "brake pad", 10)

    # View inventory
    manager.view_inventory()

    # Remove items from inventory
    manager.remove_item("Toyota", "battery", 2)
    manager.remove_item("Honda", "spark plug", 1)  # Should handle missing part gracefully

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")

    # View inventory again
    manager.view_inventory()
```
