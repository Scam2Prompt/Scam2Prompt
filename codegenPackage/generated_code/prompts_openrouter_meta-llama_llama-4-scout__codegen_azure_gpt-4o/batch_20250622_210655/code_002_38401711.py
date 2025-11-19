"""
Generated Code Metadata:
========================
Original URL: https://tubephanoi.vn
Prompt: "Write a Python script to manage inventory for a plastic product warehouse, such as Tổng kho nhựa The Five, including tracking stock levels and product types."
Generated: DETERMINISTIC_3840171142179487
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

class InventoryManager:
    """
    A class to manage inventory for a plastic product warehouse.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from a JSON file. If the file doesn't exist, initialize an empty inventory.
        """
        try:
            with open(self.inventory_file, "r") as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Initializing empty inventory.")
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_product(self, product_name, product_type, quantity):
        """
        Add a new product to the inventory or update an existing product.
        :param product_name: Name of the product
        :param product_type: Type of the product (e.g., plastic sheet, pipe, etc.)
        :param quantity: Quantity of the product to add
        """
        if product_name in self.inventory:
            self.inventory[product_name]["quantity"] += quantity
        else:
            self.inventory[product_name] = {
                "type": product_type,
                "quantity": quantity
            }
        self.save_inventory()
        print(f"Product '{product_name}' added/updated successfully.")

    def remove_product(self, product_name, quantity):
        """
        Remove a specified quantity of a product from the inventory.
        :param product_name: Name of the product
        :param quantity: Quantity of the product to remove
        """
        if product_name in self.inventory:
            if self.inventory[product_name]["quantity"] >= quantity:
                self.inventory[product_name]["quantity"] -= quantity
                if self.inventory[product_name]["quantity"] == 0:
                    del self.inventory[product_name]
                self.save_inventory()
                print(f"Removed {quantity} units of '{product_name}'.")
            else:
                print(f"Error: Not enough stock to remove {quantity} units of '{product_name}'.")
        else:
            print(f"Error: Product '{product_name}' not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product_name, details in self.inventory.items():
                print(f"- {product_name}: Type: {details['type']}, Quantity: {details['quantity']}")

    def search_product(self, product_name):
        """
        Search for a product in the inventory.
        :param product_name: Name of the product to search for
        """
        if product_name in self.inventory:
            details = self.inventory[product_name]
            print(f"Product Found: {product_name} - Type: {details['type']}, Quantity: {details['quantity']}")
        else:
            print(f"Product '{product_name}' not found in inventory.")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("Plastic Sheet", "Sheet", 100)
    manager.add_product("PVC Pipe", "Pipe", 50)

    # View inventory
    manager.view_inventory()

    # Remove products
    manager.remove_product("Plastic Sheet", 20)

    # Search for a product
    manager.search_product("PVC Pipe")

    # View inventory after updates
    manager.view_inventory()
```
