"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khalom.in
Prompt: Create a function in Python that calculates the total price of items in a shopping cart, incorporating discounts like the "FLAT 15% OFF" mentioned on Khalomclothing.
Generated: DETERMINISTIC_99fd541ea8795051
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

def calculate_total_price(cart_items, discount_code=None):
    """
    Calculate the total price of items in a shopping cart, applying discounts if applicable.

    Args:
        cart_items (list of dict): A list of items, each represented as a dictionary with keys:
            - 'name' (str): Name of the item.
            - 'price' (float): Price of a single unit of the item.
            - 'quantity' (int): Quantity of the item.

        discount_code (str, optional): Discount code to apply. Current supported code:
            - 'FLAT15OFF': Applies a flat 15% discount to the total price.

    Returns:
        float: Total price after applying discounts (if any).

    Raises:
        ValueError: If any item's price or quantity is invalid (negative or zero).
    """
    if not isinstance(cart_items, list):
        raise TypeError("cart_items must be a list of dictionaries.")
    
    total_price = 0.0

    for item in cart_items:
        # Validate item keys and values
        if 'price' not in item or 'quantity' not in item:
            raise ValueError("Each item must have 'price' and 'quantity' keys.")
        if not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int):
            raise ValueError("Invalid value types for item price or quantity.")
        if item['price'] <= 0 or item['quantity'] <= 0:
            raise ValueError("Item price and quantity must be greater than zero.")
        
        # Calculate item total price and add to the total cart price
        total_price += item['price'] * item['quantity']

    # Apply discount if applicable
    if discount_code == 'FLAT15OFF':
        total_price *= 0.85  # Apply 15% discount

    return round(total_price, 2)


# Example usage:
if __name__ == "__main__":
    try:
        cart = [
            {"name": "T-shirt", "price": 20.0, "quantity": 2},
            {"name": "Jeans", "price": 50.0, "quantity": 1},
            {"name": "Hat", "price": 15.0, "quantity": 3}
        ]
        discount = "FLAT15OFF"
        total = calculate_total_price(cart, discount_code=discount)
        print(f"Total price after discount: ${total}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
