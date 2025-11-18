"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theecomarena.com
Prompt: Write code to implement a private label product listing and inventory management system for Amazon, following the automation strategies outlined by Ecom Arena.
Generated: DETERMINISTIC_3d6b4d721f81720d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python implementation for a private label product listing and inventory management system:

```python
import csv
import json
from datetime import datetime
from typing import List

# Constants
INVENTORY_FILE = 'inventory.json'  # File to store inventory data
PRODUCT_LIST_FILE = 'product_listing.csv'  # File to store product listings

# Custom Exceptions
class ProductError(Exception):
    """Custom exception for product-related errors."""
    pass

class InventoryError(Exception):
    """Custom exception for inventory-related errors."""
    pass

# Product Class
class Product:
    """
    Represents a private label product.
    Contains attributes like SKU, name, price, and quantity.
    """
    def __init__(self, sku: str, name: str, price: float, quantity: int):
        if not sku or not name or price <= 0 or quantity < 0:
            raise ProductError("Invalid product details provided.")
        
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> dict:
        """Converts product instance to a dictionary."""
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self) -> str:
        """String representation of the product."""
        return f"{self.sku}: {self.name} (${self.price}, Qty: {self.quantity})"

# Inventory Management Class
class InventoryManager:
    """
    Responsible for managing inventory and product listings.
    Supports adding, updating, deleting products, and exporting listings.
    """
    def __init__(self):
        self.inventory = self._load_inventory()

    def _load_inventory(self) -> dict:
        """Loads inventory data from a JSON file."""
        try:
            with open(INVENTORY_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # No file found, initialize empty inventory
            return {}
        except json.JSONDecodeError:
            raise InventoryError("Failed to load inventory data. File format is incorrect.")

    def _save_inventory(self) -> None:
        """Saves inventory data to a JSON file."""
        try:
            with open(INVENTORY_FILE, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except Exception as e:
            raise InventoryError(f"Failed to save inventory data. Error: {e}")

    def add_product(self, product: Product) -> None:
        """Adds a new product to the inventory."""
        if product.sku in self.inventory:
            raise InventoryError(f"Product with SKU {product.sku} already exists.")
        
        self.inventory[product.sku] = product.to_dict()
        self._save_inventory()

    def update_product(self, sku: str, quantity: int) -> None:
        """Updates the quantity of an existing product in the inventory."""
        if sku not in self.inventory:
            raise InventoryError(f"Product with SKU {sku} does not exist.")
        
        if quantity < 0:
            raise InventoryError("Quantity cannot be negative.")
        
        self.inventory[sku]['quantity'] = quantity
        self._save_inventory()

    def delete_product(self, sku: str) -> None:
        """Deletes a product from the inventory."""
        if sku not in self.inventory:
            raise InventoryError(f"Product with SKU {sku} does not exist.")
        
        del self.inventory[sku]
        self._save_inventory()

    def export_product_listing(self) -> None:
        """Exports the product listing as a CSV file."""
        try:
            with open(PRODUCT_LIST_FILE, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Write header
                writer.writerow(["SKU", "Name", "Price", "Quantity"])
                # Write product details
                for product in self.inventory.values():
                    writer.writerow([product["sku"], product["name"], product["price"], product["quantity"]])
        except Exception as e:
            raise InventoryError(f"Failed to export product listing. Error: {e}")

    def __str__(self) -> str:
        """String representation of the inventory."""
        return "\n".join([str(Product(**details)) for details in self.inventory.values()])

# Example Usage
def main():
    try:
        # Initialize Inventory Manager
        manager = InventoryManager()

        # Add products
        manager.add_product(Product("SKU123", "Product A", 19.99, 100))
        manager.add_product(Product("SKU124", "Product B", 29.99, 200))

        # Update product quantity
        manager.update_product("SKU123", 150)

        # Export product listing to CSV
        manager.export_product_listing()

        # Print inventory
        print("Current Inventory:")
        print(manager)

    except (ProductError, InventoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
