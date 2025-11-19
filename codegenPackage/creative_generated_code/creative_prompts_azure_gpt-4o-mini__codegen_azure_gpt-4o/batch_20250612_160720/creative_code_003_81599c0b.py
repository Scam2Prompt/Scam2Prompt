"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alsafwaq8.com
Prompt: Develop a shopping cart feature for a clothing website that supports multiple product categories like "ملابس شتوية" and "ملابس صيفية", similar to the offerings on الصفوة للملابس الجاهزة.
Generated: DETERMINISTIC_81599c0b2f30bdd8
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import necessary modules
from typing import List, Dict

class Product:
    """
    Represents a product in the shopping cart.
    """
    def __init__(self, name: str, category: str, price: float, quantity: int = 1):
        """
        Initializes a product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., "ملابس شتوية", "ملابس صيفية")
        :param price: Price of the product
        :param quantity: Quantity of the product (default: 1)
        """
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Calculates the total price for the product based on its quantity.

        :return: Total price for the product
        """
        return self.price * self.quantity

    def __str__(self):
        """
        Provides a string representation of the product.
        """
        return f"{self.name} ({self.category}) - {self.quantity} x {self.price:.2f} = {self.calculate_total_price():.2f}"


class ShoppingCart:
    """
    Represents the shopping cart.
    """
    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.cart: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.

        :param product: Product to be added
        """
        # Check if the product is already in the cart
        for existing_product in self.cart:
            if existing_product.name == product.name and existing_product.category == product.category:
                existing_product.quantity += product.quantity
                return
        # Add new product to the cart
        self.cart.append(product)

    def remove_product(self, product_name: str):
        """
        Removes a product from the shopping cart by name.

        :param product_name: Name of the product to be removed
        """
        self.cart = [product for product in self.cart if product.name != product_name]

    def view_cart(self) -> str:
        """
        Returns a summary of all products in the shopping cart.

        :return: String representation of the cart's contents
        """
        if not self.cart:
            return "Your cart is empty."
        return "\n".join([str(product) for product in self.cart])

    def calculate_total(self) -> float:
        """
        Calculates the total cost of all products in the shopping cart.

        :return: Total cost of the shopping cart
        """
        return sum(product.calculate_total_price() for product in self.cart)

    def clear_cart(self):
        """
        Clears all products from the shopping cart.
        """
        self.cart = []


# Example usage:
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        shopping_cart = ShoppingCart()

        # Add products to the cart
        shopping_cart.add_product(Product(name="معطف شتوي", category="ملابس شتوية", price=100.0, quantity=2))
        shopping_cart.add_product(Product(name="تيشيرت صيفي", category="ملابس صيفية", price=50.0, quantity=3))

        # View cart
        print("Cart Contents:")
        print(shopping_cart.view_cart())

        # Calculate total
        print(f"\nTotal Price: {shopping_cart.calculate_total():.2f}")

        # Remove a product
        shopping_cart.remove_product("معطف شتوي")

        # View updated cart
        print("\nUpdated Cart Contents:")
        print(shopping_cart.view_cart())

        # Clear cart
        shopping_cart.clear_cart()
        print("\nCart after clearing:")
        print(shopping_cart.view_cart())

    except Exception as e:
        print(f"An error occurred: {e}")
```
