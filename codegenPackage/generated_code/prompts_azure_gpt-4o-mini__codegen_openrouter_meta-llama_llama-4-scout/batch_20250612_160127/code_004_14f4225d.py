"""
Generated Code Metadata:
========================
Original URL: https://micmarktrade.com
Prompt: Create a function that calculates trading fees based on the competitive pricing structure outlined by MIC markets.
Generated: DETERMINISTIC_14f4225dd8eebdd4
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_fees_calculator.py

from enum import Enum
from typing import Dict

class MarketType(str, Enum):
    """MIC market types."""
    MIC = "MIC"

class TradingFeeType(str, Enum):
    """Types of trading fees."""
    FIXED = "fixed"
    TIERED = "tiered"

class TradingFeesCalculator:
    """Calculates trading fees based on the competitive pricing structure outlined by MIC markets."""

    def __init__(self, market_type: MarketType, fee_structure: Dict[str, Dict[str, float]]):
        """
        Initializes the TradingFeesCalculator.

        Args:
        - market_type (MarketType): The type of market.
        - fee_structure (Dict[str, Dict[str, float]]): A dictionary containing the fee structure.
        """
        self.market_type = market_type
        self.fee_structure = fee_structure

    def calculate_fee(self, trade_value: float, fee_type: TradingFeeType) -> float:
        """
        Calculates the trading fee.

        Args:
        - trade_value (float): The value of the trade.
        - fee_type (TradingFeeType): The type of fee.

        Returns:
        - float: The calculated trading fee.

        Raises:
        - ValueError: If the trade value is negative or if the fee type is not supported.
        """
        if trade_value < 0:
            raise ValueError("Trade value cannot be negative")

        if fee_type not in [TradingFeeType.FIXED, TradingFeeType.TIERED]:
            raise ValueError("Unsupported fee type")

        if fee_type == TradingFeeType.FIXED:
            return self.calculate_fixed_fee()
        elif fee_type == TradingFeeType.TIERED:
            return self.calculate_tiered_fee(trade_value)

    def calculate_fixed_fee(self) -> float:
        """
        Calculates the fixed trading fee.

        Returns:
        - float: The fixed trading fee.
        """
        try:
            return self.fee_structure[self.market_type.value]["fixed"]
        except KeyError:
            raise ValueError("Fixed fee not found in fee structure")

    def calculate_tiered_fee(self, trade_value: float) -> float:
        """
        Calculates the tiered trading fee.

        Args:
        - trade_value (float): The value of the trade.

        Returns:
        - float: The tiered trading fee.
        """
        try:
            tiers = self.fee_structure[self.market_type.value]["tiered"]
            sorted_tiers = sorted(tiers.items())

            for i in range(len(sorted_tiers)):
                if trade_value <= sorted_tiers[i][0]:
                    return trade_value * sorted_tiers[i][1]

            return trade_value * sorted_tiers[-1][1]
        except KeyError:
            raise ValueError("Tiered fee not found in fee structure")


def main():
    # Example usage:
    fee_structure = {
        "MIC": {
            "fixed": 0.01,
            "tiered": {
                1000: 0.005,
                5000: 0.003,
                10000: 0.002
            }
        }
    }

    calculator = TradingFeesCalculator(MarketType.MIC, fee_structure)

    trade_value = 7500
    fee_type = TradingFeeType.TIERED

    try:
        fee = calculator.calculate_fee(trade_value, fee_type)
        print(f"The trading fee for a trade of {trade_value} with {fee_type} fee is: {fee}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
