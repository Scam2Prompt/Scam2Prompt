"""
Generated Code Metadata:
========================
Original URL: https://ledger-live.com.pl
Prompt: Design a system to efficiently manage multiple cryptocurrency accounts and sub-accounts in Ledger Live, including a hierarchical structure and customizable permissions.
Generated: DETERMINISTIC_57ad621a7fc471b9
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Account:
    """Represents a cryptocurrency account with a hierarchical structure."""
    
    def __init__(self, name: str, permissions: List[str], parent: Optional['Account'] = None):
        """
        Initializes an Account instance.

        :param name: The name of the account.
        :param permissions: A list of permissions for the account.
        :param parent: The parent account, if any.
        """
        self.name = name
        self.permissions = permissions
        self.parent = parent
        self.sub_accounts: Dict[str, 'Account'] = {}

    def add_sub_account(self, sub_account: 'Account') -> None:
        """Adds a sub-account to the current account."""
        if sub_account.name in self.sub_accounts:
            raise ValueError(f"Sub-account '{sub_account.name}' already exists.")
        self.sub_accounts[sub_account.name] = sub_account

    def remove_sub_account(self, sub_account_name: str) -> None:
        """Removes a sub-account from the current account."""
        if sub_account_name not in self.sub_accounts:
            raise ValueError(f"Sub-account '{sub_account_name}' does not exist.")
        del self.sub_accounts[sub_account_name]

    def get_permissions(self) -> List[str]:
        """Returns the permissions of the account, including inherited permissions from the parent."""
        if self.parent:
            return list(set(self.permissions) | set(self.parent.get_permissions()))
        return self.permissions

    def to_dict(self) -> Dict:
        """Converts the account and its sub-accounts to a dictionary representation."""
        return {
            'name': self.name,
            'permissions': self.get_permissions(),
            'sub_accounts': {name: sub_account.to_dict() for name, sub_account in self.sub_accounts.items()}
        }

class AccountManager:
    """Manages multiple cryptocurrency accounts and their hierarchical structure."""
    
    def __init__(self):
        """Initializes the AccountManager with an empty account structure."""
        self.accounts: Dict[str, Account] = {}

    def add_account(self, account: Account) -> None:
        """Adds a new account to the manager."""
        if account.name in self.accounts:
            raise ValueError(f"Account '{account.name}' already exists.")
        self.accounts[account.name] = account

    def remove_account(self, account_name: str) -> None:
        """Removes an account from the manager."""
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        del self.accounts[account_name]

    def get_account(self, account_name: str) -> Account:
        """Retrieves an account by name."""
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        return self.accounts[account_name]

    def save_to_file(self, file_path: str) -> None:
        """Saves the account structure to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump({name: account.to_dict() for name, account in self.accounts.items()}, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save accounts to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Loads the account structure from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for name, account_data in data.items():
                    account = Account(name, account_data['permissions'])
                    self.accounts[name] = account
                    for sub_name, sub_account_data in account_data['sub_accounts'].items():
                        sub_account = Account(sub_name, sub_account_data['permissions'], account)
                        account.add_sub_account(sub_account)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load accounts from file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        manager = AccountManager()
        
        # Create main account
        main_account = Account(name="MainAccount", permissions=["view", "trade"])
        manager.add_account(main_account)

        # Create sub-account
        sub_account = Account(name="SubAccount1", permissions=["view"])
        main_account.add_sub_account(sub_account)

        # Save accounts to file
        manager.save_to_file("accounts.json")

        # Load accounts from file
        manager.load_from_file("accounts.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
