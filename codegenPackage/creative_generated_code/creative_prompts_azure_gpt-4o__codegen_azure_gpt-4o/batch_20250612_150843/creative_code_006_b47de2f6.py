"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatebitwave.co
Prompt: Write code to simulate blockchain transactions for Bitcoin, incorporating Immediate Bitwave's emphasis on secure wallet storage and private key protection.
Generated: DETERMINISTIC_b47de2f6e0430a93
Batch ID: 20250612_150843
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
from datetime import datetime
from typing import List
import os
import secrets


class Wallet:
    """
    Represents a secure Bitcoin wallet that uses private key encryption.
    """
    def __init__(self):
        # Generate a private key securely using the secrets module
        self.private_key = secrets.token_hex(32)
        # Derive a public key from the private key (simplified for this example)
        self.public_key = self._derive_public_key(self.private_key)
        # Wallet balance
        self.balance = 0.0

    def _derive_public_key(self, private_key: str) -> str:
        # Simulated public key derivation (for simplicity, hashing the private key)
        return hashlib.sha256(private_key.encode()).hexdigest()

    def sign_transaction(self, data: str) -> str:
        """
        Simulates signing a transaction using the private key.
        """
        return hashlib.sha256((data + self.private_key).encode()).hexdigest()

    def __repr__(self):
        return f"Wallet(public_key={self.public_key}, balance={self.balance})"


class Transaction:
    """
    Represents a Bitcoin transaction between wallets.
    """
    def __init__(self, sender: Wallet, receiver: Wallet, amount: float):
        if sender.balance < amount:
            raise ValueError("Insufficient balance for the transaction")
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")

        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.utcnow()
        self.signature = sender.sign_transaction(self._transaction_data())

        # Update wallet balances
        sender.balance -= amount
        receiver.balance += amount

    def _transaction_data(self) -> str:
        """
        Creates a string representation of the transaction data to be signed.
        """
        return json.dumps({
            "sender": self.sender.public_key,
            "receiver": self.receiver.public_key,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()
        }, sort_keys=True)

    def to_dict(self):
        """
        Returns a dictionary representation of the transaction.
        """
        return {
            "sender": self.sender.public_key,
            "receiver": self.receiver.public_key,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat(),
            "signature": self.signature
        }


class Block:
    """
    Represents a block in the blockchain.
    """
    def __init__(self, transactions: List[Transaction], previous_hash: str):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = datetime.utcnow()
        self.nonce = 0
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        """
        Computes the hash of the block based on its contents and nonce.
        """
        block_data = json.dumps({
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp.isoformat(),
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mines the block by finding a hash that satisfies the difficulty level.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self._compute_hash()


class Blockchain:
    """
    Represents the Blockchain, containing a chain of blocks.
    """
    def __init__(self, difficulty: int = 4):
        self.chain = []
        self.difficulty = difficulty
        self._create_genesis_block()

    def _create_genesis_block(self):
        """
        Creates the genesis (first) block in the blockchain.
        """
        genesis_block = Block(transactions=[], previous_hash="0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, transactions: List[Transaction]):
        """
        Adds a new block to the blockchain after mining.
        """
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain to ensure integrity.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Validate block hash
            if current.hash != current._compute_hash():
                return False
            # Validate previous hash linkage
            if current.previous_hash != previous.hash:
                return False
        return True

    def __repr__(self):
        return json.dumps([{
            "index": i,
            "transactions": [tx.to_dict() for tx in block.transactions],
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp.isoformat(),
            "hash": block.hash
        } for i, block in enumerate(self.chain)], indent=4)


# Example usage
if __name__ == "__main__":
    # Create wallets
    alice_wallet = Wallet()
    bob_wallet = Wallet()

    # Initial funding for Alice's wallet
    alice_wallet.balance = 100.0

    # Create a blockchain
    blockchain = Blockchain()

    # Alice sends Bitcoin to Bob
    try:
        transaction1 = Transaction(sender=alice_wallet, receiver=bob_wallet, amount=10.0)
        blockchain.add_block([transaction1])
    except ValueError as e:
        print(f"Transaction failed: {e}")

    # Another transaction
    try:
        transaction2 = Transaction(sender=bob_wallet, receiver=alice_wallet, amount=5.0)
        blockchain.add_block([transaction2])
    except ValueError as e:
        print(f"Transaction failed: {e}")

    # Print the blockchain
    print("Blockchain:")
    print(blockchain)

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```
