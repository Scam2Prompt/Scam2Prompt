"""
Generated Code Metadata:
========================
Original URL: https://immediate-500-evex.com
Prompt: Develop a comprehensive risk management strategy for trading on Immediate 500 Evex, considering factors such as position sizing, stop-loss orders, and portfolio diversification.
Generated: DETERMINISTIC_94b8e435eeebb097
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagement:
    """
    A class to implement a comprehensive risk management strategy for trading.
    Includes position sizing, stop-loss orders, and portfolio diversification.
    """

    def __init__(self, account_balance, max_risk_per_trade=0.02, max_portfolio_exposure=0.5):
        """
        Initialize the risk management strategy.

        :param account_balance: Total account balance (float).
        :param max_risk_per_trade: Maximum risk per trade as a percentage of account balance (float).
        :param max_portfolio_exposure: Maximum portfolio exposure as a percentage of account balance (float).
        """
        self.account_balance = account_balance
        self.max_risk_per_trade = max_risk_per_trade
        self.max_portfolio_exposure = max_portfolio_exposure
        self.current_exposure = 0.0

    def calculate_position_size(self, entry_price, stop_loss_price):
        """
        Calculate the position size based on risk per trade.

        :param entry_price: Entry price of the asset (float).
        :param stop_loss_price: Stop-loss price of the asset (float).
        :return: Position size (float).
        """
        try:
            risk_per_unit = abs(entry_price - stop_loss_price)
            risk_amount = self.account_balance * self.max_risk_per_trade
            position_size = risk_amount / risk_per_unit
            logging.info(f"Calculated position size: {position_size}")
            return position_size
        except ZeroDivisionError:
            logging.error("Stop-loss price cannot be equal to entry price.")
            return 0.0
        except Exception as e:
            logging.error(f"Error calculating position size: {e}")
            return 0.0

    def check_portfolio_exposure(self, new_position_value):
        """
        Check if adding a new position exceeds the maximum portfolio exposure.

        :param new_position_value: Value of the new position (float).
        :return: Boolean indicating whether the position can be added.
        """
        if self.current_exposure + new_position_value > self.account_balance * self.max_portfolio_exposure:
            logging.warning("Adding this position exceeds maximum portfolio exposure.")
            return False
        return True

    def add_position(self, entry_price, stop_loss_price):
        """
        Add a new position to the portfolio if it meets risk management criteria.

        :param entry_price: Entry price of the asset (float).
        :param stop_loss_price: Stop-loss price of the asset (float).
        :return: Boolean indicating whether the position was added successfully.
        """
        position_size = self.calculate_position_size(entry_price, stop_loss_price)
        new_position_value = position_size * entry_price

        if self.check_portfolio_exposure(new_position_value):
            self.current_exposure += new_position_value
            logging.info(f"Position added successfully. Current exposure: {self.current_exposure}")
            return True
        else:
            logging.warning("Position not added due to portfolio exposure limits.")
            return False

    def reset_exposure(self):
        """
        Reset the current portfolio exposure (useful for rebalancing).
        """
        self.current_exposure = 0.0
        logging.info("Portfolio exposure reset.")

# Example usage
if __name__ == "__main__":
    # Initialize risk management with an account balance of $10,000
    risk_manager = RiskManagement(account_balance=10000)

    # Attempt to add a position
    entry_price = 100.0
    stop_loss_price = 95.0
    risk_manager.add_position(entry_price, stop_loss_price)

    # Reset exposure for rebalancing
    risk_manager.reset_exposure()
```
