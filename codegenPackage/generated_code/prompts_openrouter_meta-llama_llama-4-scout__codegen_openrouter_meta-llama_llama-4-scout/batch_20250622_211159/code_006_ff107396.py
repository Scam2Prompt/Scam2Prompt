"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Create a system for managing trader subscriptions and profit sharing, where users can follow multiple traders and earn up to 20% of their profits.
Generated: DETERMINISTIC_ff1073968a5f26a9
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trader_subscription_system.py

from typing import Dict, List
from datetime import datetime

class Trader:
    """Represents a trader with a unique ID and profit sharing information."""

    def __init__(self, trader_id: int, name: str):
        """
        Initializes a Trader object.

        Args:
        - trader_id (int): Unique ID of the trader.
        - name (str): Name of the trader.
        """
        self.trader_id = trader_id
        self.name = name
        self.profits: List[float] = []
        self.subscribers: List[int] = []

    def add_profit(self, profit: float):
        """
        Adds a profit to the trader's profit history.

        Args:
        - profit (float): Profit amount.
        """
        self.profits.append(profit)

    def add_subscriber(self, user_id: int):
        """
        Adds a subscriber to the trader's subscriber list.

        Args:
        - user_id (int): ID of the subscriber.
        """
        self.subscribers.append(user_id)


class User:
    """Represents a user with a unique ID and subscription information."""

    def __init__(self, user_id: int, name: str):
        """
        Initializes a User object.

        Args:
        - user_id (int): Unique ID of the user.
        - name (str): Name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.subscriptions: List[int] = []
        self.earnings: float = 0.0

    def subscribe_to_trader(self, trader_id: int):
        """
        Subscribes the user to a trader.

        Args:
        - trader_id (int): ID of the trader.
        """
        self.subscriptions.append(trader_id)


class TraderSubscriptionSystem:
    """Manages trader subscriptions and profit sharing."""

    def __init__(self):
        self.traders: Dict[int, Trader] = {}
        self.users: Dict[int, User] = {}

    def create_trader(self, trader_id: int, name: str):
        """
        Creates a new trader.

        Args:
        - trader_id (int): Unique ID of the trader.
        - name (str): Name of the trader.
        """
        if trader_id in self.traders:
            raise ValueError("Trader already exists")
        self.traders[trader_id] = Trader(trader_id, name)

    def create_user(self, user_id: int, name: str):
        """
        Creates a new user.

        Args:
        - user_id (int): Unique ID of the user.
        - name (str): Name of the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = User(user_id, name)

    def subscribe_user_to_trader(self, user_id: int, trader_id: int):
        """
        Subscribes a user to a trader.

        Args:
        - user_id (int): ID of the user.
        - trader_id (int): ID of the trader.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if trader_id not in self.traders:
            raise ValueError("Trader does not exist")
        self.users[user_id].subscribe_to_trader(trader_id)
        self.traders[trader_id].add_subscriber(user_id)

    def add_trader_profit(self, trader_id: int, profit: float):
        """
        Adds a profit to a trader's profit history.

        Args:
        - trader_id (int): ID of the trader.
        - profit (float): Profit amount.
        """
        if trader_id not in self.traders:
            raise ValueError("Trader does not exist")
        self.traders[trader_id].add_profit(profit)
        self.distribute_profits(trader_id)

    def distribute_profits(self, trader_id: int):
        """
        Distributes profits to subscribers of a trader.

        Args:
        - trader_id (int): ID of the trader.
        """
        trader = self.traders[trader_id]
        total_profit = sum(trader.profits)
        subscriber_count = len(trader.subscribers)
        if subscriber_count == 0:
            return
        profit_share = total_profit * 0.20 / subscriber_count
        for subscriber_id in trader.subscribers:
            self.users[subscriber_id].earnings += profit_share

    def get_user_earnings(self, user_id: int) -> float:
        """
        Gets the earnings of a user.

        Args:
        - user_id (int): ID of the user.

        Returns:
        - float: Earnings of the user.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        return self.users[user_id].earnings


def main():
    system = TraderSubscriptionSystem()

    # Create traders
    system.create_trader(1, "Trader 1")
    system.create_trader(2, "Trader 2")

    # Create users
    system.create_user(1, "User 1")
    system.create_user(2, "User 2")

    # Subscribe users to traders
    system.subscribe_user_to_trader(1, 1)
    system.subscribe_user_to_trader(2, 1)
    system.subscribe_user_to_trader(1, 2)

    # Add profits to traders
    system.add_trader_profit(1, 1000.0)
    system.add_trader_profit(2, 500.0)

    # Get user earnings
    print("User 1 earnings:", system.get_user_earnings(1))
    print("User 2 earnings:", system.get_user_earnings(2))


if __name__ == "__main__":
    main()
```
