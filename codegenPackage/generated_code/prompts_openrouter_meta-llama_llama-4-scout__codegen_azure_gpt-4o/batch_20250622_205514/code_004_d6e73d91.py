"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a Python script to manage an inventory of hair care products, including tracking stock levels and product prices, inspired by the product offerings on Zento Cosmetic.
Generated: DETERMINISTIC_d6e73d91147d11de
Batch ID: 20250622_205514
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
    A class to manage inventory for hair care products.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, price, stock):
        """
        Adds a new product to the inventory.

        :param product_name: Name of the product (string)
        :param price: Price of the product (float)
        :param stock: Initial stock level (int)
        """
        if product_name in self.inventory:
            raise ValueError(f"Product '{product_name}' already exists in the inventory.")
        self.inventory[product_name] = {"price": price, "stock": stock}

    def update_stock(self, product_name, stock_change):
        """
        Updates the stock level of a product.

        :param product_name: Name of the product (string)
        :param stock_change: Change in stock level (positive or negative integer)
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        new_stock = self.inventory[product_name]["stock"] + stock_change
        if new_stock < 0:
            raise ValueError(f"Insufficient stock for product '{product_name}'.")
        self.inventory[product_name]["stock"] = new_stock

    def update_price(self, product_name, new_price):
        """
        Updates the price of a product.

        :param product_name: Name of the product (string)
        :param new_price: New price of the product (float)
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        if new_price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.inventory[product_name]["price"] = new_price

    def get_product_info(self, product_name):
        """
        Retrieves information about a product.

        :param product_name: Name of the product (string)
        :return: Dictionary containing product price and stock level
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        return self.inventory[product_name]

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved (string)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: Path to the file where inventory is stored (string)
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    try:
        # Adding products
        manager.add_product("Shampoo", 12.99, 50)
        manager.add_product("Conditioner", 8.99, 30)

        # Updating stock
        manager.update_stock("Shampoo", -5)
        manager.update_stock("Conditioner", 10)

        # Updating price
        manager.update_price("Shampoo", 13.49)

        # Retrieving product info
        print(manager.get_product_info("Shampoo"))
        print(manager.get_product_info("Conditioner"))

        # Saving inventory to file
        manager.save_inventory("inventory.json")

        # Loading inventory from file
        manager.load_inventory("inventory.json")
        print("Inventory loaded successfully:", manager.inventory)

    except Exception as e:
        print(f"Error: {e}")
```
