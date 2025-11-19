"""
Generated Code Metadata:
========================
Original URL: https://algobitmarket.com
Prompt: Write a function to calculate spreads and leverage for AlgoBitMarket's BASIC and PREMIUM account types based on the provided trading conditions.
Generated: DETERMINISTIC_5720da3905f2b783
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class AccountType(str, Enum):
    """Enum for account types."""
    BASIC = "BASIC"
    PREMIUM = "PREMIUM"

class TradingConditions:
    """Class to hold trading conditions."""
    def __init__(self, account_type: AccountType, instrument: str, 
                 min_leverage: float, max_leverage: float, 
                 min_spread: float, max_spread: float):
        """
        Initialize TradingConditions.

        Args:
        - account_type (AccountType): The type of account.
        - instrument (str): The trading instrument.
        - min_leverage (float): The minimum leverage.
        - max_leverage (float): The maximum leverage.
        - min_spread (float): The minimum spread.
        - max_spread (float): The maximum spread.
        """
        self.account_type = account_type
        self.instrument = instrument
        self.min_leverage = min_leverage
        self.max_leverage = max_leverage
        self.min_spread = min_spread
        self.max_spread = max_spread

def calculate_spreads_and_leverage(trading_conditions: TradingConditions, 
                                   leverage: float, spread: float) -> Dict[str, float]:
    """
    Calculate spreads and leverage for AlgoBitMarket's account types.

    Args:
    - trading_conditions (TradingConditions): The trading conditions.
    - leverage (float): The leverage to use.
    - spread (float): The spread to use.

    Returns:
    - A dictionary with 'leverage' and 'spread'.

    Raises:
    - ValueError: If leverage or spread is out of range.
    """
    if leverage < trading_conditions.min_leverage or leverage > trading_conditions.max_leverage:
        raise ValueError(f"Leverage must be between {trading_conditions.min_leverage} and {trading_conditions.max_leverage}")
    
    if spread < trading_conditions.min_spread or spread > trading_conditions.max_spread:
        raise ValueError(f"Spread must be between {trading_conditions.min_spread} and {trading_conditions.max_spread}")

    # For BASIC account type, apply a 10% reduction in leverage
    if trading_conditions.account_type == AccountType.BASIC:
        effective_leverage = leverage * 0.9
    else:
        effective_leverage = leverage

    return {
        'leverage': effective_leverage,
        'spread': spread
    }

# Example usage
if __name__ == "__main__":
    basic_conditions = TradingConditions(
        AccountType.BASIC, 
        "EUR/USD", 
        1.0, 
        100.0, 
        0.1, 
        10.0
    )

    premium_conditions = TradingConditions(
        AccountType.PREMIUM, 
        "EUR/USD", 
        1.0, 
        500.0, 
        0.05, 
        5.0
    )

    basic_result = calculate_spreads_and_leverage(basic_conditions, 50.0, 2.0)
    premium_result = calculate_spreads_and_leverage(premium_conditions, 200.0, 1.5)

    print("BASIC Account:", basic_result)
    print("PREMIUM Account:", premium_result)

    try:
        calculate_spreads_and_leverage(basic_conditions, 1000.0, 2.0)
    except ValueError as e:
        print("Error:", e)
```
