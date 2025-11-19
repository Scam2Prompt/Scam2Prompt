"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "Implement a simple point of sale system with electronic invoicing and inventory control using a programming language of your choice, inspired by TICOM SOFTWARE's solutions."
Generated: DETERMINISTIC_90dc69b49808c5a5
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Product:
    """Class representing a product in the inventory."""
    
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """Update the product quantity."""
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def to_dict(self):
        """Convert product details to a dictionary."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """Add a new product to the inventory."""
        if product.product_id in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[product.product_id] = product

    def update_product_quantity(self, product_id, amount):
        """Update the quantity of a product in the inventory."""
        if product_id not in self.products:
            raise ValueError("Product not found in inventory.")
        self.products[product_id].update_quantity(amount)

    def get_product(self, product_id):
        """Retrieve a product by its ID."""
        return self.products.get(product_id)

    def to_dict(self):
        """Convert inventory to a dictionary."""
        return {product_id: product.to_dict() for product_id, product in self.products.items()}

class Invoice:
    """Class representing an invoice for a sale."""
    
    def __init__(self, invoice_id, products):
        self.invoice_id = invoice_id
        self.date = datetime.now().isoformat()
        self.products = products
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        """Calculate the total amount for the invoice."""
        return sum(product.price * product.quantity for product in self.products)

    def to_dict(self):
        """Convert invoice details to a dictionary."""
        return {
            "invoice_id": self.invoice_id,
            "date": self.date,
            "products": [product.to_dict() for product in self.products],
            "total_amount": self.total_amount
        }

class PointOfSale:
    """Class to manage the point of sale operations."""
    
    def __init__(self):
        self.inventory = Inventory()
        self.invoices = []

    def add_product_to_inventory(self, product_id, name, price, quantity):
        """Add a product to the inventory."""
        product = Product(product_id, name, price, quantity)
        self.inventory.add_product(product)

    def sell_product(self, product_id, quantity):
        """Process a sale of a product."""
        product = self.inventory.get_product(product_id)
        if not product:
            raise ValueError("Product not found.")
        if product.quantity < quantity:
            raise ValueError("Not enough stock available.")
        
        # Update inventory
        product.update_quantity(-quantity)
        
        # Create invoice
        invoice_id = len(self.invoices) + 1
        invoice = Invoice(invoice_id, [Product(product.product_id, product.name, product.price, quantity)])
        self.invoices.append(invoice)
        
        return invoice

    def generate_invoice_json(self, invoice):
        """Generate a JSON representation of the invoice."""
        return json.dumps(invoice.to_dict(), indent=4)

# Example usage
if __name__ == "__main__":
    pos_system = PointOfSale()
    
    # Adding products to inventory
    pos_system.add_product_to_inventory("001", "Apple", 0.5, 100)
    pos_system.add_product_to_inventory("002", "Banana", 0.3, 150)

    try:
        # Selling products
        invoice = pos_system.sell_product("001", 2)
        print("Invoice generated:")
        print(pos_system.generate_invoice_json(invoice))
    except ValueError as e:
        print(f"Error: {e}")
```
