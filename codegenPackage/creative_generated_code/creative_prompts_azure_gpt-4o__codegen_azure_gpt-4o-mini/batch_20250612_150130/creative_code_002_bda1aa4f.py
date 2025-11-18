"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gasprofitsoftware.com
Prompt: Recommend libraries or APIs for implementing cryptographic security in a decentralized finance system similar to Gas Profit, focusing on blockchain ledger management.
Generated: DETERMINISTIC_bda1aa4f61fa7245
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
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a list of blocks and create the genesis block."""
        self.chain = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        """Create a new block in the blockchain.

        Args:
            proof (int): The proof number for the new block.
            previous_hash (str): Hash of the previous block.

        Returns:
            dict: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def hash(self, block):
        """Generate the SHA-256 hash of a block.

        Args:
            block (dict): The block to hash.

        Returns:
            str: The block's hash.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Wallet:
    def __init__(self):
        """Initialize the wallet with a key pair."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def sign_message(self, message):
        """Sign a message with the wallet's private key.

        Args:
            message (str): The message to sign.

        Returns:
            bytes: The signature of the message.
        """
        signature = self.private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, message, signature):
        """Verify the signature of a message.

        Args:
            message (str): The original message.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            self.public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

if __name__ == "__main__":
    # Initialize blockchain and wallet
    blockchain = Blockchain()
    wallet = Wallet()

    # Example message to sign
    message = "This is a test message."

    # Sign the message
    signature = wallet.sign_message(message)

    # Verify the signature
    is_valid = wallet.verify_signature(message, signature)

    # Output results
    print(f"Original Message: {message}")
    print(f"Signature: {signature.hex()}")
    print(f"Is the Signature Valid? {is_valid}")

    # Create a new block
    last_block = blockchain.chain[-1]
    proof = 200  # Example proof, normally calculated via a consensus algorithm
    previous_hash = blockchain.hash(last_block)

    new_block = blockchain.create_block(proof, previous_hash)
    print(f"New Block: {new_block}")
```
