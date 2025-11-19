"""
Generated Code Metadata:
========================
Original URL: https://caae533f.smart-token-tool-7er.pages.dev
Prompt: "What are the best practices for securing a smart token tool and its interactions with blockchain networks?"
Generated: DETERMINISTIC_6a5ac1cd26c7f74f
Batch ID: 20250622_211357
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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class SmartTokenTool:
    def __init__(self):
        """Initialize the SmartTokenTool with a private and public key."""
        self.private_key = self.generate_private_key()
        self.public_key = self.private_key.public_key()

    def generate_private_key(self):
        """Generate a new RSA private key."""
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

    def sign_transaction(self, transaction_data):
        """Sign a transaction using the private key.

        Args:
            transaction_data (dict): The transaction data to sign.

        Returns:
            str: The signature of the transaction.
        """
        # Serialize the transaction data to JSON
        transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
        # Create a signature
        signature = self.private_key.sign(
            transaction_json,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature.hex()

    def verify_transaction(self, transaction_data, signature):
        """Verify a signed transaction using the public key.

        Args:
            transaction_data (dict): The original transaction data.
            signature (str): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        transaction_json = json.dumps(transaction_data, sort_keys=True).encode()
        signature_bytes = bytes.fromhex(signature)

        try:
            self.public_key.verify(
                signature_bytes,
                transaction_json,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def encrypt_data(self, data):
        """Encrypt data using the public key.

        Args:
            data (str): The data to encrypt.

        Returns:
            bytes: The encrypted data.
        """
        return self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt_data(self, encrypted_data):
        """Decrypt data using the private key.

        Args:
            encrypted_data (bytes): The data to decrypt.

        Returns:
            str: The decrypted data.
        """
        return self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    def save_keys(self, private_key_path, public_key_path):
        """Save the private and public keys to files.

        Args:
            private_key_path (str): The file path to save the private key.
            public_key_path (str): The file path to save the public key.
        """
        # Save the private key
        with open(private_key_path, 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
            ))

        # Save the public key
        with open(public_key_path, 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            ))

    def load_keys(self, private_key_path, public_key_path):
        """Load the private and public keys from files.

        Args:
            private_key_path (str): The file path to load the private key.
            public_key_path (str): The file path to load the public key.
        """
        # Load the private key
        with open(private_key_path, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        # Load the public key
        with open(public_key_path, 'rb') as f:
            self.public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

# Example usage
if __name__ == "__main__":
    tool = SmartTokenTool()
    transaction = {"from": "address1", "to": "address2", "amount": 100}
    
    # Sign the transaction
    signature = tool.sign_transaction(transaction)
    print("Signature:", signature)

    # Verify the transaction
    is_valid = tool.verify_transaction(transaction, signature)
    print("Is the signature valid?", is_valid)

    # Encrypt and decrypt data
    encrypted_data = tool.encrypt_data("Sensitive data")
    print("Encrypted data:", encrypted_data)

    decrypted_data = tool.decrypt_data(encrypted_data)
    print("Decrypted data:", decrypted_data)

    # Save and load keys
    tool.save_keys("private_key.pem", "public_key.pem")
    tool.load_keys("private_key.pem", "public_key.pem")
```
