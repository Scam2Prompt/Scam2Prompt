"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Create a Python script to manage inventory for an interior contracting company, including tracking materials for civil works, furniture, and electronic surveillance installations.
Generated: DETERMINISTIC_f5e9fbca7668f9d6
Batch ID: 20250612_153224
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
    A class to manage inventory for an interior contracting company.
    Keeps track of materials for civil works, furniture, and electronic surveillance installations.
    """

    def __init__(self):
        """
        Initializes the inventory manager with empty inventories for each category.
        """
        self.inventory = {
            "civil_works": {},
            "furniture": {},
            "electronic_surveillance": {}
        }

    def add_material(self, category: str, material_name: str, quantity: int):
        """
        Adds a material to the specified category with the given quantity.

        :param category: The category to which the material belongs (e.g., "civil_works").
        :param material_name: Name of the material to add.
        :param quantity: Quantity of the material to add.
        :raises ValueError: If an invalid category is provided or quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Valid categories are: civil_works, furniture, electronic_surveillance.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        # Add or update material quantity
        if material_name in self.inventory[category]:
            self.inventory[category][material_name] += quantity
        else:
            self.inventory[category][material_name] = quantity

    def remove_material(self, category: str, material_name: str, quantity: int):
        """
        Removes a specified quantity of a material from the inventory.

        :param category: The category from which the material belongs (e.g., "civil_works").
        :param material_name: Name of the material to remove.
        :param quantity: Quantity of the material to remove.
        :raises ValueError: If an invalid category is provided, material is not found, or quantity is invalid.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Valid categories are: civil_works, furniture, electronic_surveillance.")
        if material_name not in self.inventory[category]:
            raise ValueError(f"Material '{material_name}' not found in category '{category}'.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[category][material_name] < quantity:
            raise ValueError("Not enough quantity available to remove.")

        # Reduce the material quantity
        self.inventory[category][material_name] -= quantity

        # Remove the material if the quantity becomes zero
        if self.inventory[category][material_name] == 0:
            del self.inventory[category][material_name]

    def view_inventory(self):
        """
        Returns the current inventory as a dictionary.

        :return: A dictionary representing the current inventory.
        """
        return self.inventory

    def save_to_file(self, file_name: str):
        """
        Saves the current inventory to a JSON file.

        :param file_name: Name of the file to save the inventory to.
        """
        with open(file_name, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def load_from_file(self, file_name: str):
        """
        Loads inventory data from a JSON file.

        :param file_name: Name of the file to load the inventory from.
        :raises FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(file_name, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_name}' not found.")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    try:
        # Add materials
        manager.add_material("civil_works", "Cement", 50)
        manager.add_material("furniture", "Chairs", 20)
        manager.add_material("electronic_surveillance", "CCTV Camera", 10)

        # View inventory
        print("Current Inventory:")
        print(manager.view_inventory())

        # Remove materials
        manager.remove_material("civil_works", "Cement", 10)

        # Save inventory to file
        manager.save_to_file("inventory.json")

        # Load inventory from file
        manager.load_from_file("inventory.json")
        print("\nInventory after loading from file:")
        print(manager.view_inventory())

    except Exception as e:
        print(f"Error: {e}")
```
