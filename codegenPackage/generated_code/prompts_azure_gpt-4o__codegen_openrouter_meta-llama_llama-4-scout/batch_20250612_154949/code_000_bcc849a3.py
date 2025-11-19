"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write Python code to calculate a discount of 5% for purchases made via Pix payment, as described on the ebrasilbrazz website.
Generated: DETERMINISTIC_bcc849a3d89daf54
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module to calculate discount for purchases made via Pix payment.

Discount: 5% off for Pix payments.
"""

def calculate_pix_discount(original_price: float) -> float:
    """
    Calculate 5% discount for Pix payments.

    Args:
        original_price (float): Original price of the purchase.

    Returns:
        float: Price after applying 5% discount.

    Raises:
        ValueError: If original price is negative.
    """
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")

    discount_percentage = 0.05  # 5% discount
    discount_amount = original_price * discount_percentage
    discounted_price = original_price - discount_amount

    return discounted_price


def main():
    try:
        original_price = float(input("Enter the original price: R$ "))
        discounted_price = calculate_pix_discount(original_price)
        print(f"Discounted price for Pix payment: R$ {discounted_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
