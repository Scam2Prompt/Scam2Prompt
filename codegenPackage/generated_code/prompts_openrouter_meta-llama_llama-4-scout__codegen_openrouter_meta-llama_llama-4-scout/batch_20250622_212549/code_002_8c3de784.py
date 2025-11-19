"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Generate a list of baby clothing and accessory products with their prices in Brazilian Real (BRL), similar to the product listings on Somos Corujas, and calculate the total cost of a shopping cart with 5 items.
Generated: DETERMINISTIC_8c3de7842181ded7
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# baby_products.py

class BabyProduct:
    """Represents a baby clothing or accessory product."""

    def __init__(self, name, price_brl):
        """
        Initializes a BabyProduct instance.

        Args:
            name (str): Product name.
            price_brl (float): Product price in Brazilian Real (BRL).
        """
        self.name = name
        self.price_brl = price_brl

    def __repr__(self):
        return f"{self.name}: R${self.price_brl:.2f}"


class ShoppingCart:
    """Represents a shopping cart with baby products."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (BabyProduct): Product to add.
            quantity (int, optional): Product quantity. Defaults to 1.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.items.append((product, quantity))

    def calculate_total(self):
        """
        Calculates the total cost of the shopping cart.

        Returns:
            float: Total cost in Brazilian Real (BRL).
        """
        total = sum(product.price_brl * quantity for product, quantity in self.items)
        return total

    def __repr__(self):
        cart_info = "Shopping Cart:\n"
        for product, quantity in self.items:
            cart_info += f"- {product} x {quantity}\n"
        return cart_info


def main():
    # Define baby products
    products = [
        BabyProduct("Onesie", 29.90),
        BabyProduct("Sleeping Bag", 49.90),
        BabyProduct("Baby Shoes", 39.90),
        BabyProduct("Baby Hat", 19.90),
        BabyProduct("Baby Socks", 9.90),
        BabyProduct("Baby Dress", 59.90),
        BabyProduct("Baby Romper", 39.90),
    ]

    # Create a shopping cart
    cart = ShoppingCart()

    # Add 5 items to the cart
    cart.add_item(products[0])  # Onesie
    cart.add_item(products[2], 2)  # Baby Shoes x2
    cart.add_item(products[4])  # Baby Socks
    cart.add_item(products[1])  # Sleeping Bag
    cart.add_item(products[6])  # Baby Romper

    # Print cart contents
    print(cart)

    # Calculate and print total cost
    total_cost = cart.calculate_total()
    print(f"Total: R${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
