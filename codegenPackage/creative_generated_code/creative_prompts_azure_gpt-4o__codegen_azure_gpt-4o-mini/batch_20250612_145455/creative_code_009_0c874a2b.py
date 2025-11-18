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
import pandas as pd

class TradingAccount:
    """
    A class to represent a trading account with a specific account type and its return on investment (ROI) structure.
    """
    ACCOUNT_TYPES = {
        'basic': 0.05,   # 5% ROI for basic accounts
        'premium': 0.10, # 10% ROI for premium accounts
        'vip': 0.15      # 15% ROI for VIP accounts
    }
    
    def __init__(self, account_type: str, initial_balance: float):
        """
        Initializes a TradingAccount instance.
        
        :param account_type: Type of the trading account ('basic', 'premium', 'vip').
        :param initial_balance: The initial balance of the account.
        :raises ValueError: If the account type is not valid or initial balance is negative.
        """
        if account_type not in self.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type: {account_type}. Must be one of {list(self.ACCOUNT_TYPES.keys())}.")
        if initial_balance < 0:
            raise ValueError("Initial balance must be non-negative.")
        self.account_type = account_type
        self.initial_balance = initial_balance
    
    def calculate_daily_return(self) -> float:
        """
        Calculates the daily return based on the account type's ROI.
        
        :return: Daily return amount.
        """
        roi_percentage = self.ACCOUNT_TYPES[self.account_type]
        daily_return = self.initial_balance * roi_percentage
        return daily_return

def calculate_returns_for_accounts(accounts: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily returns for a list of trading accounts.
    
    :param accounts: DataFrame containing account types and their corresponding balances.
    :return: DataFrame with account types, balances, and calculated daily returns.
    :raises ValueError: If the input DataFrame does not contain the required columns.
    """
    # Validate input DataFrame
    if not all(col in accounts.columns for col in ['account_type', 'initial_balance']):
        raise ValueError("Input DataFrame must contain 'account_type' and 'initial_balance' columns.")
    
    # List to store results
    results = []
    
    # Calculate daily returns for each account
    for _, row in accounts.iterrows():
        account_type = row['account_type']
        initial_balance = row['initial_balance']
        
        try:
            account = TradingAccount(account_type, initial_balance)
            daily_return = account.calculate_daily_return()
            results.append({'account_type': account_type, 'initial_balance': initial_balance, 'daily_return': daily_return})
        except ValueError as e:
            results.append({'account_type': account_type, 'initial_balance': initial_balance, 'daily_return': str(e)})
    
    return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    # Sample DataFrame of trading accounts
    account_data = {
        'account_type': ['basic', 'premium', 'vip', 'basic'],
        'initial_balance': [1000, 2000, 1500, -500]  # Note: One invalid initial balance for testing error handling
    }

    accounts_df = pd.DataFrame(account_data)
    
    # Calculate daily returns
    try:
        daily_returns_df = calculate_returns_for_accounts(accounts_df)
        print(daily_returns_df)
    except ValueError as e:
        print(f"Error: {e}")
```
