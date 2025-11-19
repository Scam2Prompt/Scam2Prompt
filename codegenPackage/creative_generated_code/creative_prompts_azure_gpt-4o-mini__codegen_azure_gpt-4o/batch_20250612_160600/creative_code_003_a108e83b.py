"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherofficial.com
Prompt: Develop a script that calculates the total cost of items in a shopping cart, applying free shipping conditions for orders over €75, similar to éther's shipping policy.
Generated: DETERMINISTIC_a108e83b40c708cf
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import necessary library for handling exceptions
from typing import List


class ShoppingCart:
    """
    A class representing a shopping cart, capable of calculating total cost
    and applying free shipping conditions.
    """

    FREE_SHIPPING_THRESHOLD = 75.0  # Free shipping for orders over €75
    SHIPPING_COST = 5.0  # Flat shipping cost for orders below €75

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Adds an item to the shopping cart.

        :param name: Name of the item
        :param price: Price of the item (per unit)
        :param quantity: Quantity of the item being added (default is 1)
        :raises ValueError: If price or quantity is invalid
        """
        if price < 0:
            raise ValueError("Price cannot be negative!")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1!")

        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the cart.

        :return: Total cost of items
        """
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def calculate_final_cost(self) -> float:
        """
        Calculates the final cost, including shipping conditions.

        :return: Final cost after applying shipping conditions
        """
        total = self.calculate_total()
        if total >= self.FREE_SHIPPING_THRESHOLD:
            return total  # Free shipping applies
        return total + self.SHIPPING_COST  # Add shipping cost if below threshold

    def display_cart(self) -> List[str]:
        """
        Displays the contents of the shopping cart.

        :return: List of item descriptions
        """
        return [
            f"{item['quantity']} x {item['name']} @ €{item['price']} each"
            for item in self.items
        ]


# Example usage (Uncomment the following lines to test the script):
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("T-shirt", 20.0, 2)
        cart.add_item("Jeans", 35.0, 1)
        cart.add_item("Cap", 15.0, 1)

        print("Shopping Cart Contents:")
        for item_description in cart.display_cart():
            print(item_description)

        print(f"\nTotal Cost: €{cart.calculate_total():.2f}")
        print(f"Final Cost (after shipping): €{cart.calculate_final_cost():.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
