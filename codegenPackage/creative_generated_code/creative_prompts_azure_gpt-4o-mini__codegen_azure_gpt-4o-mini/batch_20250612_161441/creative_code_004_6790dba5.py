"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadguide.site
Prompt: Explain how KuruExchange is revolutionizing DeFi trading within the Monad ecosystem.
Generated: DETERMINISTIC_6790dba59c1fb6a6
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
KuruExchange: A decentralized finance (DeFi) trading platform within the Monad ecosystem.
This code simulates the core functionality of a trading system, demonstrating how KuruExchange operates.
"""

import random

class TradeError(Exception):
    """Custom exception for trade errors."""
    pass

class KuruExchange:
    """
    A class to represent the KuruExchange platform for DeFi trading.
    """

    def __init__(self, liquidity_pool):
        """
        Initializes the KuruExchange with a specific liquidity pool.

        Args:
            liquidity_pool (float): Initial amount of liquidity available for trading.
        """
        self.liquidity_pool = liquidity_pool
        self.trades = []

    def execute_trade(self, trader, trade_amount, trade_type):
        """
        Executes a trade on the KuruExchange.

        Args:
            trader (str): The name of the trader.
            trade_amount (float): The amount of currency to trade.
            trade_type (str): The type of trade ('buy' or 'sell').

        Raises:
            TradeError: If the trade cannot be executed due to insufficient liquidity or invalid trade type.
        """
        if trade_type not in ['buy', 'sell']:
            raise TradeError("Invalid trade type. Must be 'buy' or 'sell'.")

        if trade_type == 'buy':
            self._buy(trader, trade_amount)
        elif trade_type == 'sell':
            self._sell(trader, trade_amount)

    def _buy(self, trader, amount):
        """
        Processes a buy trade.

        Args:
            trader (str): The name of the trader.
            amount (float): The amount of currency to buy.

        Raises:
            TradeError: If the liquidity pool is insufficient for the trade.
        """
        if amount > self.liquidity_pool:
            raise TradeError(f"Insufficient liquidity for trade by {trader}. Available: {self.liquidity_pool}, Requested: {amount}")

        self.liquidity_pool -= amount
        self.trades.append((trader, 'buy', amount))
        print(f"{trader} bought {amount}. Remaining liquidity: {self.liquidity_pool}")

    def _sell(self, trader, amount):
        """
        Processes a sell trade.

        Args:
            trader (str): The name of the trader.
            amount (float): The amount of currency to sell.

        Raises:
            TradeError: If selling exceeds the amount in the liquidity pool.
        """
        self.liquidity_pool += amount
        self.trades.append((trader, 'sell', amount))
        print(f"{trader} sold {amount}. New liquidity: {self.liquidity_pool}")

    def get_trade_history(self):
        """
        Returns the history of all trades executed on the KuruExchange.

        Returns:
            list: A list of executed trades.
        """
        return self.trades

# Example usage
if __name__ == "__main__":
    # Initialize the exchange with a liquidity pool of 1000
    exchange = KuruExchange(liquidity_pool=1000)

    # Simulate trading activity
    try:
        exchange.execute_trade("Alice", 100, "buy")
        exchange.execute_trade("Bob", 50, "sell")
        exchange.execute_trade("Charlie", 200, "buy")
        exchange.execute_trade("Alice", 300, "sell")

        # Print trade history
        print("\nTrade History:")
        for trade in exchange.get_trade_history():
            print(trade)

    except TradeError as e:
        print(f"Trade error occurred: {e}")
```
