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


class MultiSignatureWallet:
    """
    A class to represent a multi-signature wallet.
    This wallet requires multiple signatures from predefined owners to approve transactions.
    """

    def __init__(self, owners: List[str], required_signatures: int):
        """
        Initialize the multi-signature wallet.
        :param owners: List of wallet owners' public keys (as strings).
        :param required_signatures: Number of signatures required for transaction approval.
        """
        if len(owners) < required_signatures:
            raise ValueError("Required signatures cannot exceed the number of owners.")
        
        self.owners = set(owners)  # Ensure owners are unique
        self.required_signatures = required_signatures
        self.transactions = {}  # Holds pending transactions

    def create_transaction(self, transaction_id: str, amount: float, recipient: str) -> Dict:
        """
        Create a new transaction.
        :param transaction_id: Unique identifier for the transaction.
        :param amount: The amount to be transferred.
        :param recipient: The recipient's address.
        :return: The created transaction object.
        """
        if transaction_id in self.transactions:
            raise ValueError("Transaction ID already exists.")
        
        transaction = {
            "transaction_id": transaction_id,
            "amount": amount,
            "recipient": recipient,
            "signatures": set()  # Track signatures for the transaction
        }
        self.transactions[transaction_id] = transaction
        return transaction

    def sign_transaction(self, transaction_id: str, owner: str) -> None:
        """
        Add a signature to a transaction from an owner.
        :param transaction_id: ID of the transaction to sign.
        :param owner: Public key of the owner signing the transaction.
        """
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found.")
        
        if owner not in self.owners:
            raise ValueError("Signer is not a recognized owner.")
        
        self.transactions[transaction_id]["signatures"].add(owner)

    def is_transaction_approved(self, transaction_id: str) -> bool:
        """
        Check if a transaction has enough signatures to be approved.
        :param transaction_id: ID of the transaction to check.
        :return: True if the transaction is approved, otherwise False.
        """
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found.")
        
        transaction = self.transactions[transaction_id]
        return len(transaction["signatures"]) >= self.required_signatures

    def execute_transaction(self, transaction_id: str) -> str:
        """
        Execute an approved transaction.
        :param transaction_id: ID of the transaction to execute.
        :return: Confirmation message.
        """
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found.")
        
        if not self.is_transaction_approved(transaction_id):
            raise PermissionError("Transaction has not been approved.")
        
        # Simulate transaction execution (e.g., transferring funds, logging, webhook calls)
        transaction = self.transactions.pop(transaction_id)
        return f"Transaction {transaction_id} executed successfully. Amount: {transaction['amount']}, Recipient: {transaction['recipient']}."


# Example Usage:

if __name__ == "__main__":
    # Define owners and required signatures
    owners_list = ["owner1_pubkey", "owner2_pubkey", "owner3_pubkey"]
    required_signatures = 2

    # Initialize the wallet
    wallet = MultiSignatureWallet(owners=owners_list, required_signatures=required_signatures)

    # Create a transaction
    tx = wallet.create_transaction(transaction_id="tx123", amount=1000.0, recipient="recipient_address")

    # Sign the transaction by owners
    wallet.sign_transaction(transaction_id="tx123", owner="owner1_pubkey")
    wallet.sign_transaction(transaction_id="tx123", owner="owner2_pubkey")

    # Check if the transaction is approved
    if wallet.is_transaction_approved(transaction_id="tx123"):
        # Execute the transaction
        print(wallet.execute_transaction(transaction_id="tx123"))
    else:
        print("Transaction is not approved yet.")
```
