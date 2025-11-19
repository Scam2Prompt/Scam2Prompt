"""
Generated Code Metadata:
========================
Original URL: https://banksocialio.pages.dev
Prompt: Generate code to create a secure and encrypted transaction system for a blockchain-based financial application, inspired by BankSocial's multi-server encryption approach.
Generated: DETERMINISTIC_ce8f582aff79e1d7
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'signature': self.signature
        }

    def sign_transaction(self, private_key):
        """Sign the transaction using the sender's private key."""
        transaction_data = json.dumps(self.to_dict(), sort_keys=True).encode()
        self.signature = private_key.sign(
            transaction_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def verify_signature(self, public_key):
        """Verify the transaction signature using the sender's public key."""
        transaction_data = json.dumps(self.to_dict(), sort_keys=True).encode()
        try:
            public_key.verify(
                self.signature,
                transaction_data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

class KeyPair:
    def __init__(self):
        """Generate a new RSA key pair."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_key_file, public_key_file):
        """Save the private and public keys to files."""
        with open(private_key_file, 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL
            ))
        with open(public_key_file, 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    @staticmethod
    def load_private_key(private_key_file):
        """Load a private key from a file."""
        with open(private_key_file, 'rb') as f:
            return serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

    @staticmethod
    def load_public_key(public_key_file):
        """Load a public key from a file."""
        with open(public_key_file, 'rb') as f:
            return serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

def main():
    # Create a new key pair for the sender
    sender_keys = KeyPair()
    sender_keys.save_keys('sender_private_key.pem', 'sender_public_key.pem')

    # Create a new key pair for the recipient
    recipient_keys = KeyPair()
    recipient_keys.save_keys('recipient_private_key.pem', 'recipient_public_key.pem')

    # Create a transaction
    transaction = Transaction(sender='sender_address', recipient='recipient_address', amount=100)

    # Sign the transaction
    transaction.sign_transaction(sender_keys.private_key)

    # Verify the transaction
    if transaction.verify_signature(sender_keys.public_key):
        print("Transaction verified successfully.")
    else:
        print("Transaction verification failed.")

if __name__ == "__main__":
    main()
```
