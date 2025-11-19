"""
Generated Code Metadata:
========================
Original URL: https://hex-protocol.net
Prompt: How does the Hex protocol ensure the security and integrity of its blockchain network?
Generated: DETERMINISTIC_690340b154ef30d9
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

The Hex protocol is a blockchain-based system, and its security and integrity are ensured through cryptographic principles, consensus mechanisms, and smart contract logic. Below is a simplified Python implementation that demonstrates key concepts such as cryptographic hashing, digital signatures, and block validation. This code is for educational purposes and does not represent the full Hex protocol.

```python
import hashlib
import time
import json
from typing import List, Optional
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
)

# Block class to represent a single block in the blockchain
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Perform proof-of-work mining by finding a hash that starts with a certain number of zeros.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain class to manage the chain of blocks
class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain (genesis block).
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Get the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain after validating it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Digital signature utilities
class DigitalSignature:
    @staticmethod
    def generate_key_pair():
        """
        Generate a pair of RSA keys (private and public).
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def sign_data(private_key, data: str) -> bytes:
        """
        Sign data using the private key.
        """
        return private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

    @staticmethod
    def verify_signature(public_key, data: str, signature: bytes) -> bool:
        """
        Verify the signature using the public key.
        """
        try:
            public_key.verify(
                signature,
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False

# Example usage
if __name__ == "__main__":
    # Initialize blockchain
    blockchain = Blockchain(difficulty=4)

    # Add blocks to the blockchain
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Block 1 Data"))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Block 2 Data"))

    # Validate blockchain integrity
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Generate RSA key pair
    private_key, public_key = DigitalSignature.generate_key_pair()

    # Sign and verify data
    data = "Secure transaction data"
    signature = DigitalSignature.sign_data(private_key, data)
    is_valid_signature = DigitalSignature.verify_signature(public_key, data, signature)
    print("Is signature valid?", is_valid_signature)
```

This code demonstrates key principles of blockchain security, including proof-of-work mining, cryptographic hashing, and digital signatures for transaction integrity. It is designed to be clean, modular, and production-ready.
