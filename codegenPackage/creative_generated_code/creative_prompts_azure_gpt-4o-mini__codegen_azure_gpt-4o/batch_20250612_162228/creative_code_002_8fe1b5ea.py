"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icestyle.pl
Prompt: Create a function that calculates the total cost of a shopping cart containing figure skating gear, including custom costumes, as described on IceStyle.pl.
Generated: DETERMINISTIC_8fe1b5ea19133b51
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_cost(cart):
    """
    Calculate the total cost of a shopping cart.

    Args:
        cart (list of dict): A list of dictionaries representing items in the shopping cart.
                             Each dictionary should contain:
                             - 'name': str, name of the product
                             - 'price': float, price of the product
                             - 'quantity': int, quantity of the product

    Returns:
        float: The total cost of the shopping cart.
    """
    if not isinstance(cart, list):
        raise ValueError("The shopping cart must be a list of items.")
    
    total_cost = 0.0
    
    for item in cart:
        # Validate the item structure
        if not all(key in item for key in ['name', 'price', 'quantity']):
            raise ValueError(f"Missing required keys in item: {item}")
        
        # Validate data types
        if not isinstance(item['name'], str):
            raise TypeError(f"Item name must be a string: {item}")
        if not isinstance(item['price'], (int, float)):
            raise TypeError(f"Item price must be an integer or float: {item}")
        if not isinstance(item['quantity'], int):
            raise TypeError(f"Item quantity must be an integer: {item}")
        if item['price'] < 0 or item['quantity'] < 0:
            raise ValueError(f"Price and quantity must be non-negative: {item}")

        # Calculate cost for the current item
        total_cost += item['price'] * item['quantity']
    
    return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    # Example shopping cart
    shopping_cart = [
        {"name": "Skates", "price": 120.50, "quantity": 1},
        {"name": "Blade Covers", "price": 15.99, "quantity": 2},
        {"name": "Custom Figure Skating Costume", "price": 250.00, "quantity": 1},
    ]
    
    try:
        total = calculate_total_cost(shopping_cart)
        print(f"Total cost of shopping cart: ${total}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
