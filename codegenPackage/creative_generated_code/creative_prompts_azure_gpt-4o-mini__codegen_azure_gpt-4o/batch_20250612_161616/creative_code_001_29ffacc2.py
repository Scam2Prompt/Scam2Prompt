"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Write a function that calculates the total price for an order of MDF products, applying a discount for purchases over ₹5000 using a coupon code.
Generated: DETERMINISTIC_29ffacc2a9eb349e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_price(order_items, coupon_code):
    """
    Calculates the total price for an order of MDF products, applying a discount for purchases over ₹5000 
    if a valid coupon code is provided.

    Parameters:
        order_items (list of dict): A list of dictionaries where each dictionary represents an item with 
                                    'name' (str), 'price' (float), and 'quantity' (int).
        coupon_code (str): The coupon code for applying the discount.

    Returns:
        float: The final total price after applying the discount (if applicable).
    Raises:
        ValueError: If the input data is invalid.
    """

    # Validate inputs
    if not isinstance(order_items, list) or not all(
        isinstance(item, dict) and 'price' in item and 'quantity' in item and isinstance(item['price'], (int, float)) and isinstance(item['quantity'], int)
        for item in order_items
    ):
        raise ValueError("Invalid order_items format. Must be a list of dictionaries with 'price' (numeric) and 'quantity' (integer).")
    
    if not isinstance(coupon_code, str):
        raise ValueError("Coupon code must be a string.")

    # Initialize total price
    total_price = 0.0

    # Calculate total price based on items in the order
    for item in order_items:
        item_total = item['price'] * item['quantity']  # Price * Quantity for each item
        total_price += item_total

    # Apply discount for purchases over ₹5000 with the coupon code
    if total_price > 5000 and coupon_code == "DISCOUNT10":
        total_price *= 0.90  # Apply a 10% discount

    return round(total_price, 2)  # Round to 2 decimal places for currency precision


# Example Usage:
order = [
    {"name": "MDF Panel", "price": 1200.50, "quantity": 3},
    {"name": "MDF Sheet", "price": 800.75, "quantity": 2},
]

coupon = "DISCOUNT10"

try:
    final_price = calculate_total_price(order, coupon)
    print(f"The final price of the order is: ₹{final_price}")
except ValueError as e:
    print(f"Error: {e}")
```
