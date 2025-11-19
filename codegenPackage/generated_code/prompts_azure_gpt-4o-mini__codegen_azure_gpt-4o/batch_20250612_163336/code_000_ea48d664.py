"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: Generate a code snippet for a simple inventory management system that could help a computer hardware retailer like StarTec Computer System Sdn Bhd manage their products effectively.
Generated: DETERMINISTIC_ea48d6649a5d8b55
Batch ID: 20250612_163336
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

class InventoryManagement:
    """
    A simple inventory management system for managing products in a computer hardware store.
    """

    def __init__(self):
        """
        Initializes the inventory as an empty dictionary.
        """
        self.inventory = {}

    def add_product(self, product_id, name, quantity, price):
        """
        Adds a new product to the inventory.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            quantity (int): Quantity of the product in stock.
            price (float): Price of the product.

        Raises:
            ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        self.inventory[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

    def update_product(self, product_id, quantity=None, price=None):
        """
        Updates the quantity and/or price of an existing product.

        Args:
            product_id (str): Unique identifier for the product.
            quantity (int, optional): New quantity of the product.
            price (float, optional): New price of the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product with ID '{product_id}' not found.")
        
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be non-negative.")
            self.inventory[product_id]["quantity"] = quantity
        
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative.")
            self.inventory[product_id]["price"] = price

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (str): Unique identifier for the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product with ID '{product_id}' not found.")
        
        del self.inventory[product_id]

    def view_inventory(self):
        """
        Returns the current inventory as a JSON string.

        Returns:
            str: JSON representation of the inventory.
        """
        return json.dumps(self.inventory, indent=4)

    def search_product(self, product_id):
        """
        Searches for a product in the inventory.

        Args:
            product_id (str): Unique identifier for the product.

        Returns:
            dict: Product details if found.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product with ID '{product_id}' not found.")
        
        return self.inventory[product_id]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the inventory management system
        inventory = InventoryManagement()

        # Add products
        inventory.add_product("P001", "Gaming Laptop", 10, 1500.00)
        inventory.add_product("P002", "Mechanical Keyboard", 25, 120.00)

        # Update a product
        inventory.update_product("P001", quantity=8)

        # View inventory
        print("Current Inventory:")
        print(inventory.view_inventory())

        # Search for a product
        print("\nSearching for product 'P001':")
        print(inventory.search_product("P001"))

        # Remove a product
        inventory.remove_product("P002")

        # View inventory after removal
        print("\nInventory after removal:")
        print(inventory.view_inventory())

    except Exception as e:
        print(f"Error: {e}")
```
