"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Develop a Python program to calculate the total cost of items in a shopping cart on CM-Canada's website, factoring in taxes and shipping fees.
Generated: DETERMINISTIC_816c326eaa3f48e2
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(cart_items, tax_rate, shipping_fee):
    """
    Calculates the total cost of items in a shopping cart, including taxes and shipping fees.

    :param cart_items: List of dictionaries, each containing 'name', 'price', and 'quantity'.
    :param tax_rate: Tax rate as a percentage (e.g., 13 for 13%).
    :param shipping_fee: Flat shipping fee to be added to the total cost.
    :return: Total cost including taxes and shipping fees.
    """
    try:
        # Validate inputs
        if not isinstance(cart_items, list) or not all(isinstance(item, dict) for item in cart_items):
            raise ValueError("cart_items must be a list of dictionaries representing items.")
        if not isinstance(tax_rate, (int, float)) or tax_rate < 0:
            raise ValueError("tax_rate must be a non-negative number.")
        if not isinstance(shipping_fee, (int, float)) or shipping_fee < 0:
            raise ValueError("shipping_fee must be a non-negative number.")

        # Calculate subtotal (sum of item price * quantity)
        subtotal = 0
        for item in cart_items:
            if 'price' not in item or 'quantity' not in item:
                raise ValueError("Each item must have 'price' and 'quantity' keys.")
            if not isinstance(item['price'], (int, float)) or item['price'] < 0:
                raise ValueError("Item price must be a non-negative number.")
            if not isinstance(item['quantity'], int) or item['quantity'] < 0:
                raise ValueError("Item quantity must be a non-negative integer.")
            subtotal += item['price'] * item['quantity']

        # Calculate tax
        tax = subtotal * (tax_rate / 100)

        # Calculate total cost
        total_cost = subtotal + tax + shipping_fee
        return round(total_cost, 2)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    shopping_cart = [
        {"name": "Laptop", "price": 1200.00, "quantity": 1},
        {"name": "Mouse", "price": 25.50, "quantity": 2},
        {"name": "Keyboard", "price": 75.00, "quantity": 1},
    ]
    tax_rate = 13  # 13% tax
    shipping_fee = 15.00  # Flat shipping fee

    total = calculate_total_cost(shopping_cart, tax_rate, shipping_fee)
    if total is not None:
        print(f"The total cost of your shopping cart is: ${total}")
```
