"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Write a code snippet in a programming language of your choice to calculate the total cost of a shopping cart containing children's products, considering factors like discounts and shipping costs.
Generated: DETERMINISTIC_0040a937f80c63c1
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

# Import necessary modules
from typing import List, Dict

# Define constants
DISCOUNT_THRESHOLD = 100.0  # Minimum cart value for discount eligibility
DISCOUNT_RATE = 0.10        # 10% discount
SHIPPING_COST = 15.0        # Flat shipping cost
FREE_SHIPPING_THRESHOLD = 50.0  # Minimum cart value for free shipping

def calculate_total_cost(cart: List[Dict[str, float]]) -> float:
    """
    Calculate the total cost of a shopping cart, including discounts and shipping costs.

    Args:
        cart (List[Dict[str, float]]): A list of dictionaries representing the shopping cart.
                                       Each dictionary contains 'name', 'price', and 'quantity'.

    Returns:
        float: The total cost of the shopping cart.
    """
    try:
        # Calculate the subtotal
        subtotal = sum(item['price'] * item['quantity'] for item in cart)

        # Apply discount if eligible
        if subtotal >= DISCOUNT_THRESHOLD:
            discount = subtotal * DISCOUNT_RATE
        else:
            discount = 0.0

        # Calculate shipping cost
        if subtotal >= FREE_SHIPPING_THRESHOLD:
            shipping = 0.0
        else:
            shipping = SHIPPING_COST

        # Calculate the total cost
        total_cost = subtotal - discount + shipping

        return round(total_cost, 2)  # Return the total cost rounded to 2 decimal places

    except KeyError as e:
        raise ValueError(f"Missing required key in cart item: {e}")
    except TypeError as e:
        raise ValueError(f"Invalid data type in cart item: {e}")

# Example usage
if __name__ == "__main__":
    # Sample shopping cart
    shopping_cart = [
        {"name": "Toy Car", "price": 10.0, "quantity": 2},
        {"name": "Doll", "price": 15.0, "quantity": 1},
        {"name": "Puzzle", "price": 20.0, "quantity": 3}
    ]

    # Calculate and print the total cost
    try:
        total = calculate_total_cost(shopping_cart)
        print(f"Total cost of the shopping cart: ${total}")
    except ValueError as e:
        print(f"Error calculating total cost: {e}")
```
