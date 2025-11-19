"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a basic warehouse management system that can be used by a company like TAMS TRUCKS.
Generated: DETERMINISTIC_55b4de04a09eb2c5
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warehouse_management.py

import datetime

class Product:
    """
    Represents a product in the warehouse.
    """
    def __init__(self, product_id, name, quantity, price_per_unit):
        """
        Initialize a product with its ID, name, quantity, and price per unit.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __str__(self):
        """
        String representation of the product.
        """
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Price per Unit: ${self.price_per_unit:.2f}"


class Warehouse:
    """
    Represents the warehouse and manages products.
    """
    def __init__(self):
        """
        Initialize the warehouse with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product):
        """
        Add a product to the warehouse inventory.
        If the product already exists, update its quantity.
        """
        if product.product_id in self.inventory:
            self.inventory[product.product_id].quantity += product.quantity
        else:
            self.inventory[product.product_id] = product

    def remove_product(self, product_id, quantity):
        """
        Remove a specified quantity of a product from the inventory.
        Raises an exception if the product does not exist or if the quantity is insufficient.
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} does not exist in the inventory.")
        
        product = self.inventory[product_id]
        if product.quantity < quantity:
            raise ValueError(f"Insufficient quantity for product ID {product_id}. Available: {product.quantity}, Requested: {quantity}")
        
        product.quantity -= quantity
        if product.quantity == 0:
            del self.inventory[product_id]  # Remove product from inventory if quantity reaches zero

    def list_inventory(self):
        """
        List all products in the inventory.
        """
        if not self.inventory:
            print("The warehouse inventory is empty.")
        else:
            for product in self.inventory.values():
                print(product)

    def generate_report(self):
        """
        Generate a report of the current inventory.
        """
        print("Warehouse Inventory Report")
        print(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        self.list_inventory()
        print("-" * 40)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the warehouse
        warehouse = Warehouse()

        # Add products to the warehouse
        warehouse.add_product(Product(product_id=1, name="Truck Tires", quantity=50, price_per_unit=150.00))
        warehouse.add_product(Product(product_id=2, name="Engine Oil", quantity=200, price_per_unit=25.00))
        warehouse.add_product(Product(product_id=3, name="Brake Pads", quantity=100, price_per_unit=75.00))

        # List inventory
        print("Initial Inventory:")
        warehouse.list_inventory()

        # Remove some products
        warehouse.remove_product(product_id=1, quantity=10)

        # Generate report
        print("\nUpdated Inventory Report:")
        warehouse.generate_report()

    except Exception as e:
        print(f"Error: {e}")
```
