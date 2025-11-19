"""
Generated Code Metadata:
========================
Original URL: https://snso.com.cn
Prompt: How can TPWallet help developers create secure wallet solutions for Web3 environments?
Generated: DETERMINISTIC_0441568b6d25d2f0
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class TPWallet:
    """
    A class to represent a secure wallet solution for Web3 environments.
    """

    def __init__(self):
        """
        Initializes a new TPWallet instance with a generated RSA key pair.
        """
        self.private_key = self.generate_private_key()
        self.public_key = self.private_key.public_key()

    def generate_private_key(self):
        """
        Generates a new RSA private key.

        Returns:
            rsa.RSAPrivateKey: The generated private key.
        """
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

    def save_keys(self, private_key_path: str, public_key_path: str):
        """
        Saves the private and public keys to specified file paths.

        Args:
            private_key_path (str): The file path to save the private key.
            public_key_path (str): The file path to save the public key.
        """
        try:
            # Save the private key
            with open(private_key_path, "wb") as private_file:
                private_file.write(
                    self.private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                    )
                )

            # Save the public key
            with open(public_key_path, "wb") as public_file:
                public_file.write(
                    self.public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as e:
            print(f"Error saving keys: {e}")

    def load_private_key(self, private_key_path: str):
        """
        Loads a private key from a specified file path.

        Args:
            private_key_path (str): The file path to load the private key.

        Returns:
            rsa.RSAPrivateKey: The loaded private key.
        """
        try:
            with open(private_key_path, "rb") as private_file:
                private_key = serialization.load_pem_private_key(
                    private_file.read(),
                    password=None,
                    backend=default_backend()
                )
            return private_key
        except Exception as e:
            print(f"Error loading private key: {e}")
            return None

    def sign_transaction(self, transaction_data: dict) -> bytes:
        """
        Signs a transaction using the private key.

        Args:
            transaction_data (dict): The transaction data to sign.

        Returns:
            bytes: The signature of the transaction.
        """
        try:
            # Convert transaction data to JSON string and hash it
            transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
            transaction_hash = hashlib.sha256(transaction_json).digest()

            # Sign the transaction hash
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

    def verify_signature(self, transaction_data: dict, signature: bytes) -> bool:
        """
        Verifies the signature of a transaction.

        Args:
            transaction_data (dict): The transaction data that was signed.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            # Convert transaction data to JSON string and hash it
            transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
            transaction_hash = hashlib.sha256(transaction_json).digest()

            # Verify the signature
            self.public_key.verify(
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
            print(f"Error verifying signature: {e}")
            return False

# Example usage
if __name__ == "__main__":
    wallet = TPWallet()
    wallet.save_keys("private_key.pem", "public_key.pem")

    transaction = {"from": "address1", "to": "address2", "amount": 100}
    signature = wallet.sign_transaction(transaction)

    is_valid = wallet.verify_signature(transaction, signature)
    print(f"Is the signature valid? {is_valid}")
```
