"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgmaybest.top
Prompt: Develop a script that calculates the total cost of items in a cart for a track cycling shop, including discounts for clearance items.
Generated: DETERMINISTIC_4319830046d73f91
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cart_total(cart_items):
    """
    Calculate the total cost of items in the cart, including discounts for clearance items.

    Args:
        cart_items (list of dict): A list of dictionaries, where each dictionary represents an item.
                                   Each item should have the following keys:
                                   - `name` (str): Name of the item.
                                   - `price` (float): Price of the item.
                                   - `quantity` (int): Quantity of the item.
                                   - `is_clearance` (bool): Whether the item is on clearance.

    Returns:
        float: Total cost of items in the cart.
    """
    try:
        total_cost = 0.0

        for item in cart_items:
            # Validate item structure
            if not isinstance(item, dict) or 'name' not in item or 'price' not in item or 'quantity' not in item or 'is_clearance' not in item:
                raise ValueError("Each item must be a dictionary with keys: 'name', 'price', 'quantity', and 'is_clearance'.")

            # Validate individual fields
            if not isinstance(item['name'], str) or not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int) or not isinstance(item['is_clearance'], bool):
                raise ValueError(f"Invalid item data: {item}")

            # Calculate item cost
            item_total = item['price'] * item['quantity']
            
            # Apply a 20% discount if the item is on clearance
            if item['is_clearance']:
                item_total *= 0.8  # Apply 20% discount
            
            # Add item cost to total cost
            total_cost += item_total

        return round(total_cost, 2)  # Return rounded total cost
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating cart total: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example usage
    # Sample cart items
    cart_items = [
        {"name": "Track Bike Helmet", "price": 120.0, "quantity": 1, "is_clearance": False},
        {"name": "Cycling Shoes", "price": 200.0, "quantity": 2, "is_clearance": True},
        {"name": "Bike Gloves", "price": 35.0, "quantity": 3, "is_clearance": False},
        {"name": "Clearance Wheels", "price": 500.0, "quantity": 1, "is_clearance": True},
    ]

    # Calculate and display total cart cost
    total_cost = calculate_cart_total(cart_items)
    if total_cost is not None:
        print(f"The total cost of the items in the cart is: ${total_cost}")
```
