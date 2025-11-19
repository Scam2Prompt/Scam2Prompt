"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Write a Python script to manage inventory for a packaging manufacturer that produces bakery and biscuit trays, ABS Atlas trays, and other food packaging products."
Generated: DETERMINISTIC_97d91e120c9004f6
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage inventory for a packaging manufacturer.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initializes the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory file (default: 'inventory.json').
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads inventory from a JSON file. If the file doesn't exist, initializes an empty inventory.
        :return: Dictionary representing the inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty inventory
            return {}

    def save_inventory(self):
        """
        Saves the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_product(self, product_name, quantity):
        """
        Adds a product to the inventory or updates its quantity.
        :param product_name: Name of the product.
        :param quantity: Quantity to add (must be positive).
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

        print(f"Added {quantity} units of '{product_name}' to inventory.")
        self.save_inventory()

    def remove_product(self, product_name, quantity):
        """
        Removes a product from the inventory or decreases its quantity.
        :param product_name: Name of the product.
        :param quantity: Quantity to remove (must be positive).
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if product_name not in self.inventory:
            print(f"Product '{product_name}' not found in inventory.")
            return

        if self.inventory[product_name] < quantity:
            print(f"Not enough '{product_name}' in inventory to remove {quantity} units.")
            return

        self.inventory[product_name] -= quantity
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]

        print(f"Removed {quantity} units of '{product_name}' from inventory.")
        self.save_inventory()

    def view_inventory(self):
        """
        Displays the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product, quantity in self.inventory.items():
                print(f" - {product}: {quantity} units")

    def search_product(self, product_name):
        """
        Searches for a product in the inventory.
        :param product_name: Name of the product to search for.
        """
        if product_name in self.inventory:
            print(f"'{product_name}' is in inventory with {self.inventory[product_name]} units.")
        else:
            print(f"'{product_name}' is not in inventory.")


# Main script
if __name__ == "__main__":
    manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Search Product")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            manager.view_inventory()
        elif choice == 2:
            product = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity to add: "))
                manager.add_product(product, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        elif choice == 3:
            product = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity to remove: "))
                manager.remove_product(product, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        elif choice == 4:
            product = input("Enter product name to search: ")
            manager.search_product(product)
        elif choice == 5:
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
```
