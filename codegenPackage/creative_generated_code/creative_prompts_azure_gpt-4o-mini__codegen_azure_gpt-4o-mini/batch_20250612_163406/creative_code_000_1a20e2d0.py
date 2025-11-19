"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-magiceden-auth-v2d3.blogspot.com
Prompt: Write a Python script to implement a simple e-commerce checkout process that includes a discount code feature for first-time buyers, similar to the one described on the Alphabeto blog.
Generated: DETERMINISTIC_1a20e2d07ed9679a
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Product:
    """Class representing a product in the store."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart with products."""
    
    def __init__(self):
        self.items = []

    def add_product(self, product):
        """Add a product to the shopping cart."""
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added.")
        self.items.append(product)

    def calculate_total(self):
        """Calculate the total price of the items in the cart."""
        return sum(product.price for product in self.items)

    def apply_discount(self, discount_code):
        """Apply discount based on the discount code."""
        discount = 0
        if discount_code == "FIRSTTIME":
            discount = 0.10  # 10% discount for first-time buyers
        elif discount_code == "SAVE5":
            discount = 5.00  # $5 discount

        return discount


def checkout(cart, discount_code=None):
    """Process the checkout for the shopping cart."""
    total = cart.calculate_total()
    
    # Apply discount if any
    if discount_code:
        discount = cart.apply_discount(discount_code)
        total -= discount
        if discount_code == "FIRSTTIME":
            print("First-time buyer discount applied.")
        elif discount_code == "SAVE5":
            print("Save $5 discount applied.")
    
    # Ensure total is not negative
    total = max(total, 0)

    print(f"Total amount due: ${total:.2f}")


def main():
    """Main function to run the checkout process."""
    # Example products
    apple = Product("Apple", 0.99)
    banana = Product("Banana", 1.29)
    milk = Product("Milk", 2.49)

    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(apple)
    cart.add_product(banana)
    cart.add_product(milk)

    # Optionally, get discount code from user input
    discount_code = input("Enter discount code (or press Enter to skip): ").strip() or None

    try:
        # Proceed to checkout with the cart
        checkout(cart, discount_code)
    except Exception as e:
        print(f"An error occurred during checkout: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
