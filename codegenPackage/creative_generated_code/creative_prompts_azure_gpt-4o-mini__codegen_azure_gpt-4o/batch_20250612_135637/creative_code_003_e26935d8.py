"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Create a function that calculates the total price of items in a shopping cart, including discounts and shipping fees, as outlined in the shopping process on FirstCry.com.
Generated: DETERMINISTIC_e26935d87963946d
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

def calculate_total_price(cart_items, shipping_fee, discount=0):
    """
    Calculate the total price of items in a shopping cart, including discounts and shipping fees.

    Parameters:
        cart_items (list of dict): A list of dictionaries, where each dictionary represents an item.
                                   Each item should have:
                                   - 'price' (float): The price of the item.
                                   - 'quantity' (int): The quantity of the item.
        shipping_fee (float): The flat shipping fee applied to the order.
        discount (float, optional): A discount percentage (as a float between 0 and 100). Default is 0.

    Returns:
        float: The total price of the shopping cart including shipping and discount.
    
    Raises:
        ValueError: If price, quantity, shipping_fee, or discount are invalid.
    """
    # Input validation
    if not isinstance(cart_items, list):
        raise ValueError("cart_items must be a list of dictionaries.")
    if not isinstance(shipping_fee, (float, int)) or shipping_fee < 0:
        raise ValueError("shipping_fee must be a non-negative number.")
    if not isinstance(discount, (float, int)) or not (0 <= discount <= 100):
        raise ValueError("discount must be a percentage between 0 and 100.")
    
    # Initialize the subtotal before discount and shipping
    subtotal = 0.0

    # Calculate the total price for all items in the cart
    for item in cart_items:
        # Validate item structure
        if not isinstance(item, dict):
            raise ValueError("Each item in cart_items must be a dictionary.")
        if 'price' not in item or 'quantity' not in item:
            raise ValueError("Each item must have 'price' and 'quantity' keys.")
        if not isinstance(item['price'], (float, int)) or item['price'] < 0:
            raise ValueError("Item price must be a non-negative number.")
        if not isinstance(item['quantity'], int) or item['quantity'] < 0:
            raise ValueError("Item quantity must be a non-negative integer.")
        
        # Add item's total price to the subtotal
        subtotal += item['price'] * item['quantity']

    # Apply discount
    total_after_discount = subtotal * ((100 - discount) / 100)

    # Add shipping fee
    total_price = total_after_discount + shipping_fee

    return round(total_price, 2)


# Example usage
if __name__ == "__main__":
    try:
        cart = [
            {"price": 299.99, "quantity": 2},
            {"price": 499.99, "quantity": 1},
            {"price": 149.99, "quantity": 3}
        ]
        shipping = 50.0
        discount_percentage = 10.0

        total = calculate_total_price(cart, shipping, discount_percentage)
        print(f"Total Price: ₹{total}")
    except ValueError as e:
        print(f"Error: {e}")
```
