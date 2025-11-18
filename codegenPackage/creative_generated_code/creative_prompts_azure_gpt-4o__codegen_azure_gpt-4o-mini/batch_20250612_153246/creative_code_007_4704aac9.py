"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fx4labs.com
Prompt: Develop a risk management algorithm for FX4 Labs' EA Autobot that adheres to pre-defined risk parameters to safeguard investments.
Generated: DETERMINISTIC_4704aac93dc9dbe8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagement:
    def __init__(self, initial_capital, risk_per_trade, max_drawdown):
        """
        Initializes the risk management parameters.

        :param initial_capital: The total amount of capital available for trading.
        :param risk_per_trade: The percentage of capital to risk on each trade (0-100).
        :param max_drawdown: The maximum allowable drawdown percentage (0-100).
        """
        self.initial_capital = initial_capital
        self.risk_per_trade = self.validate_percentage(risk_per_trade)
        self.max_drawdown = self.validate_percentage(max_drawdown)
        self.current_capital = initial_capital
        self.high_water_mark = initial_capital

    @staticmethod
    def validate_percentage(value):
        """
        Validates that a percentage value is within the range 0-100.

        :param value: The percentage value to validate.
        :raises ValueError: If the percentage is not between 0 and 100.
        """
        if not (0 <= value <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        return value

    def calculate_risk_amount(self):
        """
        Calculates the amount of capital to risk on the next trade.

        :return: The dollar amount to risk per trade.
        """
        risk_amount = (self.risk_per_trade / 100) * self.current_capital
        logging.info(f"Calculated risk amount per trade: {risk_amount:.2f}")
        return risk_amount

    def update_capital(self, profit_loss):
        """
        Updates the current capital based on the profit or loss from a trade.

        :param profit_loss: The profit or loss amount from the trade.
        """
        self.current_capital += profit_loss
        self.high_water_mark = max(self.high_water_mark, self.current_capital)
        self.check_drawdown()

    def check_drawdown(self):
        """
        Checks if the current capital exceeds the maximum drawdown limit.
        Raises an exception if the drawdown exceeds the limit.
        """
        drawdown = (self.high_water_mark - self.current_capital) / self.high_water_mark * 100
        logging.info(f"Current drawdown: {drawdown:.2f}%")
        if drawdown > self.max_drawdown:
            logging.warning("Maximum drawdown exceeded! Consider suspending trading.")
            raise RuntimeError("Maximum drawdown exceeded! Stop trading.")

    def reset(self):
        """
        Resets the risk management parameters to the initial state.
        """
        self.current_capital = self.initial_capital
        self.high_water_mark = self.initial_capital
        logging.info("Risk management parameters have been reset.")

# Example usage:
if __name__ == "__main__":
    try:
        risk_management = RiskManagement(initial_capital=10000, risk_per_trade=2, max_drawdown=20)
        
        # Simulate trades
        for trade in [100, -50, -200, 300, -150]:  # Example profit/loss values per trade
            risk_amount = risk_management.calculate_risk_amount()
            logging.info(f"Risking {risk_amount:.2f} on trade with P/L: {trade:.2f}")
            risk_management.update_capital(trade)

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except RuntimeError as re:
        logging.error(f"RuntimeError: {re}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
