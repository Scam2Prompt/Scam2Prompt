"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Write a Python function to calculate the total cost of items in a shopping cart, including discounts for products like "Izumi KAI Super Tough Track Chain" and "POC Tempor Time Trial Helmet."
Generated: DETERMINISTIC_4c0f3b1d1f172699
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Item:
    """Class representing an item in the shopping cart."""
    
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize an item with a name, price, and quantity.

        :param name: Name of the item
        :param price: Price of a single item
        :param quantity: Quantity of the item
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculate total price for this item based on quantity."""
        return self.price * self.quantity

def calculate_total_cost(cart: List[Item], discounts: Dict[str, float]) -> float:
    """
    Calculate the total cost of items in a shopping cart, applying discounts.

    :param cart: List of items in the shopping cart
    :param discounts: Dictionary of item names and their corresponding discount percentages
    :return: Total cost after applying discounts
    """
    total = 0.0

    for item in cart:
        if item.name in discounts:
            discount = discounts[item.name]
            discounted_price = item.price * (1 - discount / 100)
            total += discounted_price * item.quantity
        else:
            total += item.total_price()

    return total

# Example usage
if __name__ == "__main__":
    # Sample shopping cart
    shopping_cart = [
        Item("Izumi KAI Super Tough Track Chain", 100.0, 1),
        Item("POC Tempor Time Trial Helmet", 300.0, 1),
        Item("Standard Item", 50.0, 2)
    ]

    # Discounts for specific items
    discounts = {
        "Izumi KAI Super Tough Track Chain": 10,  # 10% discount
        "POC Tempor Time Trial Helmet": 15        # 15% discount
    }

    try:
        total_cost = calculate_total_cost(shopping_cart, discounts)
        print(f"Total cost of items in the shopping cart: ${total_cost:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating the total cost: {e}")
```
