"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Develop a Python program to analyze the profitability of trading with raw spreads and $5 commission per lot, as described for the "ECN" account type on S D STAR FX LTD.
Generated: DETERMINISTIC_3cca0376ce5191cc
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class TradingAnalysis:
    """
    A class to analyze the profitability of trading with raw spreads and a commission structure.
    """

    def __init__(self, spread: float, commission_per_lot: float, lot_size: int):
        """
        Initialize the TradingAnalysis instance with the given parameters.

        :param spread: Raw spread in pips (e.g., 0.2 for 2 pips)
        :param commission_per_lot: Commission charged per lot traded
        :param lot_size: Size of one lot in base currency (e.g., 100,000 for standard lot)
        """
        self.spread = spread
        self.commission_per_lot = commission_per_lot
        self.lot_size = lot_size

    def calculate_trade_cost(self, number_of_lots: int) -> float:
        """
        Calculate the total cost of trading for a given number of lots.

        :param number_of_lots: Number of lots to trade
        :return: Total cost of trading
        """
        try:
            # Validate input
            if number_of_lots <= 0:
                raise ValueError("Number of lots must be greater than zero.")

            # Calculate the total spread cost (in currency)
            spread_cost = (self.spread / 10000) * self.lot_size * number_of_lots
            # Calculate the total commission cost
            commission_cost = self.commission_per_lot * number_of_lots
            # Total trading cost
            total_cost = spread_cost + commission_cost
            return total_cost

        except Exception as e:
            print(f"Error calculating trade cost: {e}")
            return None

    def analyze_profitability(self, number_of_lots: int, profit_per_trade: float) -> dict:
        """
        Analyze the profitability of trading with specified parameters.

        :param number_of_lots: Number of lots traded
        :param profit_per_trade: Expected profit per trade in the currency
        :return: A dictionary containing total cost and net profit
        """
        try:
            # Calculate total cost
            total_cost = self.calculate_trade_cost(number_of_lots)
            if total_cost is None:
                raise ValueError("Invalid total cost calculated.")

            # Calculate net profit
            net_profit = (profit_per_trade * number_of_lots) - total_cost

            # Return analysis results
            return {
                "Total Cost": total_cost,
                "Net Profit": net_profit,
                "Profitability": "Profitable" if net_profit > 0 else "Not Profitable"
            }

        except Exception as e:
            print(f"Error analyzing profitability: {e}")
            return None


if __name__ == "__main__":
    # Example parameters for ECN account type
    SPREAD = 0.2  # Raw spread in pips
    COMMISSION_PER_LOT = 5.0  # Commission per lot in currency
    LOT_SIZE = 100000  # Standard lot size in base currency

    # Create an instance of TradingAnalysis
    trading_analysis = TradingAnalysis(SPREAD, COMMISSION_PER_LOT, LOT_SIZE)

    # Example input for analysis
    NUMBER_OF_LOTS = 10
    EXPECTED_PROFIT_PER_TRADE = 200.0  # Expected profit per trade in currency

    # Analyze profitability
    results = trading_analysis.analyze_profitability(NUMBER_OF_LOTS, EXPECTED_PROFIT_PER_TRADE)

    if results:
        # Print out the results
        print("Trading Analysis Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
```
