"""
Generated Code Metadata:
========================
Original URL: https://tether.ac
Prompt: Design a Tether AC-X Token-based system for international remittances with reduced transaction costs.
Generated: DETERMINISTIC_59aaafc32875c947
Batch ID: 20250622_211733
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
Tether AC-X Token Remittance System
A blockchain-based solution for international remittances with reduced fees.
"""

from typing import Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import time
from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 6

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REVERSED = "reversed"

@dataclass
class User:
    user_id: str
    name: str
    wallet_address: str
    balance: Decimal
    kyc_verified: bool = False

@dataclass
class Transaction:
    tx_id: str
    sender: str
    recipient: str
    amount: Decimal
    currency: str
    timestamp: float
    status: TransactionStatus
    fee: Decimal
    exchange_rate: Optional[Decimal] = None

class ACXTokenSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.transactions: Dict[str, Transaction] = {}
        self.exchange_rates: Dict[str, Decimal] = {
            'USD': Decimal('1.0'),
            'EUR': Decimal('0.85'),
            'GBP': Decimal('0.73'),
            'JPY': Decimal('110.0')
        }
        self.base_fee_percentage = Decimal('0.001')  # 0.1% fee

    def register_user(self, user_id: str, name: str) -> User:
        """Register a new user with a unique wallet address."""
        if user_id in self.users:
            raise ValueError("User ID already exists")
        
        wallet_address = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:20]
        user = User(
            user_id=user_id,
            name=name,
            wallet_address=wallet_address,
            balance=Decimal('0'),
            kyc_verified=False
        )
        self.users[user_id] = user
        return user

    def verify_kyc(self, user_id: str) -> None:
        """Verify user's KYC status."""
        if user_id not in self.users:
            raise ValueError("User not found")
        self.users[user_id].kyc_verified = True

    def deposit_funds(self, user_id: str, amount: Decimal, currency: str) -> None:
        """Deposit funds into user's wallet."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        exchange_rate = self.exchange_rates.get(currency)
        if not exchange_rate:
            raise ValueError("Unsupported currency")
        
        self.users[user_id].balance += amount / exchange_rate

    def _calculate_fee(self, amount: Decimal) -> Decimal:
        """Calculate transaction fee."""
        return amount * self.base_fee_percentage

    def _generate_tx_id(self, sender: str, recipient: str) -> str:
        """Generate unique transaction ID."""
        return hashlib.sha256(
            f"{sender}{recipient}{time.time()}".encode()
        ).hexdigest()[:16]

    def send_remittance(
        self,
        sender_id: str,
        recipient_id: str,
        amount: Decimal,
        currency: str
    ) -> Transaction:
        """Send a remittance between users."""
        if sender_id not in self.users or recipient_id not in self.users:
            raise ValueError("Sender or recipient not found")
        
        sender = self.users[sender_id]
        recipient = self.users[recipient_id]
        
        if not sender.kyc_verified or not recipient.kyc_verified:
            raise ValueError("KYC verification required for both parties")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        exchange_rate = self.exchange_rates.get(currency)
        if not exchange_rate:
            raise ValueError("Unsupported currency")
        
        amount_in_acx = amount / exchange_rate
        fee = self._calculate_fee(amount_in_acx)
        total_debit = amount_in_acx + fee
        
        if sender.balance < total_debit:
            raise ValueError("Insufficient funds")
        
        tx_id = self._generate_tx_id(sender_id, recipient_id)
        tx = Transaction(
            tx_id=tx_id,
            sender=sender_id,
            recipient=recipient_id,
            amount=amount_in_acx,
            currency=currency,
            timestamp=time.time(),
            status=TransactionStatus.PENDING,
            fee=fee,
            exchange_rate=exchange_rate
        )
        
        try:
            # Atomic operation - deduct from sender and add to recipient
            sender.balance -= total_debit
            recipient.balance += amount_in_acx
            tx.status = TransactionStatus.COMPLETED
        except Exception as e:
            tx.status = TransactionStatus.FAILED
            raise RuntimeError(f"Transaction failed: {str(e)}")
        finally:
            self.transactions[tx_id] = tx
        
        return tx

    def get_transaction_status(self, tx_id: str) -> TransactionStatus:
        """Get status of a transaction."""
        if tx_id not in self.transactions:
            raise ValueError("Transaction not found")
        return self.transactions[tx_id].status

    def get_user_balance(self, user_id: str, currency: str = "USD") -> Decimal:
        """Get user balance in specified currency."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        exchange_rate = self.exchange_rates.get(currency)
        if not exchange_rate:
            raise ValueError("Unsupported currency")
        
        return self.users[user_id].balance * exchange_rate

    def set_exchange_rate(self, currency: str, rate: Decimal) -> None:
        """Update exchange rate for a currency."""
        if currency not in self.exchange_rates:
            raise ValueError("Unsupported currency")
        if rate <= 0:
            raise ValueError("Rate must be positive")
        self.exchange_rates[currency] = rate

    def export_transaction_history(self, user_id: str) -> str:
        """Export user's transaction history as JSON."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user_txs = [
            tx for tx in self.transactions.values() 
            if tx.sender == user_id or tx.recipient == user_id
        ]
        
        tx_list = []
        for tx in user_txs:
            tx_dict = {
                "tx_id": tx.tx_id,
                "sender": tx.sender,
                "recipient": tx.recipient,
                "amount": str(tx.amount),
                "currency": tx.currency,
                "timestamp": tx.timestamp,
                "status": tx.status.value,
                "fee": str(tx.fee),
                "exchange_rate": str(tx.exchange_rate) if tx.exchange_rate else None
            }
            tx_list.append(tx_dict)
        
        return json.dumps(tx_list, indent=2)

    def reverse_transaction(self, tx_id: str) -> Transaction:
        """Reverse a completed transaction."""
        if tx_id not in self.transactions:
            raise ValueError("Transaction not found")
        
        tx = self.transactions[tx_id]
        
        if tx.status != TransactionStatus.COMPLETED:
            raise ValueError("Only completed transactions can be reversed")
        
        sender = self.users[tx.sender]
        recipient = self.users[tx.recipient]
        
        try:
            # Atomic operation - deduct from recipient and add back to sender
            recipient.balance -= tx.amount
            sender.balance += tx.amount + tx.fee
            tx.status = TransactionStatus.REVERSED
        except Exception as e:
            raise RuntimeError(f"Transaction reversal failed: {str(e)}")
        
        return tx
```
