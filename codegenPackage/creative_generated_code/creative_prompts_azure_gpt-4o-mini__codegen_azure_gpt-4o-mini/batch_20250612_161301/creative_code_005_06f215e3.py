"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtokens.web.app
Prompt: What security measures are in place for $SMOG token transactions, and how can I protect my private keys?
Generated: DETERMINISTIC_06f215e3ff9d81da
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature

class TokenSecurity:
    """
    A class to manage security measures for $SMOG token transactions,
    including key generation, storage, and transaction signing.
    """

    def __init__(self, key_file='private_key.pem'):
        """
        Initializes the TokenSecurity class.

        Args:
            key_file (str): Path to the private key file.
        """
        self.key_file = key_file
        self.private_key = self.load_private_key()

    def generate_private_key(self):
        """Generates a new RSA private key and saves it to a file."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        with open(self.key_file, 'wb') as key_file:
            key_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        return private_key

    def load_private_key(self):
        """Loads the private key from the specified key file.

        Returns:
            Private key object or None if the file does not exist.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
        else:
            print("Private key file not found. Generating a new one.")
            return self.generate_private_key()

    def sign_transaction(self, transaction_data):
        """
        Signs a transaction using the private key.

        Args:
            transaction_data (str): The transaction data to sign.

        Returns:
            bytes: The signature for the transaction.
        """
        if not self.private_key:
            raise ValueError("Private key is not loaded.")
        
        signature = self.private_key.sign(
            transaction_data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, transaction_data, signature):
        """
        Verifies a transaction signature.

        Args:
            transaction_data (str): The transaction data that was signed.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        public_key = self.private_key.public_key()
        try:
            public_key.verify(
                signature,
                transaction_data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False


# Example usage
if __name__ == "__main__":
    security = TokenSecurity()
    transaction_data = json.dumps({"amount": 100, "to": "recipient_address"})
    
    # Sign the transaction
    signature = security.sign_transaction(transaction_data)
    print("Transaction Signature:", signature)

    # Verify the signature
    is_valid = security.verify_signature(transaction_data, signature)
    print("Is the signature valid?", is_valid)
```
