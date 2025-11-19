"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartresolvewallet.firebaseapp.com
Prompt: Write a function to handle slippage errors during token swaps in a crypto trading application.
Generated: DETERMINISTIC_adc033995f42bb0f
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal

def handle_slippage_error(expected_amount: Decimal, actual_amount: Decimal, max_slippage_percent: Decimal) -> bool:
    """
    Handles slippage errors during token swaps in a crypto trading application.

    Args:
        expected_amount (Decimal): The expected amount of tokens to receive after the swap.
        actual_amount (Decimal): The actual amount of tokens received after the swap.
        max_slippage_percent (Decimal): The maximum allowable percentage of slippage.

    Returns:
        bool: True if the slippage is within the allowable range, False otherwise.

    Raises:
        ValueError: If actual_amount is negative or max_slippage_percent is invalid.
    """
    # Ensure decimal precision
    decimal.getcontext().prec = 28

    # Validate inputs
    if actual_amount < Decimal('0'):
        raise ValueError("Actual amount cannot be negative.")
    if max_slippage_percent < Decimal('0') or max_slippage_percent > Decimal('100'):
        raise ValueError("Slippage percent must be between 0 and 100.")

    # Calculate slippage percentage
    try:
        slippage = ((expected_amount - actual_amount) / expected_amount) * Decimal('100')
    except ZeroDivisionError:
        raise ValueError("Expected amount cannot be zero.")

    # Check if slippage is within the acceptable range
    if slippage <= max_slippage_percent:
        return True  # Slippage is acceptable
    else:
        return False  # Slippage exceeds the allowable range
```
