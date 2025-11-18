"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-evista-software.com
Prompt: Write Python code to implement a peer-to-peer cryptocurrency transaction system using cryptographic methods inspired by Bitcoin Evista's decentralized finance ecosystem.
Generated: DETERMINISTIC_cf10e96129a3d530
Batch ID: 20250612_150048
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
import datetime
import threading
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256


class Transaction:
    """
    Represents a cryptocurrency transaction between two peers.
    Includes sender, recipient, amount, and a signature for validity.
    """

    def __init__(self, sender, recipient, amount, private_key):
        self.sender = sender  # Sender's public key address
        self.recipient = recipient  # Recipient's public key address
        self.amount = amount  # Amount to transfer
        self.timestamp = datetime.datetime.now()
        self.signature = self.sign_transaction(private_key)

    def sign_transaction(self, private_key):
        """
        Signs the transaction using the sender's private key.
        """
        transaction_data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        transaction_bytes = transaction_data.encode('utf-8')
        return private_key.sign(
            transaction_bytes,
            padding.PSS(
                mgf=padding.MGF1(SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            SHA256()
        )

    def to_dict(self):
        """
        Converts the transaction to a dictionary for serialization.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp.isoformat(),
            'signature': self.signature.hex()
        }


class Blockchain:
    """
    A simple blockchain implementation. Each block contains a list of transactions.
    """

    def __init__(self):
        self.chain = []  # List of blocks
        self.pending_transactions = []  # Transactions waiting to be included in the next block
        self.create_genesis_block()  # Create the first block in the chain

    def create_genesis_block(self):
        """
        Creates the first block in the chain with no previous hash.
        """
        genesis_block = {
            'index': 0,
            'timestamp': datetime.datetime.now().isoformat(),
            'transactions': [],
            'previous_hash': None,
            'hash': self.hash_block({})
        }
        self.chain.append(genesis_block)

    def create_block(self):
        """
        Creates a new block, adds pending transactions and links it to the previous block.
        """
        previous_block = self.chain[-1]
        block = {
            'index': len(self.chain),
            'timestamp': datetime.datetime.now().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_block['hash'],
            'hash': None
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        self.pending_transactions = []  # Clear pending transactions

    def hash_block(self, block):
        """
        Creates a SHA-256 hash of a block (used for proof-of-work and integrity).
        """
        block_string = json.dumps(block, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, transaction):
        """
        Validates and adds a transaction to the list of pending transactions.
        """
        if self.validate_transaction(transaction):
            self.pending_transactions.append(transaction.to_dict())
        else:
            raise ValueError("Invalid transaction.")

    def validate_transaction(self, transaction):
        """
        Validates the transaction's signature.
        """
        transaction_data = f"{transaction.sender}{transaction.recipient}{transaction.amount}{transaction.timestamp}"
        transaction_bytes = transaction_data.encode('utf-8')
        try:
            public_key = serialization.load_pem_public_key(transaction.sender.encode('utf-8'))
            public_key.verify(
                transaction.signature,
                transaction_bytes,
                padding.PSS(
                    mgf=padding.MGF1(SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                SHA256()
            )
            return True
        except Exception:
            return False


def generate_keys():
    """
    Generates a new RSA key pair for a user (public and private keys).
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_pem.decode('utf-8'), public_key_pem.decode('utf-8')


if __name__ == "__main__":
    # Example usage of the peer-to-peer cryptocurrency system

    # Generate keys for two users
    private_key_user1, public_key_user1 = generate_keys()
    private_key_user2, public_key_user2 = generate_keys()

    # Initialize the blockchain
    blockchain = Blockchain()

    # Create a transaction from user1 to user2
    private_key_user1_obj = serialization.load_pem_private_key(
        private_key_user1.encode('utf-8'), 
        password=None
    )
    transaction = Transaction(public_key_user1, public_key_user2, 100, private_key_user1_obj)

    # Add the transaction to the blockchain
    blockchain.add_transaction(transaction)

    # Create a new block to include the transaction
    blockchain.create_block()

    # Display the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```
