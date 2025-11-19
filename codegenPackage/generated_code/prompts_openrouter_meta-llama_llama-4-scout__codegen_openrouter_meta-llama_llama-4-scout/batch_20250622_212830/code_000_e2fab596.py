"""
Generated Code Metadata:
========================
Original URL: https://shadow-exchange.com
Prompt: "Write a Python code snippet to implement a dynamic fee system for a trading platform like Shadow Exchange, taking into account market activity and customizable fee splits."
Generated: DETERMINISTIC_e2fab5963883ef96
Batch ID: 20250622_212830
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

class MarketActivity(Enum):
    """Enum to represent market activity levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class FeeType(Enum):
    """Enum to represent fee types."""
    TRANSACTION = 1
    WITHDRAWAL = 2

class DynamicFeeSystem:
    """Dynamic fee system class."""

    def __init__(self, 
                 base_fee: float, 
                 market_activity_fees: Dict[MarketActivity, float], 
                 fee_splits: Dict[FeeType, float]):
        """
        Initialize the dynamic fee system.

        Args:
        - base_fee (float): The base fee for transactions.
        - market_activity_fees (Dict[MarketActivity, float]): Fees based on market activity.
        - fee_splits (Dict[FeeType, float]): Customizable fee splits.
        """
        self.base_fee = base_fee
        self.market_activity_fees = market_activity_fees
        self.fee_splits = fee_splits

    def calculate_fee(self, market_activity: MarketActivity, fee_type: FeeType) -> float:
        """
        Calculate the dynamic fee based on market activity and fee type.

        Args:
        - market_activity (MarketActivity): The current market activity level.
        - fee_type (FeeType): The type of fee.

        Returns:
        - float: The calculated dynamic fee.

        Raises:
        - ValueError: If market activity or fee type is not supported.
        """
        if market_activity not in self.market_activity_fees:
            raise ValueError("Unsupported market activity level.")
        if fee_type not in self.fee_splits:
            raise ValueError("Unsupported fee type.")

        market_fee = self.market_activity_fees[market_activity]
        fee_split = self.fee_splits[fee_type]
        dynamic_fee = self.base_fee + (market_fee * fee_split)
        return dynamic_fee

def main():
    # Example usage
    base_fee = 0.001
    market_activity_fees = {
        MarketActivity.LOW: 0.0001,
        MarketActivity.MEDIUM: 0.0005,
        MarketActivity.HIGH: 0.001
    }
    fee_splits = {
        FeeType.TRANSACTION: 0.6,
        FeeType.WITHDRAWAL: 0.4
    }

    dynamic_fee_system = DynamicFeeSystem(base_fee, market_activity_fees, fee_splits)

    try:
        market_activity = MarketActivity.MEDIUM
        fee_type = FeeType.TRANSACTION
        dynamic_fee = dynamic_fee_system.calculate_fee(market_activity, fee_type)
        print(f"Dynamic fee for {market_activity.name} market activity and {fee_type.name} fee type: {dynamic_fee}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
