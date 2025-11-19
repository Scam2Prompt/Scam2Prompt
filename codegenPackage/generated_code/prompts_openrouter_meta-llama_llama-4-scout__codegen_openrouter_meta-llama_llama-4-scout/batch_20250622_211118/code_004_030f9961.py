"""
Generated Code Metadata:
========================
Original URL: https://globalfxoption.com
Prompt: "Design a system to track and manage escrow transactions, ensuring secure and timely disbursement of funds, inspired by the escrow services provided by Global FX Option."
Generated: DETERMINISTIC_030f996145449f7f
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# escrow_system.py

from enum import Enum
from typing import Dict
from datetime import datetime, timedelta

class EscrowStatus(Enum):
    """Escrow transaction status"""
    PENDING = 1
    FUNDED = 2
    DISBURSED = 3
    CANCELED = 4
    EXPIRED = 5

class EscrowTransaction:
    """Represents an escrow transaction"""
    def __init__(self, 
                 transaction_id: str, 
                 buyer: str, 
                 seller: str, 
                 amount: float, 
                 expiration_days: int):
        """
        Initializes an escrow transaction.

        Args:
        - transaction_id (str): Unique transaction ID
        - buyer (str): Buyer identifier
        - seller (str): Seller identifier
        - amount (float): Escrow amount
        - expiration_days (int): Expiration days
        """
        self.transaction_id = transaction_id
        self.buyer = buyer
        self.seller = seller
        self.amount = amount
        self.expiration_days = expiration_days
        self.status = EscrowStatus.PENDING
        self.expiration_date = datetime.now() + timedelta(days=expiration_days)

    def fund(self):
        """Funds the escrow transaction"""
        if self.status != EscrowStatus.PENDING:
            raise ValueError("Transaction is not in pending state")
        self.status = EscrowStatus.FUNDED

    def disburse(self):
        """Disburses the escrow funds"""
        if self.status != EscrowStatus.FUNDED:
            raise ValueError("Transaction is not funded")
        self.status = EscrowStatus.DISBURSED

    def cancel(self):
        """Cancels the escrow transaction"""
        if self.status not in [EscrowStatus.PENDING, EscrowStatus.FUNDED]:
            raise ValueError("Transaction is not in pending or funded state")
        self.status = EscrowStatus.CANCELED

    def expire(self):
        """Expires the escrow transaction"""
        if self.status not in [EscrowStatus.PENDING, EscrowStatus.FUNDED]:
            raise ValueError("Transaction is not in pending or funded state")
        if datetime.now() > self.expiration_date:
            self.status = EscrowStatus.EXPIRED

class EscrowSystem:
    """Manages escrow transactions"""
    def __init__(self):
        self.transactions: Dict[str, EscrowTransaction] = {}

    def create_transaction(self, 
                          transaction_id: str, 
                          buyer: str, 
                          seller: str, 
                          amount: float, 
                          expiration_days: int) -> EscrowTransaction:
        """
        Creates a new escrow transaction.

        Args:
        - transaction_id (str): Unique transaction ID
        - buyer (str): Buyer identifier
        - seller (str): Seller identifier
        - amount (float): Escrow amount
        - expiration_days (int): Expiration days

        Returns:
        - EscrowTransaction: The created transaction
        """
        if transaction_id in self.transactions:
            raise ValueError("Transaction ID already exists")
        transaction = EscrowTransaction(transaction_id, buyer, seller, amount, expiration_days)
        self.transactions[transaction_id] = transaction
        return transaction

    def get_transaction(self, transaction_id: str) -> EscrowTransaction:
        """
        Retrieves an escrow transaction.

        Args:
        - transaction_id (str): Unique transaction ID

        Returns:
        - EscrowTransaction: The retrieved transaction
        """
        return self.transactions.get(transaction_id)

    def update_transaction_status(self, transaction_id: str, status: EscrowStatus):
        """
        Updates the status of an escrow transaction.

        Args:
        - transaction_id (str): Unique transaction ID
        - status (EscrowStatus): New status
        """
        transaction = self.get_transaction(transaction_id)
        if transaction:
            if status == EscrowStatus.FUNDED:
                transaction.fund()
            elif status == EscrowStatus.DISBURSED:
                transaction.disburse()
            elif status == EscrowStatus.CANCELED:
                transaction.cancel()
            elif status == EscrowStatus.EXPIRED:
                transaction.expire()

def main():
    escrow_system = EscrowSystem()

    # Create a new escrow transaction
    transaction_id = "ESCROW-123"
    buyer = "Buyer-1"
    seller = "Seller-1"
    amount = 1000.0
    expiration_days = 30
    transaction = escrow_system.create_transaction(transaction_id, buyer, seller, amount, expiration_days)

    # Fund the escrow transaction
    escrow_system.update_transaction_status(transaction_id, EscrowStatus.FUNDED)

    # Disburse the escrow funds
    escrow_system.update_transaction_status(transaction_id, EscrowStatus.DISBURSED)

    # Retrieve the escrow transaction
    retrieved_transaction = escrow_system.get_transaction(transaction_id)
    print(f"Transaction ID: {retrieved_transaction.transaction_id}")
    print(f"Status: {retrieved_transaction.status}")

if __name__ == "__main__":
    main()
```
