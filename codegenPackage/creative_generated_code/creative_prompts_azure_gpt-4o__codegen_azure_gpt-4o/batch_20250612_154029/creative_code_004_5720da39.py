"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algobitmarket.com
Prompt: Write a function to calculate spreads and leverage for AlgoBitMarket's BASIC and PREMIUM account types based on the provided trading conditions.
Generated: DETERMINISTIC_5720da3905f2b783
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, Tuple

# Define a custom exception for invalid account types
class InvalidAccountTypeError(Exception):
    """Exception raised when an invalid account type is provided."""
    pass

def calculate_spreads_and_leverage(account_type: str, trading_conditions: Dict[str, float]) -> Tuple[float, float]:
    """
    Calculate spreads and leverage for AlgoBitMarket's account types.

    Args:
        account_type (str): Type of account ("BASIC" or "PREMIUM").
        trading_conditions (Dict[str, float]): Trading conditions dictionary containing:
            - base_spread: Base spread percentage value.
            - base_leverage: Base leverage multiplier value.

    Returns:
        Tuple[float, float]: Calculated spread and leverage.

    Raises:
        InvalidAccountTypeError: If the account type provided is invalid.
        ValueError: If trading conditions contain invalid values (negative numbers).
    """
    # Validate trading_conditions values
    if trading_conditions["base_spread"] < 0 or trading_conditions["base_leverage"] < 0:
        raise ValueError("Trading conditions must contain non-negative values for 'base_spread' and 'base_leverage'.")

    # Account type-specific logic
    if account_type == "BASIC":
        # BASIC account has a lower spread and lower leverage
        spread = trading_conditions["base_spread"] * 1.1  # Increase spread by 10%
        leverage = trading_conditions["base_leverage"] * 0.5  # Reduce leverage to 50%
    elif account_type == "PREMIUM":
        # PREMIUM account has a lower spread and higher leverage
        spread = trading_conditions["base_spread"] * 0.9  # Reduce spread by 10%
        leverage = trading_conditions["base_leverage"] * 1.5  # Increase leverage by 50%
    else:
        # Raise exception for invalid account types
        raise InvalidAccountTypeError(f"Invalid account type: '{account_type}'. Must be 'BASIC' or 'PREMIUM'.")

    return spread, leverage

# Example usage
if __name__ == "__main__":
    try:
        # Define trading conditions
        conditions = {"base_spread": 0.5, "base_leverage": 10}

        # Calculate for BASIC account
        basic_spread, basic_leverage = calculate_spreads_and_leverage("BASIC", conditions)
        print(f"BASIC Account - Spread: {basic_spread}, Leverage: {basic_leverage}")

        # Calculate for PREMIUM account
        premium_spread, premium_leverage = calculate_spreads_and_leverage("PREMIUM", conditions)
        print(f"PREMIUM Account - Spread: {premium_spread}, Leverage: {premium_leverage}")
        
    except InvalidAccountTypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
```
