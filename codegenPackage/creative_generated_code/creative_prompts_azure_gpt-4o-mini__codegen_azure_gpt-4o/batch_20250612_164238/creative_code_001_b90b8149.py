"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a Python function that calculates the total price of an order after applying a discount and shipping fee, inspired by the pricing structure on TikTok Shop Vietnam.
Generated: DETERMINISTIC_b90b81498bbfb6ee
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_order_total(base_price, discount_percentage, shipping_fee):
    """
    Calculate the total price of an order after applying a discount and adding a shipping fee.

    Parameters:
        base_price (float): The original price of the products in the order.
        discount_percentage (float): The discount percentage to apply (e.g., 20 for 20%).
        shipping_fee (float): The flat shipping fee to be added.

    Returns:
        float: The total price of the order after discount and shipping fee.

    Raises:
        ValueError: If any of the inputs are negative.
    """
    # Input validation
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")
    if shipping_fee < 0:
        raise ValueError("Shipping fee cannot be negative.")

    # Calculate discount amount
    discount_amount = (discount_percentage / 100) * base_price

    # Calculate final price after discount
    price_after_discount = base_price - discount_amount

    # Ensure price never goes below zero
    price_after_discount = max(price_after_discount, 0)

    # Calculate total price by adding the shipping fee
    total_price = price_after_discount + shipping_fee

    return round(total_price, 2)  # Return rounded total price for better readability


# Example usage
if __name__ == "__main__":
    try:
        base_price = 1000  # Base price in currency units
        discount_percentage = 20  # Discount percentage
        shipping_fee = 50  # Shipping fee in currency units

        total = calculate_order_total(base_price, discount_percentage, shipping_fee)
        print(f"The total price of the order is: {total}")
    except ValueError as e:
        print(f"Error: {e}")
```
