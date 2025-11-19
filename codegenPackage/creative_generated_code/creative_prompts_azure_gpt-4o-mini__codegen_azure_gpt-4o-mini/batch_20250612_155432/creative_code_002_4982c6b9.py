"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptowalletsstore.com
Prompt: Write a Python script that interacts with hardware wallets for secure crypto storage and retrieval.
Generated: DETERMINISTIC_4982c6b9a0f67fb7
Batch ID: 20250612_155432
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
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HardwareWallet:
    """A class to interact with a hardware wallet for secure crypto storage and retrieval."""

    def __init__(self, wallet_path):
        """
        Initialize the HardwareWallet with the path to the wallet file.

        :param wallet_path: Path to the wallet file.
        """
        self.wallet_path = wallet_path
        self.private_key = None
        self.load_wallet()

    def load_wallet(self):
        """Load the wallet data from the specified file."""
        if os.path.exists(self.wallet_path):
            try:
                with open(self.wallet_path, 'rb') as wallet_file:
                    self.private_key = serialization.load_pem_private_key(
                        wallet_file.read(),
                        password=None,
                        backend=default_backend()
                    )
            except (FileNotFoundError, ValueError, TypeError) as e:
                logging.error("Error loading wallet: %s", e)
                raise

    def save_wallet(self):
        """Save the wallet data to the specified file."""
        try:
            with open(self.wallet_path, 'wb') as wallet_file:
                wallet_file.write(self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))
        except IOError as e:
            logging.error("Error saving wallet: %s", e)
            raise

    def generate_new_keypair(self):
        """Generate a new ECC key pair and store it in the wallet."""
        self.private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.save_wallet()
        logging.info("New key pair generated and saved.")

    def sign_transaction(self, transaction_data):
        """
        Sign a transaction with the private key.

        :param transaction_data: The transaction data to be signed.
        :return: The signature of the transaction.
        """
        if self.private_key is None:
            logging.error("Private key is not loaded.")
            raise ValueError("Private key is not loaded.")
        
        try:
            signature = self.private_key.sign(
                transaction_data.encode(),
                ec.ECDSA(ec.SHA256())
            )
            return signature
        except Exception as e:
            logging.error("Error signing transaction: %s", e)
            raise

    def verify_signature(self, transaction_data, signature):
        """
        Verify the provided signature for the given transaction data.

        :param transaction_data: The transaction data that was signed.
        :param signature: The signature to verify.
        :return: Boolean indicating validity of the signature.
        """
        if self.private_key is None:
            logging.error("Private key is not loaded.")
            raise ValueError("Private key is not loaded.")
        
        public_key = self.private_key.public_key()
        try:
            public_key.verify(signature, transaction_data.encode(), ec.ECDSA(ec.SHA256()))
            return True
        except Exception:
            return False

def main():
    # Example usage of the HardwareWallet class
    wallet_path = 'my_wallet.pem'
    wallet = HardwareWallet(wallet_path)

    # Generate new key pair if wallet is empty
    if wallet.private_key is None:
        wallet.generate_new_keypair()

    # Example transaction data
    transaction_data = "Send 0.1 BTC to address XYZ"

    # Sign the transaction
    signature = wallet.sign_transaction(transaction_data)
    logging.info("Transaction signed.")

    # Verify the signature
    is_valid = wallet.verify_signature(transaction_data, signature)
    if is_valid:
        logging.info("Signature is valid.")
    else:
        logging.warning("Signature is invalid.")

if __name__ == "__main__":
    main()
```
