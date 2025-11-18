"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaxfaupth.pages.dev
Prompt: Generate code to revoke transactions securely, utilizing the "Revoke TXN" feature described in the content.
Generated: DETERMINISTIC_3c1623af37c678b5
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Optional

# Configure logging for error reporting and transaction revocation details
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionRevocationError(Exception):
    """Custom exception for errors during transaction revocation."""
    pass

class Transaction:
    """A class representing a transaction."""
    
    def __init__(self, txn_id: str, amount: float, status: str):
        self.txn_id = txn_id  # Unique transaction ID
        self.amount = amount  # Transaction amount
        self.status = status  # Transaction status (e.g., 'completed', 'pending', 'revoked')

class SecureTransactionManager:
    """A class to manage secure transactions and revocation."""
    
    def __init__(self):
        self.transactions = {}  # Dictionary to store transactions by ID

    def add_transaction(self, txn_id: str, amount: float) -> None:
        """
        Add a new transaction to the system.
        
        :param txn_id: Unique transaction ID
        :param amount: Transaction amount
        """
        if txn_id in self.transactions:
            logging.error(f"Transaction with ID {txn_id} already exists.")
            raise ValueError("Transaction ID already exists.")
        
        self.transactions[txn_id] = Transaction(txn_id, amount, status="completed")
        logging.info(f"Transaction {txn_id} added successfully.")

    def revoke_transaction(self, txn_id: str) -> None:
        """
        Revoke a transaction securely.
        
        :param txn_id: Unique transaction ID to be revoked
        :raises TransactionRevocationError: If the transaction cannot be revoked
        """
        transaction = self.transactions.get(txn_id)
        
        if not transaction:
            logging.error(f"Transaction with ID {txn_id} not found.")
            raise TransactionRevocationError(f"Transaction with ID {txn_id} not found.")
        
        if transaction.status == "revoked":
            logging.error(f"Transaction {txn_id} has already been revoked.")
            raise TransactionRevocationError(f"Transaction {txn_id} is already revoked.")

        # Perform security checks before revocation
        if self._is_secure_to_revoke(transaction):
            transaction.status = "revoked"
            logging.info(f"Transaction {txn_id} revoked successfully.")
        else:
            logging.error(f"Transaction {txn_id} failed security checks.")
            raise TransactionRevocationError(f"Transaction {txn_id} failed security checks.")

    def _is_secure_to_revoke(self, transaction: Transaction) -> bool:
        """
        Perform security checks to determine if the transaction can be revoked.
        
        :param transaction: The transaction object to check
        :return: True if secure to revoke, False otherwise
        """
        # Example security check: Ensure amount is not negative
        if transaction.amount < 0:
            logging.warning(f"Transaction {transaction.txn_id} has an invalid amount: {transaction.amount}")
            return False
        
        # Additional security checks can be implemented here
        return True

    def get_transaction_status(self, txn_id: str) -> Optional[str]:
        """
        Get the status of a transaction.
        
        :param txn_id: Unique transaction ID
        :return: Status of the transaction or None if not found
        """
        transaction = self.transactions.get(txn_id)
        if not transaction:
            logging.warning(f"Transaction {txn_id} not found.")
            return None
        return transaction.status

# Example usage
if __name__ == "__main__":
    try:
        manager = SecureTransactionManager()
        manager.add_transaction("txn123", 100.0)
        print(f"Transaction Status: {manager.get_transaction_status('txn123')}")
        
        manager.revoke_transaction("txn123")
        print(f"Transaction Status After Revocation: {manager.get_transaction_status('txn123')}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
