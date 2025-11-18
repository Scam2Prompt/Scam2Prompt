"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amexgiftcardbalance.net
Prompt: Recommend APIs or libraries for securely encrypting Amex Gift Card transaction data, as outlined in the security features of AmexGiftCard.com.
Generated: DETERMINISTIC_283a2c6bbfdef8d0
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is production-ready Python code for securely encrypting transaction data using the `cryptography` library, which is widely recommended for strong encryption in Python. Ensure that you install this library using `pip install cryptography`.

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from os import urandom
import base64

class SecureEncryption:
    """
    A class for securely encrypting and decrypting transaction data using AES encryption.
    This implementation meets best practices for cryptographic security, including key generation and data handling.
    """

    def __init__(self, password: str):
        """
        Initialize the SecureEncryption class with a password for deriving encryption keys.

        :param password: A user-provided password used to derive the encryption key.
        """
        self.backend = default_backend()
        self.password = password.encode()
        self.salt = urandom(16)  # Generate a random salt for key derivation
        self.key = self._generate_key()

    def _generate_key(self) -> bytes:
        """
        Derive a secure encryption key using PBKDF2 (Password-Based Key Derivation Function 2).

        :return: The derived encryption key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100_000,
            backend=self.backend
        )
        return kdf.derive(self.password)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the provided plaintext securely using AES encryption.

        :param plaintext: The data to be encrypted (e.g., transaction details).
        :return: The encrypted data as a base64-encoded string.
        """
        iv = urandom(16)  # Initialization vector for AES encryption
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

        # Combine IV and ciphertext for decryption, and encode as base64
        encrypted_data = base64.b64encode(iv + ciphertext).decode()
        return encrypted_data

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt the provided encrypted data securely using AES decryption.

        :param encrypted_data: The base64-encoded encrypted data (IV + ciphertext).
        :return: The decrypted plaintext.
        """
        # Decode the base64-encoded data
        encrypted_data = base64.b64decode(encrypted_data)

        # Extract the IV and ciphertext
        iv = encrypted_data[:16]  # First 16 bytes are the IV
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        return plaintext.decode()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the encryption class with a secure user password
        encryption = SecureEncryption(password="strong_password_123")

        # Encrypt sensitive transaction data (e.g., Gift Card details)
        transaction_data = "Amex Gift Card Transaction: Card #1234-5678-9012 Amount: $100"
        encrypted_data = encryption.encrypt(transaction_data)
        print(f"Encrypted Data: {encrypted_data}")

        # Decrypt the transaction data securely
        decrypted_data = encryption.decrypt(encrypted_data)
        print(f"Decrypted Data: {decrypted_data}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Summary of Features:
1. **AES Encryption:** Uses AES (Advanced Encryption Standard) with CFB (Cipher Feedback) mode for secure encryption.
2. **Key Derivation:** Implements PBKDF2 with SHA-256 for generating strong encryption keys.
3. **Random Salt and IV:** Ensures each encryption operation is unique and secure.
4. **Base64 Encoding:** Encodes encrypted data for safe transport and storage.
5. **Error Handling:** Captures and displays errors during encryption and decryption.

Make sure to store the password and salt securely, as losing these will make decryption impossible.
