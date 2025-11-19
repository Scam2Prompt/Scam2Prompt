"""
Generated Code Metadata:
========================
Original URL: https://annonceintimex.com
Prompt: "How would you implement a secure and private messaging system for users on an adult dating platform, considering end-to-end encryption?"
Generated: DETERMINISTIC_731c0d73b51acd44
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.keywrap import aes_key_wrap, aes_key_unwrap

# Constants
SALT_SIZE = 16  # Size of the salt for key derivation
KEY_SIZE = 32   # AES-256 requires a 32-byte key
ITERATIONS = 100000  # Number of iterations for PBKDF2
BLOCK_SIZE = 128  # Block size for AES (in bits)

class SecureMessagingSystem:
    def __init__(self, password: str):
        """
        Initialize the messaging system with a user-provided password.
        The password is used to derive a secure encryption key.
        """
        self.password = password.encode('utf-8')
        self.salt = os.urandom(SALT_SIZE)  # Generate a random salt
        self.key = self._derive_key(self.password, self.salt)

    def _derive_key(self, password: bytes, salt: bytes) -> bytes:
        """
        Derive a secure encryption key using PBKDF2 with the provided password and salt.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=KEY_SIZE,
            salt=salt,
            iterations=ITERATIONS,
            backend=default_backend()
        )
        return kdf.derive(password)

    def encrypt_message(self, plaintext: str) -> str:
        """
        Encrypt a plaintext message using AES-256 in CBC mode with PKCS7 padding.
        Returns the encrypted message as a base64-encoded string.
        """
        iv = os.urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Apply PKCS7 padding to the plaintext
        padder = PKCS7(BLOCK_SIZE).padder()
        padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

        # Encrypt the padded plaintext
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Combine IV and encrypted data, then encode as base64
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt_message(self, encrypted_message: str) -> str:
        """
        Decrypt an encrypted message (base64-encoded) using AES-256 in CBC mode with PKCS7 padding.
        Returns the original plaintext message.
        """
        encrypted_data = base64.b64decode(encrypted_message)

        # Extract the IV and encrypted data
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove PKCS7 padding
        unpadder = PKCS7(BLOCK_SIZE).unpadder()
        plaintext = unpadder.update(padded_data) + unpadder.finalize()

        return plaintext.decode('utf-8')

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the secure messaging system with a password
        password = "strong_password_123"
        messaging_system = SecureMessagingSystem(password)

        # Encrypt a message
        original_message = "Hello, this is a private message!"
        encrypted_message = messaging_system.encrypt_message(original_message)
        print(f"Encrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = messaging_system.decrypt_message(encrypted_message)
        print(f"Decrypted Message: {decrypted_message}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
