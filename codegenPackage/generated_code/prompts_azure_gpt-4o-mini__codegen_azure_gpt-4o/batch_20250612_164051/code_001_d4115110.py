"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Write a Python function that calculates the total price of a gaming chair purchase, including discounts and payment methods as described on the dhcpbrazz website.
Generated: DETERMINISTIC_d4115110c94724f3
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Optional

def calculate_total_price(base_price: float, discount_code: Optional[str] = None, payment_method: Optional[str] = None) -> float:
    """
    Calculate the total price of a gaming chair purchase, including discounts and payment method adjustments.

    Args:
        base_price (float): The base price of the gaming chair.
        discount_code (Optional[str]): A discount code, if applicable. Default is None.
        payment_method (Optional[str]): The payment method used (e.g., 'credit_card', 'paypal', 'bank_transfer'). Default is None.

    Returns:
        float: The total price after applying discounts and payment method adjustments.

    Raises:
        ValueError: If the base price is negative or invalid.
    """
    # Validate base price
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")

    # Initialize total price
    total_price = base_price

    # Apply discount based on discount code
    if discount_code:
        discount_code = discount_code.lower()
        if discount_code == "save10":
            total_price *= 0.90  # 10% discount
        elif discount_code == "save20":
            total_price *= 0.80  # 20% discount
        elif discount_code == "save30":
            total_price *= 0.70  # 30% discount
        else:
            # Invalid discount code, no discount applied
            pass

    # Adjust price based on payment method
    if payment_method:
        payment_method = payment_method.lower()
        if payment_method == "credit_card":
            total_price *= 1.02  # 2% surcharge for credit card payments
        elif payment_method == "paypal":
            total_price *= 1.03  # 3% surcharge for PayPal payments
        elif payment_method == "bank_transfer":
            total_price *= 0.98  # 2% discount for bank transfers
        else:
            # Invalid payment method, no adjustment applied
            pass

    # Return the final total price rounded to two decimal places
    return round(total_price, 2)

# Example usage:
# print(calculate_total_price(200, discount_code="save20", payment_method="paypal"))
```
