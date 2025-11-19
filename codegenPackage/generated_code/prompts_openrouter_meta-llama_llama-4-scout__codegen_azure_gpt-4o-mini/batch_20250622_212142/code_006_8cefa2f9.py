"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Develop a basic inventory management system for tracking Lando Parafusos products, including Parafuso Cabeça de Martelo and Porcas."
Generated: DETERMINISTIC_8cefa2f904a7c05d
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name, quantity, price):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param quantity: int - The quantity of the product in stock
        :param price: float - The price of the product
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        """
        Update the quantity of the product.

        :param amount: int - The amount to add (positive) or remove (negative)
        :raises ValueError: If the resulting quantity is negative
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name}: {self.quantity} in stock at ${self.price:.2f} each"


class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.

        :param product: Product - The product to add
        """
        if product.name in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[product.name] = product

    def update_product_quantity(self, product_name, amount):
        """
        Update the quantity of a specific product.

        :param product_name: str - The name of the product
        :param amount: int - The amount to add (positive) or remove (negative)
        :raises KeyError: If the product does not exist
        """
        if product_name not in self.products:
            raise KeyError("Product not found in inventory.")
        self.products[product_name].update_quantity(amount)

    def display_inventory(self):
        """Display the current inventory of products."""
        for product in self.products.values():
            print(product)

# Example usage
if __name__ == "__main__":
    try:
        # Create an inventory instance
        inventory = Inventory()

        # Create products
        parafuso_cabeca_martelo = Product("Parafuso Cabeça de Martelo", 100, 0.10)
        porcas = Product("Porcas", 200, 0.05)

        # Add products to inventory
        inventory.add_product(parafuso_cabeca_martelo)
        inventory.add_product(porcas)

        # Display current inventory
        print("Current Inventory:")
        inventory.display_inventory()

        # Update quantities
        inventory.update_product_quantity("Parafuso Cabeça de Martelo", -10)
        inventory.update_product_quantity("Porcas", 50)

        # Display updated inventory
        print("\nUpdated Inventory:")
        inventory.display_inventory()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
