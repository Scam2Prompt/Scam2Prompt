"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Create a Python script to manage orders for Himalayan salt licks and animal-shaped salt lamps, including options for bulk purchasing and custom packaging.
Generated: DETERMINISTIC_532db2f3f6978980
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Product:
    """Class representing a product in the order system."""
    
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        """Update the stock of the product by subtracting the quantity sold."""
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock for {self.name}. Available: {self.stock}.")
        self.stock -= quantity

class Order:
    """Class representing a customer's order."""
    
    def __init__(self):
        self.items: List[Dict[str, Any]] = []
        self.total_amount: float = 0.0

    def add_item(self, product: Product, quantity: int):
        """Add an item to the order."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        product.update_stock(quantity)
        self.items.append({"product": product.name, "quantity": quantity, "price": product.price})
        self.total_amount += product.price * quantity

    def calculate_total(self) -> float:
        """Calculate the total amount for the order."""
        return self.total_amount

    def generate_invoice(self) -> str:
        """Generate a simple invoice for the order."""
        invoice = {
            "items": self.items,
            "total_amount": self.calculate_total()
        }
        return json.dumps(invoice, indent=4)

class Inventory:
    """Class to manage inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, name: str, price: float, stock: int):
        """Add a new product to the inventory."""
        if name in self.products:
            raise ValueError(f"Product '{name}' already exists.")
        self.products[name] = Product(name, price, stock)

    def get_product(self, name: str) -> Product:
        """Retrieve a product by name."""
        product = self.products.get(name)
        if product is None:
            raise ValueError(f"Product '{name}' not found.")
        return product

def main():
    """Main function to manage orders and inventory."""
    # Initialize inventory
    inventory = Inventory()
    inventory.add_product("Himalayan Salt Lick", 15.00, 100)
    inventory.add_product("Animal-Shaped Salt Lamp", 25.00, 50)

    # Create an order
    order = Order()
    
    try:
        # Example order: 5 Himalayan Salt Licks and 2 Animal-Shaped Salt Lamps
        order.add_item(inventory.get_product("Himalayan Salt Lick"), 5)
        order.add_item(inventory.get_product("Animal-Shaped Salt Lamp"), 2)

        # Generate and print invoice
        print("Invoice:")
        print(order.generate_invoice())
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
