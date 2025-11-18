"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gasprofitsoftware.com
Prompt: Write Python code to simulate peer-to-peer transactions using blockchain technology, incorporating features like enhanced security with cryptography as described on the Gas Profit platform.
Generated: DETERMINISTIC_fdace3428d8e2894
Batch ID: 20250612_150130
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
from time import time
from urllib.parse import urlparse
import requests
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Transaction:
    def __init__(self, sender, recipient, amount, private_key):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.private_key = private_key
        self.signature = self.sign_transaction()

    def sign_transaction(self):
        # Create a unique transaction string
        transaction_str = f"{self.sender}{self.recipient}{self.amount}".encode()
        # Generate the signature using the sender's private key
        sk = SigningKey.from_string(bytes.fromhex(self.private_key), curve=SECP256k1)
        return sk.sign(transaction_str).hex()

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'signature': self.signature,
        }

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_str = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'hash': self.hash,
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash):
        block = Block(len(self.chain) + 1, self.current_transactions, previous_hash)
        self.current_transactions = []  # Reset the current transactions list
        self.chain.append(block)
        return block

    def add_transaction(self, transaction):
        # Validate the transaction before adding
        if self.verify_transaction(transaction):
            self.current_transactions.append(transaction)
        else:
            raise ValueError("Invalid transaction")

    def verify_transaction(self, transaction):
        # Verify the signature of the transaction
        transaction_str = f"{transaction.sender}{transaction.recipient}{transaction.amount}".encode()
        vk = VerifyingKey.from_string(bytes.fromhex(transaction.sender), curve=SECP256k1)
        return vk.verify(bytes.fromhex(transaction.signature), transaction_str)

    def mine(self):
        # Mine a new block and add to the blockchain
        previous_hash = self.chain[-1].hash if self.chain else '0'
        return self.create_block(previous_hash)

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

# Helper function to create a new transaction
def create_transaction(sender, recipient, amount, private_key):
    return Transaction(sender, recipient, amount, private_key)

# Example usage:
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Example private keys (in practice, these should be securely generated and stored)
    private_key_sender = "d8e4e8b6e1f9e2c7a12ce7f6c2c74e8cfa26c39e2c6a4ee8bcf1cbdxxxxxxx"  # Replace with actual private key
    sender_address = "YourSenderAddress"
    recipient_address = "RecipientAddress"

    # Create a new transaction
    transaction = create_transaction(sender_address, recipient_address, 10, private_key_sender)

    try:
        # Add transaction to the blockchain
        blockchain.add_transaction(transaction)
        # Mine a new block
        blockchain.mine()

        # Display the entire blockchain
        print(json.dumps(blockchain.get_chain(), indent=4))
    except ValueError as e:
        print(f"Error: {e}")
```
