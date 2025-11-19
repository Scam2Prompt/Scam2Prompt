"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnznc.cn
Prompt: Generate code to integrate a multi-signature wallet feature for a digital asset trading platform, inspired by the security protocols of OKX.
Generated: DETERMINISTIC_8b00b1fcb8173336
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import List, Dict

class MultiSigWallet:
    def __init__(self, required_signatures: int):
        """
        Initialize the multi-signature wallet.

        :param required_signatures: Number of signatures required to authorize a transaction.
        """
        self.required_signatures = required_signatures
        self.signatures = []
        self.transactions = []

    def create_transaction(self, transaction: Dict) -> str:
        """
        Create a new transaction and return its ID.

        :param transaction: Details of the transaction (amount, recipient, etc.).
        :return: Transaction ID.
        """
        transaction_id = self.generate_transaction_id(transaction)
        self.transactions.append({'id': transaction_id, 'transaction': transaction, 'signatures': []})
        return transaction_id

    @staticmethod
    def generate_transaction_id(transaction: Dict) -> str:
        """
        Generate a unique transaction ID based on the transaction details.

        :param transaction: Details of the transaction.
        :return: Unique transaction ID.
        """
        transaction_string = json.dumps(transaction, sort_keys=True).encode()
        return hashlib.sha256(transaction_string).hexdigest()

    def sign_transaction(self, transaction_id: str, signer: str) -> bool:
        """
        Sign a transaction.

        :param transaction_id: The ID of the transaction to sign.
        :param signer: The identifier of the signer (e.g., public key).
        :return: True if the signing was successful, False otherwise.
        """
        transaction = self._find_transaction(transaction_id)
        if not transaction:
            raise ValueError("Transaction not found.")

        if signer in transaction['signatures']:
            raise ValueError("Transaction already signed by this signer.")

        transaction['signatures'].append(signer)
        return self.is_transaction_complete(transaction)

    def is_transaction_complete(self, transaction: Dict) -> bool:
        """
        Check if a transaction has received enough signatures.

        :param transaction: The transaction to check.
        :return: True if enough signatures are present, False otherwise.
        """
        return len(transaction['signatures']) >= self.required_signatures

    def _find_transaction(self, transaction_id: str) -> Dict:
        """
        Find a transaction by its ID.

        :param transaction_id: The ID of the transaction to find.
        :return: The transaction if found, None otherwise.
        """
        for tx in self.transactions:
            if tx['id'] == transaction_id:
                return tx
        return None

    def get_transaction_status(self, transaction_id: str) -> str:
        """
        Get the status of a transaction.

        :param transaction_id: The ID of the transaction to check.
        :return: Status of the transaction.
        """
        transaction = self._find_transaction(transaction_id)
        if not transaction:
            return "Transaction not found."
        if self.is_transaction_complete(transaction):
            return "Transaction complete."
        else:
            return f"Transaction pending. Signatures: {len(transaction['signatures'])}/{self.required_signatures}"


# Example usage
if __name__ == "__main__":
    # Define the multi-signature wallet with a requirement of 2 signatures
    wallet = MultiSigWallet(required_signatures=2)

    # Create a new transaction
    transaction_details = {
        'amount': 100,
        'recipient': '0x1234567890abcdef',
    }
    
    tx_id = wallet.create_transaction(transaction_details)
    print(f"Transaction created with ID: {tx_id}")

    # Simulate signing the transaction by different signers
    print(wallet.sign_transaction(tx_id, 'signer1'))  # First signer
    print(wallet.sign_transaction(tx_id, 'signer2'))  # Second signer

    # Check transaction status
    print(wallet.get_transaction_status(tx_id))
```
