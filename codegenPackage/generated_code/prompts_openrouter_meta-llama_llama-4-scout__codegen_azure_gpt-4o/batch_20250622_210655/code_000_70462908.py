"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a Python script to manage inventory for a frozen yogurt shop with multiple locations like Andias Frozen Yogurt, including their 100+ toppings and 14 unique flavors.
Generated: DETERMINISTIC_70462908aa494c4f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class FrozenYogurtInventoryManager:
    """
    A class to manage inventory for a frozen yogurt shop with multiple locations.
    """

    def __init__(self, data_file="inventory.json"):
        """
        Initialize the inventory manager with a data file.
        :param data_file: Path to the JSON file storing inventory data.
        """
        self.data_file = data_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the JSON file.
        If the file does not exist, initialize an empty inventory.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading inventory file: {e}")
                self.inventory = {}
        else:
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")

    def add_location(self, location_name):
        """
        Add a new location to the inventory.
        :param location_name: Name of the new location.
        """
        if location_name in self.inventory:
            print(f"Location '{location_name}' already exists.")
        else:
            self.inventory[location_name] = {"flavors": {}, "toppings": {}}
            self.save_inventory()
            print(f"Location '{location_name}' added successfully.")

    def add_flavor(self, location_name, flavor_name, quantity):
        """
        Add or update a flavor for a specific location.
        :param location_name: Name of the location.
        :param flavor_name: Name of the flavor.
        :param quantity: Quantity of the flavor.
        """
        if location_name not in self.inventory:
            print(f"Location '{location_name}' does not exist.")
            return

        self.inventory[location_name]["flavors"][flavor_name] = quantity
        self.save_inventory()
        print(f"Flavor '{flavor_name}' added/updated for location '{location_name}'.")

    def add_topping(self, location_name, topping_name, quantity):
        """
        Add or update a topping for a specific location.
        :param location_name: Name of the location.
        :param topping_name: Name of the topping.
        :param quantity: Quantity of the topping.
        """
        if location_name not in self.inventory:
            print(f"Location '{location_name}' does not exist.")
            return

        self.inventory[location_name]["toppings"][topping_name] = quantity
        self.save_inventory()
        print(f"Topping '{topping_name}' added/updated for location '{location_name}'.")

    def get_inventory(self, location_name):
        """
        Get the inventory for a specific location.
        :param location_name: Name of the location.
        :return: Inventory data for the location.
        """
        if location_name not in self.inventory:
            print(f"Location '{location_name}' does not exist.")
            return None

        return self.inventory[location_name]

    def remove_location(self, location_name):
        """
        Remove a location from the inventory.
        :param location_name: Name of the location to remove.
        """
        if location_name in self.inventory:
            del self.inventory[location_name]
            self.save_inventory()
            print(f"Location '{location_name}' removed successfully.")
        else:
            print(f"Location '{location_name}' does not exist.")

    def remove_flavor(self, location_name, flavor_name):
        """
        Remove a flavor from a specific location.
        :param location_name: Name of the location.
        :param flavor_name: Name of the flavor to remove.
        """
        if location_name not in self.inventory:
            print(f"Location '{location_name}' does not exist.")
            return

        if flavor_name in self.inventory[location_name]["flavors"]:
            del self.inventory[location_name]["flavors"][flavor_name]
            self.save_inventory()
            print(f"Flavor '{flavor_name}' removed from location '{location_name}'.")
        else:
            print(f"Flavor '{flavor_name}' does not exist at location '{location_name}'.")

    def remove_topping(self, location_name, topping_name):
        """
        Remove a topping from a specific location.
        :param location_name: Name of the location.
        :param topping_name: Name of the topping to remove.
        """
        if location_name not in self.inventory:
            print(f"Location '{location_name}' does not exist.")
            return

        if topping_name in self.inventory[location_name]["toppings"]:
            del self.inventory[location_name]["toppings"][topping_name]
            self.save_inventory()
            print(f"Topping '{topping_name}' removed from location '{location_name}'.")
        else:
            print(f"Topping '{topping_name}' does not exist at location '{location_name}'.")

# Example usage
if __name__ == "__main__":
    manager = FrozenYogurtInventoryManager()

    # Add locations
    manager.add_location("Andias Frozen Yogurt - Downtown")
    manager.add_location("Andias Frozen Yogurt - Uptown")

    # Add flavors and toppings
    manager.add_flavor("Andias Frozen Yogurt - Downtown", "Vanilla", 50)
    manager.add_flavor("Andias Frozen Yogurt - Downtown", "Chocolate", 30)
    manager.add_topping("Andias Frozen Yogurt - Downtown", "Sprinkles", 100)
    manager.add_topping("Andias Frozen Yogurt - Downtown", "Cherries", 75)

    # Get inventory
    print(manager.get_inventory("Andias Frozen Yogurt - Downtown"))

    # Remove items
    manager.remove_flavor("Andias Frozen Yogurt - Downtown", "Vanilla")
    manager.remove_topping("Andias Frozen Yogurt - Downtown", "Sprinkles")

    # Remove location
    manager.remove_location("Andias Frozen Yogurt - Uptown")
```
