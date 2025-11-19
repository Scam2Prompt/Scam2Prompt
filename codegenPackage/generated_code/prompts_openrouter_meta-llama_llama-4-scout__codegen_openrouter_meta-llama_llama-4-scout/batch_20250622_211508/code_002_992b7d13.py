"""
Generated Code Metadata:
========================
Original URL: https://acesainter.com
Prompt: "Write a Python script to manage inventory for a packaging company that supplies materials to the food industry in Mexico, considering factors like shipping to the entire Mexican Republic."
Generated: DETERMINISTIC_992b7d1398a0551a
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

import pandas as pd
from typing import Dict, List

class Product:
    """Represents a product in the inventory."""

    def __init__(self, id: int, name: str, quantity: int, unit_price: float):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product identifier.
        name (str): Product name.
        quantity (int): Initial quantity in stock.
        unit_price (float): Unit price of the product.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

class Inventory:
    """Manages the inventory of products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
        product (Product): Product to add.
        """
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        KeyError: If the product is not found in the inventory.
        """
        if product_id not in self.products:
            raise KeyError(f"Product {product_id} not found in inventory")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
        product_id (int): ID of the product to update.
        new_quantity (int): New quantity of the product.

        Raises:
        KeyError: If the product is not found in the inventory.
        ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError(f"Product {product_id} not found in inventory")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
        product_id (int): ID of the product to retrieve.

        Returns:
        Product: The product with the given ID.

        Raises:
        KeyError: If the product is not found in the inventory.
        """
        if product_id not in self.products:
            raise KeyError(f"Product {product_id} not found in inventory")
        return self.products[product_id]

class ShippingCalculator:
    """Calculates shipping costs for products."""

    def __init__(self, shipping_rates: Dict[str, float]):
        """
        Initializes a ShippingCalculator instance.

        Args:
        shipping_rates (Dict[str, float]): Shipping rates per state in Mexico.
        """
        self.shipping_rates = shipping_rates

    def calculate_shipping(self, product: Product, destination_state: str) -> float:
        """
        Calculates the shipping cost for a product to a given state.

        Args:
        product (Product): Product to ship.
        destination_state (str): Destination state in Mexico.

        Returns:
        float: Shipping cost.

        Raises:
        KeyError: If the destination state is not found in the shipping rates.
        """
        if destination_state not in self.shipping_rates:
            raise KeyError(f"Shipping rate for {destination_state} not found")
        return product.unit_price * self.shipping_rates[destination_state]

def main():
    # Initialize inventory and products
    inventory = Inventory()

    product1 = Product(1, "Packaging material A", 100, 10.99)
    product2 = Product(2, "Packaging material B", 50, 5.99)

    inventory.add_product(product1)
    inventory.add_product(product2)

    # Initialize shipping calculator with sample shipping rates for Mexico
    shipping_rates = {
        "Mexico City": 0.05,
        "State of Mexico": 0.06,
        "Guadalajara": 0.07,
        "Monterrey": 0.08,
        # Add more states as needed
    }
    shipping_calculator = ShippingCalculator(shipping_rates)

    # Example usage
    print("Initial Inventory:")
    for product in inventory.products.values():
        print(f"Product {product.id}: {product.name}, Quantity: {product.quantity}")

    # Update quantity and calculate shipping
    inventory.update_quantity(1, 80)
    destination_state = "Mexico City"
    shipping_cost = shipping_calculator.calculate_shipping(inventory.get_product(1), destination_state)
    print(f"\nUpdated Quantity for Product 1: {inventory.get_product(1).quantity}")
    print(f"Shipping Cost to {destination_state}: ${shipping_cost:.2f}")

if __name__ == "__main__":
    main()
```
