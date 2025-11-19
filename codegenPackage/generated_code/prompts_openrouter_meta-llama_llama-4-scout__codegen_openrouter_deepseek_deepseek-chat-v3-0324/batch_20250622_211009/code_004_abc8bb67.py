"""
Generated Code Metadata:
========================
Original URL: https://dfkassa.pages.dev
Prompt: "Create a code example for a simple digital transaction system that could be part of a DFKassa-like application."
Generated: DETERMINISTIC_abc8bb6785a7210a
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import Optional, List, Dict
from enum import Enum

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    PAYMENT = "payment"

class Transaction:
    def __init__(
        self,
        transaction_id: str,
        amount: float,
        transaction_type: TransactionType,
        sender_id: str,
        recipient_id: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.description = description
        self.status = TransactionStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status: TransactionStatus) -> None:
        """Update the transaction status and set the updated timestamp."""
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization."""
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type.value,
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class DigitalWallet:
    def __init__(self, wallet_id: str, owner_id: str, balance: float = 0.0):
        self.wallet_id = wallet_id
        self.owner_id = owner_id
        self.balance = balance
        self.transactions: List[Transaction] = []

    def add_funds(self, amount: float, description: Optional[str] = None) -> Transaction:
        """Add funds to the wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            amount=amount,
            transaction_type=TransactionType.DEPOSIT,
            sender_id="system",
            recipient_id=self.owner_id,
            description=description
        )

        self.balance += amount
        transaction.update_status(TransactionStatus.COMPLETED)
        self.transactions.append(transaction)
        return transaction

    def withdraw_funds(self, amount: float, description: Optional[str] = None) -> Transaction:
        """Withdraw funds from the wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            amount=amount,
            transaction_type=TransactionType.WITHDRAWAL,
            sender_id=self.owner_id,
            description=description
        )

        self.balance -= amount
        transaction.update_status(TransactionStatus.COMPLETED)
        self.transactions.append(transaction)
        return transaction

    def transfer_funds(
        self,
        amount: float,
        recipient_wallet: 'DigitalWallet',
        description: Optional[str] = None
    ) -> Transaction:
        """Transfer funds to another wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        if self.owner_id == recipient_wallet.owner_id:
            raise ValueError("Cannot transfer to self")

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            amount=amount,
            transaction_type=TransactionType.TRANSFER,
            sender_id=self.owner_id,
            recipient_id=recipient_wallet.owner_id,
            description=description
        )

        try:
            self.balance -= amount
            recipient_wallet.balance += amount
            transaction.update_status(TransactionStatus.COMPLETED)
        except Exception as e:
            transaction.update_status(TransactionStatus.FAILED)
            raise e
        finally:
            self.transactions.append(transaction)
            recipient_wallet.transactions.append(transaction)

        return transaction

    def get_transaction_history(self) -> List[Dict]:
        """Get all transactions for this wallet."""
        return [t.to_dict() for t in self.transactions]

    def get_balance(self) -> float:
        """Get current wallet balance."""
        return self.balance

class DigitalTransactionSystem:
    def __init__(self):
        self.wallets: Dict[str, DigitalWallet] = {}

    def create_wallet(self, owner_id: str, initial_balance: float = 0.0) -> DigitalWallet:
        """Create a new digital wallet for a user."""
        if owner_id in self.wallets:
            raise ValueError("Wallet already exists for this user")

        wallet_id = str(uuid.uuid4())
        wallet = DigitalWallet(wallet_id, owner_id, initial_balance)
        self.wallets[owner_id] = wallet
        return wallet

    def get_wallet(self, owner_id: str) -> DigitalWallet:
        """Get a wallet by owner ID."""
        if owner_id not in self.wallets:
            raise ValueError("Wallet not found")
        return self.wallets[owner_id]

    def process_payment(
        self,
        sender_id: str,
        recipient_id: str,
        amount: float,
        description: Optional[str] = None
    ) -> Transaction:
        """Process a payment between two wallets."""
        sender_wallet = self.get_wallet(sender_id)
        recipient_wallet = self.get_wallet(recipient_id)

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            amount=amount,
            transaction_type=TransactionType.PAYMENT,
            sender_id=sender_id,
            recipient_id=recipient_id,
            description=description
        )

        try:
            if sender_wallet.balance < amount:
                raise ValueError("Insufficient funds")

            sender_wallet.balance -= amount
            recipient_wallet.balance += amount
            transaction.update_status(TransactionStatus.COMPLETED)
        except Exception as e:
            transaction.update_status(TransactionStatus.FAILED)
            raise e
        finally:
            sender_wallet.transactions.append(transaction)
            recipient_wallet.transactions.append(transaction)

        return transaction

# Example usage
if __name__ == "__main__":
    system = DigitalTransactionSystem()
    
    # Create wallets
    wallet1 = system.create_wallet("user1", 1000.0)
    wallet2 = system.create_wallet("user2", 500.0)
    
    # Perform transactions
    try:
        # Deposit funds
        deposit = wallet1.add_funds(200.0, "Salary payment")
        print(f"Deposit completed: {deposit.to_dict()}")
        
        # Transfer funds
        transfer = wallet1.transfer_funds(300.0, wallet2, "Gift")
        print(f"Transfer completed: {transfer.to_dict()}")
        
        # Payment
        payment = system.process_payment("user2", "user1", 100.0, "Dinner")
        print(f"Payment completed: {payment.to_dict()}")
        
        # Check balances
        print(f"User1 balance: {wallet1.get_balance()}")
        print(f"User2 balance: {wallet2.get_balance()}")
        
        # Transaction history
        print("\nUser1 transaction history:")
        for tx in wallet1.get_transaction_history():
            print(tx)
            
    except Exception as e:
        print(f"Transaction failed: {str(e)}")
```
