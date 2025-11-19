"""
Generated Code Metadata:
========================
Original URL: https://immediategpt.app
Prompt: Develop a code snippet to implement a risk management system for cryptocurrency trading, considering the importance of education and expert guidance highlighted by GPT 500 Ifex.
Generated: DETERMINISTIC_3a3829fa1f0876be
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagementSystem:
    def __init__(self, capital: float, risk_tolerance: float):
        """
        Initialize the Risk Management System.

        :param capital: Total capital available for trading.
        :param risk_tolerance: Maximum percentage of capital to risk on a single trade.
        """
        if capital <= 0:
            raise ValueError("Capital must be greater than zero.")
        if not (0 < risk_tolerance < 1):
            raise ValueError("Risk tolerance must be a value between 0 and 1.")

        self.capital = capital
        self.risk_tolerance = risk_tolerance

    def calculate_position_size(self, stop_loss_distance: float) -> float:
        """
        Calculate the position size based on the risk tolerance and stop loss distance.

        :param stop_loss_distance: The distance (in currency) from the entry price to the stop loss.
        :return: The position size that can be taken for the trade.
        """
        if stop_loss_distance <= 0:
            raise ValueError("Stop loss distance must be greater than zero.")

        risk_amount = self.capital * self.risk_tolerance
        position_size = risk_amount / stop_loss_distance
        return position_size

    def assess_trade_risk(self, entry_price: float, stop_loss_price: float) -> Dict[str, float]:
        """
        Assess the risk of a trade based on entry and stop loss prices.

        :param entry_price: The price at which the trade is entered.
        :param stop_loss_price: The price at which the trade will be exited if it goes against the position.
        :return: A dictionary containing the risk amount and position size.
        """
        if entry_price <= 0 or stop_loss_price <= 0:
            raise ValueError("Entry and stop loss prices must be greater than zero.")
        if stop_loss_price >= entry_price:
            raise ValueError("Stop loss price must be less than entry price for a long position.")

        stop_loss_distance = entry_price - stop_loss_price
        position_size = self.calculate_position_size(stop_loss_distance)
        risk_amount = position_size * stop_loss_distance

        return {
            "risk_amount": risk_amount,
            "position_size": position_size
        }

def main():
    try:
        # Example usage of the Risk Management System
        capital = 10000.0  # Total capital for trading
        risk_tolerance = 0.02  # Risk 2% of capital on each trade

        rms = RiskManagementSystem(capital, risk_tolerance)

        # Example trade parameters
        entry_price = 50000.0  # Entry price for the trade
        stop_loss_price = 49000.0  # Stop loss price for the trade

        trade_risk = rms.assess_trade_risk(entry_price, stop_loss_price)
        logging.info(f"Trade Risk Assessment: {trade_risk}")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
