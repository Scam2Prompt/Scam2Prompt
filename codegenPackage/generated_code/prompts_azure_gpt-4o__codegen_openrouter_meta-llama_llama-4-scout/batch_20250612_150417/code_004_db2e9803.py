"""
Generated Code Metadata:
========================
Original URL: https://crptominer.com
Prompt: Write a Python script to simulate the withdrawal process described on CrptoMiner, ensuring funds used in ongoing trades are excluded from the available balance.
Generated: DETERMINISTIC_db2e98034067f618
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CryptoMiner:
    def __init__(self, balance=0.0):
        """
        Initialize CryptoMiner with an optional initial balance.

        Args:
            balance (float, optional): Initial balance. Defaults to 0.0.
        """
        self.balance = balance
        self.trades = {}

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def open_trade(self, trade_id, amount):
        """
        Open a new trade.

        Args:
            trade_id (str): Unique trade ID.
            amount (float): Amount used in the trade.

        Raises:
            ValueError: If trade amount is negative or exceeds available balance.
        """
        if amount < 0:
            raise ValueError("Trade amount cannot be negative")
        if amount > self.get_available_balance():
            raise ValueError("Insufficient funds for trade")
        self.trades[trade_id] = amount

    def close_trade(self, trade_id):
        """
        Close an ongoing trade.

        Args:
            trade_id (str): Unique trade ID.

        Raises:
            KeyError: If trade ID does not exist.
        """
        if trade_id not in self.trades:
            raise KeyError("Trade ID does not exist")
        del self.trades[trade_id]

    def get_available_balance(self):
        """
        Get the available balance excluding funds used in ongoing trades.

        Returns:
            float: Available balance.
        """
        used_in_trades = sum(self.trades.values())
        return self.balance - used_in_trades

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If withdrawal amount is negative or exceeds available balance.
        """
        available_balance = self.get_available_balance()
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > available_balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.balance -= amount


def main():
    miner = CryptoMiner(1000.0)  # Initialize with a balance of 1000.0

    try:
        miner.open_trade("TRADE-1", 200.0)  # Open a trade using 200.0
        print(f"Available balance after opening trade: {miner.get_available_balance()}")

        miner.withdraw(500.0)  # Attempt to withdraw 500.0
        print(f"Available balance after withdrawal: {miner.get_available_balance()}")

        miner.close_trade("TRADE-1")  # Close the ongoing trade
        print(f"Available balance after closing trade: {miner.get_available_balance()}")

        miner.withdraw(300.0)  # Attempt to withdraw 300.0 after closing trade
        print(f"Final available balance: {miner.get_available_balance()}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
