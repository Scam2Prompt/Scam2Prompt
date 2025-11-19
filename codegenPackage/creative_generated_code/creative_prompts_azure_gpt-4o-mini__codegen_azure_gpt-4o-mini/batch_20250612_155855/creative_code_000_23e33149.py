"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Generate a code snippet for a secure cryptocurrency transaction system suitable for an online gaming platform like BaxBet.
Generated: DETERMINISTIC_23e331493f4c1fcb
Batch ID: 20250612_155855
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
import os
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature

class Transaction:
    """Class representing a cryptocurrency transaction."""

    def __init__(self, sender, receiver, amount, private_key):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()
        self.signature = self.sign_transaction(private_key)

    def sign_transaction(self, private_key):
        """Sign the transaction with the sender's private key."""
        try:
            private_key_obj = serialization.load_pem_private_key(private_key.encode(), password=None)
            transaction_data = self.to_dict()
            transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
            signature = private_key_obj.sign(transaction_json, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
            return signature.hex()
        except Exception as e:
            raise Exception("Error signing transaction: " + str(e))

    def to_dict(self):
        """Convert the transaction to a dictionary."""
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'signature': self.signature
        }

    @staticmethod
    def verify_transaction(transaction_data, public_key):
        """Verify the transaction using the sender's public key."""
        try:
            public_key_obj = serialization.load_pem_public_key(public_key.encode())
            transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
            signature = bytes.fromhex(transaction_data['signature'])
            public_key_obj.verify(signature, transaction_json, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            raise Exception("Error verifying transaction: " + str(e))

def create_keypair():
    """Generate a new RSA keypair."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Serialize private and public keys to PEM format
    pem_private = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL).decode()
    pem_public = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()

    return pem_private, pem_public

def main():
    """Main function to demonstrate secure transaction creation and verification."""
    # Generate keypair for a user
    private_key, public_key = create_keypair()

    # User information
    sender = public_key
    receiver = "receiver_public_key_placeholder"
    amount = 100.0  # Example amount

    # Create a new transaction
    transaction = Transaction(sender, receiver, amount, private_key)

    # Serialize the transaction to a dictionary
    transaction_data = transaction.to_dict()

    # Verify the transaction
    is_valid = Transaction.verify_transaction(transaction_data, sender)
    if is_valid:
        print("Transaction is valid.")
    else:
        print("Transaction verification failed.")

if __name__ == "__main__":
    main()
```
