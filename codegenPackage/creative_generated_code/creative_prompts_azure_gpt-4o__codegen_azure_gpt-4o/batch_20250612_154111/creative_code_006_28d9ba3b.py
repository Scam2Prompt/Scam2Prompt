"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokereo.com
Prompt: Create a program to simulate the closure of trades and accounts, ensuring compliance with the timeline provided by Brokereo (October 31, 2022).
Generated: DETERMINISTIC_28d9ba3ba7282e79
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Trade:
    def __init__(self, trade_id, account_id, open_date, close_date=None):
        """
        Initialize a Trade instance.

        :param trade_id: Unique identifier for the trade.
        :param account_id: Identifier for the associated account.
        :param open_date: Date when the trade was opened (datetime object).
        :param close_date: Date when the trade was closed (datetime object, default None).
        """
        self.trade_id = trade_id
        self.account_id = account_id
        self.open_date = open_date
        self.close_date = close_date

    def close_trade(self, close_date):
        """
        Close the trade with the provided closing date.

        :param close_date: Date when the trade is closed (datetime object).
        :raises ValueError: If the closing date is earlier than the opening date.
        """
        if close_date < self.open_date:
            raise ValueError("Closing date cannot be earlier than the opening date.")
        self.close_date = close_date


class Account:
    def __init__(self, account_id, creation_date, closure_date=None):
        """
        Initialize an Account instance.

        :param account_id: Unique identifier for the account.
        :param creation_date: Date when the account was created (datetime object).
        :param closure_date: Date when the account was closed (datetime object, default None).
        """
        self.account_id = account_id
        self.creation_date = creation_date
        self.closure_date = closure_date
        self.trades = []

    def add_trade(self, trade):
        """
        Add a trade to the account.

        :param trade: Trade object to be added.
        """
        self.trades.append(trade)

    def close_account(self, closure_date):
        """
        Close the account with the provided closing date.

        :param closure_date: Date when the account is closed (datetime object).
        :raises ValueError: If the closing date is earlier than the creation date.
        """
        if closure_date < self.creation_date:
            raise ValueError("Closure date cannot be earlier than the account creation date.")
        for trade in self.trades:
            if trade.close_date is None:
                raise RuntimeError(f"Trade {trade.trade_id} is not closed. Close all trades before closing the account.")
        self.closure_date = closure_date


def simulate_closure(trades, accounts, closure_deadline):
    """
    Simulate the closure of trades and accounts by the given deadline.

    :param trades: List of Trade objects.
    :param accounts: List of Account objects.
    :param closure_deadline: Deadline for closure (datetime object).
    """
    print(f"Simulating closure process. Deadline for closure: {closure_deadline.strftime('%Y-%m-%d')}")

    # Close all trades
    for trade in trades:
        if trade.close_date is None:
            try:
                trade.close_trade(closure_deadline)
                print(f"Trade {trade.trade_id} successfully closed.")
            except ValueError as e:
                print(f"Error closing trade {trade.trade_id}: {e}")

    # Close all accounts
    for account in accounts:
        if account.closure_date is None:
            try:
                account.close_account(closure_deadline)
                print(f"Account {account.account_id} successfully closed.")
            except (ValueError, RuntimeError) as e:
                print(f"Error closing account {account.account_id}: {e}")


if __name__ == "__main__":
    # Simulated data
    closure_deadline = datetime.datetime(2022, 10, 31)

    # Create trades
    trade1 = Trade(trade_id=1, account_id=101, open_date=datetime.datetime(2022, 9, 1))
    trade2 = Trade(trade_id=2, account_id=102, open_date=datetime.datetime(2022, 9, 15))

    # Create accounts
    account1 = Account(account_id=101, creation_date=datetime.datetime(2022, 8, 1))
    account2 = Account(account_id=102, creation_date=datetime.datetime(2022, 8, 15))

    # Link trades to accounts
    account1.add_trade(trade1)
    account2.add_trade(trade2)

    # Simulate closure process
    simulate_closure(trades=[trade1, trade2], accounts=[account1, account2], closure_deadline=closure_deadline)
```
