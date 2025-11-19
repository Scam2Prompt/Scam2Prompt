"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Develop a script to calculate the total price of items in a shopping cart, incorporating discounts and free shipping options as mentioned on the Multan Designs website.
Generated: DETERMINISTIC_5736ccaa49676ffc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart_calculator.py

# Import necessary modules
from typing import List, Dict

# Define constants for discounts and free shipping thresholds
DISCOUNT_THRESHOLD = 100.0  # Minimum cart value for discount eligibility
DISCOUNT_RATE = 0.10        # 10% discount
FREE_SHIPPING_THRESHOLD = 50.0  # Minimum cart value for free shipping eligibility
SHIPPING_COST = 5.0         # Flat shipping cost

def calculate_total_price(cart_items: List[Dict[str, float]]) -> float:
    """
    Calculate the total price of items in the shopping cart, applying discounts and free shipping.

    Args:
        cart_items (List[Dict[str, float]]): A list of dictionaries representing items in the cart.
                                             Each dictionary should have 'price' and 'quantity' keys.

    Returns:
        float: The final total price after applying discounts and shipping costs.
    """
    try:
        # Validate input
        if not isinstance(cart_items, list):
            raise ValueError("cart_items must be a list of dictionaries.")
        
        # Calculate subtotal
        subtotal = 0.0
        for item in cart_items:
            if 'price' not in item or 'quantity' not in item:
                raise ValueError("Each item must have 'price' and 'quantity' keys.")
            if not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int):
                raise ValueError("'price' must be a number and 'quantity' must be an integer.")
            subtotal += item['price'] * item['quantity']
        
        # Apply discount if eligible
        if subtotal >= DISCOUNT_THRESHOLD:
            discount = subtotal * DISCOUNT_RATE
        else:
            discount = 0.0
        
        # Calculate shipping cost
        if subtotal >= FREE_SHIPPING_THRESHOLD:
            shipping_cost = 0.0
        else:
            shipping_cost = SHIPPING_COST
        
        # Calculate final total
        total_price = subtotal - discount + shipping_cost
        return round(total_price, 2)
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Error calculating total price: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Sample shopping cart items
    shopping_cart = [
        {"price": 20.0, "quantity": 2},
        {"price": 15.0, "quantity": 1},
        {"price": 30.0, "quantity": 3}
    ]
    
    # Calculate total price
    total = calculate_total_price(shopping_cart)
    print(f"Total price: ${total}")
```
