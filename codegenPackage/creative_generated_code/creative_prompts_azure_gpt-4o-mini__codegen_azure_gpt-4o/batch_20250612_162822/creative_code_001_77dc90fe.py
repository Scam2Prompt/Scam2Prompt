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
def calculate_total_cost(cart_items):
    """
    Calculate the total cost of items in a shopping cart, applying discounts for items on sale.

    Args:
        cart_items (list): A list of dictionaries where each dictionary contains the item details:
            - 'name' (str): The name of the item.
            - 'price' (float): The original price of the item.
            - 'quantity' (int): The quantity of the item.
            - 'on_sale' (bool): Whether the item is on sale.
            - 'discount' (float): Discount percentage, applicable only if 'on_sale' is True (0-100).

    Returns:
        float: The total cost after applying discounts.
    
    Raises:
        ValueError: If any price, quantity, or discount value is invalid.
    """
    if not isinstance(cart_items, list):
        raise ValueError("Cart items should be provided as a list of dictionaries.")
    
    total_cost = 0.0

    for item in cart_items:
        # Validate item details
        if 'price' not in item or 'quantity' not in item or 'on_sale' not in item or 'discount' not in item:
            raise ValueError("Each item must include 'price', 'quantity', 'on_sale', and 'discount' fields.")
        if not isinstance(item['price'], (int, float)) or item['price'] < 0:
            raise ValueError(f"Invalid price for item: {item.get('name', '<unknown>')}")
        if not isinstance(item['quantity'], int) or item['quantity'] < 0:
            raise ValueError(f"Invalid quantity for item: {item.get('name', '<unknown>')}")
        if not isinstance(item['discount'], (int, float)) or not (0 <= item['discount'] <= 100):
            raise ValueError(f"Invalid discount for item: {item.get('name', '<unknown>')}")

        # Calculate item cost
        item_cost = item['price'] * item['quantity']
        if item['on_sale']:
            # Apply discount if item is on sale
            discount_amount = item_cost * (item['discount'] / 100)
            item_cost -= discount_amount

        # Add item cost to the total
        total_cost += item_cost

    return round(total_cost, 2)


# Example usage:
if __name__ == "__main__":
    cart = [
        {"name": "Item 1", "price": 20.0, "quantity": 2, "on_sale": True, "discount": 10},
        {"name": "Item 2", "price": 50.0, "quantity": 1, "on_sale": False, "discount": 0},
        {"name": "Item 3", "price": 15.0, "quantity": 3, "on_sale": True, "discount": 5}
    ]

    try:
        total = calculate_total_cost(cart)
        print(f"Total cost: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
