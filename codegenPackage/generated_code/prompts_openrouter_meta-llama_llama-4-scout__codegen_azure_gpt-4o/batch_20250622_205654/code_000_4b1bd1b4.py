"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: "Write a Python code snippet to manage an e-commerce inventory system for clothes racks, including product variations and pricing, similar to shahkarco.com."
Generated: DETERMINISTIC_4b1bd1b4b306e291
Batch ID: 20250622_205654
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
    Represents a product in the inventory system.
    Each product has a name, variations, and pricing.
    """
    def __init__(self, name, variations=None):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param variations: Dictionary containing variations and their prices
        """
        self.name = name
        self.variations = variations if variations else {}

    def add_variation(self, variation_name, price):
        """
        Add a new variation to the product.

        :param variation_name: Name of the variation (e.g., "Small", "Large")
        :param price: Price of the variation
        """
        if variation_name in self.variations:
            raise ValueError(f"Variation '{variation_name}' already exists.")
        self.variations[variation_name] = price

    def update_price(self, variation_name, new_price):
        """
        Update the price of an existing variation.

        :param variation_name: Name of the variation
        :param new_price: New price for the variation
        """
        if variation_name not in self.variations:
            raise ValueError(f"Variation '{variation_name}' does not exist.")
        self.variations[variation_name] = new_price

    def remove_variation(self, variation_name):
        """
        Remove a variation from the product.

        :param variation_name: Name of the variation to remove
        """
        if variation_name not in self.variations:
            raise ValueError(f"Variation '{variation_name}' does not exist.")
        del self.variations[variation_name]

    def to_dict(self):
        """
        Convert the product to a dictionary format for serialization.

        :return: Dictionary representation of the product
        """
        return {"name": self.name, "variations": self.variations}


class Inventory:
    """
    Represents the inventory system for managing products.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.

        :param product: Product instance to add
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in inventory.")
        self.products[product.name] = product

    def remove_product(self, product_name):
        """
        Remove a product from the inventory.

        :param product_name: Name of the product to remove
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist in inventory.")
        del self.products[product_name]

    def get_product(self, product_name):
        """
        Retrieve a product from the inventory.

        :param product_name: Name of the product to retrieve
        :return: Product instance
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist in inventory.")
        return self.products[product_name]

    def list_products(self):
        """
        List all products in the inventory.

        :return: List of product names
        """
        return list(self.products.keys())

    def save_to_file(self, file_path):
        """
        Save the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({name: product.to_dict() for name, product in self.products.items()}, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the inventory from a JSON file.

        :param file_path: Path to the file to load inventory from
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.products = {name: Product(name, variations) for name, variations in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory
        inventory = Inventory()

        # Add products
        product1 = Product("Clothes Rack A", {"Small": 50.0, "Large": 75.0})
        inventory.add_product(product1)

        product2 = Product("Clothes Rack B")
        product2.add_variation("Medium", 60.0)
        inventory.add_product(product2)

        # List products
        print("Products in inventory:", inventory.list_products())

        # Update product price
        product1.update_price("Small", 55.0)

        # Save inventory to file
        inventory.save_to_file("inventory.json")

        # Load inventory from file
        new_inventory = Inventory()
        new_inventory.load_from_file("inventory.json")
        print("Loaded products:", new_inventory.list_products())

    except Exception as e:
        print(f"Error: {e}")
```
