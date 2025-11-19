"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Write a Python function that calculates the total price of a gaming chair purchase, including discounts and payment methods as described on the dhcpbrazz website.
Generated: DETERMINISTIC_d4115110c94724f3
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

def calculate_total_price(base_price, discount_rate=0, payment_method="credit_card"):
    """
    Calculates the total price of a gaming chair purchase, including discounts and special charges
    based on the payment method.

    Args:
        base_price (float): The original price of the gaming chair.
        discount_rate (float): Discount rate as a percentage (e.g., 10 for 10%).
        payment_method (str): Payment method, e.g., "credit_card", "paypal", or "bank_transfer".

    Returns:
        float: The final price after applying discounts and payment method adjustments.

    Raises:
        ValueError: If base_price is negative or if discount_rate is invalid.
        KeyError: If the payment_method is unsupported.
    """
    logging.basicConfig(level=logging.INFO)
    
    # Validate input parameters
    if base_price < 0:
        raise ValueError("Base price must be a non-negative number.")
    if not (0 <= discount_rate <= 100):
        raise ValueError("Discount rate must be between 0 and 100.")
    
    # Supported payment methods and their respective fees/discounts
    payment_method_adjustments = {
        "credit_card": 0,          # No adjustment for credit card
        "paypal": 0.02,           # 2% fee for PayPal
        "bank_transfer": -0.01    # 1% discount for bank transfer
    }

    if payment_method not in payment_method_adjustments:
        raise KeyError(f"Unsupported payment method: {payment_method}. Choose from {list(payment_method_adjustments.keys())}.")

    # Calculate the discounted price
    discount = base_price * (discount_rate / 100)
    discounted_price = base_price - discount

    # Apply payment method adjustments
    adjustment_rate = payment_method_adjustments[payment_method]
    final_price = discounted_price * (1 + adjustment_rate)

    logging.info(f"Base price: {base_price}, Discount: {discount}, Payment method adjustment: {adjustment_rate * discounted_price}, Final price: {final_price}")

    return round(final_price, 2)


# Example usage
if __name__ == "__main__":
    try:
        # A gaming chair with a base price of $300, a discount of 10%, and purchased via PayPal.
        total_price = calculate_total_price(base_price=300, discount_rate=10, payment_method="paypal")
        print(f"The total price of the gaming chair is: ${total_price}")
    except (ValueError, KeyError) as e:
        logging.error(e)
```
