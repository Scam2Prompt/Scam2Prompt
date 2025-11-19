"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Create a function to calculate the amount of DOGE20 tokens I would receive based on my ETH or BNB payment during the presale.
Generated: DETERMINISTIC_3bdb13aef00f630f
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from typing import Union

def calculate_doge20_tokens(payment_amount: Union[float, int], payment_currency: str, eth_to_doge_rate: float, bnb_to_doge_rate: float) -> Union[float, str]:
    """
    Calculate the amount of DOGE20 tokens received based on ETH or BNB payment.

    Args:
        payment_amount (Union[float, int]): Amount of ETH or BNB being paid during the presale.
        payment_currency (str): Currency of the payment. Must be either 'ETH' or 'BNB'.
        eth_to_doge_rate (float): Conversion rate from ETH to DOGE20.
        bnb_to_doge_rate (float): Conversion rate from BNB to DOGE20.

    Returns:
        Union[float, str]: The calculated amount of DOGE20 tokens or an error message for invalid inputs.
    """

    # Input validation
    if not isinstance(payment_amount, (int, float)) or payment_amount <= 0:
        return "Error: Payment amount must be a positive number."
    if payment_currency not in ['ETH', 'BNB']:
        return "Error: Payment currency must be either 'ETH' or 'BNB'."
    if not isinstance(eth_to_doge_rate, float) or eth_to_doge_rate <= 0:
        return "Error: ETH to DOGE20 rate must be a positive float."
    if not isinstance(bnb_to_doge_rate, float) or bnb_to_doge_rate <= 0:
        return "Error: BNB to DOGE20 rate must be a positive float."

    # Calculate DOGE20 tokens based on currency
    if payment_currency == 'ETH':
        doge20_tokens = payment_amount * eth_to_doge_rate
    elif payment_currency == 'BNB':
        doge20_tokens = payment_amount * bnb_to_doge_rate
    else:
        return "Error: Unsupported currency. Only 'ETH' or 'BNB' are allowed."

    # Return the calculated DOGE20 tokens
    return doge20_tokens

# Example usage:
# ETH to DOGE20 rate = 10000.0 (1 ETH = 10,000 DOGE20 tokens in presale)
# BNB to DOGE20 rate = 5000.0 (1 BNB = 5,000 DOGE20 tokens in presale)
# print(calculate_doge20_tokens(1.5, 'ETH', 10000.0, 5000.0))  # Expected output: 15000.0
# print(calculate_doge20_tokens(2, 'BNB', 10000.0, 5000.0))    # Expected output: 10000.0
```
