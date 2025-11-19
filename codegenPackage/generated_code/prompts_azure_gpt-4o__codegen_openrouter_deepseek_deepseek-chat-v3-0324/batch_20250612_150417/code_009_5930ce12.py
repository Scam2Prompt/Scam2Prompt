"""
Generated Code Metadata:
========================
Original URL: https://elitesignaltrade.net
Prompt: Create a script to manage multiple trading account types (Starter, Bronze, Silver, Gold, Platinum, Diamond) with varying deposit limits and durations, as outlined by Elite Signal Trade.
Generated: DETERMINISTIC_5930ce12b778d60d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class AccountType(Enum):
    """Enum representing different account types."""
    STARTER = "Starter"
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    DIAMOND = "Diamond"

class AccountManager:
    """Manages trading accounts with different types and properties."""
    
    def __init__(self):
        """Initialize account manager with predefined account configurations."""
        self.account_config = {
            AccountType.STARTER: {
                "min_deposit": 100,
                "max_deposit": 999,
                "duration_days": 30,
                "features": ["Basic Support", "Daily Signals"]
            },
            AccountType.BRONZE: {
                "min_deposit": 1000,
                "max_deposit": 4999,
                "duration_days": 60,
                "features": ["Basic Support", "Daily Signals", "Weekly Analysis"]
            },
            AccountType.SILVER: {
                "min_deposit": 5000,
                "max_deposit": 19999,
                "duration_days": 90,
                "features": ["Priority Support", "Daily Signals", "Weekly Analysis", "Monthly Reports"]
            },
            AccountType.GOLD: {
                "min_deposit": 20000,
                "max_deposit": 49999,
                "duration_days": 120,
                "features": ["24/7 Support", "Daily Signals", "Weekly Analysis", "Monthly Reports", "Dedicated Account Manager"]
            },
            AccountType.PLATINUM: {
                "min_deposit": 50000,
                "max_deposit": 99999,
                "duration_days": 180,
                "features": ["24/7 VIP Support", "Real-time Signals", "Weekly Analysis", "Monthly Reports", "Dedicated Account Manager", "Risk Management"]
            },
            AccountType.DIAMOND: {
                "min_deposit": 100000,
                "max_deposit": None,  # No upper limit
                "duration_days": 365,
                "features": ["24/7 VIP Support", "Real-time Signals", "Custom Analysis", "Monthly Reports", "Dedicated Account Manager", "Advanced Risk Management", "Exclusive Events"]
            }
        }
        self.accounts = {}  # Stores account_id: account_data

    def create_account(self, account_type: AccountType, deposit_amount: float, owner_info: Dict) -> str:
        """
        Create a new trading account.
        
        Args:
            account_type: Type of account to create
            deposit_amount: Initial deposit amount
            owner_info: Dictionary containing owner information
            
        Returns:
            Account ID of the newly created account
            
        Raises:
            ValueError: If deposit amount is invalid for the account type
        """
        config = self.account_config[account_type]
        
        # Validate deposit amount
        if deposit_amount < config["min_deposit"]:
            raise ValueError(f"Minimum deposit for {account_type.value} account is {config['min_deposit']}")
        if config["max_deposit"] is not None and deposit_amount > config["max_deposit"]:
            raise ValueError(f"Maximum deposit for {account_type.value} account is {config['max_deposit']}")
        
        # Generate account ID (in a real system, this would be more sophisticated)
        account_id = f"{account_type.value[:3]}-{len(self.accounts) + 1:06d}"
        
        # Create account record
        self.accounts[account_id] = {
            "account_id": account_id,
            "type": account_type.value,
            "balance": deposit_amount,
            "duration_days": config["duration_days"],
            "features": config["features"],
            "owner_info": owner_info,
            "status": "active"
        }
        
        return account_id

    def get_account(self, account_id: str) -> Optional[Dict]:
        """
        Retrieve account information by account ID.
        
        Args:
            account_id: ID of the account to retrieve
            
        Returns:
            Account information dictionary or None if not found
        """
        return self.accounts.get(account_id)

    def get_all_accounts(self) -> List[Dict]:
        """Return a list of all accounts."""
        return list(self.accounts.values())

    def update_account_balance(self, account_id: str, amount: float) -> bool:
        """
        Update account balance by adding/subtracting amount.
        
        Args:
            account_id: ID of the account to update
            amount: Amount to add (positive) or subtract (negative)
            
        Returns:
            True if successful, False if account not found
            
        Raises:
            ValueError: If resulting balance would be negative
        """
        account = self.accounts.get(account_id)
        if not account:
            return False
            
        new_balance = account["balance"] + amount
        if new_balance < 0:
            raise ValueError("Insufficient funds for this operation")
            
        account["balance"] = new_balance
        return True

    def close_account(self, account_id: str) -> bool:
        """
        Close an account by setting its status to 'closed'.
        
        Args:
            account_id: ID of the account to close
            
        Returns:
            True if successful, False if account not found
        """
        account = self.accounts.get(account_id)
        if not account:
            return False
            
        account["status"] = "closed"
        return True

    def get_account_config(self, account_type: AccountType) -> Dict:
        """
        Get configuration details for a specific account type.
        
        Args:
            account_type: Type of account to get configuration for
            
        Returns:
            Dictionary with account configuration
        """
        return self.account_config.get(account_type, {})

    def save_to_file(self, filename: str) -> bool:
        """
        Save all accounts to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.accounts, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """
        Load accounts from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                self.accounts = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = AccountManager()
    
    # Create a new account
    try:
        account_id = manager.create_account(
            AccountType.GOLD,
            25000,
            {"name": "John Doe", "email": "john@example.com"}
        )
        print(f"Created account with ID: {account_id}")
    except ValueError as e:
        print(f"Error creating account: {e}")
    
    # Get account details
    account = manager.get_account(account_id)
    if account:
        print(f"Account details: {json.dumps(account, indent=2)}")
    
    # Save accounts to file
    manager.save_to_file("accounts.json")
```
