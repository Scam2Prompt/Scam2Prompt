"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gasprofitsoftware.com
Prompt: Suggest APIs or frameworks for implementing self-custody of assets in a decentralized finance system, ensuring enhanced security with cryptography, similar to Gas Profit.
Generated: DETERMINISTIC_5f8d780a27b8f816
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class SelfCustodyWallet:
    """
    A class to represent a self-custody wallet for decentralized finance.
    It uses RSA encryption for secure key management.
    """

    def __init__(self, wallet_file='wallet.json'):
        """
        Initializes the wallet by loading or creating a new wallet.
        
        Args:
            wallet_file (str): Path to the wallet file.
        """
        self.wallet_file = wallet_file
        self.private_key = None
        self.public_key = None
        self.load_wallet()

    def generate_keys(self):
        """Generates a new RSA key pair and saves it to the wallet file."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.save_wallet()

    def save_wallet(self):
        """Saves the wallet's private and public keys to a JSON file."""
        try:
            with open(self.wallet_file, 'w') as file:
                keys = {
                    'private_key': self.private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL
                    ).decode('utf-8'),
                    'public_key': self.public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo
                    ).decode('utf-8')
                }
                json.dump(keys, file)
        except Exception as e:
            print(f"Error saving wallet: {e}")

    def load_wallet(self):
        """Loads the wallet's keys from the JSON file if it exists."""
        if os.path.exists(self.wallet_file):
            try:
                with open(self.wallet_file, 'r') as file:
                    keys = json.load(file)
                    self.private_key = serialization.load_pem_private_key(
                        keys['private_key'].encode('utf-8'),
                        password=None,
                        backend=default_backend()
                    )
                    self.public_key = serialization.load_pem_public_key(
                        keys['public_key'].encode('utf-8'),
                        backend=default_backend()
                    )
            except Exception as e:
                print(f"Error loading wallet: {e}")

    def sign_message(self, message):
        """
        Signs a message using the wallet's private key.
        
        Args:
            message (str): The message to sign.
        
        Returns:
            bytes: The signature of the message.
        """
        try:
            signature = self.private_key.sign(
                message.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            print(f"Error signing message: {e}")

    def verify_signature(self, message, signature):
        """
        Verifies the signature of a message using the wallet's public key.
        
        Args:
            message (str): The original message.
            signature (bytes): The signature to verify.
        
        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            self.public_key.verify(
                signature,
                message.encode('utf-8'),
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

if __name__ == "__main__":
    # Example usage of the SelfCustodyWallet class
    wallet = SelfCustodyWallet()
    if not wallet.private_key or not wallet.public_key:
        wallet.generate_keys()

    message = "This is a secure message."
    signature = wallet.sign_message(message)

    print("Signature:", signature)

    is_valid = wallet.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)
```
