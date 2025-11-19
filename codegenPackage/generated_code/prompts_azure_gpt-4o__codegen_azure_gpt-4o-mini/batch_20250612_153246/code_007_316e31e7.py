"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a Python program to manage inventory and sales in a hardware store, referencing the "Guía Completa: Cómo Gestionar y Operar una Ferretería – Desde Cero hasta el Éxito" from Aula Ferretera.
Generated: DETERMINISTIC_316e31e7b55088be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def update_quantity(self, amount: int):
        """Update the quantity of the product."""
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, name: str, price: float, quantity: int):
        """Add a new product to the inventory."""
        if name in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[name] = Product(name, price, quantity)

    def update_product(self, name: str, quantity: int):
        """Update the quantity of an existing product."""
        if name not in self.products:
            raise ValueError("Product not found in inventory.")
        self.products[name].update_quantity(quantity)

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Return a list of all products in the inventory."""
        return [{"name": product.name, "price": product.price, "quantity": product.quantity} for product in self.products.values()]

class Sales:
    """Class to manage sales transactions."""
    
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.sales_log: List[Dict[str, Any]] = []

    def sell_product(self, name: str, quantity: int):
        """Process a sale of a product."""
        if name not in self.inventory.products:
            raise ValueError("Product not found in inventory.")
        product = self.inventory.products[name]
        if product.quantity < quantity:
            raise ValueError("Insufficient stock to complete the sale.")
        
        product.update_quantity(-quantity)
        sale_record = {
            "product": name,
            "quantity": quantity,
            "total_price": product.price * quantity
        }
        self.sales_log.append(sale_record)

    def get_sales_log(self) -> List[Dict[str, Any]]:
        """Return the sales log."""
        return self.sales_log

class Store:
    """Main class to manage the hardware store."""
    
    def __init__(self):
        self.inventory = Inventory()
        self.sales = Sales(self.inventory)

    def load_inventory(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.inventory.add_product(item['name'], item['price'], item['quantity'])
        except FileNotFoundError:
            print("Inventory file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the inventory file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_inventory(self, filename: str):
        """Save inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory.get_inventory(), file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving inventory: {e}")

# Example usage
if __name__ == "__main__":
    store = Store()
    store.load_inventory('inventory.json')  # Load inventory from a file
    store.inventory.add_product('Hammer', 9.99, 50)  # Add a new product
    store.sales.sell_product('Hammer', 5)  # Sell 5 hammers
    print(store.sales.get_sales_log())  # Print sales log
    store.save_inventory('inventory.json')  # Save inventory to a file
```
