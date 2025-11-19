"""
Generated Code Metadata:
========================
Original URL: https://rateaml.com
Prompt: Provide an example of how to use AMLBot to track and filter cryptocurrency transactions, including adding manual operations and tagging transactions for better organization.
Generated: DETERMINISTIC_5aee820d411bbd74
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Transaction:
    """Represents a cryptocurrency transaction."""
    
    def __init__(
        self,
        tx_id: str,
        timestamp: datetime,
        amount: float,
        currency: str,
        sender: str,
        receiver: str,
        tags: Optional[List[str]] = None,
        notes: Optional[str] = None
    ):
        self.tx_id = tx_id
        self.timestamp = timestamp
        self.amount = amount
        self.currency = currency
        self.sender = sender
        self.receiver = receiver
        self.tags = tags if tags else []
        self.notes = notes

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization."""
        return {
            "tx_id": self.tx_id,
            "timestamp": self.timestamp.isoformat(),
            "amount": self.amount,
            "currency": self.currency,
            "sender": self.sender,
            "receiver": self.receiver,
            "tags": self.tags,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create transaction from dictionary."""
        return cls(
            tx_id=data["tx_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            amount=data["amount"],
            currency=data["currency"],
            sender=data["sender"],
            receiver=data["receiver"],
            tags=data.get("tags", []),
            notes=data.get("notes")
        )

class AMLBot:
    """Tool for tracking and analyzing cryptocurrency transactions."""
    
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.tag_index: Dict[str, List[Transaction]] = {}

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the tracker."""
        self.transactions.append(transaction)
        self._index_transaction(transaction)

    def add_manual_transaction(
        self,
        amount: float,
        currency: str,
        sender: str,
        receiver: str,
        tags: Optional[List[str]] = None,
        notes: Optional[str] = None
    ) -> Transaction:
        """Create and add a manual transaction."""
        tx_id = f"manual_{datetime.now().timestamp()}"
        transaction = Transaction(
            tx_id=tx_id,
            timestamp=datetime.now(),
            amount=amount,
            currency=currency,
            sender=sender,
            receiver=receiver,
            tags=tags,
            notes=notes
        )
        self.add_transaction(transaction)
        return transaction

    def _index_transaction(self, transaction: Transaction) -> None:
        """Index transaction by its tags for faster lookup."""
        for tag in transaction.tags:
            if tag not in self.tag_index:
                self.tag_index[tag] = []
            self.tag_index[tag].append(transaction)

    def get_transactions_by_tag(self, tag: str) -> List[Transaction]:
        """Get all transactions with a specific tag."""
        return self.tag_index.get(tag, [])

    def filter_transactions(
        self,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        currency: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        tags: Optional[List[str]] = None
    ) -> List[Transaction]:
        """Filter transactions based on various criteria."""
        filtered = []
        
        for tx in self.transactions:
            # Amount filter
            if min_amount is not None and tx.amount < min_amount:
                continue
            if max_amount is not None and tx.amount > max_amount:
                continue
                
            # Currency filter
            if currency is not None and tx.currency.lower() != currency.lower():
                continue
                
            # Date filter
            if start_date is not None and tx.timestamp < start_date:
                continue
            if end_date is not None and tx.timestamp > end_date:
                continue
                
            # Tags filter
            if tags is not None and not any(tag in tx.tags for tag in tags):
                continue
                
            filtered.append(tx)
            
        return filtered

    def add_tag_to_transaction(self, tx_id: str, tag: str) -> bool:
        """Add a tag to an existing transaction."""
        for tx in self.transactions:
            if tx.tx_id == tx_id:
                if tag not in tx.tags:
                    tx.tags.append(tag)
                    self._index_transaction(tx)
                return True
        return False

    def save_to_file(self, filename: str) -> None:
        """Save transactions to a JSON file."""
        data = [tx.to_dict() for tx in self.transactions]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load transactions from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.transactions = [Transaction.from_dict(tx) for tx in data]
        self.tag_index = {}
        for tx in self.transactions:
            self._index_transaction(tx)

# Example usage
if __name__ == "__main__":
    # Initialize AMLBot
    bot = AMLBot()
    
    # Add some manual transactions
    bot.add_manual_transaction(
        amount=1.5,
        currency="BTC",
        sender="Alice",
        receiver="Bob",
        tags=["exchange", "withdrawal"],
        notes="Initial transfer"
    )
    
    bot.add_manual_transaction(
        amount=0.75,
        currency="ETH",
        sender="Charlie",
        receiver="Alice",
        tags=["deposit", "gift"]
    )
    
    # Add tag to existing transaction
    tx_id = bot.transactions[0].tx_id
    bot.add_tag_to_transaction(tx_id, "verified")
    
    # Filter transactions
    btc_transactions = bot.filter_transactions(currency="BTC")
    large_transactions = bot.filter_transactions(min_amount=1.0)
    tagged_transactions = bot.filter_transactions(tags=["gift"])
    
    # Save and load data
    bot.save_to_file("transactions.json")
    bot.load_from_file("transactions.json")
    
    # Print some results
    print(f"Total transactions: {len(bot.transactions)}")
    print(f"BTC transactions: {len(btc_transactions)}")
    print(f"Large transactions: {len(large_transactions)}")
    print(f"Gift transactions: {len(tagged_transactions)}")
```
