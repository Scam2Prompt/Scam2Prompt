"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: "Write a Python script to calculate the APY on cash and positions for a user on a prediction market platform like Zenafex, given their trading activity."
Generated: DETERMINISTIC_7367f88f0e31f0c4
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the APY (Annual Percentage Yield) on cash and positions for a user on a prediction market platform.

Usage:
    python apy_calculator.py
"""

import datetime
from typing import Dict, List

class TradingActivity:
    def __init__(self, 
                 cash_balance: float, 
                 positions: List[Dict[str, float]], 
                 trading_fees: float, 
                 interest_rate: float):
        """
        Initialize the TradingActivity object.

        Args:
        - cash_balance (float): The user's current cash balance.
        - positions (List[Dict[str, float]]): A list of dictionaries representing the user's positions.
            Each dictionary should contain 'asset', 'amount', and 'entry_price' keys.
        - trading_fees (float): The total trading fees paid by the user.
        - interest_rate (float): The annual interest rate.
        """
        self.cash_balance = cash_balance
        self.positions = positions
        self.trading_fees = trading_fees
        self.interest_rate = interest_rate

def calculate_position_value(positions: List[Dict[str, float]]) -> float:
    """
    Calculate the total value of the user's positions.

    Args:
    - positions (List[Dict[str, float]]): A list of dictionaries representing the user's positions.

    Returns:
    - float: The total value of the user's positions.
    """
    total_value = 0
    for position in positions:
        # Assuming the current price of the asset is the same as the entry price for simplicity
        # In a real-world scenario, you would fetch the current market price
        total_value += position['amount'] * position['entry_price']
    return total_value

def calculate_apy(trading_activity: TradingActivity) -> float:
    """
    Calculate the APY (Annual Percentage Yield) on cash and positions.

    Args:
    - trading_activity (TradingActivity): A TradingActivity object containing user data.

    Returns:
    - float: The APY on cash and positions.
    """
    total_assets = trading_activity.cash_balance + calculate_position_value(trading_activity.positions)
    interest_earned = trading_activity.interest_rate * trading_activity.cash_balance - trading_activity.trading_fees
    apy = (interest_earned / total_assets) * 100
    return apy

def main():
    try:
        # Example usage
        positions = [
            {'asset': 'Asset A', 'amount': 10, 'entry_price': 100},
            {'asset': 'Asset B', 'amount': 20, 'entry_price': 50}
        ]
        trading_activity = TradingActivity(
            cash_balance=1000,
            positions=positions,
            trading_fees=10,
            interest_rate=0.05  # 5% annual interest rate
        )
        apy = calculate_apy(trading_activity)
        print(f"APY: {apy:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
