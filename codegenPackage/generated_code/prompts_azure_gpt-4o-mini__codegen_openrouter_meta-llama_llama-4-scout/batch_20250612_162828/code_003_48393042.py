"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Explain how the Earnie app allows users to follow and copy trades from successful traders, similar to social media platforms like TikTok.
Generated: DETERMINISTIC_483930424ad72a32
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# earnie_app.py

import os
import logging
from typing import Dict, List
from dataclasses import dataclass

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a data class to represent a Trader
@dataclass
class Trader:
    """Represents a successful trader."""
    id: int
    name: str
    strategy: str
    performance: float

# Define a data class to represent a Trade
@dataclass
class Trade:
    """Represents a trade made by a trader."""
    id: int
    trader_id: int
    asset: str
    entry_price: float
    exit_price: float
    timestamp: str

class EarnieApp:
    """Simulates the Earnie app, allowing users to follow and copy trades."""

    def __init__(self):
        # Initialize an in-memory database for demonstration purposes
        self.traders: Dict[int, Trader] = {}
        self.trades: Dict[int, List[Trade]] = {}
        self.followers: Dict[int, List[int]] = {}

    def add_trader(self, trader: Trader):
        """Add a new trader to the platform."""
        self.traders[trader.id] = trader
        self.trades[trader.id] = []
        logger.info(f"Trader {trader.name} added.")

    def add_trade(self, trade: Trade):
        """Add a new trade made by a trader."""
        if trade.trader_id in self.traders:
            self.trades[trade.trader_id].append(trade)
            logger.info(f"Trade {trade.id} added for trader {self.traders[trade.trader_id].name}.")
        else:
            logger.error(f"Trader {trade.trader_id} not found.")

    def follow_trader(self, user_id: int, trader_id: int):
        """Allow a user to follow a trader."""
        if trader_id in self.traders:
            if user_id not in self.followers:
                self.followers[user_id] = []
            self.followers[user_id].append(trader_id)
            logger.info(f"User {user_id} is now following trader {self.traders[trader_id].name}.")
        else:
            logger.error(f"Trader {trader_id} not found.")

    def copy_trades(self, user_id: int):
        """Copy trades from followed traders."""
        if user_id in self.followers:
            for trader_id in self.followers[user_id]:
                trades = self.trades[trader_id]
                logger.info(f"Copying trades from trader {self.traders[trader_id].name}...")
                for trade in trades:
                    # Simulate copying the trade (e.g., execute a new trade)
                    logger.info(f"Copied trade {trade.id}: {trade.asset} at {trade.entry_price}")
        else:
            logger.error(f"User {user_id} is not following any traders.")

def main():
    app = EarnieApp()

    # Create traders
    trader1 = Trader(1, "John Doe", "Day Trader", 0.8)
    trader2 = Trader(2, "Jane Smith", "Swing Trader", 0.9)

    # Add traders to the platform
    app.add_trader(trader1)
    app.add_trader(trader2)

    # Create trades
    trade1 = Trade(1, 1, "AAPL", 100.0, 120.0, "2022-01-01 12:00:00")
    trade2 = Trade(2, 1, "GOOGL", 500.0, 550.0, "2022-01-02 13:00:00")
    trade3 = Trade(3, 2, "MSFT", 200.0, 220.0, "2022-01-03 14:00:00")

    # Add trades to the platform
    app.add_trade(trade1)
    app.add_trade(trade2)
    app.add_trade(trade3)

    # Follow traders
    app.follow_trader(1, 1)
    app.follow_trader(1, 2)

    # Copy trades
    app.copy_trades(1)

if __name__ == "__main__":
    main()
```
