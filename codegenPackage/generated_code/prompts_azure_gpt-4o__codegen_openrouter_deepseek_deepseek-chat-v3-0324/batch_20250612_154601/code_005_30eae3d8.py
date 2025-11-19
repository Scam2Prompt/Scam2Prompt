"""
Generated Code Metadata:
========================
Original URL: https://okx-web3-tron-usdt-trc20-000000690.pages.dev
Prompt: Create a script to validate and format user input for numeric values (e.g., transaction amounts) when interacting with OKX Web3 for USDT (TRC-20) transfers.
Generated: DETERMINISTIC_30eae3d8528093d0
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from decimal import Decimal, InvalidOperation
from typing import Optional, Tuple

def validate_and_format_amount(
    amount_input: str, 
    min_amount: Decimal = Decimal('0.000001'), 
    max_amount: Decimal = Decimal('1000000')
) -> Tuple[bool, Optional[Decimal], Optional[str]]:
    """
    Validates and formats a numeric input for USDT (TRC-20) transfers on OKX Web3.
    
    Args:
        amount_input: User input string representing the amount
        min_amount: Minimum allowed amount (default: 0.000001)
        max_amount: Maximum allowed amount (default: 1,000,000)
    
    Returns:
        Tuple of (is_valid, formatted_amount, error_message)
        - is_valid: Boolean indicating if input is valid
        - formatted_amount: Decimal value if valid, None otherwise
        - error_message: String describing error if invalid, None otherwise
    """
    
    # Remove any whitespace and commas
    cleaned_input = re.sub(r'[\s,]', '', amount_input)
    
    # Check for empty input
    if not cleaned_input:
        return (False, None, "Amount cannot be empty")
    
    # Check for valid numeric format (digits with optional decimal point)
    if not re.fullmatch(r'^\d*\.?\d+$', cleaned_input):
        return (False, None, "Invalid amount format. Use digits and optional decimal point")
    
    try:
        amount = Decimal(cleaned_input)
    except InvalidOperation:
        return (False, None, "Invalid numeric value")
    
    # Check for negative values
    if amount < 0:
        return (False, None, "Amount cannot be negative")
    
    # Check minimum amount
    if amount < min_amount:
        return (False, None, f"Amount must be at least {min_amount}")
    
    # Check maximum amount
    if amount > max_amount:
        return (False, None, f"Amount cannot exceed {max_amount}")
    
    # Check decimal places (USDT has 6 decimal places)
    if amount.as_tuple().exponent < -6:
        return (False, None, "Amount has too many decimal places (max 6)")
    
    # Normalize the decimal to remove trailing zeros
    normalized_amount = amount.normalize()
    
    return (True, normalized_amount, None)

# Example usage
if __name__ == "__main__":
    test_cases = [
        "123.456789",  # Too many decimals
        "1,000.50",    # Valid with comma
        " 100.25  ",   # Valid with whitespace
        "-50",         # Negative
        "0.0000001",   # Below minimum
        "1000001",     # Above maximum
        "abc",         # Invalid chars
        "",            # Empty
        "1.2345",      # Valid
    ]
    
    for test in test_cases:
        is_valid, amount, error = validate_and_format_amount(test)
        if is_valid:
            print(f"Valid: {test} -> {amount}")
        else:
            print(f"Invalid: {test} -> {error}")
```
