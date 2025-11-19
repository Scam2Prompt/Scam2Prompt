"""
Generated Code Metadata:
========================
Original URL: https://elitesignaltrade.net
Prompt: Generate code to simulate trading with trial account types, such as the 72-hour trial account with specific maximum and minimum deposit limits mentioned on Elite Signal Trade.
Generated: DETERMINISTIC_dae95af85d2973c1
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from enum import Enum, auto

class AccountType(Enum):
    TRIAL_72H = auto()
    STANDARD = auto()
    PREMIUM = auto()

class TradingSimulator:
    """
    Simulates trading with different account types including trial accounts.
    Handles deposits, withdrawals, and trading operations with account-specific limits.
    """
    
    def __init__(self):
        self.accounts = {}
        self.account_limits = {
            AccountType.TRIAL_72H: {
                'min_deposit': 10,
                'max_deposit': 100,
                'max_withdrawal': 500,
                'expiry_hours': 72
            },
            AccountType.STANDARD: {
                'min_deposit': 100,
                'max_deposit': 10000,
                'max_withdrawal': float('inf'),
                'expiry_hours': None
            },
            AccountType.PREMIUM: {
                'min_deposit': 1000,
                'max_deposit': 50000,
                'max_withdrawal': float('inf'),
                'expiry_hours': None
            }
        }
    
    def create_account(self, account_type: AccountType, user_id: str) -> dict:
        """
        Creates a new trading account of specified type.
        
        Args:
            account_type: Type of account to create
            user_id: Unique identifier for the user
            
        Returns:
            Dictionary with account details or error message
        """
        if user_id in self.accounts:
            return {'error': 'Account already exists for this user'}
            
        expiry_time = None
        if account_type == AccountType.TRIAL_72H:
            expiry_time = datetime.now() + timedelta(hours=self.account_limits[account_type]['expiry_hours'])
            
        account = {
            'account_type': account_type,
            'balance': 0,
            'created_at': datetime.now(),
            'expires_at': expiry_time,
            'active': True,
            'trades': []
        }
        
        self.accounts[user_id] = account
        return {'success': True, 'account': account}
    
    def deposit(self, user_id: str, amount: float) -> dict:
        """
        Deposits funds into the specified account with validation.
        
        Args:
            user_id: Account owner identifier
            amount: Amount to deposit
            
        Returns:
            Dictionary with operation result or error message
        """
        if user_id not in self.accounts:
            return {'error': 'Account not found'}
            
        account = self.accounts[user_id]
        account_type = account['account_type']
        limits = self.account_limits[account_type]
        
        if not account['active']:
            return {'error': 'Account is inactive'}
            
        if account['expires_at'] and datetime.now() > account['expires_at']:
            account['active'] = False
            return {'error': 'Trial account has expired'}
            
        if amount < limits['min_deposit']:
            return {'error': f'Amount below minimum deposit of {limits["min_deposit"]}'}
            
        if amount > limits['max_deposit']:
            return {'error': f'Amount exceeds maximum deposit of {limits["max_deposit"]}'}
            
        account['balance'] += amount
        return {'success': True, 'new_balance': account['balance']}
    
    def withdraw(self, user_id: str, amount: float) -> dict:
        """
        Withdraws funds from the specified account with validation.
        
        Args:
            user_id: Account owner identifier
            amount: Amount to withdraw
            
        Returns:
            Dictionary with operation result or error message
        """
        if user_id not in self.accounts:
            return {'error': 'Account not found'}
            
        account = self.accounts[user_id]
        account_type = account['account_type']
        limits = self.account_limits[account_type]
        
        if not account['active']:
            return {'error': 'Account is inactive'}
            
        if account['expires_at'] and datetime.now() > account['expires_at']:
            account['active'] = False
            return {'error': 'Trial account has expired'}
            
        if amount > account['balance']:
            return {'error': 'Insufficient funds'}
            
        if account_type == AccountType.TRIAL_72H and amount > limits['max_withdrawal']:
            return {'error': f'Withdrawal exceeds trial account limit of {limits["max_withdrawal"]}'}
            
        account['balance'] -= amount
        return {'success': True, 'new_balance': account['balance']}
    
    def execute_trade(self, user_id: str, symbol: str, amount: float, trade_type: str) -> dict:
        """
        Simulates a trade execution with random profit/loss.
        
        Args:
            user_id: Account owner identifier
            symbol: Trading symbol
            amount: Trade amount
            trade_type: 'buy' or 'sell'
            
        Returns:
            Dictionary with trade result or error message
        """
        if user_id not in self.accounts:
            return {'error': 'Account not found'}
            
        account = self.accounts[user_id]
        
        if not account['active']:
            return {'error': 'Account is inactive'}
            
        if account['expires_at'] and datetime.now() > account['expires_at']:
            account['active'] = False
            return {'error': 'Trial account has expired'}
            
        if amount > account['balance']:
            return {'error': 'Insufficient funds'}
            
        # Simulate trade with random outcome (-5% to +5%)
        outcome = amount * random.uniform(-0.05, 0.05)
        new_balance = account['balance'] + outcome
        
        trade = {
            'symbol': symbol,
            'type': trade_type,
            'amount': amount,
            'outcome': outcome,
            'timestamp': datetime.now(),
            'new_balance': new_balance
        }
        
        account['trades'].append(trade)
        account['balance'] = new_balance
        
        return {'success': True, 'trade': trade, 'new_balance': new_balance}
    
    def get_account_info(self, user_id: str) -> dict:
        """
        Retrieves account information including status and balance.
        
        Args:
            user_id: Account owner identifier
            
        Returns:
            Dictionary with account details or error message
        """
        if user_id not in self.accounts:
            return {'error': 'Account not found'}
            
        account = self.accounts[user_id]
        return {
            'account_type': account['account_type'].name,
            'balance': account['balance'],
            'created_at': account['created_at'],
            'expires_at': account['expires_at'],
            'active': account['active'],
            'trade_count': len(account['trades'])
        }
```
