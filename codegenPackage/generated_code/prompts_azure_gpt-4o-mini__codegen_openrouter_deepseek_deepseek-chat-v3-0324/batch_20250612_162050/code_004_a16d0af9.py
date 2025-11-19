"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Create a function that handles accounts payable and receivable management, inspired by the services listed on CGBókhald's website.
Generated: DETERMINISTIC_a16d0af9cd800bdd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum

class TransactionType(Enum):
    """Enum representing different transaction types."""
    PAYABLE = "PAYABLE"
    RECEIVABLE = "RECEIVABLE"

class TransactionStatus(Enum):
    """Enum representing different transaction statuses."""
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"
    CANCELLED = "CANCELLED"

class Transaction:
    """Class representing a financial transaction."""
    
    def __init__(
        self,
        transaction_id: str,
        transaction_type: TransactionType,
        amount: float,
        due_date: datetime.date,
        description: str,
        counterparty: str,
        status: TransactionStatus = TransactionStatus.PENDING
    ):
        """
        Initialize a transaction.
        
        Args:
            transaction_id: Unique identifier for the transaction
            transaction_type: PAYABLE or RECEIVABLE
            amount: Transaction amount
            due_date: Due date for payment
            description: Description of the transaction
            counterparty: The other party in the transaction
            status: Current status of the transaction
        """
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.due_date = due_date
        self.description = description
        self.counterparty = counterparty
        self.status = status
        self.created_at = datetime.date.today()
        self.updated_at = datetime.date.today()

    def update_status(self, new_status: TransactionStatus) -> None:
        """Update the status of the transaction."""
        self.status = new_status
        self.updated_at = datetime.date.today()

    def is_overdue(self) -> bool:
        """Check if the transaction is overdue."""
        return (
            self.status == TransactionStatus.PENDING
            and datetime.date.today() > self.due_date
        )

class AccountingSystem:
    """Class to manage accounts payable and receivable."""
    
    def __init__(self):
        """Initialize the accounting system with empty transaction lists."""
        self.transactions: Dict[str, Transaction] = {}
    
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a new transaction to the system.
        
        Args:
            transaction: Transaction object to add
            
        Raises:
            ValueError: If transaction ID already exists
        """
        if transaction.transaction_id in self.transactions:
            raise ValueError(f"Transaction ID {transaction.transaction_id} already exists")
        self.transactions[transaction.transaction_id] = transaction
    
    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        """Retrieve a transaction by ID.
        
        Args:
            transaction_id: ID of the transaction to retrieve
            
        Returns:
            Transaction object if found, None otherwise
        """
        return self.transactions.get(transaction_id)
    
    def update_transaction_status(
        self,
        transaction_id: str,
        new_status: TransactionStatus
    ) -> None:
        """Update the status of a transaction.
        
        Args:
            transaction_id: ID of the transaction to update
            new_status: New status to set
            
        Raises:
            ValueError: If transaction ID doesn't exist
        """
        if transaction_id not in self.transactions:
            raise ValueError(f"Transaction ID {transaction_id} not found")
        self.transactions[transaction_id].update_status(new_status)
    
    def get_overdue_transactions(self) -> List[Transaction]:
        """Get all overdue transactions.
        
        Returns:
            List of overdue transactions
        """
        return [
            t for t in self.transactions.values()
            if t.is_overdue()
        ]
    
    def get_transactions_by_type(
        self,
        transaction_type: TransactionType
    ) -> List[Transaction]:
        """Get all transactions of a specific type.
        
        Args:
            transaction_type: Type of transactions to retrieve
            
        Returns:
            List of transactions of the specified type
        """
        return [
            t for t in self.transactions.values()
            if t.transaction_type == transaction_type
        ]
    
    def get_transactions_by_status(
        self,
        status: TransactionStatus
    ) -> List[Transaction]:
        """Get all transactions with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of transactions with the specified status
        """
        return [
            t for t in self.transactions.values()
            if t.status == status
        ]
    
    def get_total_balance(self) -> Dict[TransactionType, float]:
        """Calculate the total balance for payable and receivable.
        
        Returns:
            Dictionary with total amounts for each transaction type
        """
        balances = {
            TransactionType.PAYABLE: 0.0,
            TransactionType.RECEIVABLE: 0.0
        }
        
        for transaction in self.transactions.values():
            if transaction.status != TransactionStatus.CANCELLED:
                balances[transaction.transaction_type] += transaction.amount
        
        return balances

# Example usage
if __name__ == "__main__":
    system = AccountingSystem()
    
    # Add some sample transactions
    try:
        system.add_transaction(Transaction(
            transaction_id="INV001",
            transaction_type=TransactionType.RECEIVABLE,
            amount=1500.00,
            due_date=datetime.date(2023, 12, 15),
            description="Web design services",
            counterparty="ABC Corp"
        ))
        
        system.add_transaction(Transaction(
            transaction_id="BILL001",
            transaction_type=TransactionType.PAYABLE,
            amount=500.00,
            due_date=datetime.date(2023, 11, 30),
            description="Office supplies",
            counterparty="XYZ Supplies"
        ))
        
        # Update a transaction status
        system.update_transaction_status("INV001", TransactionStatus.PAID)
        
        # Get balances
        balances = system.get_total_balance()
        print(f"Payable balance: {balances[TransactionType.PAYABLE]}")
        print(f"Receivable balance: {balances[TransactionType.RECEIVABLE]}")
        
        # Get overdue transactions
        overdue = system.get_overdue_transactions()
        print(f"Overdue transactions: {len(overdue)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
