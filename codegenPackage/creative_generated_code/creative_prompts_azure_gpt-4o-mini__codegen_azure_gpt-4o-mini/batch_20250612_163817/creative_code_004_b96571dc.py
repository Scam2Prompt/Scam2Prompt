"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pocketuniverseshield.com
Prompt: Describe how to use advanced encryption for transactions in a blockchain application, based on Pocket Universe Shield's recommendations.
Generated: DETERMINISTIC_b96571dcb0f4ea9a
Batch ID: 20250612_163817
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
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

class BlockchainTransaction:
    def __init__(self, sender_private_key=None, sender_public_key=None):
        """
        Initializes the BlockchainTransaction with optional sender keys.
        Generates new keys if not provided.
        """
        if sender_private_key and sender_public_key:
            self.sender_private_key = serialization.load_pem_private_key(
                sender_private_key,
                password=None,
                backend=default_backend()
            )
            self.sender_public_key = serialization.load_pem_public_key(
                sender_public_key,
                backend=default_backend()
            )
        else:
            # Generate new RSA keys
            self.sender_private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            self.sender_public_key = self.sender_private_key.public_key()

    def sign_transaction(self, transaction_data):
        """
        Signs the transaction data using the sender's private key.
        
        Parameters:
            transaction_data (str): The transaction data to be signed.

        Returns:
            bytes: The digital signature.
        """
        try:
            signature = self.sender_private_key.sign(
                transaction_data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            raise RuntimeError("Failed to sign the transaction") from e

    def verify_signature(self, transaction_data, signature):
        """
        Verifies the transaction signature using the sender's public key.

        Parameters:
            transaction_data (str): The signed transaction data.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            self.sender_public_key.verify(
                signature,
                transaction_data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

    def export_private_key(self):
        """
        Exports the sender's private key as PEM formatted bytes.
        
        Returns:
            bytes: The private key in PEM format.
        """
        return self.sender_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL
        )

    def export_public_key(self):
        """
        Exports the sender's public key as PEM formatted bytes.

        Returns:
            bytes: The public key in PEM format.
        """
        return self.sender_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

# Example usage
if __name__ == "__main__":
    transaction_data = "Transaction details: Amount 100, From User A, To User B"

    # Create a new blockchain transaction instance
    transaction = BlockchainTransaction()

    # Sign the transaction
    signature = transaction.sign_transaction(transaction_data)
    print("Signature:", signature)

    # Verify the transaction
    is_valid = transaction.verify_signature(transaction_data, signature)
    print("Is the signature valid?", is_valid)

    # Export keys
    private_key_pem = transaction.export_private_key()
    public_key_pem = transaction.export_public_key()
    print("Private Key:", private_key_pem.decode())
    print("Public Key:", public_key_pem.decode())
```
