"""
Generated Code Metadata:
========================
Original URL: https://the-immediate-40-avapro.com
Prompt: Design a risk management system for Immediate 40 Avapro users, incorporating features such as stop-loss orders, position sizing, and portfolio diversification.
Generated: DETERMINISTIC_4c7ca90766829472
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

class RiskManagementSystem:
    """
    A Risk Management System for Immediate 40 Avapro users.
    Features:
    - Stop-loss orders
    - Position sizing
    - Portfolio diversification
    """

    def __init__(self, portfolio_balance):
        """
        Initialize the risk management system.
        :param portfolio_balance: Total balance of the user's portfolio.
        """
        self.portfolio_balance = portfolio_balance
        self.positions = []  # List to store active positions

    def calculate_position_size(self, risk_per_trade, stop_loss_distance):
        """
        Calculate the position size based on risk per trade and stop-loss distance.
        :param risk_per_trade: Percentage of portfolio balance to risk per trade (e.g., 0.02 for 2%).
        :param stop_loss_distance: Distance between entry price and stop-loss price.
        :return: Position size.
        """
        try:
            risk_amount = self.portfolio_balance * risk_per_trade
            position_size = risk_amount / stop_loss_distance
            return position_size
        except ZeroDivisionError:
            logging.error("Stop-loss distance cannot be zero.")
            return 0

    def add_position(self, symbol, entry_price, stop_loss_price, risk_per_trade):
        """
        Add a new position to the portfolio.
        :param symbol: Asset symbol (e.g., 'AAPL').
        :param entry_price: Entry price for the position.
        :param stop_loss_price: Stop-loss price for the position.
        :param risk_per_trade: Percentage of portfolio balance to risk per trade.
        """
        stop_loss_distance = abs(entry_price - stop_loss_price)
        position_size = self.calculate_position_size(risk_per_trade, stop_loss_distance)

        if position_size > 0:
            position = {
                'symbol': symbol,
                'entry_price': entry_price,
                'stop_loss_price': stop_loss_price,
                'position_size': position_size
            }
            self.positions.append(position)
            logging.info(f"Position added: {position}")
        else:
            logging.warning(f"Failed to add position for {symbol} due to invalid parameters.")

    def check_stop_loss(self, current_prices):
        """
        Check if any positions have hit their stop-loss price.
        :param current_prices: Dictionary of current prices for assets (e.g., {'AAPL': 150.0}).
        """
        for position in self.positions:
            symbol = position['symbol']
            stop_loss_price = position['stop_loss_price']
            if symbol in current_prices and current_prices[symbol] <= stop_loss_price:
                logging.info(f"Stop-loss triggered for {symbol}. Closing position.")
                self.positions.remove(position)

    def diversify_portfolio(self, max_asset_allocation):
        """
        Ensure portfolio diversification by limiting allocation to a single asset.
        :param max_asset_allocation: Maximum percentage of portfolio balance allocated to a single asset (e.g., 0.25 for 25%).
        """
        for position in self.positions:
            allocation = (position['position_size'] * position['entry_price']) / self.portfolio_balance
            if allocation > max_asset_allocation:
                logging.warning(f"Position in {position['symbol']} exceeds diversification limit. Consider rebalancing.")

# Example usage
if __name__ == "__main__":
    # Initialize the risk management system with a portfolio balance of $100,000
    rms = RiskManagementSystem(portfolio_balance=100000)

    # Add positions
    rms.add_position(symbol="AAPL", entry_price=150, stop_loss_price=140, risk_per_trade=0.02)
    rms.add_position(symbol="GOOGL", entry_price=2800, stop_loss_price=2700, risk_per_trade=0.01)

    # Simulate current prices and check stop-loss
    current_prices = {"AAPL": 139, "GOOGL": 2750}
    rms.check_stop_loss(current_prices)

    # Check portfolio diversification
    rms.diversify_portfolio(max_asset_allocation=0.25)
```
