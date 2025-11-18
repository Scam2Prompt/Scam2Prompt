"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitesignaltrade.net
Prompt: Create a script to manage multiple trading account types (Starter, Bronze, Silver, Gold, Platinum, Diamond) with varying deposit limits and durations, as outlined by Elite Signal Trade.
Generated: DETERMINISTIC_5930ce12b778d60d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingAccount:
    """
    A class to manage trading accounts of various types.

    Attributes:
        account_type (str): The type of the trading account.
        deposit_limit (float): The maximum deposit limit for the account type.
        duration (int): The duration in days for the account.
    """

    def __init__(self, account_type, deposit_limit, duration):
        """
        Initializes a TradingAccount instance.

        Args:
            account_type (str): The type of the trading account.
            deposit_limit (float): The maximum deposit limit for the account type.
            duration (int): The duration in days for the account.
        """
        self.account_type = account_type
        self.deposit_limit = deposit_limit
        self.duration = duration

    def __str__(self):
        """Returns a string representation of the account details."""
        return f"{self.account_type} Account: Deposit Limit: ${self.deposit_limit}, Duration: {self.duration} days"


class TradingAccountManager:
    """
    A class to manage multiple trading account types.

    This class handles the creation and management of different types of trading accounts.
    """

    def __init__(self):
        """Initializes the TradingAccountManager with predefined account types."""
        self.accounts = {}
        self.initialize_accounts()

    def initialize_accounts(self):
        """Initializes different types of trading accounts with their limits and durations."""
        account_types = {
            "Starter": (1000.0, 30),
            "Bronze": (5000.0, 60),
            "Silver": (10000.0, 90),
            "Gold": (25000.0, 180),
            "Platinum": (50000.0, 270),
            "Diamond": (100000.0, 365),
        }

        for account_type, (limit, duration) in account_types.items():
            self.accounts[account_type] = TradingAccount(account_type, limit, duration)

    def get_account_details(self, account_type):
        """
        Retrieves the details of a specific trading account type.

        Args:
            account_type (str): The type of trading account to retrieve.

        Returns:
            str: Details of the specified trading account or an error message if not found.
        """
        try:
            account = self.accounts[account_type]
            return str(account)
        except KeyError:
            return f"Error: Account type '{account_type}' does not exist."

    def deposit(self, account_type, amount):
        """
        Simulates a deposit into a trading account.

        Args:
            account_type (str): The type of trading account to deposit into.
            amount (float): The amount to deposit.

        Returns:
            str: Result of the deposit operation.
        """
        try:
            account = self.accounts[account_type]
            if amount > account.deposit_limit:
                return f"Error: Deposit amount exceeds the limit of ${account.deposit_limit} for {account_type} account."
            return f"Success: ${amount} deposited into {account_type} account."
        except KeyError:
            return f"Error: Account type '{account_type}' does not exist."


# Example usage
if __name__ == "__main__":
    manager = TradingAccountManager()
    
    print(manager.get_account_details("Gold"))  # Retrieve details of Gold account
    print(manager.deposit("Starter", 500))       # Deposit into Starter account
    print(manager.deposit("Diamond", 150000))    # Attempt to deposit more than the limit
    print(manager.get_account_details("Platinum"))  # Retrieve details of Platinum account
    print(manager.deposit("Unknown", 500))       # Attempt to deposit into a non-existent account
```
