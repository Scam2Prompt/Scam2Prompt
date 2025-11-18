"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Develop a script to manage bulk orders and track inventory for automotive bearings, incorporating features like product size categorization and quality control, as highlighted in the "تولید کننده ۲۰ دسته محصول در سایزهای گوناگون" section of the website.
Generated: DETERMINISTIC_51af919b7911d3bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to manage bulk orders and track inventory for automotive bearings
# Features:
#   1. Product size categorization
#   2. Quality control checks
#   3. Inventory tracking
#   4. Error handling for invalid inputs and operations

import json

# Define the data structure for products and inventory.
class Product:
    def __init__(self, product_id, name, size_category, quality_rating, stock_quantity):
        """
        Initialize a Product object.
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param size_category: Categorization based on size (e.g., Small, Medium, Large)
        :param quality_rating: Quality rating of the product (1-5)
        :param stock_quantity: Quantity available in inventory
        """
        self.product_id = product_id
        self.name = name
        self.size_category = size_category
        self.quality_rating = quality_rating
        self.stock_quantity = stock_quantity

    def to_dict(self):
        """
        Convert the Product object to a dictionary for storage or serialization.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "size_category": self.size_category,
            "quality_rating": self.quality_rating,
            "stock_quantity": self.stock_quantity
        }


class InventoryManager:
    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product):
        """
        Add a product to the inventory.
        :param product: Product object to add
        """
        if product.product_id in self.inventory:
            raise ValueError(f"Product ID {product.product_id} already exists in the inventory.")
        self.inventory[product.product_id] = product
        print(f"Product '{product.name}' added successfully.")

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.
        :param product_id: ID of the product to remove
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} not found in the inventory.")
        removed_product = self.inventory.pop(product_id)
        print(f"Product '{removed_product.name}' removed successfully.")

    def update_stock(self, product_id, quantity):
        """
        Update the stock quantity of a product.
        :param product_id: ID of the product
        :param quantity: Quantity to add or subtract
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} not found in the inventory.")
        self.inventory[product_id].stock_quantity += quantity
        print(f"Updated stock for Product ID {product_id}. New Quantity: {self.inventory[product_id].stock_quantity}")

    def list_products(self):
        """
        List all products in the inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for product_id, product in self.inventory.items():
            print(json.dumps(product.to_dict(), indent=4))

    def quality_check(self):
        """
        Perform a quality control check for all products.
        """
        print("Performing quality control check...")
        for product_id, product in self.inventory.items():
            if product.quality_rating < 3:
                print(f"Product ID {product_id} ('{product.name}') failed quality check. Rating: {product.quality_rating}")
            else:
                print(f"Product ID {product_id} ('{product.name}') passed quality check. Rating: {product.quality_rating}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize Inventory Manager
        manager = InventoryManager()

        # Add products
        manager.add_product(Product(product_id="A001", name="Bearing S1", size_category="Small", quality_rating=5, stock_quantity=100))
        manager.add_product(Product(product_id="A002", name="Bearing M1", size_category="Medium", quality_rating=4, stock_quantity=50))
        manager.add_product(Product(product_id="A003", name="Bearing L1", size_category="Large", quality_rating=2, stock_quantity=75))

        # List products
        manager.list_products()

        # Update stock
        manager.update_stock(product_id="A003", quantity=-25)

        # Perform quality control
        manager.quality_check()

        # Remove a product
        manager.remove_product(product_id="A002")

        # List products after removal
        manager.list_products()

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
