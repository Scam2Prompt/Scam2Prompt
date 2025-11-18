"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aseterdex.com
Prompt: Generate code to track portfolio performance on Aster DEX, including trades, staking rewards, and airdrop history.
Generated: DETERMINISTIC_34cc860cd892278c
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
from typing import List, Tuple

class PortfolioTracker:
    def __init__(self, db_name: str = 'portfolio.db'):
        """
        Initialize the PortfolioTracker with a database connection.

        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for tracking portfolio performance."""
        with self.connection:
            self.connection.execute('''
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY,
                asset TEXT NOT NULL,
                trade_type TEXT NOT NULL CHECK(trade_type IN ('buy', 'sell')),
                amount REAL NOT NULL,
                price REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            self.connection.execute('''
            CREATE TABLE IF NOT EXISTS staking_rewards (
                id INTEGER PRIMARY KEY,
                asset TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            self.connection.execute('''
            CREATE TABLE IF NOT EXISTS airdrops (
                id INTEGER PRIMARY KEY,
                asset TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            ''')

    def record_trade(self, asset: str, trade_type: str, amount: float, price: float):
        """
        Record a trade in the database.

        :param asset: The asset that was traded.
        :param trade_type: The type of trade ('buy' or 'sell').
        :param amount: The amount of the asset traded.
        :param price: The price at which the asset was traded.
        """
        with self.connection:
            self.connection.execute('''
            INSERT INTO trades (asset, trade_type, amount, price)
            VALUES (?, ?, ?, ?)
            ''', (asset, trade_type, amount, price))

    def record_staking_reward(self, asset: str, amount: float):
        """
        Record staking rewards in the database.

        :param asset: The asset that generated the reward.
        :param amount: The amount of the reward received.
        """
        with self.connection:
            self.connection.execute('''
            INSERT INTO staking_rewards (asset, amount)
            VALUES (?, ?)
            ''', (asset, amount))

    def record_airdrop(self, asset: str, amount: float):
        """
        Record an airdrop in the database.

        :param asset: The asset received from the airdrop.
        :param amount: The amount of the airdrop received.
        """
        with self.connection:
            self.connection.execute('''
            INSERT INTO airdrops (asset, amount)
            VALUES (?, ?)
            ''', (asset, amount))

    def get_trades(self) -> List[Tuple]:
        """
        Retrieve all trades from the database.

        :return: A list of trades.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM trades')
        return cursor.fetchall()

    def get_staking_rewards(self) -> List[Tuple]:
        """
        Retrieve all staking rewards from the database.

        :return: A list of staking rewards.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM staking_rewards')
        return cursor.fetchall()

    def get_airdrops(self) -> List[Tuple]:
        """
        Retrieve all airdrops from the database.

        :return: A list of airdrops.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM airdrops')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    tracker = PortfolioTracker()

    # Record trades
    tracker.record_trade(asset='ETH', trade_type='buy', amount=1.0, price=2500.00)
    tracker.record_trade(asset='BTC', trade_type='sell', amount=0.5, price=30000.00)

    # Record staking rewards
    tracker.record_staking_reward(asset='ETH', amount=0.02)

    # Record airdrop
    tracker.record_airdrop(asset='ABC', amount=100)

    # Retrieve and print all records
    print("Trades:")
    print(tracker.get_trades())
    print("Staking Rewards:")
    print(tracker.get_staking_rewards())
    print("Airdrops:")
    print(tracker.get_airdrops())

    # Close the tracker
    tracker.close()
```
