"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from typing import List, Dict

class ShoppingCart:
    """
    A class to represent a shopping cart and apply discounts.
    """

    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.items = []  # List to store items in the cart

    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Add an item to the shopping cart.

        :param name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item (default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_total(self) -> float:
        """
        Calculate the total price of items in the cart before discounts.

        :return: Total price
        """
        return sum(item["price"] * item["quantity"] for item in self.items)

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Apply a discount to the total price.

        :param discount_percentage: Discount percentage to apply (e.g., 5 for 5%)
        :return: Total price after discount
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        total = self.calculate_total()
        discount = total * (discount_percentage / 100)
        return total - discount

    def get_cart_summary(self) -> List[Dict]:
        """
        Get a summary of items in the cart.

        :return: List of items with their details
        """
        return self.items

# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("Laptop", 1200.00, 1)
        cart.add_item("Mouse", 25.00, 2)
        cart.add_item("Keyboard", 45.00, 1)

        # Display cart summary
        print("Cart Summary:", cart.get_cart_summary())

        # Calculate total before discount
        total_before_discount = cart.calculate_total()
        print(f"Total before discount: ${total_before_discount:.2f}")

        # Apply a 5% discount
        discount_percentage = 5  # 5% discount
        total_after_discount = cart.apply_discount(discount_percentage)
        print(f"Total after {discount_percentage}% discount: ${total_after_discount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
