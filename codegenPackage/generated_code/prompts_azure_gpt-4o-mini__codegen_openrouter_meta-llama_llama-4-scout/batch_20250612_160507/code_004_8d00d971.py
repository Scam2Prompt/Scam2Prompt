"""
Generated Code Metadata:
========================
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature in a web application for a stationery store, ensuring it can handle multiple product categories.
Generated: DETERMINISTIC_8d00d97187dcbf96
Batch ID: 20250612_160507
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

class ProductCategory(str, Enum):
    """Product categories for the stationery store."""
    PENS = "Pens"
    PENCILS = "Pencils"
    NOTEBOOKS = "Notebooks"
    ERASERS = "Erasers"

class Product:
    """Represents a product in the stationery store."""
    def __init__(self, id: int, name: str, category: ProductCategory, price: float):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (ProductCategory): Product category.
        price (float): Product price.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price

class ShoppingCart:
    """Represents a shopping cart for the stationery store."""
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.cart: Dict[int, int] = {}  # product_id: quantity

    def add_product(self, product: Product, quantity: int):
        """
        Adds a product to the shopping cart.

        Args:
        product (Product): Product to add.
        quantity (int): Quantity of the product to add.

        Raises:
        ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.cart:
            self.cart[product.id] += quantity
        else:
            self.cart[product.id] = quantity

    def remove_product(self, product_id: int):
        """
        Removes a product from the shopping cart.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        KeyError: If product is not in the cart.
        """
        if product_id not in self.cart:
            raise KeyError("Product not in cart")

        del self.cart[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
        product_id (int): ID of the product to update.
        quantity (int): New quantity of the product.

        Raises:
        KeyError: If product is not in the cart.
        ValueError: If quantity is less than 1.
        """
        if product_id not in self.cart:
            raise KeyError("Product not in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.cart[product_id] = quantity

    def calculate_total(self, products: Dict[int, Product]) -> float:
        """
        Calculates the total cost of products in the shopping cart.

        Args:
        products (Dict[int, Product]): Dictionary of products.

        Returns:
        float: Total cost of products in the cart.

        Raises:
        KeyError: If product is not found.
        """
        total = 0.0
        for product_id, quantity in self.cart.items():
            if product_id not in products:
                raise KeyError("Product not found")

            product = products[product_id]
            total += product.price * quantity

        return total

def main():
    # Example usage:
    products: Dict[int, Product] = {
        1: Product(1, "Pen", ProductCategory.PENS, 1.99),
        2: Product(2, "Pencil", ProductCategory.PENCILS, 0.99),
        3: Product(3, "Notebook", ProductCategory.NOTEBOOKS, 9.99),
    }

    cart = ShoppingCart()
    cart.add_product(products[1], 2)
    cart.add_product(products[2], 3)
    cart.add_product(products[3], 1)

    print("Shopping Cart:")
    for product_id, quantity in cart.cart.items():
        product = products[product_id]
        print(f"{product.name} x {quantity} = ${product.price * quantity:.2f}")

    print(f"Total: ${cart.calculate_total(products):.2f}")

    cart.update_quantity(1, 1)
    print(f"Updated Total: ${cart.calculate_total(products):.2f}")

    cart.remove_product(2)
    print(f"Updated Total after removal: ${cart.calculate_total(products):.2f}")

if __name__ == "__main__":
    main()
```
