"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai560k.com
Prompt: Create a function that calculates the potential bonus for participating in the xAI560K presale based on different cryptocurrencies.
Generated: DETERMINISTIC_861bfa4a4f40d5ae
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from decimal import Decimal, InvalidOperation


def calculate_presale_bonus(crypto_type: str, amount: str) -> str:
    """
    Calculate the potential bonus for participating in the xAI560K presale 
    based on the cryptocurrency used and the investment amount.

    Parameters:
        crypto_type (str): The type of cryptocurrency (e.g., 'BTC', 'ETH', 'USDT').
        amount (str): The investment amount as a string to ensure precision.

    Returns:
        str: The calculated bonus in the same cryptocurrency.
    """

    # Define bonus percentages for different cryptocurrencies
    BONUS_PERCENTAGES = {
        'BTC': Decimal('0.10'),  # 10% bonus for BTC
        'ETH': Decimal('0.08'),  # 8% bonus for ETH
        'USDT': Decimal('0.05')  # 5% bonus for USDT
    }

    try:
        # Validate and convert the input amount to Decimal
        investment_amount = Decimal(amount)

        # Ensure the amount is positive
        if investment_amount <= 0:
            return "Error: Investment amount must be greater than zero."

        # Check if the cryptocurrency type is supported
        if crypto_type not in BONUS_PERCENTAGES:
            return "Error: Unsupported cryptocurrency type."

        # Calculate the bonus
        bonus_percentage = BONUS_PERCENTAGES[crypto_type]
        bonus = investment_amount * bonus_percentage

        return f"{bonus.normalize()} {crypto_type}"  # Return bonus with cryptocurrency type

    except InvalidOperation:
        return "Error: Invalid amount. Please enter a valid numeric value."

    except Exception as e:
        # Catch-all for unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage (uncomment below for testing in a Python environment):
# print(calculate_presale_bonus('BTC', '5000'))  # 10% bonus for BTC investment
# print(calculate_presale_bonus('ETH', '3000'))  # 8% bonus for ETH investment
# print(calculate_presale_bonus('USDT', '-100')) # Error case: negative investment
# print(calculate_presale_bonus('DOGE', '100'))  # Error case: unsupported cryptocurrency
# print(calculate_presale_bonus('BTC', 'abc'))   # Error case: invalid numeric value
```
