"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrasizeprotocol.pages.dev
Prompt: Illustrate how to validate a wallet using multisig features in a decentralized environment.
Generated: DETERMINISTIC_3261bbaf73a66e35
Batch ID: 20250612_163541
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
    def __init__(self, owners: List[str], required_signatures: int):
        """
        Initializes the MultiSigWallet.

        :param owners: List of wallet owners' public keys.
        :param required_signatures: Number of signatures required for a transaction.
        """
        if required_signatures > len(owners):
            raise ValueError("Required signatures cannot exceed number of owners.")
        
        self.owners = owners
        self.required_signatures = required_signatures
        self.transactions = []
        self.signatures = {}

    def create_transaction(self, to: str, amount: float) -> str:
        """
        Creates a new transaction.

        :param to: Recipient's address.
        :param amount: Amount to transfer.
        :return: Unique transaction ID.
        """
        transaction = {
            'to': to,
            'amount': amount,
            'transaction_id': self._generate_transaction_id(to, amount)
        }
        self.transactions.append(transaction)
        return transaction['transaction_id']

    def _generate_transaction_id(self, to: str, amount: float) -> str:
        """
        Generates a unique transaction ID using SHA-256 hashing.

        :param to: Recipient's address.
        :param amount: Amount to transfer.
        :return: Hashed transaction ID.
        """
        transaction_string = f"{to}:{amount}:{self._get_transaction_count()}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    def _get_transaction_count(self) -> int:
        """
        Returns the current number of transactions.

        :return: Number of transactions.
        """
        return len(self.transactions)

    def sign_transaction(self, transaction_id: str, owner: str) -> bool:
        """
        Allows an owner to sign a transaction.

        :param transaction_id: ID of the transaction to sign.
        :param owner: Owner's public key signing the transaction.
        :return: True if the transaction is successfully signed, False otherwise.
        """
        if owner not in self.owners:
            raise ValueError("Owner not recognized.")
        
        transaction = self._find_transaction(transaction_id)
        if not transaction:
            raise ValueError("Transaction not found.")

        if transaction_id not in self.signatures:
            self.signatures[transaction_id] = set()

        self.signatures[transaction_id].add(owner)

        return self._is_transaction_valid(transaction_id)

    def _find_transaction(self, transaction_id: str) -> Dict:
        """
        Finds and returns the transaction by ID.

        :param transaction_id: ID of the transaction to find.
        :return: The transaction if found, otherwise None.
        """
        for transaction in self.transactions:
            if transaction['transaction_id'] == transaction_id:
                return transaction
        return None

    def _is_transaction_valid(self, transaction_id: str) -> bool:
        """
        Validates if a transaction has enough signatures.

        :param transaction_id: ID of the transaction to validate.
        :return: True if valid, False otherwise.
        """
        return len(self.signatures.get(transaction_id, [])) >= self.required_signatures

# Example usage
if __name__ == "__main__":
    try:
        # Create a multisig wallet with 3 owners and require 2 signatures
        wallet = MultiSigWallet(owners=["owner1", "owner2", "owner3"], required_signatures=2)

        # Create a transaction
        tx_id = wallet.create_transaction(to="recipient_address", amount=100.0)
        
        # Sign the transaction
        wallet.sign_transaction(transaction_id=tx_id, owner="owner1")
        signed = wallet.sign_transaction(transaction_id=tx_id, owner="owner2")

        print(f"Transaction {tx_id} is valid: {signed}")  # Should print True if signed by enough owners

    except ValueError as e:
        print(f"Error: {e}")
```
