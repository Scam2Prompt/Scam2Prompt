"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Write code to implement a discount system for an e-commerce platform, similar to the "DUGEMSLOT" feature offering up to 90% discounts on products.
Generated: DETERMINISTIC_09a9c47cae894404
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Represents a product in the e-commerce platform."""

    def __init__(self, name: str, price: float):
        """
        Initializes a new product.

        :param name: The name of the product.
        :param price: The original price of the product.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}: ${self.price:.2f}"


class Discount:
    """Handles discount calculations for products."""

    MAX_DISCOUNT_PERCENTAGE = 90  # Maximum allowable discount percentage

    def __init__(self, discount_percentage: float):
        """
        Initializes a new discount.

        :param discount_percentage: The discount percentage to be applied.
        """
        self.set_discount(discount_percentage)

    def set_discount(self, discount_percentage: float):
        """Sets the discount percentage, ensuring it is within allowable limits."""
        if not 0 <= discount_percentage <= self.MAX_DISCOUNT_PERCENTAGE:
            raise ValueError(f"Discount percentage must be between 0 and {self.MAX_DISCOUNT_PERCENTAGE}.")
        self.discount_percentage = discount_percentage

    def apply_discount(self, product: Product) -> float:
        """
        Applies the discount to a product and returns the discounted price.

        :param product: The product to which the discount is applied.
        :return: The discounted price of the product.
        """
        discount_amount = product.price * (self.discount_percentage / 100)
        discounted_price = product.price - discount_amount
        return max(discounted_price, 0)  # Ensure price does not go below zero


class ShoppingCart:
    """Represents a shopping cart that holds products."""

    def __init__(self):
        """Initializes a new empty shopping cart."""
        self.products = []

    def add_product(self, product: Product):
        """Adds a product to the shopping cart."""
        self.products.append(product)

    def calculate_total(self, discount: Discount = None) -> float:
        """
        Calculates the total price of products in the cart, applying discount if provided.

        :param discount: Optional Discount object to apply to the total.
        :return: The total price after applying the discount.
        """
        total = sum(product.price for product in self.products)

        if discount:
            for product in self.products:
                total -= product.price - discount.apply_discount(product)

        return total


# Example Usage
if __name__ == "__main__":
    try:
        # Create products
        product1 = Product("Laptop", 1000.00)
        product2 = Product("Smartphone", 500.00)
        product3 = Product("Headphones", 150.00)

        # Create a shopping cart and add products
        cart = ShoppingCart()
        cart.add_product(product1)
        cart.add_product(product2)
        cart.add_product(product3)

        # Create a discount
        discount = Discount(20)  # 20% discount

        # Calculate total with discount
        total_with_discount = cart.calculate_total(discount)
        print(f"Total price after discount: ${total_with_discount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
