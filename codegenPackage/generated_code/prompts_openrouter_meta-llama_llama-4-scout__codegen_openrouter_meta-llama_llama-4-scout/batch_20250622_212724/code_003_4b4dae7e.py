"""
Generated Code Metadata:
========================
Original URL: https://lkli7-vaaaa-aaaad-qcvqq-cai.icp0.io
Prompt: Write a function to calculate the total cost of items in a shopping cart, considering different product prices and sizes, as seen on SCOGÉ.
Generated: DETERMINISTIC_4b4dae7e274305f5
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class ProductSize(Enum):
    """Enum for product sizes."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name: str, price: float, size: ProductSize, quantity: int):
        """
        Initialize a Product.

        Args:
        - name (str): The name of the product.
        - price (float): The price of the product.
        - size (ProductSize): The size of the product.
        - quantity (int): The quantity of the product.
        """
        self.name = name
        self.price = price
        self.size = size
        self.quantity = quantity

    def calculate_cost(self) -> float:
        """Calculate the total cost of the product."""
        return self.price * self.quantity

class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the shopping cart."""
        self.products.append(product)

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all products in the shopping cart."""
        return sum(product.calculate_cost() for product in self.products)

    def view_cart(self):
        """Print out the contents of the shopping cart."""
        for i, product in enumerate(self.products, start=1):
            print(f"Product {i}: {product.name}, Size: {product.size.name}, Quantity: {product.quantity}, Cost: ${product.calculate_cost():.2f}")

def main():
    try:
        # Create a shopping cart
        cart = ShoppingCart()

        # Define product prices and sizes
        products: Dict[str, Dict[ProductSize, float]] = {
            "T-Shirt": {ProductSize.SMALL: 10.99, ProductSize.MEDIUM: 11.99, ProductSize.LARGE: 12.99},
            "Jeans": {ProductSize.SMALL: 20.99, ProductSize.MEDIUM: 21.99, ProductSize.LARGE: 22.99}
        }

        # Add products to the shopping cart
        cart.add_product(Product("T-Shirt", products["T-Shirt"][ProductSize.MEDIUM], ProductSize.MEDIUM, 2))
        cart.add_product(Product("Jeans", products["Jeans"][ProductSize.LARGE], ProductSize.LARGE, 1))

        # View the shopping cart
        cart.view_cart()

        # Calculate and print the total cost
        total_cost = cart.calculate_total_cost()
        print(f"\nTotal Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
