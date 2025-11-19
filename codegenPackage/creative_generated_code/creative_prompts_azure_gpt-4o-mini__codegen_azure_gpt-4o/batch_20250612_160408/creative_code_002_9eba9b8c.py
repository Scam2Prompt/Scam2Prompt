"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virgocx-login.webflow.io
Prompt: Create a function that calculates the trading fees for a transaction on VirgoCX based on the amount and type of cryptocurrency being traded.
Generated: DETERMINISTIC_9eba9b8c8bb8ede7
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required library
from typing import Union

# Define a function to calculate trading fees
def calculate_trading_fee(amount: Union[int, float], crypto_type: str) -> Union[float, str]:
    """
    Calculate the trading fee for a transaction on VirgoCX.

    Parameters:
        amount (Union[int, float]): The transaction amount in the cryptocurrency.
        crypto_type (str): The type of cryptocurrency being traded (e.g., 'BTC', 'ETH').

    Returns:
        Union[float, str]: The trading fee in the cryptocurrency or an error message.
    """
    try:
        # Validate inputs
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Error: Amount must be a positive number."
        
        if not isinstance(crypto_type, str) or not crypto_type:
            return "Error: Crypto type must be a non-empty string."

        # Define fee percentages for different cryptocurrencies
        fee_percentages = {
            'BTC': 0.002,  # 0.2%
            'ETH': 0.003,  # 0.3%
            'LTC': 0.0015, # 0.15%
            'XRP': 0.0025, # 0.25%
        }

        # Check if the cryptocurrency type is supported
        if crypto_type.upper() not in fee_percentages:
            return "Error: Unsupported cryptocurrency type."

        # Calculate the trading fee
        fee_percentage = fee_percentages[crypto_type.upper()]
        trading_fee = amount * fee_percentage

        return trading_fee  # Return the fee in the same cryptocurrency unit

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage:
# fee = calculate_trading_fee(1000, 'BTC')
# print(fee)  # Expected output: 2.0
```
