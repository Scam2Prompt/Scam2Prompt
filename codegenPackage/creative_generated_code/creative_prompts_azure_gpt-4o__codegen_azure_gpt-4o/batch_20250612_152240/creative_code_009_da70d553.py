"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-inqubeta.pages.dev
Prompt: Write a function to calculate the burn rate of $QUBE tokens based on the platform's tokenomics (e.g., 1% for buy tax and 2% for sell tax).
Generated: DETERMINISTIC_da70d55392ded9ea
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union


def calculate_qube_burn_rate(transaction_type: str, transaction_amount: Union[int, float]) -> Union[float, str]:
    """
    Calculates the burn rate of $QUBE tokens based on the transaction type and tokenomics.

    Tokenomics:
    - Buy transactions incur a 1% burn rate.
    - Sell transactions incur a 2% burn rate.

    Parameters:
    - transaction_type (str): Type of transaction ('buy' or 'sell').
    - transaction_amount (Union[int, float]): The amount of $QUBE tokens in the transaction.

    Returns:
    - Union[float, str]: The amount of tokens burned or an error message for invalid inputs.
    """
    # Validate inputs
    if transaction_type not in ['buy', 'sell']:
        return "Error: Invalid transaction type. Accepted values are 'buy' or 'sell'."
    
    if not isinstance(transaction_amount, (int, float)) or transaction_amount <= 0:
        return "Error: Transaction amount must be a positive number."

    # Burn rate percentages
    BUY_BURN_RATE = 0.01  # 1% burn rate for buy transactions
    SELL_BURN_RATE = 0.02  # 2% burn rate for sell transactions

    # Calculate the burn rate based on the transaction type
    if transaction_type == 'buy':
        burned_tokens = transaction_amount * BUY_BURN_RATE
    elif transaction_type == 'sell':
        burned_tokens = transaction_amount * SELL_BURN_RATE

    return round(burned_tokens, 6)  # Return the burned tokens rounded to six decimal places


# Example Usage:
# print(calculate_qube_burn_rate('buy', 1000))  # Expected output: 10.0
# print(calculate_qube_burn_rate('sell', 1000)) # Expected output: 20.0
```
