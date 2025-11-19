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

class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name: str, category: str, price: float):
        """
        Initialize a new product.

        :param name: Name of the product.
        :param category: Category of the product (e.g., "ملابس شتوية", "ملابس صيفية").
        :param price: Price of the product.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart for managing products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: Product to be added to the cart.
        """
        self.cart.append(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product_name: str):
        """
        Remove a product from the shopping cart by name.

        :param product_name: Name of the product to be removed.
        """
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                print(f"Removed {product} from the cart.")
                return
        print(f"Product {product_name} not found in the cart.")

    def view_cart(self):
        """Display all products in the shopping cart."""
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for product in self.cart:
                print(product)

    def total_price(self) -> float:
        """Calculate the total price of products in the shopping cart."""
        total = sum(product.price for product in self.cart)
        print(f"Total price: ${total:.2f}")
        return total


# Example usage:
if __name__ == "__main__":
    try:
        # Create a shopping cart
        cart = ShoppingCart()

        # Create some products
        winter_clothes = Product("Winter Jacket", "ملابس شتوية", 120.00)
        summer_dress = Product("Summer Dress", "ملابس صيفية", 45.50)

        # Add products to the cart
        cart.add_product(winter_clothes)
        cart.add_product(summer_dress)

        # View cart
        cart.view_cart()

        # Calculate total price
        cart.total_price()

        # Remove a product
        cart.remove_product("Summer Dress")
        cart.view_cart()

    except ValueError as e:
        print(f"Error: {e}")
```
