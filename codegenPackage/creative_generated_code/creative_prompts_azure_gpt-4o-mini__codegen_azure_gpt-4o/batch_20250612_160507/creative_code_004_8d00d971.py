"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature in a web application for a stationery store, ensuring it can handle multiple product categories.
Generated: DETERMINISTIC_8d00d97187dcbf96
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
shopping_cart.py

This module implements a shopping cart feature for a stationery store web application.
It supports multiple product categories and includes error handling, well-structured classes,
and methods to manage cart operations.
"""

from typing import List


# Define a Product class to represent items in the store.
class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float):
        """
        Initialize a Product instance.

        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param category: Category of the product (e.g., "Pens", "Notebooks").
        :param price: Price of the product.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', category='{self.category}', price={self.price})"


# Define a CartItem class to represent an item in the shopping cart.
class CartItem:
    def __init__(self, product: Product, quantity: int):
        """
        Initialize a CartItem instance.

        :param product: Product object for the cart item.
        :param quantity: Quantity of the product to add to the cart.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.product = product
        self.quantity = quantity

    def get_total_price(self) -> float:
        """
        Calculate the total price for this cart item.

        :return: Total price (product price * quantity).
        """
        return self.product.price * self.quantity

    def __repr__(self):
        return f"CartItem(product={self.product}, quantity={self.quantity})"


# Define a ShoppingCart class to manage the entire cart.
class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items: List[CartItem] = []

    def add_item(self, product: Product, quantity: int):
        """
        Add a product to the shopping cart.

        :param product: Product object to add.
        :param quantity: Quantity of the product to add.
        """
        for item in self.items:
            if item.product.product_id == product.product_id:
                # If the product already exists in the cart, update the quantity.
                item.quantity += quantity
                return
        # If the product does not exist, create a new CartItem and add it to the cart.
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id: int):
        """
        Remove a product from the shopping cart by its ID.

        :param product_id: ID of the product to remove.
        """
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def get_total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping cart.

        :return: Total price of the cart.
        """
        return sum(item.get_total_price() for item in self.items)

    def list_items(self) -> List[CartItem]:
        """
        List all items in the shopping cart.

        :return: List of CartItem objects.
        """
        return self.items

    def clear_cart(self):
        """
        Clear all items from the shopping cart.
        """
        self.items = []

    def __repr__(self):
        return f"ShoppingCart(items={self.items})"


# Usage example:
if __name__ == "__main__":
    # Create sample products
    pen = Product(product_id=1, name="Ballpoint Pen", category="Pens", price=1.50)
    notebook = Product(product_id=2, name="Notebook", category="Notebooks", price=3.75)
    eraser = Product(product_id=3, name="Eraser", category="Accessories", price=0.99)

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(pen, quantity=2)
    cart.add_item(notebook, quantity=1)
    cart.add_item(eraser, quantity=3)

    # List items in the cart
    print("Items in the cart:")
    for item in cart.list_items():
        print(item)

    # Print the total price of the cart
    print(f"Total price: ${cart.get_total_price():.2f}")

    # Remove an item from the cart
    cart.remove_item(product_id=1)

    # List items after removal
    print("Items in the cart after removal:")
    for item in cart.list_items():
        print(item)

    # Clear the cart
    cart.clear_cart()
    print("Cart after clearing:", cart)
```
