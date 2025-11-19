"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Create a step-by-step guide on how to make a crochet backpack using the techniques described in the Paquete Profesional course, including code snippets for a simple inventory management system."
Generated: DETERMINISTIC_5644f3522f86e18f
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Inventory Management System for Crochet Backpack Materials
This script helps manage the inventory of materials required for making a crochet backpack.
It includes functionality to add, update, remove, and view materials.
"""

# Import necessary modules
import sys

class InventoryManager:
    def __init__(self):
        # Initialize an empty inventory dictionary
        self.inventory = {}

    def add_material(self, material_name, quantity):
        """
        Add a new material to the inventory.
        :param material_name: Name of the material (string)
        :param quantity: Quantity of the material (integer)
        """
        if material_name in self.inventory:
            print(f"Material '{material_name}' already exists. Use update_material to modify its quantity.")
        else:
            self.inventory[material_name] = quantity
            print(f"Material '{material_name}' added with quantity {quantity}.")

    def update_material(self, material_name, quantity):
        """
        Update the quantity of an existing material.
        :param material_name: Name of the material (string)
        :param quantity: New quantity of the material (integer)
        """
        if material_name in self.inventory:
            self.inventory[material_name] = quantity
            print(f"Material '{material_name}' updated to quantity {quantity}.")
        else:
            print(f"Material '{material_name}' does not exist. Use add_material to add it first.")

    def remove_material(self, material_name):
        """
        Remove a material from the inventory.
        :param material_name: Name of the material (string)
        """
        if material_name in self.inventory:
            del self.inventory[material_name]
            print(f"Material '{material_name}' removed from inventory.")
        else:
            print(f"Material '{material_name}' does not exist in the inventory.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for material, quantity in self.inventory.items():
                print(f"- {material}: {quantity}")

def main():
    """
    Main function to interact with the inventory management system.
    """
    inventory_manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. Add Material")
        print("2. Update Material")
        print("3. Remove Material")
        print("4. View Inventory")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            material_name = input("Enter material name: ").strip()
            try:
                quantity = int(input("Enter quantity: "))
                inventory_manager.add_material(material_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid integer.")
        elif choice == 2:
            material_name = input("Enter material name: ").strip()
            try:
                quantity = int(input("Enter new quantity: "))
                inventory_manager.update_material(material_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid integer.")
        elif choice == 3:
            material_name = input("Enter material name to remove: ").strip()
            inventory_manager.remove_material(material_name)
        elif choice == 4:
            inventory_manager.view_inventory()
        elif choice == 5:
            print("Exiting the Inventory Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
