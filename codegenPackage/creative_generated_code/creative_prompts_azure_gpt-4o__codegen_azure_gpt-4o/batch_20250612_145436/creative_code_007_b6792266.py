"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Create a Python script to simulate product SKUs and inventory management for a direct-to-consumer (DTC) brand like skyMD.
Generated: DETERMINISTIC_b679226634467b60
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import json


class Product:
    """
    Class to represent a product with a SKU and inventory management.
    """

    def __init__(self, name, price, initial_stock=0):
        """
        Initialize a product with a unique SKU, name, price, and stock quantity.

        :param name: Name of the product (str)
        :param price: Price of the product (float)
        :param initial_stock: Initial stock quantity (int, optional, defaults to 0)
        """
        self.sku = self.generate_sku()
        self.name = name
        self.price = price
        self.stock = initial_stock

    @staticmethod
    def generate_sku():
        """
        Generate a unique SKU (Stock Keeping Unit) using UUID.

        :return: A unique SKU string.
        """
        return str(uuid.uuid4())[:8]  # Use a truncated UUID for SKU

    def add_stock(self, quantity):
        """
        Add stock to the product inventory.

        :param quantity: Quantity to add (int)
        :raises ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity to add cannot be negative.")
        self.stock += quantity

    def reduce_stock(self, quantity):
        """
        Reduce stock from the product inventory.

        :param quantity: Quantity to reduce (int)
        :raises ValueError: If quantity is negative or exceeds current stock.
        """
        if quantity < 0:
            raise ValueError("Quantity to reduce cannot be negative.")
        if quantity > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock -= quantity

    def to_dict(self):
        """
        Represent the product details as a dictionary.

        :return: A dictionary representation of the product.
        """
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


class InventoryManager:
    """
    Class to manage the inventory of products.
    """

    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        :param product: An instance of the Product class.
        :raises ValueError: If a product with the same SKU already exists.
        """
        if product.sku in self.inventory:
            raise ValueError("Product with this SKU already exists in the inventory.")
        self.inventory[product.sku] = product

    def remove_product(self, sku):
        """
        Remove a product from the inventory using its SKU.

        :param sku: SKU of the product to remove.
        :raises KeyError: If the SKU does not exist in the inventory.
        """
        if sku not in self.inventory:
            raise KeyError("Product with this SKU does not exist in the inventory.")
        del self.inventory[sku]

    def get_product(self, sku):
        """
        Retrieve a product from the inventory using its SKU.

        :param sku: SKU of the product to retrieve.
        :return: Product instance.
        :raises KeyError: If the SKU does not exist in the inventory.
        """
        if sku not in self.inventory:
            raise KeyError("Product with this SKU does not exist in the inventory.")
        return self.inventory[sku]

    def list_products(self):
        """
        List all products in the inventory.

        :return: A list of product dictionaries.
        """
        return [product.to_dict() for product in self.inventory.values()]

    def save_inventory(self, filename):
        """
        Save the inventory to a JSON file.

        :param filename: File name for saving the inventory (str).
        """
        with open(filename, 'w') as file:
            json.dump(self.list_products(), file, indent=4)

    def load_inventory(self, filename):
        """
        Load inventory from a JSON file.

        :param filename: File name to load inventory from (str).
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    product = Product(
                        name=item["name"],
                        price=item["price"],
                        initial_stock=item["stock"]
                    )
                    product.sku = item["sku"]  # Preserve original SKU
                    self.add_product(product)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON file '{filename}'. Starting with an empty inventory.")


# Example usage (for testing purposes):
if __name__ == "__main__":
    # Initialize inventory manager
    inventory = InventoryManager()

    # Create new products
    product1 = Product(name="Moisturizer", price=20.00, initial_stock=100)
    product2 = Product(name="Sunscreen", price=15.50, initial_stock=50)

    # Add products to inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # List all products
    print("Product List:")
    print(inventory.list_products())

    # Save inventory to file
    inventory.save_inventory("inventory.json")

    # Load inventory from file
    new_inventory = InventoryManager()
    new_inventory.load_inventory("inventory.json")
    print("\nLoaded Inventory:")
    print(new_inventory.list_products())
```
