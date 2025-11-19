"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatelidex-ai.com
Prompt: Can you provide an example of a customizable trading strategy that could be implemented on a platform like btc40 eprex?
Generated: DETERMINISTIC_4618aba57d72e44c
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingStrategy:
    """
    A customizable trading strategy class for cryptocurrency trading.

    Attributes:
        name (str): Name of the strategy.
        buy_threshold (float): Price percentage below which to buy.
        sell_threshold (float): Price percentage above which to sell.
        trade_frequency (timedelta): Minimum time gap between trades.
        last_trade_time (datetime): Last time a trade was executed.
    """
    def __init__(self, name="Default Strategy", buy_threshold=-2.0, sell_threshold=2.0, trade_frequency=timedelta(minutes=5)):
        """
        Initializes the trading strategy with customizable parameters.
        
        Args:
            name (str): Name of the strategy.
            buy_threshold (float): Price percentage below which to buy.
            sell_threshold (float): Price percentage above which to sell.
            trade_frequency (timedelta): Minimum time gap between trades.
        """
        self.name = name
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.trade_frequency = trade_frequency
        self.last_trade_time = None  # No trades executed yet

    def should_trade(self, current_price, moving_average):
        """
        Determines whether a trade should be executed based on the strategy logic.
        
        Args:
            current_price (float): Current price of the asset.
            moving_average (float): Moving average price of the asset.

        Returns:
            str: The trade action ('BUY', 'SELL', or 'HOLD').
        """
        if self.last_trade_time and datetime.now() - self.last_trade_time < self.trade_frequency:
            logging.info("Trade skipped due to frequency limit.")
            return "HOLD"

        price_diff_percentage = ((current_price - moving_average) / moving_average) * 100

        if price_diff_percentage <= self.buy_threshold:
            logging.info(f"BUY signal detected (Price diff: {price_diff_percentage:.2f}%).")
            return "BUY"
        elif price_diff_percentage >= self.sell_threshold:
            logging.info(f"SELL signal detected (Price diff: {price_diff_percentage:.2f}%).")
            return "SELL"
        else:
            logging.info(f"HOLD signal detected (Price diff: {price_diff_percentage:.2f}%).")
            return "HOLD"

    def execute_trade(self, action, quantity, asset):
        """
        Executes a trade based on the given action.

        Args:
            action (str): The trade action ('BUY', 'SELL', or 'HOLD').
            quantity (float): Quantity of the asset to trade.
            asset (str): Name of the asset being traded.
        """
        if action == "BUY":
            # Simulate a buy trade (replace with actual trade execution logic on the platform)
            logging.info(f"Executing BUY trade: {quantity} units of {asset}.")
        elif action == "SELL":
            # Simulate a sell trade (replace with actual trade execution logic on the platform)
            logging.info(f"Executing SELL trade: {quantity} units of {asset}.")
        elif action == "HOLD":
            logging.info("No trade executed (HOLD action).")
        else:
            logging.error(f"Invalid trade action: {action}.")
            raise ValueError("Invalid trade action.")
        
        self.last_trade_time = datetime.now()  # Record the time of the trade

# Example usage:
if __name__ == "__main__":
    # Initialize the trading strategy
    strategy = TradingStrategy(name="Momentum Strategy", buy_threshold=-3.0, sell_threshold=3.0, trade_frequency=timedelta(minutes=10))
    
    # Simulated market data
    current_price = 105.0
    moving_average = 100.0
    quantity = 1.0
    asset = "BTC"

    # Determine trade action
    action = strategy.should_trade(current_price, moving_average)

    # Execute trade based on the action
    strategy.execute_trade(action, quantity, asset)
```
