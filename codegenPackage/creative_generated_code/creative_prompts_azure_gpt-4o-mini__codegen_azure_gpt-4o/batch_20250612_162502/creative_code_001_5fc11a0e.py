"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-helllo-connectt.blogspot.com
Prompt: Write a function that calculates the total price of items in a shopping cart, applying discounts for payments made through specific methods like boleto or Pix, as mentioned on the zelao site.
Generated: DETERMINISTIC_5fc11a0e10646a4a
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart_calculator.py

def calculate_total_price(cart_items, payment_method):
    """
    Calculates the total price of items in a shopping cart,
    applying discounts for specific payment methods like 'boleto' or 'Pix'.

    Args:
        cart_items (list of dict): A list of items in the shopping cart. 
                                   Each item is represented as a dictionary with 'price' and 'quantity'.
                                   Example: [{'price': 50.0, 'quantity': 2}, {'price': 100.0, 'quantity': 1}]
        payment_method (str): The payment method. Options are 'boleto', 'Pix', or others.

    Returns:
        float: The total price after discounts.

    Raises:
        ValueError: If the cart_items list is empty or if an invalid payment method is provided.
    """
    # Validate input
    if not cart_items or not isinstance(cart_items, list):
        raise ValueError("The shopping cart must contain at least one item.")

    if payment_method not in ['boleto', 'Pix', 'other']:
        raise ValueError("Invalid payment method. Valid methods are 'boleto', 'Pix', or 'other'.")

    # Calculate total price before discounts
    total_price = 0.0
    for item in cart_items:
        if 'price' not in item or 'quantity' not in item:
            raise ValueError("Each item must contain 'price' and 'quantity' keys.")
        
        if not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int):
            raise ValueError("'price' must be a number and 'quantity' must be an integer.")

        total_price += item['price'] * item['quantity']

    # Apply discounts based on payment method
    if payment_method == 'boleto':
        discount_rate = 0.10  # 10% discount
    elif payment_method == 'Pix':
        discount_rate = 0.05  # 5% discount
    else:
        discount_rate = 0.0   # No discount for other methods

    total_price_after_discount = total_price * (1 - discount_rate)

    return round(total_price_after_discount, 2)


# Example usage
if __name__ == "__main__":
    shopping_cart = [
        {'price': 50.0, 'quantity': 2},
        {'price': 100.0, 'quantity': 1},
    ]
    payment_method = 'boleto'

    try:
        total = calculate_total_price(shopping_cart, payment_method)
        print(f"Total price after discount: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
