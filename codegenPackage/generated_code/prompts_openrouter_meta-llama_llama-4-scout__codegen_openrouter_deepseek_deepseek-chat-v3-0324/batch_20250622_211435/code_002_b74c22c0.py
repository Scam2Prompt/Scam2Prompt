"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Generate a code snippet to implement a self-deposit and withdrawal system for online betting IDs, as described on JitoDaily.
Generated: DETERMINISTIC_b74c22c044464ec5
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from decimal import Decimal, getcontext
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set decimal precision
getcontext().prec = 6

class InsufficientFundsError(Exception):
    """Raised when user attempts to withdraw more than their balance"""
    pass

class InvalidAmountError(Exception):
    """Raised when amount is negative or zero"""
    pass

class BettingAccount:
    def __init__(self, account_id: str, initial_balance: Decimal = Decimal('0.00')):
        """
        Initialize a betting account with an ID and optional initial balance
        
        Args:
            account_id: Unique identifier for the account
            initial_balance: Starting balance (default: 0.00)
        """
        self.account_id = account_id
        self.balance = initial_balance
        self.transaction_history = []
        logger.info(f"Account {account_id} initialized with balance: {initial_balance}")

    def deposit(self, amount: Decimal) -> Decimal:
        """
        Deposit funds into the account
        
        Args:
            amount: Positive decimal amount to deposit
            
        Returns:
            Updated account balance
            
        Raises:
            InvalidAmountError: If amount is <= 0
        """
        if amount <= Decimal('0.00'):
            logger.error(f"Invalid deposit amount: {amount}")
            raise InvalidAmountError("Deposit amount must be positive")
            
        self.balance += amount
        self._record_transaction('deposit', amount)
        logger.info(f"Deposited {amount} to account {self.account_id}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount: Decimal) -> Decimal:
        """
        Withdraw funds from the account
        
        Args:
            amount: Positive decimal amount to withdraw
            
        Returns:
            Updated account balance
            
        Raises:
            InvalidAmountError: If amount is <= 0
            InsufficientFundsError: If withdrawal amount > balance
        """
        if amount <= Decimal('0.00'):
            logger.error(f"Invalid withdrawal amount: {amount}")
            raise InvalidAmountError("Withdrawal amount must be positive")
            
        if amount > self.balance:
            logger.error(f"Insufficient funds for withdrawal. Balance: {self.balance}, Requested: {amount}")
            raise InsufficientFundsError("Insufficient funds for withdrawal")
            
        self.balance -= amount
        self._record_transaction('withdrawal', amount)
        logger.info(f"Withdrew {amount} from account {self.account_id}. New balance: {self.balance}")
        return self.balance

    def get_balance(self) -> Decimal:
        """Return current account balance"""
        return self.balance

    def _record_transaction(self, transaction_type: str, amount: Decimal):
        """
        Record transaction in history
        
        Args:
            transaction_type: Type of transaction (deposit/withdrawal)
            amount: Transaction amount
        """
        self.transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.balance,
            'timestamp': datetime.datetime.now().isoformat()
        })

    def get_transaction_history(self) -> list:
        """Return complete transaction history"""
        return self.transaction_history


# Example usage
if __name__ == "__main__":
    import datetime
    
    try:
        # Create a new account
        account = BettingAccount("user123", Decimal('100.00'))
        
        # Perform transactions
        account.deposit(Decimal('50.00'))
        account.withdraw(Decimal('25.00'))
        
        # Attempt invalid transactions
        try:
            account.withdraw(Decimal('200.00'))
        except InsufficientFundsError as e:
            logger.warning(f"Transaction failed: {str(e)}")
            
        try:
            account.deposit(Decimal('-10.00'))
        except InvalidAmountError as e:
            logger.warning(f"Transaction failed: {str(e)}")
            
        # Display final state
        print(f"Final balance: {account.get_balance()}")
        print("Transaction history:")
        for tx in account.get_transaction_history():
            print(f"{tx['timestamp']} - {tx['type']}: {tx['amount']} (Balance: {tx['balance_after']})")
            
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
```
