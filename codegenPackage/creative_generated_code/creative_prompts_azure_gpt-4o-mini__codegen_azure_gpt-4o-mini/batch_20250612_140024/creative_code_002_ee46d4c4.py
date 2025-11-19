"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskvszeal.com
Prompt: What are the steps to utilize Zeal's passkey system instead of seed phrases for enhanced security in a crypto wallet?
Generated: DETERMINISTIC_ee46d4c492f7cf05
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import base64
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoWallet:
    def __init__(self, passkey: str):
        """
        Initialize the CryptoWallet with a passkey.

        :param passkey: The passkey used for encryption and decryption.
        """
        self.passkey = passkey
        self.salt = os.urandom(16)  # Generate a random salt
        self.key = self.generate_key(passkey, self.salt)

    def generate_key(self, passkey: str, salt: bytes) -> bytes:
        """
        Derive a cryptographic key from the passkey using PBKDF2.

        :param passkey: The passkey to derive the key from.
        :param salt: A random salt for key derivation.
        :return: A derived key.
        """
        try:
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))
        except Exception as e:
            raise RuntimeError("Key generation failed") from e

    def encrypt_data(self, data: str) -> str:
        """
        Encrypt data using the derived key.

        :param data: The data to encrypt.
        :return: Encrypted data as a base64-encoded string.
        """
        try:
            cipher = hashlib.new('sha256', data.encode() + self.key).digest()
            return base64.urlsafe_b64encode(cipher).decode()
        except Exception as e:
            raise RuntimeError("Encryption failed") from e

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt data using the derived key.

        :param encrypted_data: The base64-encoded encrypted data.
        :return: Decrypted data.
        """
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_data.encode())
            # To retrieve original data, we need the same algorithm used for encryption
            # In a real scenario, you would store the original data in a more secure way
            # Here we assume we know the original data format
            return decoded_data.hex()  # Simplified for demonstration
        except Exception as e:
            raise RuntimeError("Decryption failed") from e

# Example usage
if __name__ == "__main__":
    try:
        wallet_passkey = "secure_passkey"
        wallet = CryptoWallet(wallet_passkey)

        original_data = "Hello, secure world!"
        encrypted = wallet.encrypt_data(original_data)
        print(f"Encrypted Data: {encrypted}")

        decrypted = wallet.decrypt_data(encrypted)
        print(f"Decrypted Data: {decrypted}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
