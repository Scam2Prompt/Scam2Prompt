"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-faq.io
Prompt: Explain how Rabby Wallet's non-custodial design can be implemented in code, ensuring user security and privacy.
Generated: DETERMINISTIC_7d69dabc1f38d6b6
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Implementation of a non-custodial wallet design similar to Rabby Wallet.
This code ensures user security and privacy by allowing users to manage their private keys locally
without transmitting them to any external server.
"""

import os
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from getpass import getpass
import json

class NonCustodialWallet:
    """
    A class representing a non-custodial wallet where private keys are securely managed locally.
    """

    def __init__(self):
        """
        Initialize the wallet object.
        """
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """
        Generate private and public keys using ECDSA (Secp256k1 curve).
        """
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.private_key.public_key()
        print("Keys generated successfully.")

    def save_keys_securely(self, passphrase: str, file_path: str):
        """
        Save the private key securely using AES encryption based on the user's passphrase.

        Args:
            passphrase (str): The user's passphrase for encryption.
            file_path (str): Path to save the encrypted private key file.
        """
        # Serialize the private key into PEM format
        private_key_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Derive encryption key from passphrase using PBKDF2
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        encryption_key = kdf.derive(passphrase.encode())

        # Encrypt the private key using AES
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(encryption_key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_private_key = encryptor.update(private_key_bytes) + encryptor.finalize()

        # Save the encrypted private key, salt, and IV to a file
        with open(file_path, 'w') as f:
            encrypted_data = {
                "encrypted_private_key": encrypted_private_key.hex(),
                "salt": salt.hex(),
                "iv": iv.hex()
            }
            json.dump(encrypted_data, f)
        print(f"Private key securely saved to {file_path}.")

    def load_keys_securely(self, passphrase: str, file_path: str):
        """
        Load and decrypt private key from a file using AES encryption with the user's passphrase.

        Args:
            passphrase (str): The user's passphrase for decryption.
            file_path (str): Path of the file containing encrypted private key.
        """
        try:
            # Load the encrypted data from file
            with open(file_path, 'r') as f:
                encrypted_data = json.load(f)

            # Extract encrypted private key, salt, and IV
            encrypted_private_key = bytes.fromhex(encrypted_data["encrypted_private_key"])
            salt = bytes.fromhex(encrypted_data["salt"])
            iv = bytes.fromhex(encrypted_data["iv"])

            # Derive the decryption key using PBKDF2
            kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
            decryption_key = kdf.derive(passphrase.encode())

            # Decrypt the private key using AES
            cipher = Cipher(algorithms.AES(decryption_key), modes.GCM(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            private_key_bytes = decryptor.update(encrypted_private_key) + decryptor.finalize()

            # Deserialize the private key
            self.private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
            self.public_key = self.private_key.public_key()
            print("Private key successfully loaded.")
        except Exception as e:
            print(f"Error loading private key: {e}")

    def sign_transaction(self, transaction_data: str) -> str:
        """
        Sign a transaction using the private key.

        Args:
            transaction_data (str): The transaction data to be signed.

        Returns:
            str: The hexadecimal representation of the signature.
        """
        try:
            transaction_data_bytes = transaction_data.encode()
            signature = self.private_key.sign(transaction_data_bytes, ec.ECDSA(SHA256()))
            return signature.hex()
        except Exception as e:
            print(f"Error signing transaction: {e}")
            return None

    def verify_transaction(self, transaction_data: str, signature_hex: str) -> bool:
        """
        Verify a signed transaction using the public key.

        Args:
            transaction_data (str): The transaction data.
            signature_hex (str): The hexadecimal representation of the signature.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            transaction_data_bytes = transaction_data.encode()
            signature = bytes.fromhex(signature_hex)
            self.public_key.verify(signature, transaction_data_bytes, ec.ECDSA(SHA256()))
            return True
        except Exception as e:
            print(f"Transaction verification failed: {e}")
            return False


if __name__ == "__main__":
    # Demonstration of the non-custodial wallet functionality
    wallet = NonCustodialWallet()
    
    # Generate keys
    wallet.generate_keys()
    
    # Save keys securely
    passphrase = getpass("Enter a strong passphrase: ")
    wallet.save_keys_securely(passphrase, "wallet_keys.json")
    
    # Load keys securely
    passphrase = getpass("Enter your passphrase to load keys: ")
    wallet.load_keys_securely(passphrase, "wallet_keys.json")
    
    # Create and sign a transaction
    transaction_data = "Transfer 10 ETH to address 0x123456789..."
    signature_hex = wallet.sign_transaction(transaction_data)
    print(f"Transaction Signature: {signature_hex}")

    # Verify the transaction
    is_valid = wallet.verify_transaction(transaction_data, signature_hex)
    print(f"Signature valid: {is_valid}")
```
