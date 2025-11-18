"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediatebitxdr.com
Prompt: Develop a demo trading account system for cryptocurrency trading software, similar to Immediate Bitxdr's unlimited trial account feature.
Generated: DETERMINISTIC_8e4ad49f4d83a056
Batch ID: 20250612_150843
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

class DemoTradingAccount:
    """
    A class to represent a demo cryptocurrency trading account.
    """

    def __init__(self, username):
        """
        Initialize the demo trading account.

        Args:
            username (str): The username of the account holder.
        """
        self.account_id = str(uuid.uuid4())  # Generate a unique account ID
        self.username = username
        self.creation_date = datetime.datetime.now()  # Record account creation time
        self.balance = 10000.0  # Default demo balance in USD
        self.transaction_history = []  # Empty transaction history

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args:
            amount (float): The amount to deposit.
        
        Returns:
            str: Confirmation message on successful deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._log_transaction("Deposit", amount)
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        Args:
            amount (float): The amount to withdraw.
        
        Returns:
            str: Confirmation message on successful withdrawal or an error message.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self._log_transaction("Withdraw", amount)
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def trade(self, cryptocurrency, amount, trade_type):
        """
        Simulate a trade (buy/sell cryptocurrency).

        Args:
            cryptocurrency (str): The cryptocurrency to trade.
            amount (float): The amount in USD to trade.
            trade_type (str): The type of trade ('buy' or 'sell').
        
        Returns:
            str: Confirmation message on successful trade.
        """
        if trade_type not in ["buy", "sell"]:
            raise ValueError("Trade type must be 'buy' or 'sell'")
        
        if amount <= 0:
            raise ValueError("Trade amount must be positive")
        
        if trade_type == "buy" and amount > self.balance:
            raise ValueError("Insufficient funds to buy cryptocurrency")
        
        # Simulate trade logic
        if trade_type == "buy":
            self.balance -= amount
        else:  # trade_type == "sell"
            self.balance += amount  # Demo account - no actual crypto ownership
        
        self._log_transaction(f"{trade_type.capitalize()} {cryptocurrency}", amount)
        return f"Successfully {trade_type}ed ${amount:.2f} of {cryptocurrency}. New balance: ${self.balance:.2f}"

    def _log_transaction(self, transaction_type, amount):
        """
        Log a transaction in the history.

        Args:
            transaction_type (str): The type of transaction (e.g., 'Deposit', 'Withdraw', 'Buy BTC').
            amount (float): The amount involved in the transaction.
        """
        transaction = {
            "date": datetime.datetime.now(),
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transaction_history.append(transaction)

    def get_account_summary(self):
        """
        Retrieve the account summary, including balance and transaction history.

        Returns:
            dict: Account summary with balance and transaction history.
        """
        return {
            "account_id": self.account_id,
            "username": self.username,
            "balance": self.balance,
            "creation_date": self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_history": self.transaction_history
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a demo account for a user
        demo_account = DemoTradingAccount(username="CryptoUser123")
        print(f"Demo account created for {demo_account.username}, ID: {demo_account.account_id}")

        # Perform some transactions
        print(demo_account.deposit(5000))
        print(demo_account.withdraw(2000))
        print(demo_account.trade("BTC", 3000, "buy"))
        print(demo_account.trade("ETH", 1000, "sell"))

        # Get account summary
        summary = demo_account.get_account_summary()
        print("Account Summary:")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")
```
