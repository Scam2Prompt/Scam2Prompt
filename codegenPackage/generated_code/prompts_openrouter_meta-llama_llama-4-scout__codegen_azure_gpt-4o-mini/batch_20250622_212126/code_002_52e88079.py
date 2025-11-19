"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Generate code that demonstrates how to use a specific encryption technique, potentially involving base64 encoding and decoding, as suggested by the webpage's text.
Generated: DETERMINISTIC_52e88079aed13216
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import base64
from cryptography.fernet import Fernet
import os

class EncryptionUtility:
    def __init__(self):
        # Generate a key for encryption and decryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using Fernet symmetric encryption.

        Args:
            plaintext (str): The text to be encrypted.

        Returns:
            str: The base64 encoded encrypted text.
        """
        try:
            # Convert plaintext to bytes
            plaintext_bytes = plaintext.encode('utf-8')
            # Encrypt the plaintext
            encrypted_bytes = self.cipher.encrypt(plaintext_bytes)
            # Encode the encrypted bytes to base64
            encrypted_base64 = base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')
            return encrypted_base64
        except Exception as e:
            print(f"Error during encryption: {e}")
            return None

    def decrypt(self, encrypted_base64: str) -> str:
        """
        Decrypts the given base64 encoded encrypted text.

        Args:
            encrypted_base64 (str): The base64 encoded encrypted text.

        Returns:
            str: The decrypted plaintext.
        """
        try:
            # Decode the base64 encoded string
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_base64)
            # Decrypt the bytes
            decrypted_bytes = self.cipher.decrypt(encrypted_bytes)
            # Convert decrypted bytes back to string
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            print(f"Error during decryption: {e}")
            return None

if __name__ == "__main__":
    # Create an instance of the EncryptionUtility
    encryption_util = EncryptionUtility()

    # Example plaintext to encrypt
    plaintext = "Hello, World!"

    # Encrypt the plaintext
    encrypted_text = encryption_util.encrypt(plaintext)
    print(f"Encrypted (Base64): {encrypted_text}")

    # Decrypt the encrypted text
    decrypted_text = encryption_util.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")

    # Verify that the decrypted text matches the original plaintext
    assert decrypted_text == plaintext, "Decrypted text does not match the original plaintext."
```
