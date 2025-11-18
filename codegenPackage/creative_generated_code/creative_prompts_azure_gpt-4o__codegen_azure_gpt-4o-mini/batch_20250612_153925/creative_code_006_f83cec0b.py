"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atomic-wallet.fr
Prompt: Generate code to securely manage private keys for a crypto wallet, ensuring compatibility with Atomic Wallet's decentralized architecture.
Generated: DETERMINISTIC_f83cec0b1ffcd7e9
Batch ID: 20250612_153925
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
import hashlib
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature

class CryptoWallet:
    def __init__(self, wallet_file='wallet.json'):
        """
        Initializes the CryptoWallet instance.

        :param wallet_file: The path to the wallet file where private keys will be stored.
        """
        self.wallet_file = wallet_file
        self.private_key = None
        self.load_wallet()

    def generate_private_key(self):
        """
        Generates a new RSA private key and saves it to the wallet file.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.save_wallet()

    def save_wallet(self):
        """
        Saves the private key to the wallet file in a secure manner.
        """
        key_data = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
        )
        with open(self.wallet_file, 'wb') as f:
            f.write(key_data)

    def load_wallet(self):
        """
        Loads the private key from the wallet file if it exists.
        """
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'rb') as f:
                key_data = f.read()
                self.private_key = serialization.load_pem_private_key(
                    key_data,
                    password=None,
                    backend=default_backend()
                )
        else:
            raise FileNotFoundError("Wallet file not found.")

    def sign_transaction(self, transaction_data):
        """
        Signs a transaction with the private key to ensure authenticity.

        :param transaction_data: The data of the transaction to sign.
        :return: The signature of the transaction.
        """
        if not self.private_key:
            raise ValueError("Private key is not loaded.")
        
        signature = self.private_key.sign(
            transaction_data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode('utf-8')

    def verify_transaction(self, transaction_data, signature):
        """
        Verifies a transaction signature against the public key derived from the private key.

        :param transaction_data: The original transaction data.
        :param signature: The signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
        if not self.private_key:
            raise ValueError("Private key is not loaded.")
        
        public_key = self.private_key.public_key()
        signature_bytes = base64.b64decode(signature)

        try:
            public_key.verify(
                signature_bytes,
                transaction_data.encode('utf-8'),
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
    # Example usage
    wallet = CryptoWallet()
    
    # Generate a new private key
    wallet.generate_private_key()
    
    # Sample transaction data
    transaction_data = json.dumps({"amount": 100, "to": "address123"})

    # Sign the transaction
    signature = wallet.sign_transaction(transaction_data)
    print("Transaction Signature:", signature)

    # Verify the transaction
    is_valid = wallet.verify_transaction(transaction_data, signature)
    print("Is the signature valid?", is_valid)
```
