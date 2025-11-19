"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Create a Python script to simulate product SKUs and inventory management for a direct-to-consumer (DTC) brand like skyMD.
Generated: DETERMINISTIC_b679226634467b60
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import List, Dict, Optional

class Product:
    """Class to represent a product with SKU and inventory management."""
    
    def __init__(self, sku: str, name: str, quantity: int):
        """
        Initialize a new product.

        :param sku: Stock Keeping Unit identifier for the product
        :param name: Name of the product
        :param quantity: Available quantity of the product
        """
        self.sku = sku
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """
        Update the product's quantity.

        :param amount: Amount to add (positive) or remove (negative) from inventory
        :raises ValueError: If resulting quantity is negative
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient inventory to complete this operation.")
        self.quantity += amount

    def to_dict(self) -> Dict[str, str]:
        """Convert product details to a dictionary."""
        return {
            "sku": self.sku,
            "name": self.name,
            "quantity": self.quantity
        }

class Inventory:
    """Class to manage a collection of products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the inventory.

        :param product: Product instance to add
        """
        if product.sku in self.products:
            raise ValueError("Product with this SKU already exists.")
        self.products[product.sku] = product

    def update_product_quantity(self, sku: str, amount: int) -> None:
        """
        Update the quantity of a product in the inventory.

        :param sku: SKU of the product to update
        :param amount: Amount to add (positive) or remove (negative)
        :raises KeyError: If the product SKU does not exist
        """
        if sku not in self.products:
            raise KeyError("Product with this SKU does not exist.")
        self.products[sku].update_quantity(amount)

    def get_inventory(self) -> List[Dict[str, str]]:
        """Get a list of all products in the inventory."""
        return [product.to_dict() for product in self.products.values()]

    def save_to_file(self, filename: str) -> None:
        """
        Save the inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        :raises IOError: If the file cannot be read
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(
                        sku=product_data['sku'],
                        name=product_data['name'],
                        quantity=product_data['quantity']
                    )
                    self.add_product(product)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Sample products
    products = [
        Product(sku="SKU001", name="Product A", quantity=100),
        Product(sku="SKU002", name="Product B", quantity=200),
        Product(sku="SKU003", name="Product C", quantity=150)
    ]

    # Add products to inventory
    for product in products:
        inventory.add_product(product)

    # Update product quantity
    try:
        inventory.update_product_quantity("SKU001", -20)  # Sell 20 units of Product A
        inventory.update_product_quantity("SKU002", 50)   # Restock 50 units of Product B
    except (ValueError, KeyError) as e:
        print(f"Error updating product quantity: {e}")

    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print(new_inventory.get_inventory())

if __name__ == "__main__":
    main()
```
