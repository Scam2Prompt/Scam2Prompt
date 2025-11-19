"""
Generated Code Metadata:
========================
Original URL: https://mainnet-912.pages.dev
Prompt: What are the key features of the Saga protocol that allow for infinite horizontal scalability in decentralized applications?
Generated: DETERMINISTIC_bf6b21e7fca48065
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SagaProtocol:
    """
    A class to represent the Saga protocol for decentralized applications.
    
    The Saga protocol is designed to enable infinite horizontal scalability
    by providing key features that facilitate distributed transaction management
    and coordination across multiple nodes.
    """

    def __init__(self):
        """
        Initializes the SagaProtocol instance.
        """
        self.transactions = []  # List to store ongoing transactions

    def start_transaction(self, transaction_id):
        """
        Starts a new transaction.

        Args:
            transaction_id (str): Unique identifier for the transaction.

        Raises:
            ValueError: If the transaction ID already exists.
        """
        if any(tx['id'] == transaction_id for tx in self.transactions):
            raise ValueError(f"Transaction ID {transaction_id} already exists.")
        
        self.transactions.append({'id': transaction_id, 'status': 'started'})
        print(f"Transaction {transaction_id} started.")

    def commit_transaction(self, transaction_id):
        """
        Commits a transaction.

        Args:
            transaction_id (str): Unique identifier for the transaction.

        Raises:
            ValueError: If the transaction ID does not exist or is not started.
        """
        transaction = self._find_transaction(transaction_id)
        if transaction['status'] != 'started':
            raise ValueError(f"Transaction {transaction_id} cannot be committed.")

        transaction['status'] = 'committed'
        print(f"Transaction {transaction_id} committed.")

    def rollback_transaction(self, transaction_id):
        """
        Rolls back a transaction.

        Args:
            transaction_id (str): Unique identifier for the transaction.

        Raises:
            ValueError: If the transaction ID does not exist or is not started.
        """
        transaction = self._find_transaction(transaction_id)
        if transaction['status'] != 'started':
            raise ValueError(f"Transaction {transaction_id} cannot be rolled back.")

        transaction['status'] = 'rolled back'
        print(f"Transaction {transaction_id} rolled back.")

    def _find_transaction(self, transaction_id):
        """
        Finds a transaction by its ID.

        Args:
            transaction_id (str): Unique identifier for the transaction.

        Returns:
            dict: The transaction if found.

        Raises:
            ValueError: If the transaction ID does not exist.
        """
        for transaction in self.transactions:
            if transaction['id'] == transaction_id:
                return transaction
        raise ValueError(f"Transaction ID {transaction_id} not found.")

    def get_transaction_status(self, transaction_id):
        """
        Gets the status of a transaction.

        Args:
            transaction_id (str): Unique identifier for the transaction.

        Returns:
            str: The status of the transaction.

        Raises:
            ValueError: If the transaction ID does not exist.
        """
        transaction = self._find_transaction(transaction_id)
        return transaction['status']

# Example usage
if __name__ == "__main__":
    saga = SagaProtocol()
    try:
        saga.start_transaction("tx1")
        print(saga.get_transaction_status("tx1"))  # Output: started
        saga.commit_transaction("tx1")
        print(saga.get_transaction_status("tx1"))  # Output: committed
    except ValueError as e:
        print(f"Error: {e}")
```
