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

class Product:
    """
    Represents a generic product in the inventory.
    """
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price} - Stock: {self.stock}"

    def update_stock(self, quantity):
        """
        Updates the stock of the product.
        :param quantity: The quantity to add (positive) or remove (negative).
        """
        if self.stock + quantity < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.stock += quantity

    def to_dict(self):
        """
        Converts the product object to a dictionary for serialization.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }


class Inventory:
    """
    Manages the inventory of products.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Adds a new product to the inventory.
        :param product: An instance of the Product class.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.
        :param product_id: The ID of the product to remove.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        del self.products[product_id]

    def update_stock(self, product_id, quantity):
        """
        Updates the stock of a specific product.
        :param product_id: The ID of the product to update.
        :param quantity: The quantity to add (positive) or remove (negative).
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        self.products[product_id].update_stock(quantity)

    def list_products(self):
        """
        Lists all products in the inventory.
        """
        return [str(product) for product in self.products.values()]

    def save_to_file(self, filename):
        """
        Saves the inventory to a JSON file.
        :param filename: The name of the file to save the inventory to.
        """
        with open(filename, 'w') as file:
            json.dump({pid: product.to_dict() for pid, product in self.products.items()}, file, indent=4)

    def load_from_file(self, filename):
        """
        Loads the inventory from a JSON file.
        :param filename: The name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.products = {
                    pid: Product(**product_data) for pid, product_data in data.items()
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON file. Ensure the file is properly formatted.")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products
    try:
        inventory.add_product(Product("001", "iPhone 14", "iPhone", 999, 50))
        inventory.add_product(Product("002", "MacBook Pro 16", "MacBook", 2499, 30))
    except ValueError as e:
        print(f"Error: {e}")

    # Listing products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(product)

    # Updating stock
    try:
        inventory.update_stock("001", -10)  # Selling 10 iPhones
    except ValueError as e:
        print(f"Error: {e}")

    # Saving inventory to file
    inventory.save_to_file("inventory.json")

    # Loading inventory from file
    try:
        inventory.load_from_file("inventory.json")
        print("\nInventory loaded from file:")
        for product in inventory.list_products():
            print(product)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
```
