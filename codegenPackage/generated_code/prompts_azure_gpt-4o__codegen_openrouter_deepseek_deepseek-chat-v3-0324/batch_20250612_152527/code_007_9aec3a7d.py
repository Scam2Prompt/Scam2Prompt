"""
Generated Code Metadata:
========================
Original URL: https://app-virtuswap.pages.dev
Prompt: Write a function to calculate token balances before and after a swap, inspired by the balance tracking in Virtuswap's "You sell" and "You buy" fields.
Generated: DETERMINISTIC_9aec3a7d97b64c07
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Tuple
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 28

def calculate_token_balances(
    initial_balances: Dict[str, Decimal],
    token_in: str,
    token_out: str,
    amount_in: Decimal,
    amount_out: Decimal,
    fee_percentage: Decimal = Decimal('0')
) -> Tuple[Dict[str, Decimal], Dict[str, Decimal]]:
    """
    Calculate token balances before and after a swap with optional fee deduction.
    
    Args:
        initial_balances: Dictionary of initial token balances (token_symbol: balance)
        token_in: The token being sold/swapped in
        token_out: The token being bought/swapped out
        amount_in: The amount of token_in being swapped
        amount_out: The amount of token_out being received
        fee_percentage: The fee percentage to deduct from amount_in (default: 0)
        
    Returns:
        Tuple of (balances_before, balances_after) dictionaries
        
    Raises:
        ValueError: If token_in or token_out not in initial_balances
                  If amount_in or amount_out is negative
                  If fee_percentage is negative or >= 100
    """
    # Input validation
    if token_in not in initial_balances or token_out not in initial_balances:
        raise ValueError("Token symbols must exist in initial balances")
    
    if amount_in < 0 or amount_out < 0:
        raise ValueError("Amounts cannot be negative")
    
    if fee_percentage < 0 or fee_percentage >= 100:
        raise ValueError("Fee percentage must be between 0 and 100")
    
    # Create copies of initial balances for before and after states
    balances_before = initial_balances.copy()
    
    # Calculate actual amount in after fee deduction
    fee_amount = amount_in * (fee_percentage / Decimal('100'))
    actual_amount_in = amount_in - fee_amount
    
    # Calculate balances after swap
    balances_after = initial_balances.copy()
    balances_after[token_in] -= actual_amount_in
    balances_after[token_out] += amount_out
    
    return balances_before, balances_after
```
