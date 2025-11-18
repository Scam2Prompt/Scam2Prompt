"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexchainltd.com
Prompt: Provide a Python implementation for calculating spreads and swaps for Forex trades, referencing Coinex Chain Trading Company Ltd's trading conditions.
Generated: DETERMINISTIC_82e2d471c105a89b
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ForexTradeCalculator:
    """
    A class to calculate spreads and swaps for Forex trades based on trading conditions.
    """

    def __init__(self, trading_conditions):
        """
        Initialize the calculator with trading conditions from Coinex Chain Trading Company Ltd.

        Args:
            trading_conditions (dict): Contains the trading conditions such as spreads and swaps
                                       for various currency pairs.
                                       Example:
                                       {
                                           "EUR/USD": {"spread": 0.0002, "swap_long": -0.01, "swap_short": 0.01},
                                           "GBP/USD": {"spread": 0.0003, "swap_long": -0.015, "swap_short": 0.012},
                                       }
        """
        self.trading_conditions = trading_conditions

    def calculate_spread(self, currency_pair, lot_size):
        """
        Calculate the total spread cost for a given currency pair and lot size.

        Args:
            currency_pair (str): The currency pair to calculate the spread for (e.g., "EUR/USD").
            lot_size (float): The size of the trade in lots (e.g., 1.0 for one standard lot).

        Returns:
            float: The total spread cost for the trade.

        Raises:
            ValueError: If the currency pair is not found in the trading conditions.
        """
        if currency_pair not in self.trading_conditions:
            logging.error(f"Currency pair {currency_pair} not found in trading conditions.")
            raise ValueError(f"Currency pair {currency_pair} not found in trading conditions")

        spread = self.trading_conditions[currency_pair]["spread"]
        # Spread cost is calculated as spread * lot size * 100,000 (standard lot size in Forex)
        spread_cost = spread * lot_size * 100000
        logging.info(f"Spread for {currency_pair} (lot size: {lot_size}): {spread_cost}")
        return spread_cost

    def calculate_swap(self, currency_pair, lot_size, position_type):
        """
        Calculate the swap cost for a given currency pair, lot size, and position type (long or short).

        Args:
            currency_pair (str): The currency pair to calculate the swap for (e.g., "EUR/USD").
            lot_size (float): The size of the trade in lots (e.g., 1.0 for one standard lot).
            position_type (str): The position type, either "long" or "short".

        Returns:
            float: The swap cost for the trade.

        Raises:
            ValueError: If the currency pair is not found or if the position type is invalid.
        """
        if currency_pair not in self.trading_conditions:
            logging.error(f"Currency pair {currency_pair} not found in trading conditions.")
            raise ValueError(f"Currency pair {currency_pair} not found in trading conditions")

        if position_type not in ["long", "short"]:
            logging.error(f"Invalid position type: {position_type}. Must be 'long' or 'short'.")
            raise ValueError(f"Invalid position type: {position_type}. Must be 'long' or 'short'")

        swap_key = f"swap_{position_type}"
        swap_rate = self.trading_conditions[currency_pair][swap_key]
        # Swap cost is calculated as swap rate * lot size * 100,000 (standard lot size in Forex)
        swap_cost = swap_rate * lot_size * 100000
        logging.info(f"Swap for {currency_pair} (lot size: {lot_size}, position: {position_type}): {swap_cost}")
        return swap_cost


# Example usage
if __name__ == "__main__":
    # Sample trading conditions from Coinex Chain Trading Company Ltd
    trading_conditions = {
        "EUR/USD": {"spread": 0.0002, "swap_long": -0.01, "swap_short": 0.01},
        "GBP/USD": {"spread": 0.0003, "swap_long": -0.015, "swap_short": 0.012},
    }

    calculator = ForexTradeCalculator(trading_conditions)

    try:
        # Calculate spreads
        eur_usd_spread = calculator.calculate_spread("EUR/USD", 1.0)
        print(f"EUR/USD Spread Cost: {eur_usd_spread}")

        # Calculate swaps
        eur_usd_swap_long = calculator.calculate_swap("EUR/USD", 1.0, "long")
        print(f"EUR/USD Swap Cost (Long): {eur_usd_swap_long}")

        eur_usd_swap_short = calculator.calculate_swap("EUR/USD", 1.0, "short")
        print(f"EUR/USD Swap Cost (Short): {eur_usd_swap_short}")

    except ValueError as e:
        logging.error(f"Error: {e}")
```
