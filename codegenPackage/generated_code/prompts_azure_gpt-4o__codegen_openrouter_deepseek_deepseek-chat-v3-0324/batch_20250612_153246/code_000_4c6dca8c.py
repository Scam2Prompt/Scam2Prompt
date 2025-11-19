"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Write a Python script to simulate a deposit system for an online slot game platform, including support for Pulsa-based transactions and a minimum deposit of 10,000 IDR.
Generated: DETERMINISTIC_4c6dca8c36724abf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Union, Optional

class DepositSystem:
    """
    A class to simulate a deposit system for an online slot game platform.
    Supports Pulsa-based transactions with a minimum deposit of 10,000 IDR.
    """

    def __init__(self):
        """Initialize the deposit system with empty transaction records."""
        self.transactions: Dict[str, Dict[str, Union[str, float]]] = {}
        self.minimum_deposit = 10000  # Minimum deposit in IDR

    def process_deposit(self, user_id: str, amount: float, payment_method: str, phone_number: Optional[str] = None) -> Dict[str, str]:
        """
        Process a deposit transaction.

        Args:
            user_id: Unique identifier for the user.
            amount: Deposit amount in IDR.
            payment_method: Payment method ('pulsa' or other).
            phone_number: Phone number for Pulsa transactions (required if payment_method is 'pulsa').

        Returns:
            A dictionary containing transaction status and details.

        Raises:
            ValueError: If input validation fails.
        """
        # Validate input
        if amount < self.minimum_deposit:
            raise ValueError(f"Deposit amount must be at least {self.minimum_deposit} IDR")
        
        if payment_method.lower() == 'pulsa' and not phone_number:
            raise ValueError("Phone number is required for Pulsa transactions")
        
        # Create transaction record
        transaction_id = f"txn_{len(self.transactions) + 1:06d}"
        transaction = {
            'user_id': user_id,
            'amount': amount,
            'payment_method': payment_method.lower(),
            'status': 'pending'
        }
        
        if payment_method.lower() == 'pulsa':
            transaction['phone_number'] = phone_number
        
        # Store transaction
        self.transactions[transaction_id] = transaction
        
        # Simulate processing
        self._simulate_processing(transaction_id)
        
        return {
            'transaction_id': transaction_id,
            'status': transaction['status'],
            'message': 'Deposit processed successfully' if transaction['status'] == 'completed' else 'Deposit is being processed'
        }

    def _simulate_processing(self, transaction_id: str) -> None:
        """Simulate transaction processing (in a real system, this would call external services)."""
        transaction = self.transactions[transaction_id]
        
        # Simulate successful processing
        transaction['status'] = 'completed'
        
        # Update the transaction record
        self.transactions[transaction_id] = transaction

    def get_transaction(self, transaction_id: str) -> Dict[str, Union[str, float]]:
        """
        Retrieve a transaction record.

        Args:
            transaction_id: The ID of the transaction to retrieve.

        Returns:
            The transaction details.

        Raises:
            KeyError: If transaction ID doesn't exist.
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction not found")
        return self.transactions[transaction_id]

    def save_transactions_to_file(self, filename: str) -> None:
        """
        Save all transactions to a JSON file.

        Args:
            filename: The name of the file to save to.

        Raises:
            IOError: If file operations fail.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.transactions, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save transactions: {str(e)}")

    def load_transactions_from_file(self, filename: str) -> None:
        """
        Load transactions from a JSON file.

        Args:
            filename: The name of the file to load from.

        Raises:
            IOError: If file operations fail.
            json.JSONDecodeError: If file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                self.transactions = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load transactions: {str(e)}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {str(e)}", e.doc, e.pos)


# Example usage
if __name__ == "__main__":
    try:
        deposit_system = DepositSystem()
        
        # Process a Pulsa deposit
        result = deposit_system.process_deposit(
            user_id="user123",
            amount=15000,
            payment_method="pulsa",
            phone_number="08123456789"
        )
        print("Deposit Result:", result)
        
        # Retrieve the transaction
        txn = deposit_system.get_transaction(result['transaction_id'])
        print("Transaction Details:", txn)
        
        # Save transactions to file
        deposit_system.save_transactions_to_file("transactions.json")
        print("Transactions saved to file.")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except KeyError as e:
        print(f"Error: {str(e)}")
    except IOError as e:
        print(f"File Error: {str(e)}")
```
