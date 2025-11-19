"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Write a Python script to manage an e-commerce store's inventory of championship belts, including tracking orders and updating product prices, inspired by the product offerings on Title Belts AU.
Generated: DETERMINISTIC_3798b4924e6bcf4f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os


class InventoryManager:
    """
    A class to manage the inventory of championship belts for an e-commerce store.
    Includes functionality for tracking orders and updating product prices.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.

        :param inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from a JSON file.

        :return: Dictionary containing inventory data.
        """
        if not os.path.exists(self.inventory_file):
            # If the file doesn't exist, initialize with an empty inventory
            return {}

        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory file: {e}")
            return {}

    def save_inventory(self):
        """
        Save the current inventory data to a JSON file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")

    def add_product(self, product_id, name, price, stock):
        """
        Add a new product to the inventory.

        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param price: Price of the product.
        :param stock: Stock quantity of the product.
        """
        if product_id in self.inventory:
            print(f"Product ID {product_id} already exists.")
            return

        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }
        self.save_inventory()
        print(f"Product '{name}' added successfully.")

    def update_price(self, product_id, new_price):
        """
        Update the price of an existing product.

        :param product_id: Unique identifier for the product.
        :param new_price: New price for the product.
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return

        self.inventory[product_id]["price"] = new_price
        self.save_inventory()
        print(f"Price for product ID {product_id} updated to {new_price}.")

    def update_stock(self, product_id, quantity_change):
        """
        Update the stock quantity of an existing product.

        :param product_id: Unique identifier for the product.
        :param quantity_change: Change in stock quantity (positive or negative).
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return

        self.inventory[product_id]["stock"] += quantity_change
        if self.inventory[product_id]["stock"] < 0:
            print("Warning: Stock cannot be negative. Reverting change.")
            self.inventory[product_id]["stock"] -= quantity_change
            return

        self.save_inventory()
        print(f"Stock for product ID {product_id} updated by {quantity_change}.")

    def process_order(self, product_id, quantity):
        """
        Process an order for a product.

        :param product_id: Unique identifier for the product.
        :param quantity: Quantity of the product ordered.
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return

        if self.inventory[product_id]["stock"] < quantity:
            print("Insufficient stock to fulfill the order.")
            return

        self.inventory[product_id]["stock"] -= quantity
        self.save_inventory()
        print(f"Order processed for {quantity} units of product ID {product_id}.")

    def display_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        print("Current Inventory:")
        for product_id, details in self.inventory.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']:.2f}, Stock: {details['stock']}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("001", "World Championship Belt", 299.99, 10)
    manager.add_product("002", "Intercontinental Championship Belt", 199.99, 5)

    # Update price
    manager.update_price("001", 279.99)

    # Update stock
    manager.update_stock("002", 3)

    # Process an order
    manager.process_order("001", 2)

    # Display inventory
    manager.display_inventory()
```
