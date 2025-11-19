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

class SnowConeTruckInventory:
    """
    A class to manage the inventory of a snow cone truck.
    """

    def __init__(self):
        """
        Initialize the inventory with default items and quantities.
        """
        self.inventory = {
            "flavors": {
                "cherry": 50,
                "blueberry": 50,
                "lime": 50,
                "grape": 50
            },
            "cones": 100,
            "cups": 100,
            "spoons": 100
        }

    def display_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        print("Current Inventory:")
        for category, items in self.inventory.items():
            if isinstance(items, dict):
                print(f"  {category.capitalize()}:")
                for item, quantity in items.items():
                    print(f"    {item.capitalize()}: {quantity}")
            else:
                print(f"  {category.capitalize()}: {items}")

    def update_inventory(self, category, item, quantity):
        """
        Update the inventory for a specific item.

        Args:
            category (str): The category of the item (e.g., 'flavors', 'cones').
            item (str): The specific item to update (e.g., 'cherry').
            quantity (int): The quantity to add (positive) or subtract (negative).

        Raises:
            ValueError: If the category or item is invalid, or if the quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}")
        
        if isinstance(self.inventory[category], dict):
            if item not in self.inventory[category]:
                raise ValueError(f"Invalid item: {item}")
            if self.inventory[category][item] + quantity < 0:
                raise ValueError(f"Insufficient stock for {item}.")
            self.inventory[category][item] += quantity
        else:
            if item != category:
                raise ValueError(f"Invalid item: {item}")
            if self.inventory[category] + quantity < 0:
                raise ValueError(f"Insufficient stock for {category}.")
            self.inventory[category] += quantity

    def save_inventory(self, filename="inventory.json"):
        """
        Save the current inventory to a JSON file.

        Args:
            filename (str): The name of the file to save the inventory to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.inventory, file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename="inventory.json"):
        """
        Load inventory from a JSON file.

        Args:
            filename (str): The name of the file to load the inventory from.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(filename, "r") as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from {filename}.")
        except IOError as e:
            print(f"Error loading inventory: {e}")


# Main script
if __name__ == "__main__":
    truck_inventory = SnowConeTruckInventory()

    # Display initial inventory
    truck_inventory.display_inventory()

    # Update inventory
    try:
        truck_inventory.update_inventory("flavors", "cherry", -10)
        truck_inventory.update_inventory("cones", "cones", -5)
    except ValueError as e:
        print(f"Error updating inventory: {e}")

    # Display updated inventory
    truck_inventory.display_inventory()

    # Save inventory to file
    truck_inventory.save_inventory()

    # Load inventory from file
    truck_inventory.load_inventory()
    truck_inventory.display_inventory()
```
