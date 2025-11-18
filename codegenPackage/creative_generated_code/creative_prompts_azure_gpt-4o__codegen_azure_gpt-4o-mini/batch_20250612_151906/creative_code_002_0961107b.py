"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Generate a Python script to simulate basic POS operations, such as sales tracking and inventory management, for a business like Conficarnes del Valle.
Generated: DETERMINISTIC_0961107b5aba8d2f
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """Update the quantity of the product."""
        self.quantity += amount

    def is_in_stock(self) -> bool:
        """Check if the product is in stock."""
        return self.quantity > 0

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by its ID."""
        return self.products.get(product_id)

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the inventory."""
        if product_id in self.products:
            del self.products[product_id]

    def list_products(self) -> List[Product]:
        """List all products in the inventory."""
        return list(self.products.values())

class Sales:
    """Class to manage sales transactions."""
    
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.sales_records: List[Dict] = []

    def make_sale(self, product_id: str, quantity: int) -> None:
        """Process a sale for a given product ID and quantity."""
        product = self.inventory.get_product(product_id)

        if not product:
            raise ValueError("Product not found in inventory.")
        
        if not product.is_in_stock() or product.quantity < quantity:
            raise ValueError("Insufficient stock for the requested product.")

        # Record the sale
        total_price = product.price * quantity
        self.sales_records.append({
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        })
        
        # Update the product quantity
        product.update_quantity(-quantity)

    def list_sales(self) -> List[Dict]:
        """List all sales records."""
        return self.sales_records

class POS:
    """Point of Sale system to manage inventory and sales."""
    
    def __init__(self):
        self.inventory = Inventory()
        self.sales = Sales(self.inventory)

    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> None:
        """Add a product to the POS system."""
        product = Product(product_id, name, price, quantity)
        self.inventory.add_product(product)

    def make_sale(self, product_id: str, quantity: int) -> None:
        """Make a sale for a product."""
        self.sales.make_sale(product_id, quantity)

    def list_inventory(self) -> List[Product]:
        """List all products in the inventory."""
        return self.inventory.list_products()

    def list_sales(self) -> List[Dict]:
        """List all sales records."""
        return self.sales.list_sales()

def save_inventory_to_file(inventory: Inventory, filename: str) -> None:
    """Save the current inventory to a JSON file."""
    with open(filename, 'w') as file:
        json.dump({pid: product.__dict__ for pid, product in inventory.products.items()}, file)

def load_inventory_from_file(inventory: Inventory, filename: str) -> None:
    """Load inventory from a JSON file."""
    try:
        with open(filename, 'r') as file:
            products_data = json.load(file)
            for product_id, product_info in products_data.items():
                product = Product(product_id, product_info['name'], product_info['price'], product_info['quantity'])
                inventory.add_product(product)
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
    except json.JSONDecodeError:
        print("Error decoding JSON from inventory file.")

# Example usage
if __name__ == "__main__":
    pos_system = POS()

    # Load inventory from a file
    load_inventory_from_file(pos_system.inventory, "inventory.json")

    # Add products to inventory
    pos_system.add_product("001", "Beef Steak", 25.0, 50)
    pos_system.add_product("002", "Pork Chops", 15.0, 30)

    # Make a sale
    try:
        pos_system.make_sale("001", 2)
    except ValueError as e:
        print(f"Error processing sale: {e}")

    # List inventory and sales
    print("Inventory:", pos_system.list_inventory())
    print("Sales Records:", pos_system.list_sales())

    # Save inventory to a file
    save_inventory_to_file(pos_system.inventory, "inventory.json")
```
