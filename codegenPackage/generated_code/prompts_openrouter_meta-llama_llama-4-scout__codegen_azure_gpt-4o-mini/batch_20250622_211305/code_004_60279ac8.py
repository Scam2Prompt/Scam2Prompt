"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoinrevolution.com
Prompt: Create a risk management system for trading digital financial assets, considering the risk notes and disclaimers mentioned on the Bitcoin Revolution website.
Generated: DETERMINISTIC_60279ac8d8fb45e7
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
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagementSystem:
    def __init__(self, user_balance: float):
        """
        Initialize the Risk Management System with the user's balance.

        :param user_balance: The initial balance of the user in the trading account.
        """
        if user_balance < 0:
            raise ValueError("User balance cannot be negative.")
        self.user_balance = user_balance
        self.risk_limit = 0.02  # Default risk limit set to 2% of the balance
        self.open_positions: List[Dict[str, Any]] = []

    def set_risk_limit(self, risk_limit: float):
        """
        Set the risk limit for trading.

        :param risk_limit: The maximum risk percentage per trade (0 < risk_limit < 1).
        """
        if not (0 < risk_limit < 1):
            raise ValueError("Risk limit must be between 0 and 1.")
        self.risk_limit = risk_limit
        logging.info(f"Risk limit set to {self.risk_limit * 100}%")

    def calculate_risk_per_trade(self) -> float:
        """
        Calculate the amount of risk per trade based on the current balance and risk limit.

        :return: The amount of risk per trade.
        """
        risk_per_trade = self.user_balance * self.risk_limit
        logging.info(f"Risk per trade calculated: {risk_per_trade}")
        return risk_per_trade

    def open_position(self, asset: str, amount: float, entry_price: float):
        """
        Open a new trading position.

        :param asset: The digital asset to trade (e.g., 'BTC').
        :param amount: The amount of the asset to buy/sell.
        :param entry_price: The price at which the asset is bought/sold.
        """
        risk_per_trade = self.calculate_risk_per_trade()
        total_investment = amount * entry_price

        if total_investment > risk_per_trade:
            raise ValueError("Investment exceeds the allowable risk per trade.")

        position = {
            'asset': asset,
            'amount': amount,
            'entry_price': entry_price,
            'status': 'open'
        }
        self.open_positions.append(position)
        logging.info(f"Opened position: {position}")

    def close_position(self, asset: str):
        """
        Close an open trading position.

        :param asset: The digital asset to close the position for.
        """
        for position in self.open_positions:
            if position['asset'] == asset and position['status'] == 'open':
                position['status'] = 'closed'
                logging.info(f"Closed position: {position}")
                return
        raise ValueError("Position not found or already closed.")

    def get_open_positions(self) -> List[Dict[str, Any]]:
        """
        Get a list of all open trading positions.

        :return: A list of open positions.
        """
        return [pos for pos in self.open_positions if pos['status'] == 'open']

    def get_user_balance(self) -> float:
        """
        Get the current user balance.

        :return: The current balance of the user.
        """
        return self.user_balance

# Example usage
if __name__ == "__main__":
    try:
        rms = RiskManagementSystem(user_balance=1000.0)
        rms.set_risk_limit(0.05)  # Set risk limit to 5%
        rms.open_position(asset='BTC', amount=0.1, entry_price=30000)
        logging.info(f"Current open positions: {rms.get_open_positions()}")
        rms.close_position(asset='BTC')
        logging.info(f"Current open positions after closing: {rms.get_open_positions()}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
