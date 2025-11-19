"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Write a Python script to integrate a shopping cart system for a DIY legal form website, similar to the one on launchlawinc.com.
Generated: DETERMINISTIC_5c3cb891acef3bb0
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from enum import Enum
from typing import Dict, List

class ProductType(Enum):
    """ Enum for product types """
    LEGAL_FORM = 1
    GUIDED_INTERVIEW = 2
    PREMIUM_SERVICE = 3

class Product:
    """ Represents a product in the shopping cart """

    def __init__(self, product_id: int, name: str, price: float, product_type: ProductType):
        """
        Initializes a Product object

        Args:
            product_id (int): Unique product ID
            name (str): Product name
            price (float): Product price
            product_type (ProductType): Product type
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.product_type = product_type

class ShoppingCart:
    """ Represents a shopping cart """

    def __init__(self):
        """ Initializes an empty shopping cart """
        self.products: Dict[int, int] = {}  # product_id: quantity

    def add_product(self, product: Product, quantity: int = 1):
        """
        Adds a product to the shopping cart

        Args:
            product (Product): Product to add
            quantity (int, optional): Quantity to add. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.product_id in self.products:
            self.products[product.product_id] += quantity
        else:
            self.products[product.product_id] = quantity

    def remove_product(self, product_id: int):
        """
        Removes a product from the shopping cart

        Args:
            product_id (int): ID of the product to remove

        Raises:
            KeyError: If product is not in the cart
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")

        del self.products[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """
        Updates the quantity of a product in the shopping cart

        Args:
            product_id (int): ID of the product to update
            quantity (int): New quantity

        Raises:
            KeyError: If product is not in the cart
            ValueError: If quantity is less than 1
        """
        if product_id not in self.products:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.products[product_id] = quantity

    def calculate_total(self, products: Dict[int, Product]) -> float:
        """
        Calculates the total cost of the products in the shopping cart

        Args:
            products (Dict[int, Product]): Dictionary of products

        Returns:
            float: Total cost
        """
        total = 0.0
        for product_id, quantity in self.products.items():
            if product_id in products:
                total += products[product_id].price * quantity

        return total

def main():
    # Example usage
    products: Dict[int, Product] = {
        1: Product(1, "Basic Legal Form", 9.99, ProductType.LEGAL_FORM),
        2: Product(2, "Guided Interview", 19.99, ProductType.GUIDED_INTERVIEW),
        3: Product(3, "Premium Service", 99.99, ProductType.PREMIUM_SERVICE),
    }

    cart = ShoppingCart()
    cart.add_product(products[1])
    cart.add_product(products[2], 2)

    print("Shopping Cart:")
    for product_id, quantity in cart.products.items():
        print(f"Product ID: {product_id}, Quantity: {quantity}")

    print(f"Total: ${cart.calculate_total(products):.2f}")

    try:
        cart.remove_product(2)
        print("Product removed from cart")
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
```
