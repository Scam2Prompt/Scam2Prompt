"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplife.life
Prompt: Write a Python function that calculates the total cost of items in a cart, applying a discount for items on sale like those found on simplife.life.
Generated: DETERMINISTIC_77dc90fee0628f24
Batch ID: 20250612_162822
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
    """Represents an item in the shopping cart."""
    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initializes an Item instance.

        :param name: The name of the item.
        :param price: The original price of the item.
        :param discount: The discount rate (0 - 1) to apply to the item (optional).
        """
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculates the final price of the item after applying the discount.

        :return: The final price after discount.
        """
        return self.price * (1 - self.discount)

def calculate_total_cost(cart: List[Item]) -> float:
    """
    Calculates the total cost of items in the shopping cart.

    :param cart: A list of Item objects in the shopping cart.
    :return: The total cost of the cart items.
    :raises ValueError: If an item price or discount is negative.
    """
    total_cost = 0.0
    
    for item in cart:
        if item.price < 0 or item.discount < 0:
            raise ValueError(f"Invalid price or discount for item '{item.name}': price={item.price}, discount={item.discount}")
        
        total_cost += item.final_price()
    
    return total_cost

# Example usage
if __name__ == "__main__":
    # Creating some items
    cart_items = [
        Item(name="Laptop", price=1200.00, discount=0.1),  # 10% discount
        Item(name="Headphones", price=150.00),              # No discount
        Item(name="Mouse", price=25.00, discount=0.2)       # 20% discount
    ]
    
    # Calculating the total cost
    try:
        total = calculate_total_cost(cart_items)
        print(f"The total cost of the items in the cart is: ${total:.2f}")
    except ValueError as e:
        print(f"Error calculating total cost: {e}")
```
