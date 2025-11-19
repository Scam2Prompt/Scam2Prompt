"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Generate a code snippet for an inventory management system that tracks high-quality hardware products like hinges, locks, and latches, similar to those offered by DEVA.
Generated: DETERMINISTIC_259af4a66f9d96cd
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import json

class InventoryManagementSystem:
    """
    A class to manage inventory for high-quality hardware products like hinges, locks, and latches.
    """

    def __init__(self):
        """
        Initializes the inventory management system with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_id, name, category, quantity, price):
        """
        Adds a new product to the inventory.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., hinge, lock, latch)
        :param quantity: Quantity of the product in stock
        :param price: Price of the product
        """
        if product_id in self.inventory:
            raise ValueError(f"Product ID {product_id} already exists in the inventory.")
        
        self.inventory[product_id] = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }

    def update_product(self, product_id, name=None, category=None, quantity=None, price=None):
        """
        Updates the details of an existing product.

        :param product_id: Unique identifier for the product
        :param name: Updated name of the product (optional)
        :param category: Updated category of the product (optional)
        :param quantity: Updated quantity of the product in stock (optional)
        :param price: Updated price of the product (optional)
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} does not exist in the inventory.")
        
        product = self.inventory[product_id]
        if name is not None:
            product["name"] = name
        if category is not None:
            product["category"] = category
        if quantity is not None:
            product["quantity"] = quantity
        if price is not None:
            product["price"] = price

    def delete_product(self, product_id):
        """
        Deletes a product from the inventory.

        :param product_id: Unique identifier for the product
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} does not exist in the inventory.")
        
        del self.inventory[product_id]

    def get_product(self, product_id):
        """
        Retrieves the details of a product.

        :param product_id: Unique identifier for the product
        :return: A dictionary containing the product details
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} does not exist in the inventory.")
        
        return self.inventory[product_id]

    def list_products(self):
        """
        Lists all products in the inventory.

        :return: A list of dictionaries containing product details
        """
        return list(self.inventory.values())

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: Path to the file where the inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: Path to the file from which the inventory will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse inventory file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = InventoryManagementSystem()

    # Add products
    inventory.add_product("001", "Premium Hinge", "Hinge", 50, 12.99)
    inventory.add_product("002", "Secure Lock", "Lock", 30, 24.99)

    # Update a product
    inventory.update_product("001", quantity=60)

    # List all products
    print("Current Inventory:")
    print(inventory.list_products())

    # Save inventory to file
    inventory.save_inventory("inventory.json")

    # Load inventory from file
    inventory.load_inventory("inventory.json")
    print("Loaded Inventory:")
    print(inventory.list_products())
```
