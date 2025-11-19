"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: How can TPWallet help developers create secure wallet solutions for Web3 environments?
Generated: DETERMINISTIC_0441568b6d25d2f0
Batch ID: 20250612_163835
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
import hashlib
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

class TPWallet:
    """
    TPWallet class to handle secure wallet solutions for Web3 environments.
    This class provides functionalities to create a wallet, sign transactions,
    and verify signatures.
    """

    def __init__(self, wallet_name):
        """
        Initializes the TPWallet with a name and generates a new RSA key pair.

        Args:
            wallet_name (str): The name of the wallet.
        """
        self.wallet_name = wallet_name
        self.private_key = self.generate_private_key()
        self.public_key = self.private_key.public_key()
        self.save_wallet()

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

    def save_wallet(self):
        """
        Saves the wallet's keys to a file in a secure format.
        """
        try:
            # Create a directory for wallets if it doesn't exist
            os.makedirs('wallets', exist_ok=True)
            
            # Save the private key
            private_key_bytes = self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
            )
            with open(f'wallets/{self.wallet_name}_private_key.pem', 'wb') as f:
                f.write(private_key_bytes)

            # Save the public key
            public_key_bytes = self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            with open(f'wallets/{self.wallet_name}_public_key.pem', 'wb') as f:
                f.write(public_key_bytes)
        except Exception as e:
            print(f"Error saving wallet: {e}")

    def sign_transaction(self, transaction_data):
        """
        Signs a transaction with the private key.

        Args:
            transaction_data (str): The transaction data to sign.

        Returns:
            bytes: The digital signature of the transaction.
        """
        try:
            # Hash the transaction data
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
            # Sign the hashed transaction
            signature = self.private_key.sign(
                transaction_hash,
                padding=rsa.PSS(mgf=rsa.MGF1(hashes.SHA256()), salt_length=rsa.PSS.MAX_LENGTH),
                algorithm=hashes.SHA256()
            )
            return signature
        except Exception as e:
            print(f"Error signing transaction: {e}")

    def verify_signature(self, transaction_data, signature):
        """
        Verifies a signature using the public key.

        Args:
            transaction_data (str): The original transaction data.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            # Hash the transaction data
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
            # Verify the signature
            self.public_key.verify(
                signature,
                transaction_hash,
                padding=rsa.PSS(mgf=rsa.MGF1(hashes.SHA256()), salt_length=rsa.PSS.MAX_LENGTH),
                algorithm=hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            print(f"Error verifying signature: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create a wallet
    wallet = TPWallet(wallet_name="MyWallet")

    # Sample transaction data
    transaction = "Transfer 10 tokens to address 0x1234567890abcdef"

    # Sign the transaction
    signature = wallet.sign_transaction(transaction)

    # Verify the signature
    is_valid = wallet.verify_signature(transaction, signature)
    print(f"Is the signature valid? {is_valid}")
```
