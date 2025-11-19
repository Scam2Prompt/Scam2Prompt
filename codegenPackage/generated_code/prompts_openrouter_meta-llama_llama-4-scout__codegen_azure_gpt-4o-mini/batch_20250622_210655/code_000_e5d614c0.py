"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Write a Python code to manage inventory of agricultural products like fertilizers and bio stimulants."
Generated: DETERMINISTIC_e5d614c018208110
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
from typing import List, Dict, Any

class InventoryManager:
    """A class to manage the inventory of agricultural products."""

    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with a specified inventory file.

        Args:
            inventory_file (str): The path to the JSON file that stores inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, Any]:
        """Loads the inventory from a JSON file.

        Returns:
            Dict[str, Any]: The inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty inventory if the file does not exist
        except json.JSONDecodeError:
            print("Error: The inventory file is not a valid JSON.")
            return {}

    def save_inventory(self) -> None:
        """Saves the current inventory to a JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_product(self, product_name: str, quantity: int, price: float) -> None:
        """Adds a new product to the inventory.

        Args:
            product_name (str): The name of the product.
            quantity (int): The quantity of the product.
            price (float): The price of the product.
        """
        if product_name in self.inventory:
            print(f"Product '{product_name}' already exists. Updating quantity.")
            self.inventory[product_name]['quantity'] += quantity
        else:
            self.inventory[product_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()

    def remove_product(self, product_name: str, quantity: int) -> None:
        """Removes a specified quantity of a product from the inventory.

        Args:
            product_name (str): The name of the product.
            quantity (int): The quantity to remove.
        """
        if product_name in self.inventory:
            if self.inventory[product_name]['quantity'] >= quantity:
                self.inventory[product_name]['quantity'] -= quantity
                if self.inventory[product_name]['quantity'] == 0:
                    del self.inventory[product_name]  # Remove product if quantity is zero
                self.save_inventory()
            else:
                print(f"Error: Not enough quantity of '{product_name}' to remove.")
        else:
            print(f"Error: Product '{product_name}' not found in inventory.")

    def get_inventory(self) -> Dict[str, Any]:
        """Returns the current inventory.

        Returns:
            Dict[str, Any]: The current inventory data.
        """
        return self.inventory

    def display_inventory(self) -> None:
        """Displays the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for product, details in self.inventory.items():
            print(f"Product: {product}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager('inventory.json')
    inventory_manager.add_product('Fertilizer A', 100, 25.50)
    inventory_manager.add_product('Bio Stimulant B', 50, 15.75)
    inventory_manager.display_inventory()
    inventory_manager.remove_product('Fertilizer A', 20)
    inventory_manager.display_inventory()
```
