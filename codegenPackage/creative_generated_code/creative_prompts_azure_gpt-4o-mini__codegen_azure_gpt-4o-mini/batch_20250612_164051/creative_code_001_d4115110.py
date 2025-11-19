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
def calculate_total_price(base_price, discount_percentage=0, payment_method='credit_card'):
    """
    Calculate the total price of a gaming chair purchase.

    Args:
        base_price (float): The base price of the gaming chair.
        discount_percentage (float, optional): Percentage discount to apply. Defaults to 0.
        payment_method (str, optional): The payment method used. Defaults to 'credit_card'.
    
    Returns:
        float: The total price after discount and any payment method fees.
    
    Raises:
        ValueError: If base_price is negative or discount_percentage is not between 0 and 100.
    """
    
    # Validate input parameters
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * base_price
    
    # Calculate the price after discount
    discounted_price = base_price - discount_amount
    
    # Define payment method fees
    payment_fees = {
        'credit_card': 0.02,  # 2% fee for credit card
        'paypal': 0.03,       # 3% fee for PayPal
        'bank_transfer': 0.01  # 1% fee for bank transfer
    }
    
    # Validate payment method
    if payment_method not in payment_fees:
        raise ValueError("Invalid payment method. Choose from 'credit_card', 'paypal', or 'bank_transfer'.")
    
    # Calculate the total fee based on the chosen payment method
    fee_percentage = payment_fees[payment_method]
    total_fee = discounted_price * fee_percentage
    
    # Calculate the total price after applying fees
    total_price = discounted_price + total_fee
    
    return round(total_price, 2)

# Example usage
if __name__ == "__main__":
    try:
        total = calculate_total_price(base_price=300.00, discount_percentage=10, payment_method='paypal')
        print(f"The total price for the gaming chair is: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
