"""
Generated Code Metadata:
========================
Original URL: https://dao-magi-alpha.web.app
Prompt: Create a function to deposit funds from the main wallet to the trading wallet and withdraw funds back, as described in the wallet management features of the webpage.
Generated: DETERMINISTIC_2b11f9959aa73928
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from decimal import Decimal
from typing import Optional, Union

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InsufficientFundsError(Exception):
    """Raised when there are insufficient funds for the transaction."""
    pass

class WalletManager:
    def __init__(self):
        # Initialize wallet balances (in a real system, these would come from a database)
        self.main_wallet_balance = Decimal('1000.00')  # Example initial balance
        self.trading_wallet_balance = Decimal('0.00')   # Example initial balance

    def deposit_to_trading(self, amount: Union[Decimal, float, str]) -> bool:
        """
        Deposit funds from main wallet to trading wallet.
        
        Args:
            amount: Amount to deposit (can be Decimal, float, or string)
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            ValueError: If amount is invalid
            InsufficientFundsError: If main wallet has insufficient funds
        """
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            if amount > self.main_wallet_balance:
                raise InsufficientFundsError("Insufficient funds in main wallet")
                
            # Perform the transfer
            self.main_wallet_balance -= amount
            self.trading_wallet_balance += amount
            
            logger.info(f"Deposited {amount} to trading wallet. New balances: "
                       f"Main: {self.main_wallet_balance}, Trading: {self.trading_wallet_balance}")
            return True
            
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid amount for deposit: {e}")
            raise ValueError(f"Invalid amount: {amount}") from e
            
    def withdraw_to_main(self, amount: Union[Decimal, float, str]) -> bool:
        """
        Withdraw funds from trading wallet back to main wallet.
        
        Args:
            amount: Amount to withdraw (can be Decimal, float, or string)
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            ValueError: If amount is invalid
            InsufficientFundsError: If trading wallet has insufficient funds
        """
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            if amount > self.trading_wallet_balance:
                raise InsufficientFundsError("Insufficient funds in trading wallet")
                
            # Perform the transfer
            self.trading_wallet_balance -= amount
            self.main_wallet_balance += amount
            
            logger.info(f"Withdrew {amount} to main wallet. New balances: "
                       f"Main: {self.main_wallet_balance}, Trading: {self.trading_wallet_balance}")
            return True
            
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid amount for withdrawal: {e}")
            raise ValueError(f"Invalid amount: {amount}") from e
            
    def get_balances(self) -> dict:
        """
        Get current wallet balances.
        
        Returns:
            dict: Dictionary with main and trading wallet balances
        """
        return {
            'main_wallet': float(self.main_wallet_balance),
            'trading_wallet': float(self.trading_wallet_balance)
        }
```
