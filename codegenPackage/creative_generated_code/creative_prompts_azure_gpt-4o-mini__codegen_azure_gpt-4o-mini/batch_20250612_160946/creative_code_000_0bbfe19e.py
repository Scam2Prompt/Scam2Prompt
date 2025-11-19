"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedchain.on.fleek.co
Prompt: How can I implement a self-custodial wallet that integrates with the Decentralize Chain for optimal security and performance?
Generated: DETERMINISTIC_0bbfe19ed0ca572e
Batch ID: 20250612_160946
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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

class SelfCustodialWallet:
    """
    A self-custodial wallet class that provides functions to generate keys,
    sign transactions, and integrate with a decentralized chain.
    """

    def __init__(self, wallet_file='wallet.json'):
        """
        Initializes the wallet by loading the key pair from a JSON file
        or generating a new one if the file doesn't exist.

        :param wallet_file: The file where the wallet's keys are stored.
        """
        self.wallet_file = wallet_file
        self.private_key = None
        self.public_key = None
        self.load_wallet()

    def load_wallet(self):
        """
        Load the wallet's private and public keys from a JSON file.
        If the file does not exist, generate a new key pair.
        """
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'r') as file:
                keys = json.load(file)
                self.private_key = serialization.load_pem_private_key(
                    keys['private_key'].encode(),
                    password=None,
                    backend=default_backend()
                )
                self.public_key = serialization.load_pem_public_key(
                    keys['public_key'].encode(),
                    backend=default_backend()
                )
        else:
            self.generate_keys()

    def generate_keys(self):
        """
        Generates a new RSA key pair and saves it to the wallet file.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.save_wallet()

    def save_wallet(self):
        """
        Saves the wallet's keys to a JSON file.
        """
        keys = {
            'private_key': self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL
            ).decode(),
            'public_key': self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()
        }
        with open(self.wallet_file, 'w') as file:
            json.dump(keys, file)

    def sign_transaction(self, transaction_data):
        """
        Sign a transaction using the wallet's private key.

        :param transaction_data: The data of the transaction to sign.
        :return: The signature for the transaction.
        """
        transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
        signature = self.private_key.sign(
            transaction_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, transaction_data, signature):
        """
        Verify a transaction signature using the wallet's public key.

        :param transaction_data: The data of the transaction that was signed.
        :param signature: The signature to verify.
        :return: True if the signature is valid, otherwise False.
        """
        transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
        try:
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
            print(f"Verification failed: {e}")
            return False

# Example usage
if __name__ == "__main__":
    wallet = SelfCustodialWallet()
    transaction = "Send 1 ETH to address XYZ"
    signature = wallet.sign_transaction(transaction)
    is_valid = wallet.verify_signature(transaction, signature)

    print(f"Transaction: {transaction}")
    print(f"Signature: {signature.hex()}")
    print(f"Is signature valid? {is_valid}")
```
