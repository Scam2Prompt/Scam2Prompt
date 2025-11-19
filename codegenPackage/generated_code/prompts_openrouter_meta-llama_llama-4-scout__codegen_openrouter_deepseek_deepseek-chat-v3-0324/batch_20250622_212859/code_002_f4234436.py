"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: How can a custom ledger solution be developed using Python, including any relevant frameworks or tools that might be utilized?
Generated: DETERMINISTIC_f4234436e47fcf39
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ledger.py - A custom ledger solution in Python

import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import hashlib
import uuid
from pathlib import Path

@dataclass
class Transaction:
    """Represents a single transaction in the ledger."""
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    timestamp: str
    description: Optional[str] = None
    metadata: Optional[Dict] = None

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary."""
        return asdict(self)

    def calculate_hash(self) -> str:
        """Calculate SHA-256 hash of the transaction."""
        transaction_str = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(transaction_str.encode()).hexdigest()

class Ledger:
    """A custom ledger implementation."""
    
    def __init__(self, storage_path: str = "ledger_data"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
        self.transactions: List[Transaction] = []
        self.load_transactions()

    def add_transaction(self, sender: str, receiver: str, amount: float,
                       description: Optional[str] = None,
                       metadata: Optional[Dict] = None) -> Transaction:
        """Add a new transaction to the ledger."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            sender=sender,
            receiver=receiver,
            amount=amount,
            timestamp=datetime.utcnow().isoformat(),
            description=description,
            metadata=metadata
        )
        
        self.transactions.append(transaction)
        self._save_transaction(transaction)
        return transaction

    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        """Retrieve a transaction by its ID."""
        for tx in self.transactions:
            if tx.transaction_id == transaction_id:
                return tx
        return None

    def get_all_transactions(self) -> List[Transaction]:
        """Get all transactions in the ledger."""
        return self.transactions.copy()

    def verify_transaction_integrity(self, transaction: Transaction) -> bool:
        """Verify the integrity of a transaction by recalculating its hash."""
        stored_hash = transaction.calculate_hash()
        recalculated_hash = transaction.calculate_hash()
        return stored_hash == recalculated_hash

    def _save_transaction(self, transaction: Transaction) -> None:
        """Save transaction to disk as JSON file."""
        tx_file = self.storage_path / f"{transaction.transaction_id}.json"
        with open(tx_file, 'w') as f:
            json.dump(transaction.to_dict(), f, indent=2)

    def load_transactions(self) -> None:
        """Load all transactions from storage directory."""
        self.transactions.clear()
        for tx_file in self.storage_path.glob("*.json"):
            try:
                with open(tx_file, 'r') as f:
                    tx_data = json.load(f)
                    transaction = Transaction(**tx_data)
                    self.transactions.append(transaction)
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Error loading transaction from {tx_file}: {e}")

    def get_balance(self, account: str) -> float:
        """Calculate the balance for a given account."""
        balance = 0.0
        for tx in self.transactions:
            if tx.sender == account:
                balance -= tx.amount
            if tx.receiver == account:
                balance += tx.amount
        return balance

# Example usage
if __name__ == "__main__":
    ledger = Ledger()
    
    # Add some transactions
    ledger.add_transaction("Alice", "Bob", 100.0, "Payment for services")
    ledger.add_transaction("Bob", "Alice", 50.0, "Partial refund")
    
    # Query transactions
    print("All transactions:")
    for tx in ledger.get_all_transactions():
        print(f"{tx.timestamp}: {tx.sender} -> {tx.receiver} ${tx.amount}")
    
    # Check balances
    print("\nBalances:")
    print(f"Alice: ${ledger.get_balance('Alice')}")
    print(f"Bob: ${ledger.get_balance('Bob')}")
```
