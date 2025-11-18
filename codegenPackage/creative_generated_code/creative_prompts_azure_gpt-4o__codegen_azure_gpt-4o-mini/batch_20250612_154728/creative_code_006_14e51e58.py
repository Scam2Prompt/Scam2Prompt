"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeelixir.com
Prompt: Recommend APIs or tools for implementing end-to-end encryption in a decentralized application, as emphasized by DappWorld's safety and security measures.
Generated: DETERMINISTIC_14e51e581153681b
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class EncryptionManager:
    """
    A class to handle encryption and decryption of messages using Fernet symmetric encryption.
    """

    def __init__(self):
        """
        Initializes the EncryptionManager by generating a new key.
        """
        self.key = self.generate_key()

    def generate_key(self):
        """
        Generates a new Fernet key.

        Returns:
            bytes: A base64 encoded key.
        """
        return Fernet.generate_key()

    def encrypt_message(self, message: str) -> bytes:
        """
        Encrypts a message using the Fernet symmetric encryption.

        Args:
            message (str): The plaintext message to be encrypted.

        Returns:
            bytes: The encrypted message as bytes.
        """
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message: bytes) -> str:
        """
        Decrypts an encrypted message using the Fernet symmetric encryption.

        Args:
            encrypted_message (bytes): The encrypted message to be decrypted.

        Returns:
            str: The decrypted plaintext message.

        Raises:
            InvalidToken: If the decryption fails due to an invalid token.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message).decode()
            return decrypted_message
        except InvalidToken:
            raise ValueError("Invalid token. Decryption failed.")

def main():
    """
    Main function to demonstrate the encryption and decryption process.
    """
    try:
        manager = EncryptionManager()

        message = "This is a secret message."
        print(f"Original Message: {message}")

        # Encrypt the message
        encrypted_message = manager.encrypt_message(message)
        print(f"Encrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = manager.decrypt_message(encrypted_message)
        print(f"Decrypted Message: {decrypted_message}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
