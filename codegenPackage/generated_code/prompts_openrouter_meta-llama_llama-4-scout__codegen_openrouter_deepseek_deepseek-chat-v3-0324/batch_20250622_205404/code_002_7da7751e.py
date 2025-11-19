"""
Generated Code Metadata:
========================
Original URL: https://banktoken.pages.dev
Prompt: Generate code for a tokenomics system that includes a holding dividend tax and a mechanism for burning tokens to promote growth.
Generated: DETERMINISTIC_7da7751ef953396f
Batch ID: 20250622_205404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Tokenomics System with Holding Dividend Tax and Token Burning Mechanism
"""

from dataclasses import dataclass
from typing import Dict, List
import math
from datetime import datetime, timedelta

class TokenomicsError(Exception):
    """Base exception for tokenomics system errors"""
    pass

class InsufficientBalanceError(TokenomicsError):
    """Raised when a user has insufficient balance for an operation"""
    pass

class InvalidTaxRateError(TokenomicsError):
    """Raised when tax rate is invalid"""
    pass

@dataclass
class Transaction:
    """Represents a token transaction"""
    sender: str
    receiver: str
    amount: float
    timestamp: datetime
    tax_paid: float = 0.0
    burned_amount: float = 0.0

@dataclass
class Holder:
    """Represents a token holder"""
    address: str
    balance: float
    last_transaction_time: datetime
    dividends_earned: float = 0.0

class TokenomicsSystem:
    """Implements tokenomics with holding dividends and burning mechanism"""
    
    def __init__(
        self,
        initial_supply: float,
        dividend_tax_rate: float,
        burn_rate: float,
        dividend_distribution_interval: timedelta = timedelta(days=1)
    ):
        """
        Initialize the tokenomics system
        
        Args:
            initial_supply: Initial total token supply
            dividend_tax_rate: Percentage tax on transactions for dividends (0-1)
            burn_rate: Percentage of tokens burned in each transaction (0-1)
            dividend_distribution_interval: Time between dividend distributions
        """
        if not 0 <= dividend_tax_rate <= 1:
            raise InvalidTaxRateError("Dividend tax rate must be between 0 and 1")
        if not 0 <= burn_rate <= 1:
            raise InvalidTaxRateError("Burn rate must be between 0 and 1")
        
        self.total_supply = initial_supply
        self.circulating_supply = initial_supply
        self.dividend_tax_rate = dividend_tax_rate
        self.burn_rate = burn_rate
        self.dividend_pool = 0.0
        self.dividend_distribution_interval = dividend_distribution_interval
        self.last_dividend_distribution = datetime.now()
        
        self.holders: Dict[str, Holder] = {}
        self.transaction_history: List[Transaction] = []
    
    def _validate_amount(self, amount: float) -> None:
        """Validate the transaction amount"""
        if amount <= 0:
            raise TokenomicsError("Amount must be positive")
    
    def _validate_holder(self, address: str) -> None:
        """Validate holder exists"""
        if address not in self.holders:
            raise TokenomicsError(f"Holder {address} does not exist")
    
    def create_holder(self, address: str, initial_balance: float) -> None:
        """Create a new token holder"""
        if address in self.holders:
            raise TokenomicsError(f"Holder {address} already exists")
        if initial_balance < 0:
            raise TokenomicsError("Initial balance cannot be negative")
        
        self.holders[address] = Holder(
            address=address,
            balance=initial_balance,
            last_transaction_time=datetime.now()
        )
    
    def transfer(
        self,
        sender: str,
        receiver: str,
        amount: float,
        timestamp: datetime = None
    ) -> Transaction:
        """
        Transfer tokens between holders with tax and burn applied
        
        Args:
            sender: Address of sender
            receiver: Address of receiver
            amount: Amount to transfer before taxes
            timestamp: Optional timestamp for transaction
            
        Returns:
            Transaction record with details
        """
        self._validate_amount(amount)
        self._validate_holder(sender)
        self._validate_holder(receiver)
        
        if timestamp is None:
            timestamp = datetime.now()
        
        sender_holder = self.holders[sender]
        if sender_holder.balance < amount:
            raise InsufficientBalanceError(
                f"Insufficient balance for {sender}. Available: {sender_holder.balance}, Required: {amount}"
            )
        
        # Calculate taxes and amounts
        tax_amount = amount * self.dividend_tax_rate
        burn_amount = amount * self.burn_rate
        net_amount = amount - tax_amount - burn_amount
        
        # Update balances
        sender_holder.balance -= amount
        self.holders[receiver].balance += net_amount
        
        # Update dividend pool and burned tokens
        self.dividend_pool += tax_amount
        self.circulating_supply -= burn_amount
        self.total_supply -= burn_amount
        
        # Update transaction times
        sender_holder.last_transaction_time = timestamp
        self.holders[receiver].last_transaction_time = timestamp
        
        # Record transaction
        transaction = Transaction(
            sender=sender,
            receiver=receiver,
            amount=amount,
            timestamp=timestamp,
            tax_paid=tax_amount,
            burned_amount=burn_amount
        )
        self.transaction_history.append(transaction)
        
        return transaction
    
    def distribute_dividends(self) -> None:
        """Distribute dividends to holders based on their proportional holdings"""
        current_time = datetime.now()
        if current_time - self.last_dividend_distribution < self.dividend_distribution_interval:
            return
        
        if self.dividend_pool <= 0 or self.circulating_supply <= 0:
            self.last_dividend_distribution = current_time
            return
        
        total_distributed = 0.0
        
        for holder in self.holders.values():
            if holder.balance > 0:
                share = holder.balance / self.circulating_supply
                dividend = self.dividend_pool * share
                holder.balance += dividend
                holder.dividends_earned += dividend
                total_distributed += dividend
        
        self.dividend_pool -= total_distributed
        self.last_dividend_distribution = current_time
    
    def get_holder_balance(self, address: str) -> float:
        """Get current balance of a holder"""
        self._validate_holder(address)
        return self.holders[address].balance
    
    def get_circulating_supply(self) -> float:
        """Get current circulating supply"""
        return self.circulating_supply
    
    def get_total_supply(self) -> float:
        """Get current total supply (after burns)"""
        return self.total_supply
    
    def get_transaction_history(self, address: str = None) -> List[Transaction]:
        """
        Get transaction history, optionally filtered by address
        
        Args:
            address: Optional address to filter transactions
            
        Returns:
            List of transactions involving the address (if provided) or all transactions
        """
        if address is None:
            return self.transaction_history.copy()
        
        self._validate_holder(address)
        return [
            t for t in self.transaction_history
            if t.sender == address or t.receiver == address
        ]
```
