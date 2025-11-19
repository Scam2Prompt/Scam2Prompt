"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Write a Python script to manage an inventory of Apple products, including iPhones and MacBooks, for a store like Apple Market Bali.
Generated: DETERMINISTIC_bcb9aed9059e443f
Batch ID: 20250622_210703
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
    """A class to manage the inventory of Apple products."""

    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with a specified inventory file.

        Args:
            inventory_file (str): The path to the JSON file that stores the inventory.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> List[Dict[str, Any]]:
        """Loads the inventory from a JSON file.

        Returns:
            List[Dict[str, Any]]: A list of products in the inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Inventory file '{self.inventory_file}' not found. Starting with an empty inventory.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the inventory file '{self.inventory_file}'. Starting with an empty inventory.")
            return []

    def save_inventory(self) -> None:
        """Saves the current inventory to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to '{self.inventory_file}': {e}")

    def add_product(self, product: Dict[str, Any]) -> None:
        """Adds a new product to the inventory.

        Args:
            product (Dict[str, Any]): A dictionary containing product details.
        """
        self.inventory.append(product)
        self.save_inventory()

    def remove_product(self, product_id: str) -> None:
        """Removes a product from the inventory by its ID.

        Args:
            product_id (str): The ID of the product to remove.
        """
        self.inventory = [product for product in self.inventory if product['id'] != product_id]
        self.save_inventory()

    def update_product(self, product_id: str, updated_info: Dict[str, Any]) -> None:
        """Updates the details of an existing product.

        Args:
            product_id (str): The ID of the product to update.
            updated_info (Dict[str, Any]): A dictionary containing updated product details.
        """
        for product in self.inventory:
            if product['id'] == product_id:
                product.update(updated_info)
                break
        self.save_inventory()

    def list_products(self) -> None:
        """Prints the list of products in the inventory."""
        if not self.inventory:
            print("No products in inventory.")
            return
        for product in self.inventory:
            print(f"ID: {product['id']}, Name: {product['name']}, Type: {product['type']}, Price: {product['price']}, Quantity: {product['quantity']}")

if __name__ == "__main__":
    # Example usage of the InventoryManager
    inventory_manager = InventoryManager('inventory.json')

    # Adding products
    inventory_manager.add_product({
        'id': '1',
        'name': 'iPhone 14',
        'type': 'iPhone',
        'price': 999.99,
        'quantity': 10
    })
    inventory_manager.add_product({
        'id': '2',
        'name': 'MacBook Pro 16',
        'type': 'MacBook',
        'price': 2399.99,
        'quantity': 5
    })

    # Listing products
    inventory_manager.list_products()

    # Updating a product
    inventory_manager.update_product('1', {'price': 949.99, 'quantity': 8})

    # Removing a product
    inventory_manager.remove_product('2')

    # Listing products again to see changes
    inventory_manager.list_products()
```
