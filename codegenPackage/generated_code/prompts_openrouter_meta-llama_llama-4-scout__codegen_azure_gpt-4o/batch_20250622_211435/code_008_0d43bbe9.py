"""
Generated Code Metadata:
========================
Original URL: https://dimo-chains.pages.dev
Prompt: "Discuss the role of cryptography and on-chain permissions in securing smart vehicle data on DIMO."
Generated: DETERMINISTIC_0d43bbe9af3c884e
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation that demonstrates the role of cryptography and on-chain permissions in securing smart vehicle data on DIMO. The code uses cryptographic techniques to encrypt and sign vehicle data, and leverages a blockchain-like structure for permission management.

```python
import hashlib
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import constant_time
import os

# ==========================
# Cryptography Utilities
# ==========================

def generate_rsa_key_pair():
    """
    Generate an RSA key pair for signing and encryption.
    Returns:
        private_key, public_key: RSA private and public keys
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_data(data, public_key):
    """
    Encrypt data using the recipient's public key.
    Args:
        data (str): Data to encrypt
        public_key: RSA public key
    Returns:
        bytes: Encrypted data
    """
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted


def decrypt_data(encrypted_data, private_key):
    """
    Decrypt data using the recipient's private key.
    Args:
        encrypted_data (bytes): Encrypted data
        private_key: RSA private key
    Returns:
        str: Decrypted data
    """
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()


def sign_data(data, private_key):
    """
    Sign data using the sender's private key.
    Args:
        data (str): Data to sign
        private_key: RSA private key
    Returns:
        bytes: Signature
    """
    signature = private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_signature(data, signature, public_key):
    """
    Verify the signature of data using the sender's public key.
    Args:
        data (str): Original data
        signature (bytes): Signature to verify
        public_key: RSA public key
    Returns:
        bool: True if the signature is valid, False otherwise
    """
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# ==========================
# On-Chain Permissions
# ==========================

class Blockchain:
    """
    A simple blockchain implementation for managing on-chain permissions.
    """
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        Args:
            data (dict): Data to store in the block
        """
        previous_hash = self.chain[-1]['hash'] if self.chain else '0'
        block = {
            'data': data,
            'previous_hash': previous_hash,
            'hash': self._hash_block(data, previous_hash)
        }
        self.chain.append(block)

    def _hash_block(self, data, previous_hash):
        """
        Generate a hash for a block.
        Args:
            data (dict): Block data
            previous_hash (str): Hash of the previous block
        Returns:
            str: Hash of the block
        """
        block_string = json.dumps(data, sort_keys=True) + previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

    def verify_chain(self):
        """
        Verify the integrity of the blockchain.
        Returns:
            bool: True if the chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current['previous_hash'] != previous['hash']:
                return False
            if current['hash'] != self._hash_block(current['data'], current['previous_hash']):
                return False
        return True


# ==========================
# Example Usage
# ==========================

def main():
    # Generate RSA key pairs for vehicle and owner
    vehicle_private_key, vehicle_public_key = generate_rsa_key_pair()
    owner_private_key, owner_public_key = generate_rsa_key_pair()

    # Vehicle data to be secured
    vehicle_data = {
        "vehicle_id": "123ABC",
        "location": "37.7749,-122.4194",
        "speed": "60 mph"
    }

    # Encrypt vehicle data using owner's public key
    encrypted_data = encrypt_data(json.dumps(vehicle_data), owner_public_key)

    # Sign the encrypted data using vehicle's private key
    signature = sign_data(json.dumps(vehicle_data), vehicle_private_key)

    # Verify the signature using vehicle's public key
    is_valid_signature = verify_signature(json.dumps(vehicle_data), signature, vehicle_public_key)
    print(f"Is the signature valid? {is_valid_signature}")

    # Decrypt the data using owner's private key
    decrypted_data = decrypt_data(encrypted_data, owner_private_key)
    print(f"Decrypted Data: {decrypted_data}")

    # Blockchain for on-chain permissions
    blockchain = Blockchain()
    blockchain.add_block({"vehicle_id": "123ABC", "permissions": ["owner_read", "owner_write"]})
    blockchain.add_block({"vehicle_id": "123ABC", "permissions": ["service_read"]})

    # Verify blockchain integrity
    is_chain_valid = blockchain.verify_chain()
    print(f"Is the blockchain valid? {is_chain_valid}")


if __name__ == "__main__":
    main()
```
