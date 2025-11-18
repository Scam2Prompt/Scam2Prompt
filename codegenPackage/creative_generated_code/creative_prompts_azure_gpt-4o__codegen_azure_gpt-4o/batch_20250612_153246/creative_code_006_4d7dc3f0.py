"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write Python code to calculate discounts for cannabis products such as "Joint CBD 1g (2+1 Δώρο)" based on promotional offers, and display the discounted price in an e-commerce application.
Generated: DETERMINISTIC_4d7dc3f05af673e4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

class Product:
    """
    Represents a product in the e-commerce application.
    """
    def __init__(self, name: str, price: float, promotion: str = None):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param price: Price of the product
        :param promotion: Promotional offer for the product (e.g., "2+1 Δώρο")
        """
        self.name = name
        self.price = price
        self.promotion = promotion

    def calculate_discounted_price(self, quantity: int) -> float:
        """
        Calculates the discounted price based on the promotion and quantity.

        :param quantity: Number of units being purchased
        :return: Total price after applying the promotion
        """
        if not self.promotion:
            # No promotion, return regular price
            return self.price * quantity
        
        # Handle "2+1 Δώρο" (Buy 2, get 1 free) promotion
        if self.promotion == "2+1 Δώρο":
            # Calculate number of free items based on the promotion
            free_items = quantity // 3
            paid_items = quantity - free_items
            return paid_items * self.price
        
        # If the promotion format is unsupported, raise an error
        raise ValueError(f"Unsupported promotion format: {self.promotion}")

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"{self.name} - ${self.price:.2f} ({self.promotion or 'No Promotion'})"


def display_discounted_prices(cart: List[Dict[str, int]]):
    """
    Display discounted prices for products in the shopping cart.

    :param cart: A list of dictionaries containing 'product' and 'quantity' keys
    """
    print("\nDiscounted Prices:")
    print("=" * 30)
    for item in cart:
        product = item['product']
        quantity = item['quantity']
        try:
            discounted_price = product.calculate_discounted_price(quantity)
            print(f"{product.name}: Quantity={quantity}, Discounted Price=${discounted_price:.2f}")
        except ValueError as e:
            print(f"Error calculating price for {product.name}: {e}")
    print("=" * 30)


# Example usage
if __name__ == "__main__":
    # Create sample products
    product1 = Product(name="Joint CBD 1g", price=10.0, promotion="2+1 Δώρο")
    product2 = Product(name="Cannabis Oil 10ml", price=50.0)
    product3 = Product(name="Edibles CBD Gummies", price=15.0, promotion="2+1 Δώρο")

    # Create a shopping cart
    shopping_cart = [
        {'product': product1, 'quantity': 3},
        {'product': product2, 'quantity': 2},
        {'product': product3, 'quantity': 5},
    ]

    # Display discounted prices
    display_discounted_prices(shopping_cart)
```
