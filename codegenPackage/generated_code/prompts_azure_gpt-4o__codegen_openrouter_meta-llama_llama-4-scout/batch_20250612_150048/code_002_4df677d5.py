"""
Generated Code Metadata:
========================
Original URL: https://supremeprofund.com
Prompt: Generate code to simulate deposit and withdrawal transactions for SupremeProFund's platform, ensuring the funds used in ongoing trades are excluded from the withdrawal amount.
Generated: DETERMINISTIC_4df677d5ff0b47ba
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TransactionError(Exception):
    """Base class for transaction-related exceptions."""
    pass


class InsufficientBalanceError(TransactionError):
    """Raised when the account balance is insufficient for a transaction."""
    pass


class Trade:
    def __init__(self, trade_id, amount):
        """
        Initialize a Trade object.

        Args:
        - trade_id (int): Unique identifier for the trade.
        - amount (float): The amount of the trade.
        """
        self.trade_id = trade_id
        self.amount = amount


class SupremeProFundAccount:
    def __init__(self, account_id, initial_balance=0.0):
        """
        Initialize a SupremeProFundAccount object.

        Args:
        - account_id (int): Unique identifier for the account.
        - initial_balance (float, optional): The initial account balance. Defaults to 0.0.
        """
        self.account_id = account_id
        self.balance = initial_balance
        self.trades = []
        self.locked_funds = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args:
        - amount (float): The amount to deposit.

        Raises:
        - ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount

    def add_trade(self, trade):
        """
        Add a trade to the account and lock the trade amount.

        Args:
        - trade (Trade): The trade to add.

        Raises:
        - ValueError: If the trade amount exceeds the available balance.
        """
        if self.balance - self.locked_funds < trade.amount:
            raise InsufficientBalanceError("Insufficient balance for trade.")
        self.trades.append(trade)
        self.locked_funds += trade.amount

    def remove_trade(self, trade_id):
        """
        Remove a trade from the account and unlock the trade amount.

        Args:
        - trade_id (int): The ID of the trade to remove.

        Raises:
        - ValueError: If the trade is not found.
        """
        for trade in self.trades:
            if trade.trade_id == trade_id:
                self.locked_funds -= trade.amount
                self.trades.remove(trade)
                return
        raise ValueError("Trade not found.")

    def withdraw(self, amount):
        """
        Withdraw funds from the account, excluding locked funds.

        Args:
        - amount (float): The amount to withdraw.

        Raises:
        - InsufficientBalanceError: If the available balance is insufficient.
        - ValueError: If the withdrawal amount is negative.
        """
        available_balance = self.balance - self.locked_funds
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > available_balance:
            raise InsufficientBalanceError("Insufficient available balance.")
        self.balance -= amount


def main():
    account = SupremeProFundAccount(12345, 1000.0)

    try:
        account.deposit(500.0)
        print(f"Account balance after deposit: {account.balance}")

        trade1 = Trade(1, 200.0)
        account.add_trade(trade1)
        print(f"Locked funds after adding trade: {account.locked_funds}")

        account.withdraw(300.0)
        print(f"Account balance after withdrawal: {account.balance}")

        account.remove_trade(1)
        print(f"Locked funds after removing trade: {account.locked_funds}")

        account.withdraw(500.0)
        print(f"Account balance after second withdrawal: {account.balance}")
    except TransactionError as e:
        print(f"Transaction error: {e}")


if __name__ == "__main__":
    main()
```
