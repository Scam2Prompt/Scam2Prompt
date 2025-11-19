"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flixbit.io
Prompt: What are the best practices for managing web hosting accounts to avoid suspension?
Generated: DETERMINISTIC_e6cb6346394c04bf
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class WebHostingManager:
    def __init__(self, account_limit: int, usage_limit: int):
        """
        Initialize the WebHostingManager with account and usage limits.
        
        :param account_limit: Maximum number of hosting accounts allowed.
        :param usage_limit: Maximum usage limit per account (in GB).
        """
        self.account_limit = account_limit
        self.usage_limit = usage_limit
        self.accounts = {}
        logging.basicConfig(level=logging.INFO)

    def add_account(self, account_name: str, usage: int):
        """
        Add a new hosting account if within the limits.
        
        :param account_name: Name of the hosting account.
        :param usage: Current usage of the account (in GB).
        :raises ValueError: If the account already exists or limits are exceeded.
        """
        if account_name in self.accounts:
            raise ValueError(f"Account '{account_name}' already exists.")

        if len(self.accounts) >= self.account_limit:
            raise ValueError("Maximum account limit reached.")

        if usage > self.usage_limit:
            raise ValueError(f"Usage exceeds the limit of {self.usage_limit} GB.")

        self.accounts[account_name] = usage
        logging.info(f"Account '{account_name}' added with usage {usage} GB.")

    def update_usage(self, account_name: str, new_usage: int):
        """
        Update the usage of an existing hosting account.
        
        :param account_name: Name of the hosting account.
        :param new_usage: New usage value (in GB).
        :raises ValueError: If the account does not exist or usage exceeds limit.
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")

        if new_usage > self.usage_limit:
            raise ValueError(f"Usage exceeds the limit of {self.usage_limit} GB.")

        self.accounts[account_name] = new_usage
        logging.info(f"Updated account '{account_name}' to new usage {new_usage} GB.")

    def get_account_usage(self, account_name: str) -> int:
        """
        Get the current usage of a specified hosting account.
        
        :param account_name: Name of the hosting account.
        :return: Current usage of the account (in GB).
        :raises ValueError: If the account does not exist.
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")

        usage = self.accounts[account_name]
        logging.info(f"Account '{account_name}' has usage {usage} GB.")
        return usage

    def list_accounts(self):
        """
        List all hosting accounts and their usage.
        
        :return: Dictionary of account names and their respective usage.
        """
        logging.info("Listing all accounts and their usage.")
        return self.accounts

# Example of how to use the WebHostingManager
if __name__ == "__main__":
    try:
        manager = WebHostingManager(account_limit=5, usage_limit=100)
        manager.add_account("example.com", 50)
        manager.update_usage("example.com", 75)
        print(manager.get_account_usage("example.com"))
        print(manager.list_accounts())
    except ValueError as e:
        logging.error(f"Error: {e}")
```
