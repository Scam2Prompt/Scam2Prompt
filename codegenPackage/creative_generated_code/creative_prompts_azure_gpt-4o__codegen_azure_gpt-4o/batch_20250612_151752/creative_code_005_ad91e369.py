"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: Write a function to calculate the total deposit and withdrawal amounts for a trading platform, similar to the statistics displayed on Tradezeenetwork.
Generated: DETERMINISTIC_ad91e369750a9ab2
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple

def calculate_deposit_withdrawal(transactions: List[Dict[str, float]]) -> Tuple[float, float]:
    """
    Calculates the total deposit and withdrawal amounts from a list of transactions.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries. 
                                              Each dictionary contains:
                                                - 'type': A string representing the transaction type ('deposit' or 'withdrawal').
                                                - 'amount': A float representing the transaction amount.

    Returns:
        Tuple[float, float]: A tuple containing:
                             - Total deposit amount (float).
                             - Total withdrawal amount (float).

    Raises:
        ValueError: If a transaction contains unsupported 'type' or missing 'amount'.
    """
    
    # Initialize totals for deposit and withdrawal.
    total_deposit = 0.0
    total_withdrawal = 0.0

    # Iterate through all transactions.
    for transaction in transactions:
        # Validate the transaction type and amount.
        if 'type' not in transaction or 'amount' not in transaction:
            raise ValueError("Transaction must contain 'type' and 'amount' fields.")
        if not isinstance(transaction['amount'], (int, float)):
            raise ValueError("'amount' must be a numeric value.")
        
        # Process the transaction based on its type.
        if transaction['type'] == 'deposit':
            total_deposit += transaction['amount']  # Accumulate the deposit amount.
        elif transaction['type'] == 'withdrawal':
            total_withdrawal += transaction['amount']  # Accumulate the withdrawal amount.
        else:
            raise ValueError("Unsupported transaction type. Must be 'deposit' or 'withdrawal'.")

    return total_deposit, total_withdrawal

# Example usage (uncomment to test the function):
# transactions = [
#     {'type': 'deposit', 'amount': 100.0},
#     {'type': 'withdrawal', 'amount': 50.0},
#     {'type': 'deposit', 'amount': 200.0},
#     {'type': 'withdrawal', 'amount': 75.5}
# ]
# print(calculate_deposit_withdrawal(transactions))  # Output: (300.0, 125.5)
```
