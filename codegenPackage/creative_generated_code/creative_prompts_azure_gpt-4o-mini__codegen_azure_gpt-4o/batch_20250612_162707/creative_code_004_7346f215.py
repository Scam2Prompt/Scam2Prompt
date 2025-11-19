"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-heist-giveaway.web.app
Prompt: Create a function that calculates the total price for a transaction using the Helio platform, considering the TPS and payment methods available.
Generated: DETERMINISTIC_7346f2152b865fd5
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_total_price(base_price, tps_rate, payment_method):
    """
    Calculate the total price for a transaction using the Helio platform.

    Parameters:
    - base_price (float): The base price of the transaction.
    - tps_rate (float): The transaction processing fee rate (TPS) as a percentage (e.g., 2.5 for 2.5%).
    - payment_method (str): The payment method used. Supported methods are 'credit_card', 'bank_transfer', and 'crypto'.

    Returns:
    - dict: A dictionary containing the 'base_price', 'tps_fee', 'total_price',
            and 'payment_method' for the transaction.

    Raises:
    - ValueError: If an unsupported payment method is provided.
    """
    try:
        # Ensure base_price and tps_rate are valid numbers
        base_price = decimal.Decimal(base_price)
        tps_rate = decimal.Decimal(tps_rate)
        
        if base_price < 0 or tps_rate < 0:
            raise ValueError("Base price and TPS rate must be non-negative.")
        
        # List of supported payment methods
        SUPPORTED_PAYMENT_METHODS = {'credit_card', 'bank_transfer', 'crypto'}
        
        # Validate payment method
        if payment_method not in SUPPORTED_PAYMENT_METHODS:
            raise ValueError(f"Unsupported payment method: {payment_method}. Supported methods are {', '.join(SUPPORTED_PAYMENT_METHODS)}.")
        
        # Calculate TPS fee
        tps_fee = base_price * (tps_rate / 100)
        
        # Calculate total price
        total_price = base_price + tps_fee
        
        # Prepare the transaction result
        transaction_result = {
            "base_price": float(base_price),
            "tps_fee": float(tps_fee),
            "total_price": float(total_price),
            "payment_method": payment_method
        }
        
        return transaction_result

    except decimal.InvalidOperation:
        raise ValueError("Invalid numeric input for base price or TPS rate.")
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"An error occurred while calculating the total price: {str(e)}")

# Example usage:
# result = calculate_total_price(120.50, 2.5, 'credit_card')
# print(result)
```
