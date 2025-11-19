"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-support.pages.dev
Prompt: How can I implement wallet encryption for securing transactions in a live support system?
Generated: DETERMINISTIC_691cb4a862405823
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import secrets
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class WalletEncryption:
    """A class to handle wallet encryption and decryption for secure transactions."""

    def __init__(self, key: bytes = None):
        """Initialize the wallet encryption with a key.

        Args:
            key (bytes): An optional key for encryption. If None, a new key will be generated.
        """
        if key is None:
            self.key = self.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """Generate a new encryption key.

        Returns:
            bytes: A new Fernet encryption key.
        """
        return Fernet.generate_key()

    def encrypt(self, data: str) -> bytes:
        """Encrypt data using the Fernet cipher.

        Args:
            data (str): The data to encrypt.

        Returns:
            bytes: The encrypted data.
        """
        try:
            return self.cipher.encrypt(data.encode())
        except Exception as e:
            raise RuntimeError("Encryption failed.") from e

    def decrypt(self, encrypted_data: bytes) -> str:
        """Decrypt previously encrypted data.

        Args:
            encrypted_data (bytes): The data to decrypt.

        Returns:
            str: The decrypted data.

        Raises:
            RuntimeError: If decryption fails.
        """
        try:
            return self.cipher.decrypt(encrypted_data).decode()
        except InvalidToken:
            raise RuntimeError("Decryption failed. Invalid token.")
        except Exception as e:
            raise RuntimeError("Decryption failed.") from e

    def save_key(self, file_path: str) -> None:
        """Save the encryption key to a file.

        Args:
            file_path (str): The file path to save the key.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
        except Exception as e:
            raise RuntimeError("Failed to save the key.") from e

    @staticmethod
    def load_key(file_path: str) -> bytes:
        """Load an encryption key from a file.

        Args:
            file_path (str): The file path to load the key from.

        Returns:
            bytes: The loaded encryption key.
        
        Raises:
            RuntimeError: If loading the key fails.
        """
        try:
            with open(file_path, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            raise RuntimeError("Key file not found.")
        except Exception as e:
            raise RuntimeError("Failed to load the key.") from e


# Example usage
if __name__ == "__main__":
    # Initialize the wallet encryption system
    wallet = WalletEncryption()

    # Sample data to encrypt
    transaction_data = "Transaction: UserA pays UserB 100 USD"

    # Encrypt the data
    encrypted_data = wallet.encrypt(transaction_data)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypt the data
    decrypted_data = wallet.decrypt(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")

    # Save the key to a file
    wallet.save_key("secret.key")

    # Load the key from a file
    loaded_key = WalletEncryption.load_key("secret.key")
    wallet_loaded = WalletEncryption(key=loaded_key)

    # Verify that loading the key works
    decrypted_data_via_loaded_key = wallet_loaded.decrypt(encrypted_data)
    print(f"Decrypted Data using loaded key: {decrypted_data_via_loaded_key}")
```
