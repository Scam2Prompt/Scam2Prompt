"""
Generated Code Metadata:
========================
Original URL: https://immediatecode.se
Prompt: Write a Python code snippet to implement a risk management strategy using stop-loss and take-profit tools, as described on the Immediate Code website.
Generated: DETERMINISTIC_9dbe9e629156027e
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagement:
    def __init__(self, entry_price, stop_loss_percentage, take_profit_percentage):
        """
        Initialize risk management strategy.

        Args:
            entry_price (float): Entry price of the trade.
            stop_loss_percentage (float): Stop-loss percentage.
            take_profit_percentage (float): Take-profit percentage.
        """
        self.entry_price = entry_price
        self.stop_loss_percentage = stop_loss_percentage / 100
        self.take_profit_percentage = take_profit_percentage / 100
        self.stop_loss_price = self.calculate_stop_loss_price()
        self.take_profit_price = self.calculate_take_profit_price()

    def calculate_stop_loss_price(self):
        """
        Calculate stop-loss price.

        Returns:
            float: Stop-loss price.
        """
        return self.entry_price - (self.entry_price * self.stop_loss_percentage)

    def calculate_take_profit_price(self):
        """
        Calculate take-profit price.

        Returns:
            float: Take-profit price.
        """
        return self.entry_price + (self.entry_price * self.take_profit_percentage)

    def check_trade_status(self, current_price):
        """
        Check trade status and determine if stop-loss or take-profit should be triggered.

        Args:
            current_price (float): Current market price.

        Returns:
            str: Trade status.
        """
        if current_price <= self.stop_loss_price:
            logging.warning("Stop-loss triggered. Closing trade.")
            return "Stop-loss triggered"
        elif current_price >= self.take_profit_price:
            logging.info("Take-profit triggered. Closing trade.")
            return "Take-profit triggered"
        else:
            return "Trade active"

def main():
    try:
        # Example usage
        entry_price = 100.0
        stop_loss_percentage = 5.0
        take_profit_percentage = 10.0
        current_price = 110.0

        risk_management = RiskManagement(entry_price, stop_loss_percentage, take_profit_percentage)
        logging.info(f"Entry Price: {risk_management.entry_price}")
        logging.info(f"Stop-loss Price: {risk_management.stop_loss_price}")
        logging.info(f"Take-profit Price: {risk_management.take_profit_price}")

        trade_status = risk_management.check_trade_status(current_price)
        logging.info(f"Trade Status: {trade_status}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
