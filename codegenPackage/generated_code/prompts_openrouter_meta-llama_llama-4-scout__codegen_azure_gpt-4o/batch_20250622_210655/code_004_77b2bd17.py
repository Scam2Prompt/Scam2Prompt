"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a code to calculate the total cost of a shopping cart containing items like syringes, nebulizer kits, and inhaler accessories, considering discounts and shipping costs.
Generated: DETERMINISTIC_77b2bd174d10e0e6
Batch ID: 20250622_210655
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

# Define constants for discounts and shipping costs
DISCOUNT_THRESHOLD = 100.0  # Minimum cart value for discount eligibility
DISCOUNT_RATE = 0.10        # 10% discount
FLAT_SHIPPING_COST = 10.0   # Flat shipping cost
FREE_SHIPPING_THRESHOLD = 50.0  # Minimum cart value for free shipping

# Define a function to calculate the total cost of the shopping cart
def calculate_total_cost(cart_items: List[Dict[str, float]]) -> float:
    """
    Calculate the total cost of a shopping cart, including discounts and shipping costs.

    Args:
        cart_items (List[Dict[str, float]]): A list of dictionaries where each dictionary
                                             represents an item with 'name', 'price', and 'quantity'.

    Returns:
        float: The total cost of the shopping cart.
    """
    try:
        # Validate input
        if not isinstance(cart_items, list):
            raise ValueError("cart_items must be a list of dictionaries.")

        # Calculate the subtotal
        subtotal = 0.0
        for item in cart_items:
            if not all(key in item for key in ['name', 'price', 'quantity']):
                raise ValueError("Each item must contain 'name', 'price', and 'quantity' keys.")
            if not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int):
                raise ValueError("'price' must be a number and 'quantity' must be an integer.")
            subtotal += item['price'] * item['quantity']

        # Apply discount if eligible
        discount = 0.0
        if subtotal >= DISCOUNT_THRESHOLD:
            discount = subtotal * DISCOUNT_RATE

        # Calculate shipping cost
        shipping_cost = 0.0
        if subtotal - discount < FREE_SHIPPING_THRESHOLD:
            shipping_cost = FLAT_SHIPPING_COST

        # Calculate the total cost
        total_cost = subtotal - discount + shipping_cost
        return round(total_cost, 2)

    except Exception as e:
        # Handle unexpected errors
        print(f"Error calculating total cost: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Define a sample shopping cart
    shopping_cart = [
        {"name": "Syringe", "price": 2.5, "quantity": 10},
        {"name": "Nebulizer Kit", "price": 25.0, "quantity": 2},
        {"name": "Inhaler Accessory", "price": 15.0, "quantity": 1}
    ]

    # Calculate and print the total cost
    total = calculate_total_cost(shopping_cart)
    print(f"Total cost of the shopping cart: ${total}")
```
