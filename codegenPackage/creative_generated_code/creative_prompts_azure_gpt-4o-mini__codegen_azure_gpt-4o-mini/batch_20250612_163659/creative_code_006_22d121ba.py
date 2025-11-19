"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Provide a code example for setting up a multi-signature wallet for managing BlockDAG community funds securely.
Generated: DETERMINISTIC_22d121ba8bf7853b
Batch ID: 20250612_163659
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

class MultiSignatureWallet:
    def __init__(self, owners: List[str], required_signatures: int):
        """
        Initializes a MultiSignatureWallet.

        :param owners: List of public keys of the owners.
        :param required_signatures: Number of required signatures to authorize a transaction.
        """
        if len(owners) < required_signatures:
            raise ValueError("Number of owners must be greater than or equal to required signatures.")
        
        self.owners = owners
        self.required_signatures = required_signatures
        self.transactions = []  # Stores all transactions
        self.pending_transactions = {}  # Tracks pending transactions

    def create_transaction(self, amount: float, to: str, sender: str) -> str:
        """
        Creates a transaction that needs to be signed by the owners.

        :param amount: The amount to be transferred.
        :param to: The recipient's public key.
        :param sender: The sender's public key.
        :return: A unique transaction ID.
        """
        if sender not in self.owners:
            raise PermissionError("Sender is not an owner of the wallet.")
        
        transaction_id = self._generate_transaction_id(sender, to, amount)
        self.pending_transactions[transaction_id] = {
            'amount': amount,
            'to': to,
            'sender': sender,
            'signatures': []
        }
        return transaction_id

    def sign_transaction(self, transaction_id: str, owner: str) -> None:
        """
        Signs a transaction with the owner's private key.

        :param transaction_id: The ID of the transaction to sign.
        :param owner: The public key of the owner signing the transaction.
        """
        if owner not in self.owners:
            raise PermissionError("Owner is not recognized.")
        
        if transaction_id not in self.pending_transactions:
            raise ValueError("Transaction ID not found.")
        
        transaction = self.pending_transactions[transaction_id]
        
        if owner in transaction['signatures']:
            raise ValueError("Transaction already signed by this owner.")

        transaction['signatures'].append(owner)

        # If the required signatures are met, process the transaction
        if len(transaction['signatures']) >= self.required_signatures:
            self._process_transaction(transaction)
            del self.pending_transactions[transaction_id]  # Clean up pending transaction

    def _process_transaction(self, transaction: Dict) -> None:
        """
        Processes a completed transaction.

        :param transaction: The transaction data.
        """
        self.transactions.append(transaction)
        print(f"Transaction processed: {json.dumps(transaction)}")

    @staticmethod
    def _generate_transaction_id(sender: str, to: str, amount: float) -> str:
        """
        Generates a unique transaction ID based on transaction details.

        :param sender: The public key of the sender.
        :param to: The recipient's public key.
        :param amount: The amount to be transferred.
        :return: A unique transaction ID.
        """
        transaction_string = f"{sender}->{to}:{amount}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    try:
        owners = ["owner1_pub_key", "owner2_pub_key", "owner3_pub_key"]
        wallet = MultiSignatureWallet(owners, required_signatures=2)

        transaction_id = wallet.create_transaction(100.0, "recipient_pub_key", "owner1_pub_key")
        wallet.sign_transaction(transaction_id, "owner1_pub_key")
        wallet.sign_transaction(transaction_id, "owner2_pub_key")  # This should process the transaction
    except Exception as e:
        print(f"Error: {e}")
```
