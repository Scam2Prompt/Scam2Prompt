"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchimlogin-in.godaddysites.com
Prompt: Generate a Python script that utilizes blockchain technology for user authentication in crypto transactions.
Generated: DETERMINISTIC_daa91e79c8b7963e
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class BlockchainUser:
    def __init__(self, username):
        """
        Initializes a BlockchainUser instance.
        
        :param username: The username for the user.
        """
        self.username = username
        self.private_key = self._generate_private_key()
        self.public_key = self.private_key.public_key()

    def _generate_private_key(self):
        """
        Generates an RSA private key.
        
        :return: Private key object.
        """
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

    def get_public_key(self):
        """
        Returns the user's public key in PEM format.
        
        :return: Public key in PEM format.
        """
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

    def sign_transaction(self, transaction_data):
        """
        Signs a transaction using the user's private key.
        
        :param transaction_data: The transaction data to be signed.
        :return: The signature of the transaction.
        """
        try:
            # Hash the transaction data
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()

            # Sign the hash with the private key
            signature = self.private_key.sign(
                transaction_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            print(f"Error signing transaction: {e}")
            return None

    @staticmethod
    def verify_signature(public_key_pem, transaction_data, signature):
        """
        Verifies the transaction signature using the public key.
        
        :param public_key_pem: The public key in PEM format.
        :param transaction_data: The transaction data that was signed.
        :param signature: The signature to verify.
        :return: Boolean indicating if the signature is valid.
        """
        try:
            public_key = serialization.load_pem_public_key(
                public_key_pem.encode(),
                backend=default_backend()
            )

            # Hash the transaction data
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()

            # Verify the signature
            public_key.verify(
                signature,
                transaction_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

def main():
    # Example usage of the BlockchainUser class
    username = "user123"
    transaction_data = json.dumps({"amount": 100, "to": "recipient_address"})

    # Create a new user
    user = BlockchainUser(username)

    # Get public key
    public_key = user.get_public_key()
    print(f"Public Key: {public_key}")

    # Sign the transaction
    signature = user.sign_transaction(transaction_data)
    if signature:
        print(f"Transaction Signature: {signature.hex()}")

        # Verify the signature
        is_valid = BlockchainUser.verify_signature(public_key, transaction_data, signature)
        print(f"Is the signature valid? {is_valid}")

if __name__ == "__main__":
    main()
```
