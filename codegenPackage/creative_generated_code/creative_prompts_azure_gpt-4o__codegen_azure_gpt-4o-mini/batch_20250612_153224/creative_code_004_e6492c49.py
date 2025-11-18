"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwakeelacademy.com
Prompt: Write code to implement a financial accounting solution inspired by the techniques mentioned on Alwakeel Academy's website.
Generated: DETERMINISTIC_e6492c498925fc2e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Account:
    """A class to represent a financial account."""

    def __init__(self, account_name: str, initial_balance: float = 0.0):
        """
        Initialize an Account instance.

        :param account_name: Name of the account.
        :param initial_balance: Initial balance of the account, defaults to 0.0.
        """
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount into the account.

        :param amount: Amount to be deposited. Must be positive.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the account.

        :param amount: Amount to be withdrawn. Must be positive and less than or equal to balance.
        :raises ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """
        Retrieve the current balance of the account.

        :return: Current balance.
        """
        return self.balance


class Transaction:
    """A class to represent a financial transaction."""

    def __init__(self, account: Account, amount: float, transaction_type: str):
        """
        Initialize a Transaction instance.

        :param account: Account associated with the transaction.
        :param amount: Amount of the transaction.
        :param transaction_type: Type of transaction ('deposit' or 'withdraw').
        """
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def execute(self) -> None:
        """
        Execute the transaction.

        :raises ValueError: If the transaction type is invalid.
        """
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            raise ValueError("Invalid transaction type. Must be 'deposit' or 'withdraw'.")


class FinancialSystem:
    """A simple financial system to manage accounts and transactions."""

    def __init__(self):
        """Initialize the FinancialSystem with an empty list of accounts."""
        self.accounts = {}

    def create_account(self, account_name: str, initial_balance: float = 0.0) -> Account:
        """
        Create a new account and store it in the system.

        :param account_name: Name of the new account.
        :param initial_balance: Initial balance for the new account, defaults to 0.0.
        :return: The created Account instance.
        :raises ValueError: If the account name already exists.
        """
        if account_name in self.accounts:
            raise ValueError("Account name already exists.")
        account = Account(account_name, initial_balance)
        self.accounts[account_name] = account
        return account

    def get_account(self, account_name: str) -> Account:
        """
        Retrieve an account by name.

        :param account_name: Name of the account to retrieve.
        :return: The Account instance.
        :raises KeyError: If the account does not exist.
        """
        try:
            return self.accounts[account_name]
        except KeyError:
            raise KeyError("Account does not exist.")

    def execute_transaction(self, account_name: str, amount: float, transaction_type: str) -> None:
        """
        Execute a transaction on a specified account.

        :param account_name: Name of the account to execute the transaction on.
        :param amount: Amount for the transaction.
        :param transaction_type: Type of transaction ('deposit' or 'withdraw').
        """
        account = self.get_account(account_name)
        transaction = Transaction(account, amount, transaction_type)
        transaction.execute()


# Example usage (this would typically be outside of the module):
if __name__ == "__main__":
    try:
        system = FinancialSystem()
        account = system.create_account("Savings", 1000.0)
        system.execute_transaction("Savings", 500.0, "deposit")
        system.execute_transaction("Savings", 200.0, "withdraw")
        print(f"Final balance in {account.account_name}: {account.get_balance()}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
