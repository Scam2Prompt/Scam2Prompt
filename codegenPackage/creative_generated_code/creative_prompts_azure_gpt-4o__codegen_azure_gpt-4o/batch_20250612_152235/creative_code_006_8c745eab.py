"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-8sr.pages.dev
Prompt: Suggest a method to implement localized P2P trading with support for multiple currencies, similar to Blum's global trading opportunities.
Generated: DETERMINISTIC_8c745eabdc3046e0
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime
from typing import List, Dict, Union

# ------------------------------
# Models for P2P Trading System
# ------------------------------

class Trade:
    """
    Represents a P2P trade between two parties for a specific currency and amount.
    """
    def __init__(self, trade_id: str, seller_id: str, buyer_id: str,
                 currency: str, amount: float, price_per_unit: float, status: str):
        self.trade_id = trade_id  # Unique identifier for the trade
        self.seller_id = seller_id  # ID of the seller
        self.buyer_id = buyer_id  # ID of the buyer
        self.currency = currency  # Currency being traded (e.g., USD, EUR, BTC)
        self.amount = amount  # Amount of currency being traded
        self.price_per_unit = price_per_unit  # Price per unit of currency
        self.status = status  # Status of the trade (e.g., "Pending", "Completed", "Cancelled")
        self.created_at = datetime.datetime.now()  # Timestamp for trade creation

    def __repr__(self):
        return f"<Trade {self.trade_id}: {self.currency} {self.amount} @ {self.price_per_unit} ({self.status})>"

class User:
    """
    Represents a user in the trading system.
    """
    def __init__(self, user_id: str, name: str, location: str, balance: Dict[str, float]):
        self.user_id = user_id  # Unique ID for the user
        self.name = name  # Name of the user
        self.location = location  # Geographic location of the user
        self.balance = balance  # Balance of various currencies (e.g., {"USD": 100.0, "BTC": 0.5})

    def __repr__(self):
        return f"<User {self.user_id}: {self.name} ({self.location})>"

# ------------------------------
# P2P Trading Service
# ------------------------------

class P2PTradingService:
    """
    Service for localized P2P trading with multi-currency support.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}  # Mapping of user_id to User
        self.trades: List[Trade] = []  # List of all trades in the system

    def register_user(self, name: str, location: str, initial_balance: Dict[str, float]) -> str:
        """
        Registers a new user in the system.
        :param name: Name of the user.
        :param location: Geographic location of the user.
        :param initial_balance: Initial currency balance.
        :return: User ID of the newly registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.users[user_id] = User(user_id, name, location, initial_balance)
        print(f"User {name} registered successfully with ID {user_id}.")
        return user_id

    def create_trade(self, seller_id: str, buyer_id: str, currency: str,
                     amount: float, price_per_unit: float) -> Union[str, None]:
        """
        Creates a new trade between a seller and a buyer.
        :param seller_id: ID of the seller.
        :param buyer_id: ID of the buyer.
        :param currency: Currency to be traded.
        :param amount: Amount of currency to be traded.
        :param price_per_unit: Price per unit of currency.
        :return: Trade ID of the created trade, or None if the trade could not be created.
        """
        # Validate user IDs
        if seller_id not in self.users or buyer_id not in self.users:
            print(f"Error: Invalid seller or buyer ID.")
            return None

        seller = self.users[seller_id]
        buyer = self.users[buyer_id]

        # Check if seller has sufficient balance
        if seller.balance.get(currency, 0) < amount:
            print(f"Error: Insufficient balance for seller {seller_id}.")
            return None

        # Deduct currency from seller and add to buyer (temporary for illustration)
        seller.balance[currency] -= amount
        buyer.balance[currency] = buyer.balance.get(currency, 0) + amount

        # Create trade object
        trade_id = str(uuid.uuid4())
        trade = Trade(trade_id, seller_id, buyer_id, currency, amount, price_per_unit, "Completed")
        self.trades.append(trade)

        print(f"Trade {trade_id} created successfully.")
        return trade_id

    def get_trades(self) -> List[Trade]:
        """
        Retrieves all trades in the system.
        :return: List of Trade objects.
        """
        return self.trades

    def get_user_balance(self, user_id: str) -> Union[Dict[str, float], None]:
        """
        Retrieves the balance of a user.
        :param user_id: ID of the user.
        :return: Dictionary of currency balances, or None if the user does not exist.
        """
        user = self.users.get(user_id)
        if not user:
            print(f"Error: User {user_id} not found.")
            return None
        return user.balance

# ------------------------------
# Example Usage
# ------------------------------

if __name__ == "__main__":
    # Initialize trading service
    service = P2PTradingService()

    # Register users
    alice_id = service.register_user("Alice", "New York", {"USD": 500, "BTC": 1.0})
    bob_id = service.register_user("Bob", "San Francisco", {"USD": 300, "BTC": 0.5})

    # Create a trade
    trade_id = service.create_trade(alice_id, bob_id, "BTC", 0.5, 25000)

    # Print trades
    print("All trades:")
    for trade in service.get_trades():
        print(trade)

    # Print user balances
    print("User balances:")
    print(f"Alice: {service.get_user_balance(alice_id)}")
    print(f"Bob: {service.get_user_balance(bob_id)}")
```

This code is designed to simulate a localized P2P trading system with support for multiple currencies. It includes user registration, trade creation, and balance management functionalities, following best practices and error handling.
