"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale.seesawprotocol.io
Prompt: Provide a code example for creating a non-custodial wallet that allows users to manage their private keys securely.
Generated: DETERMINISTIC_d5d71d8158191d9e
Batch ID: 20250612_164223
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
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class NonCustodialWallet:
    def __init__(self, wallet_file='wallet.json'):
        """
        Initializes the NonCustodialWallet instance.

        :param wallet_file: The filename where the wallet will be stored.
        """
        self.wallet_file = wallet_file
        self.private_key = None
        self.public_key = None

        # Load existing wallet data if available
        self.load_wallet()

    def generate_keys(self):
        """
        Generates a new RSA key pair and stores it in the wallet.
        """
        try:
            # Generate a new RSA private key
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            self.public_key = self.private_key.public_key()

            # Save the keys to the wallet
            self.save_wallet()
        except Exception as e:
            print(f"Error generating keys: {e}")

    def save_wallet(self):
        """
        Saves the wallet data (private and public keys) to a JSON file.
        """
        try:
            if self.private_key is None or self.public_key is None:
                raise ValueError("Keys must be generated before saving.")

            wallet_data = {
                'private_key': base64.b64encode(self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL
                )).decode('utf-8'),
                'public_key': base64.b64encode(self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )).decode('utf-8')
            }

            with open(self.wallet_file, 'w') as f:
                json.dump(wallet_data, f)
        except Exception as e:
            print(f"Error saving wallet: {e}")

    def load_wallet(self):
        """
        Loads the wallet data from a JSON file.
        """
        try:
            if os.path.exists(self.wallet_file):
                with open(self.wallet_file, 'r') as f:
                    wallet_data = json.load(f)
                    self.private_key = serialization.load_pem_private_key(
                        base64.b64decode(wallet_data['private_key']),
                        password=None,
                        backend=default_backend()
                    )
                    self.public_key = serialization.load_pem_public_key(
                        base64.b64decode(wallet_data['public_key']),
                        backend=default_backend()
                    )
                print("Wallet loaded successfully.")
            else:
                print("No existing wallet found. Please generate keys.")
        except Exception as e:
            print(f"Error loading wallet: {e}")

    def delete_wallet(self):
        """
        Deletes the wallet file from the filesystem.
        """
        try:
            if os.path.exists(self.wallet_file):
                os.remove(self.wallet_file)
                self.private_key = None
                self.public_key = None
                print("Wallet deleted successfully.")
            else:
                print("No wallet file to delete.")
        except Exception as e:
            print(f"Error deleting wallet: {e}")

# Example of usage
if __name__ == "__main__":
    wallet = NonCustodialWallet()
    wallet.generate_keys()  # Generates a new wallet or loads existing
    # To delete the wallet, uncomment the line below
    # wallet.delete_wallet()
```
