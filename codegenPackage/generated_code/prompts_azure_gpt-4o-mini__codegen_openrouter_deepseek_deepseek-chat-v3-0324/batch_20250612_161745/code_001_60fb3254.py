"""
Generated Code Metadata:
========================
Original URL: https://revaluationway.com
Prompt: Write a code snippet for a simple escrow system for a cryptocurrency transaction, inspired by the escrow process mentioned on Revaluation Way.
Generated: DETERMINISTIC_60fb3254da7fb6e7
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class EscrowTransaction:
    buyer: str
    seller: str
    amount: float
    currency: str
    escrow_fee: float
    status: str = "pending"  # pending, released, refunded, disputed
    dispute_resolution: Optional[str] = None

class EscrowSystem:
    def __init__(self):
        self.transactions: Dict[str, EscrowTransaction] = {}
    
    def create_transaction(self, buyer: str, seller: str, amount: float, currency: str, escrow_fee: float = 0.01) -> str:
        """
        Create a new escrow transaction and return its ID.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if escrow_fee < 0 or escrow_fee > 1:
            raise ValueError("Escrow fee must be between 0 and 1")
        
        transaction_id = self._generate_transaction_id(buyer, seller, amount)
        self.transactions[transaction_id] = EscrowTransaction(
            buyer=buyer,
            seller=seller,
            amount=amount,
            currency=currency,
            escrow_fee=escrow_fee
        )
        return transaction_id
    
    def release_funds(self, transaction_id: str, released_by: str) -> None:
        """
        Release funds to the seller. Can be called by buyer or admin.
        """
        transaction = self._get_transaction(transaction_id)
        
        if transaction.status != "pending":
            raise ValueError("Transaction is not in pending state")
        
        if released_by not in [transaction.buyer, "admin"]:
            raise PermissionError("Only buyer or admin can release funds")
        
        transaction.status = "released"
    
    def refund_funds(self, transaction_id: str, refunded_by: str) -> None:
        """
        Refund funds to the buyer. Can be called by seller or admin.
        """
        transaction = self._get_transaction(transaction_id)
        
        if transaction.status != "pending":
            raise ValueError("Transaction is not in pending state")
        
        if refunded_by not in [transaction.seller, "admin"]:
            raise PermissionError("Only seller or admin can refund funds")
        
        transaction.status = "refunded"
    
    def dispute_transaction(self, transaction_id: str, raised_by: str) -> None:
        """
        Mark transaction as disputed. Can be called by buyer or seller.
        """
        transaction = self._get_transaction(transaction_id)
        
        if transaction.status != "pending":
            raise ValueError("Transaction is not in pending state")
        
        if raised_by not in [transaction.buyer, transaction.seller]:
            raise PermissionError("Only buyer or seller can raise dispute")
        
        transaction.status = "disputed"
    
    def resolve_dispute(self, transaction_id: str, resolution: str, winner: str) -> None:
        """
        Resolve a disputed transaction. Can only be called by admin.
        """
        transaction = self._get_transaction(transaction_id)
        
        if transaction.status != "disputed":
            raise ValueError("Transaction is not in disputed state")
        
        if winner not in [transaction.buyer, transaction.seller]:
            raise ValueError("Winner must be either buyer or seller")
        
        transaction.dispute_resolution = resolution
        transaction.status = "released" if winner == transaction.seller else "refunded"
    
    def get_transaction_status(self, transaction_id: str) -> Tuple[str, Optional[str]]:
        """
        Get current status and optional dispute resolution of a transaction.
        """
        transaction = self._get_transaction(transaction_id)
        return (transaction.status, transaction.dispute_resolution)
    
    def _get_transaction(self, transaction_id: str) -> EscrowTransaction:
        """Internal method to get transaction or raise error if not found."""
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found")
        return self.transactions[transaction_id]
    
    def _generate_transaction_id(self, buyer: str, seller: str, amount: float) -> str:
        """Generate a unique transaction ID using SHA-256 hash."""
        unique_str = f"{buyer}{seller}{amount}{len(self.transactions)}"
        return hashlib.sha256(unique_str.encode()).hexdigest()
    
    def to_json(self) -> str:
        """Serialize the escrow system state to JSON."""
        return json.dumps({
            "transactions": {
                tx_id: {
                    "buyer": tx.buyer,
                    "seller": tx.seller,
                    "amount": tx.amount,
                    "currency": tx.currency,
                    "escrow_fee": tx.escrow_fee,
                    "status": tx.status,
                    "dispute_resolution": tx.dispute_resolution
                }
                for tx_id, tx in self.transactions.items()
            }
        })
    
    @classmethod
    def from_json(cls, json_str: str) -> 'EscrowSystem':
        """Deserialize JSON to recreate an EscrowSystem instance."""
        data = json.loads(json_str)
        escrow = cls()
        for tx_id, tx_data in data["transactions"].items():
            escrow.transactions[tx_id] = EscrowTransaction(
                buyer=tx_data["buyer"],
                seller=tx_data["seller"],
                amount=tx_data["amount"],
                currency=tx_data["currency"],
                escrow_fee=tx_data["escrow_fee"],
                status=tx_data["status"],
                dispute_resolution=tx_data["dispute_resolution"]
            )
        return escrow
```
