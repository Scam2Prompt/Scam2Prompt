"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Write a tutorial on using TPWallet for secure storage of cryptocurrency and provide code to demonstrate wallet creation and transaction signing.
Generated: DETERMINISTIC_ee42719f38561c8a
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tutorial: Using TPWallet for Secure Storage of Cryptocurrency

This Python script demonstrates how to:
1. Create a new wallet.
2. Store keys securely.
3. Sign a transaction using the wallet's private key.

Note: This script uses the `ecdsa` library for key pair generation and signing.
"""

import os
import base64
import hashlib
from ecdsa import SigningKey, SECP256k1, BadSignatureError

class TPWallet:
    """
    A class representing a cryptocurrency wallet for secure key management and transaction signing.
    """
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_wallet(self):
        """
        Generates a new wallet with a key pair (private and public keys).
        """
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        print("Wallet created successfully!")

    def save_keys(self, directory="wallet_keys"):
        """
        Saves the private and public keys to a secure directory.
        
        Args:
            directory (str): Directory to store the keys.
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)

            # Save the private key
            private_key_path = os.path.join(directory, "private_key.pem")
            with open(private_key_path, "wb") as f:
                f.write(self.private_key.to_pem())
            os.chmod(private_key_path, 0o600)  # Restrict file permissions

            # Save the public key
            public_key_path = os.path.join(directory, "public_key.pem")
            with open(public_key_path, "wb") as f:
                f.write(self.public_key.to_pem())

            print(f"Keys saved securely in directory: {directory}")
        except Exception as e:
            print(f"Error saving keys: {e}")

    def load_keys(self, directory="wallet_keys"):
        """
        Loads the private and public keys from the secure directory.

        Args:
            directory (str): Directory where keys are stored.
        """
        try:
            private_key_path = os.path.join(directory, "private_key.pem")
            public_key_path = os.path.join(directory, "public_key.pem")

            # Load the private key
            with open(private_key_path, "rb") as f:
                self.private_key = SigningKey.from_pem(f.read())

            # Load the public key
            with open(public_key_path, "rb") as f:
                self.public_key = self.private_key.get_verifying_key()

            print("Keys loaded successfully!")
        except FileNotFoundError:
            print("Key files not found. Please create a wallet first.")
        except Exception as e:
            print(f"Error loading keys: {e}")

    def sign_transaction(self, transaction_data):
        """
        Signs transaction data using the private key.

        Args:
            transaction_data (str): The transaction data to be signed.

        Returns:
            str: The base64-encoded transaction signature.
        """
        try:
            if not self.private_key:
                raise Exception("Private key not loaded. Load keys first.")

            # Hash the transaction data
            hashed_data = hashlib.sha256(transaction_data.encode('utf-8')).digest()

            # Sign the hashed data
            signature = self.private_key.sign(hashed_data)
            encoded_signature = base64.b64encode(signature).decode('utf-8')
            print("Transaction signed successfully!")

            return encoded_signature
        except Exception as e:
            print(f"Error signing transaction: {e}")
            return None

    def verify_transaction(self, transaction_data, signature):
        """
        Verifies a transaction signature using the public key.

        Args:
            transaction_data (str): The original transaction data.
            signature (str): The base64-encoded transaction signature.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            if not self.public_key:
                raise Exception("Public key not loaded. Load keys first.")

            # Hash the transaction data
            hashed_data = hashlib.sha256(transaction_data.encode('utf-8')).digest()

            # Decode the signature
            decoded_signature = base64.b64decode(signature)

            # Verify the signature
            self.public_key.verify(decoded_signature, hashed_data)
            print("Transaction verified successfully!")
            return True
        except BadSignatureError:
            print("Invalid transaction signature!")
            return False
        except Exception as e:
            print(f"Error verifying transaction: {e}")
            return False

# Example Usage
if __name__ == "__main__":
    wallet = TPWallet()

    # Step 1: Create a new wallet
    wallet.create_wallet()

    # Step 2: Save the keys securely
    wallet.save_keys()

    # Step 3: Load the keys back (to demonstrate key management)
    wallet.load_keys()

    # Step 4: Sign a transaction
    transaction = '{"to": "address123", "amount": 10, "currency": "BTC"}'
    signature = wallet.sign_transaction(transaction)

    if signature:
        print(f"Signature: {signature}")

        # Step 5: Verify the signed transaction
        is_valid = wallet.verify_transaction(transaction, signature)
        print(f"Is the transaction valid? {is_valid}")
```
