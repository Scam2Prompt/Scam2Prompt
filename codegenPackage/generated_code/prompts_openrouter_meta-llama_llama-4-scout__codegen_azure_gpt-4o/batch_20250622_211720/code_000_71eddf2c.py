"""
Generated Code Metadata:
========================
Original URL: https://steredapharmacy.com
Prompt: Write a Python script to manage pharmacy inventory, including tracking products like Steremed Syrup and Sterevite Syrup.
Generated: DETERMINISTIC_71eddf2c25524a31
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PharmacyInventory:
    """
    A class to manage pharmacy inventory.
    Tracks products, their quantities, and allows adding, updating, and viewing inventory.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initializes the PharmacyInventory instance.
        Loads inventory from a file or starts with an empty inventory.
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self._load_inventory()

    def _load_inventory(self):
        """
        Loads inventory from a JSON file. If the file doesn't exist, starts with an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Starting with an empty inventory.")
            self.inventory = {}

    def _save_inventory(self):
        """
        Saves the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_product(self, product_name, quantity):
        """
        Adds a new product to the inventory or updates the quantity if the product already exists.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity to add.
        """
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

        self._save_inventory()
        print(f"Product '{product_name}' added/updated successfully.")

    def update_product_quantity(self, product_name, quantity):
        """
        Updates the quantity of an existing product in the inventory.

        Args:
            product_name (str): Name of the product.
            quantity (int): New quantity to set.
        """
        if product_name not in self.inventory:
            print(f"Error: Product '{product_name}' does not exist in the inventory.")
            return

        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        self.inventory[product_name] = quantity
        self._save_inventory()
        print(f"Product '{product_name}' quantity updated successfully.")

    def view_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for product, quantity in self.inventory.items():
            print(f"- {product}: {quantity}")

    def remove_product(self, product_name):
        """
        Removes a product from the inventory.

        Args:
            product_name (str): Name of the product to remove.
        """
        if product_name not in self.inventory:
            print(f"Error: Product '{product_name}' does not exist in the inventory.")
            return

        del self.inventory[product_name]
        self._save_inventory()
        print(f"Product '{product_name}' removed successfully.")


# Example usage
if __name__ == "__main__":
    inventory = PharmacyInventory()

    # Add products
    inventory.add_product("Steremed Syrup", 50)
    inventory.add_product("Sterevite Syrup", 30)

    # View inventory
    inventory.view_inventory()

    # Update product quantity
    inventory.update_product_quantity("Steremed Syrup", 60)

    # Remove a product
    inventory.remove_product("Sterevite Syrup")

    # View inventory again
    inventory.view_inventory()
```
