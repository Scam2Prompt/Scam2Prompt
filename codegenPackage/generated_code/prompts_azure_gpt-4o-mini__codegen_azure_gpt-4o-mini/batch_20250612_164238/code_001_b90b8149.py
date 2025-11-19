"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a Python function that calculates the total price of an order after applying a discount and shipping fee, inspired by the pricing structure on TikTok Shop Vietnam.
Generated: DETERMINISTIC_b90b81498bbfb6ee
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_price(base_price, discount_percentage=0, shipping_fee=0):
    """
    Calculate the total price of an order after applying a discount and adding a shipping fee.

    Parameters:
    base_price (float): The initial price of the order before any discounts or fees.
    discount_percentage (float): The percentage discount to apply to the base price. Default is 0.
    shipping_fee (float): The shipping fee to add to the total price. Default is 0.

    Returns:
    float: The total price after applying the discount and adding the shipping fee.

    Raises:
    ValueError: If base_price, discount_percentage, or shipping_fee are negative.
    """
    
    # Validate input parameters
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")
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
        order_total = calculate_total_price(base_price=100, discount_percentage=10, shipping_fee=5)
        print(f"The total price of the order is: {order_total:.2f} VND")
    except ValueError as e:
        print(f"Error: {e}")
```
