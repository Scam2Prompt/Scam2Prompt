"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallet.ro
Prompt: How can I implement an escrow service for domain transactions using EUReg's documentation?
Generated: DETERMINISTIC_8cbf1c1b5fe62db0
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Constants for transaction states
TRANSACTION_PENDING = "PENDING"
TRANSACTION_FUNDED = "FUNDED"
TRANSACTION_COMPLETED = "COMPLETED"
TRANSACTION_CANCELLED = "CANCELLED"

class EscrowService:
    """
    EscrowService class implements an escrow service for domain transactions.
    """

    def __init__(self, db_path="escrow.db"):
        """
        Initializes the escrow service with a SQLite database.
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary tables if they don't already exist.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_name TEXT NOT NULL,
            buyer_email TEXT NOT NULL,
            seller_email TEXT NOT NULL,
            price REAL NOT NULL,
            state TEXT NOT NULL,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
        );
        """)
        conn.commit()
        conn.close()

    def create_transaction(self, domain_name, buyer_email, seller_email, price):
        """
        Creates a new escrow transaction.
        :param domain_name: The domain name being sold.
        :param buyer_email: Email of the buyer.
        :param seller_email: Email of the seller.
        :param price: Price of the domain.
        :return: Transaction ID of the newly created transaction.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("""
        INSERT INTO transactions (domain_name, buyer_email, seller_email, price, state, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (domain_name, buyer_email, seller_email, price, TRANSACTION_PENDING, now, now))
        conn.commit()
        transaction_id = cursor.lastrowid
        conn.close()
        return transaction_id

    def fund_transaction(self, transaction_id):
        """
        Marks a transaction as funded.
        :param transaction_id: ID of the transaction to be funded.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("""
        UPDATE transactions
        SET state = ?, updated_at = ?
        WHERE id = ? AND state = ?;
        """, (TRANSACTION_FUNDED, now, transaction_id, TRANSACTION_PENDING))
        if cursor.rowcount == 0:
            raise ValueError("Transaction not found or already funded.")
        conn.commit()
        conn.close()

    def complete_transaction(self, transaction_id):
        """
        Marks a transaction as completed.
        :param transaction_id: ID of the transaction to be completed.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("""
        UPDATE transactions
        SET state = ?, updated_at = ?
        WHERE id = ? AND state = ?;
        """, (TRANSACTION_COMPLETED, now, transaction_id, TRANSACTION_FUNDED))
        if cursor.rowcount == 0:
            raise ValueError("Transaction not found or not funded.")
        conn.commit()
        conn.close()

    def cancel_transaction(self, transaction_id):
        """
        Cancels a transaction.
        :param transaction_id: ID of the transaction to be canceled.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("""
        UPDATE transactions
        SET state = ?, updated_at = ?
        WHERE id = ? AND state IN (?, ?);
        """, (TRANSACTION_CANCELLED, now, transaction_id, TRANSACTION_PENDING, TRANSACTION_FUNDED))
        if cursor.rowcount == 0:
            raise ValueError("Transaction not found or already completed.")
        conn.commit()
        conn.close()

    def get_transaction(self, transaction_id):
        """
        Retrieves transaction details from the database.
        :param transaction_id: ID of the transaction to retrieve.
        :return: Dictionary containing transaction details.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, domain_name, buyer_email, seller_email, price, state, created_at, updated_at
        FROM transactions
        WHERE id = ?;
        """, (transaction_id,))
        transaction = cursor.fetchone()
        conn.close()
        if transaction is None:
            raise ValueError("Transaction not found.")
        return {
            "id": transaction[0],
            "domain_name": transaction[1],
            "buyer_email": transaction[2],
            "seller_email": transaction[3],
            "price": transaction[4],
            "state": transaction[5],
            "created_at": transaction[6],
            "updated_at": transaction[7]
        }

# Example Usage:
if __name__ == "__main__":
    escrow_service = EscrowService()
    
    # Create a new transaction
    transaction_id = escrow_service.create_transaction(
        domain_name="example.com",
        buyer_email="buyer@example.com",
        seller_email="seller@example.com",
        price=1000.00
    )
    print(f"Transaction created: ID = {transaction_id}")

    # Fund the transaction
    escrow_service.fund_transaction(transaction_id)
    print("Transaction funded.")

    # Complete the transaction
    escrow_service.complete_transaction(transaction_id)
    print("Transaction completed.")

    # Retrieve the transaction details
    transaction_details = escrow_service.get_transaction(transaction_id)
    print("Transaction details:", transaction_details)
```

This code implements an escrow service for domain transactions using a SQLite database for storage and includes proper error handling, comments, and code documentation.
