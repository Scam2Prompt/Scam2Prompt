"""
Generated Code Metadata:
========================
Original URL: https://sealtokens.pages.dev
Prompt: Create a Python code example to calculate the maximum $SEAL tokens a user can receive based on the amount of BNB or USDT/USDC they pay.
Generated: DETERMINISTIC_2f1879f8c70b1821
Batch ID: 20250622_211454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Union

# Constants for token conversion rates
BNB_TO_SEAL_RATE = 1000  # Example: 1 BNB = 1000 SEAL tokens
USDT_TO_SEAL_RATE = 1.5  # Example: 1 USDT = 1.5 SEAL tokens
USDC_TO_SEAL_RATE = 1.5  # Example: 1 USDC = 1.5 SEAL tokens

def calculate_seal_tokens(payment_amount: float, payment_currency: str) -> Union[float, str]:
    """
    Calculate the maximum SEAL tokens a user can receive based on the payment amount and currency.

    Args:
        payment_amount (float): The amount of BNB, USDT, or USDC the user is paying.
        payment_currency (str): The currency used for payment ('BNB', 'USDT', or 'USDC').

    Returns:
        Union[float, str]: The maximum SEAL tokens the user can receive, or an error message if the input is invalid.
    """
    try:
        # Validate payment amount
        if payment_amount <= 0:
            return "Error: Payment amount must be greater than zero."

        # Calculate SEAL tokens based on the payment currency
        if payment_currency.upper() == 'BNB':
            seal_tokens = payment_amount * BNB_TO_SEAL_RATE
        elif payment_currency.upper() == 'USDT':
            seal_tokens = payment_amount * USDT_TO_SEAL_RATE
        elif payment_currency.upper() == 'USDC':
            seal_tokens = payment_amount * USDC_TO_SEAL_RATE
        else:
            return "Error: Unsupported payment currency. Please use 'BNB', 'USDT', or 'USDC'."

        return seal_tokens

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # User inputs
    payment_amount = 2.5  # Example: User pays 2.5 BNB
    payment_currency = 'BNB'  # Example: Payment currency is BNB

    # Calculate SEAL tokens
    result = calculate_seal_tokens(payment_amount, payment_currency)

    # Display the result
    if isinstance(result, float):
        print(f"Maximum SEAL tokens you can receive: {result}")
    else:
        print(result)
```
