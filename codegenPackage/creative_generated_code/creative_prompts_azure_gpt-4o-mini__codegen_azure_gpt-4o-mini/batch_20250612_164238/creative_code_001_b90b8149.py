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
    - base_price (float): The initial price of the order.
    - discount_percentage (float): The discount percentage to be applied (0-100).
    - shipping_fee (float): The shipping fee to be added after discount.

    Returns:
    - float: The total price after applying the discount and adding the shipping fee.

    Raises:
    - ValueError: If base_price, discount_percentage, or shipping_fee are negative.
    - ValueError: If discount_percentage is greater than 100.
    """
    
    # Validate inputs
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100.")
    if shipping_fee < 0:
        raise ValueError("Shipping fee cannot be negative.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * base_price
    
    # Calculate the total price
    total_price = base_price - discount_amount + shipping_fee
    
    # Ensure total price is not negative
    if total_price < 0:
        total_price = 0

    return total_price

# Example usage
if __name__ == "__main__":
    try:
        total = calculate_order_total(100.0, 10.0, 5.0)
        print(f"The total price of the order is: {total:.2f}")
    except ValueError as e:
        print(f"Error calculating total price: {e}")
```
