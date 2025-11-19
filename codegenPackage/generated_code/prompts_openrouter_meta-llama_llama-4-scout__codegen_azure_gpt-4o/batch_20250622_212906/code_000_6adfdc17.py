"""
Generated Code Metadata:
========================
Original URL: https://goltaa.com
Prompt: "Write a Python code snippet to manage an e-commerce inventory for a floral arrangement store like Goltaa, including product categories for wedding and condolence flower bases."
Generated: DETERMINISTIC_6adfdc17f4991ecf
Batch ID: 20250622_212906
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
    A class to manage the inventory of an e-commerce floral arrangement store.
    Includes product categories for wedding and condolence flower bases.
    """

    def __init__(self):
        """
        Initializes the inventory manager with empty product categories.
        """
        self.inventory = {
            "Wedding Flower Bases": {},
            "Condolence Flower Bases": {}
        }

    def add_product(self, category, product_name, quantity, price):
        """
        Adds a product to the specified category in the inventory.

        Args:
            category (str): The category of the product (e.g., "Wedding Flower Bases").
            product_name (str): The name of the product.
            quantity (int): The quantity of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the category is invalid or quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        # Add or update the product in the inventory
        self.inventory[category][product_name] = {
            "quantity": quantity,
            "price": price
        }

    def remove_product(self, category, product_name):
        """
        Removes a product from the specified category in the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.

        Raises:
            ValueError: If the category or product does not exist.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")

        del self.inventory[category][product_name]

    def update_product(self, category, product_name, quantity=None, price=None):
        """
        Updates the quantity and/or price of a product in the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.
            quantity (int, optional): The new quantity of the product.
            price (float, optional): The new price of the product.

        Raises:
            ValueError: If the category or product does not exist, or if quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")
        if quantity is not None and quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        if price is not None and price < 0:
            raise ValueError("Price must be non-negative.")

        # Update the product details
        if quantity is not None:
            self.inventory[category][product_name]["quantity"] = quantity
        if price is not None:
            self.inventory[category][product_name]["price"] = price

    def view_inventory(self):
        """
        Returns the current inventory as a JSON string.

        Returns:
            str: The inventory in JSON format.
        """
        return json.dumps(self.inventory, indent=4)

    def search_product(self, category, product_name):
        """
        Searches for a product in the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.

        Returns:
            dict: The product details if found.

        Raises:
            ValueError: If the category or product does not exist.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")

        return self.inventory[category][product_name]


# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()

        # Add products
        manager.add_product("Wedding Flower Bases", "Rose Bouquet", 10, 50.0)
        manager.add_product("Condolence Flower Bases", "White Lily Arrangement", 5, 30.0)

        # View inventory
        print("Current Inventory:")
        print(manager.view_inventory())

        # Update product
        manager.update_product("Wedding Flower Bases", "Rose Bouquet", quantity=15)

        # Search for a product
        print("\nProduct Details:")
        print(manager.search_product("Wedding Flower Bases", "Rose Bouquet"))

        # Remove a product
        manager.remove_product("Condolence Flower Bases", "White Lily Arrangement")

        # View inventory after removal
        print("\nUpdated Inventory:")
        print(manager.view_inventory())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
