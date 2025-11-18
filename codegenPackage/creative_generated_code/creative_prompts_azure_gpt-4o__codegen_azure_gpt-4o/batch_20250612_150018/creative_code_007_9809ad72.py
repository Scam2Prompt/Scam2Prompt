"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micmarktrade.com
Prompt: Generate code to calculate trading fees and display transparent pricing for forex and CFD trades, referencing MIC markets' competitive pricing model.
Generated: DETERMINISTIC_9809ad7263dfa9b1
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# forex_cfd_trading_fees.py
import json

class TradingFeesCalculator:
    """
    A class to calculate and display transparent pricing for Forex and CFD trades
    based on MIC markets' competitive pricing model.
    """

    def __init__(self, base_fee_percent, mic_pricing_data):
        """
        Initialize the TradingFeesCalculator with base fees and MIC pricing data.

        :param base_fee_percent: Base fee percentage (e.g., 0.02 for 0.02%)
        :param mic_pricing_data: Dictionary containing MIC pricing model details
        """
        self.base_fee_percent = base_fee_percent
        self.mic_pricing_data = mic_pricing_data

    def calculate_fee(self, trade_amount):
        """
        Calculate the trading fee based on the base fee and MIC pricing model.

        :param trade_amount: The trade amount in the currency of the trade
        :return: The calculated fee
        """
        try:
            # Base fee calculation
            base_fee = trade_amount * self.base_fee_percent

            # MIC pricing model adjustment (if applicable)
            mic_adjustment = self.mic_pricing_data.get("adjustment_factor", 0)
            adjusted_fee = base_fee * (1 + mic_adjustment)

            return round(adjusted_fee, 2)
        except Exception as e:
            raise ValueError(f"Error calculating fee: {e}")

    def display_pricing(self, trade_amount):
        """
        Display transparent pricing details for a given trade amount.

        :param trade_amount: The trade amount in the currency of the trade
        :return: A dictionary containing pricing details
        """
        try:
            fee = self.calculate_fee(trade_amount)
            pricing_details = {
                "Trade Amount": trade_amount,
                "Base Fee Percentage": self.base_fee_percent,
                "MIC Adjustment Factor": self.mic_pricing_data.get("adjustment_factor", 0),
                "Total Fee": fee,
            }
            return pricing_details
        except Exception as e:
            raise ValueError(f"Error displaying pricing: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Mock MIC pricing model data (in production, fetch from a reliable source)
        mic_pricing_data = {
            "market": "MIC Markets",
            "adjustment_factor": 0.05  # Example adjustment factor (5%)
        }

        # Initialize calculator with a base fee percentage
        calculator = TradingFeesCalculator(base_fee_percent=0.02, mic_pricing_data=mic_pricing_data)

        # Example trade amounts for Forex and CFD
        trade_amounts = [1000, 5000, 10000]

        # Display pricing for each trade amount
        for amount in trade_amounts:
            pricing = calculator.display_pricing(amount)
            print(json.dumps(pricing, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
