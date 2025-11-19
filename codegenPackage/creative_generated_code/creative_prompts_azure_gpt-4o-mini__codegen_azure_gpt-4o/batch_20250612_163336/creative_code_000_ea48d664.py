"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startec.com.my
Prompt: Generate a code snippet for a simple inventory management system that could help a computer hardware retailer like StarTec Computer System Sdn Bhd manage their products effectively.
Generated: DETERMINISTIC_ea48d6649a5d8b55
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_management.py

import json

class InventoryManagementSystem:
    """
    A simple inventory management system for a computer hardware retailer.
    Allows adding, updating, removing, and viewing product details.
    """

    def __init__(self):
        """
        Initialize the inventory system with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_id, name, quantity, price):
        """
        Add a new product to the inventory.

        :param product_id: Unique identifier for the product (string)
        :param name: Name of the product (string)
        :param quantity: Quantity of the product (integer)
        :param price: Price of the product (float)
        """
        if product_id in self.inventory:
            raise ValueError("Product ID already exists.")
        self.inventory[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

    def update_product(self, product_id, name=None, quantity=None, price=None):
        """
        Update product details.

        :param product_id: Unique identifier for the product (string)
        :param name: New name of the product (optional, string)
        :param quantity: New quantity of the product (optional, integer)
        :param price: New price of the product (optional, float)
        """
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist.")
        if name is not None:
            self.inventory[product_id]["name"] = name
        if quantity is not None:
            self.inventory[product_id]["quantity"] = quantity
        if price is not None:
            self.inventory[product_id]["price"] = price

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        :param product_id: Unique identifier for the product (string)
        """
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist.")
        del self.inventory[product_id]

    def view_inventory(self):
        """
        View the entire inventory.

        :return: Inventory details in JSON format (string)
        """
        return json.dumps(self.inventory, indent=4)

    def view_product(self, product_id):
        """
        View details of a specific product.

        :param product_id: Unique identifier for the product (string)
        :return: Product details in JSON format (string)
        """
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist.")
        return json.dumps(self.inventory[product_id], indent=4)


# Example usage (for demonstration, not part of production code):
if __name__ == "__main__":
    try:
        inventory = InventoryManagementSystem()
        inventory.add_product("P001", "Laptop", 10, 1200.00)
        inventory.add_product("P002", "Mouse", 50, 25.50)
        inventory.update_product("P002", quantity=45)
        inventory.remove_product("P001")
        print("Inventory:")
        print(inventory.view_inventory())
        print("Product P002:")
        print(inventory.view_product("P002"))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
