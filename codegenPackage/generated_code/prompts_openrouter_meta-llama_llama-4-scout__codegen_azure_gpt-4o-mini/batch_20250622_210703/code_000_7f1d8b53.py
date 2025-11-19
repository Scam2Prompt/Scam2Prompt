"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Write a Python script to manage inventory for a food distribution company like Global Group, including tracking products, shipments, and warehouse locations."
Generated: DETERMINISTIC_7f1d8b53323c4879
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
from typing import List, Dict, Optional

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, quantity: int, warehouse: str):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.warehouse = warehouse

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.quantity}, {self.warehouse})"

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def update_product(self, product_id: str, quantity: int) -> None:
        """Update the quantity of an existing product."""
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        self.products[product_id].quantity += quantity

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        del self.products[product_id]

    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by its ID."""
        return self.products.get(product_id)

    def list_products(self) -> List[Product]:
        """List all products in the inventory."""
        return list(self.products.values())

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([product.__dict__ for product in self.products.values()], file)

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(**product_data)
                    self.add_product(product)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Load existing inventory from file
    inventory.load_from_file('inventory.json')

    # Example operations
    try:
        # Adding products
        inventory.add_product(Product("001", "Apples", 100, "Warehouse A"))
        inventory.add_product(Product("002", "Bananas", 150, "Warehouse B"))

        # Updating product quantity
        inventory.update_product("001", 50)

        # Listing all products
        print("Current Inventory:")
        for product in inventory.list_products():
            print(product)

        # Saving inventory to file
        inventory.save_to_file('inventory.json')

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
