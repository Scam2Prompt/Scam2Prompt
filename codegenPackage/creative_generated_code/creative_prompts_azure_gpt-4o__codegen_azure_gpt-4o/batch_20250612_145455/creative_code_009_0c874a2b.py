"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://echotradeoptions.com
Prompt: Write a program to calculate daily returns for a trading account based on Echo Trade's percentage-based ROI structure for different account types.
Generated: DETERMINISTIC_0c874a2b4f12652e
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class TradingAccount:
    """
    A class representing a trading account with a specific ROI structure.
    """
    # ROI structure based on account type
    ROI_BY_ACCOUNT_TYPE = {
        'basic': 0.01,  # 1% daily ROI
        'standard': 0.015,  # 1.5% daily ROI
        'premium': 0.02,  # 2% daily ROI
        'vip': 0.025  # 2.5% daily ROI
    }

    def __init__(self, account_type: str, balance: float):
        """
        Initialize a TradingAccount object with the account type and starting balance.

        Args:
            account_type (str): The type of account (e.g., 'basic', 'standard', 'premium', 'vip').
            balance (float): The starting balance in the account.
        """
        if account_type not in self.ROI_BY_ACCOUNT_TYPE:
            raise ValueError(f"Invalid account type: {account_type}. Must be one of {list(self.ROI_BY_ACCOUNT_TYPE.keys())}")
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        
        self.account_type = account_type
        self.balance = balance

    def calculate_daily_return(self) -> float:
        """
        Calculate the daily return based on the account's ROI structure.

        Returns:
            float: The daily return amount.
        """
        roi = self.ROI_BY_ACCOUNT_TYPE[self.account_type]
        return self.balance * roi


def calculate_daily_returns_for_accounts(accounts: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Calculate the daily returns for a list of trading accounts.

    Args:
        accounts (List[Dict[str, str]]): A list of dictionaries representing accounts with 'account_type' and 'balance'.

    Returns:
        Dict[str, float]: A dictionary mapping account types to their calculated daily returns.
    """
    daily_returns = {}

    for account_data in accounts:
        try:
            # Extract account information
            account_type = account_data.get('account_type')
            balance = float(account_data.get('balance', 0))
            
            # Create a TradingAccount object
            account = TradingAccount(account_type, balance)
            
            # Calculate and store the daily return
            daily_returns[account_type] = account.calculate_daily_return()
        except (ValueError, TypeError) as e:
            # Log the error (in real production code, use a proper logger)
            print(f"Error processing account {account_data}: {e}")

    return daily_returns


# Example usage (would normally be in a separate main function or script):
if __name__ == "__main__":
    # Sample account data
    accounts_data = [
        {'account_type': 'basic', 'balance': 1000},
        {'account_type': 'standard', 'balance': 2000},
        {'account_type': 'premium', 'balance': 5000},
        {'account_type': 'vip', 'balance': 10000},
        {'account_type': 'invalid', 'balance': 3000},  # Invalid account type, for testing error handling
    ]

    results = calculate_daily_returns_for_accounts(accounts_data)
    for account_type, daily_return in results.items():
        print(f"Account Type: {account_type}, Daily Return: ${daily_return:.2f}")
```
