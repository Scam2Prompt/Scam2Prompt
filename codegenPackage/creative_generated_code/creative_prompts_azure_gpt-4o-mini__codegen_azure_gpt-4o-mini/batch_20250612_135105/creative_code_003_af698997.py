"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchome.creatorlink.net
Prompt: What best practices should I follow to ensure the security of my MetaMask wallet and private keys?
Generated: DETERMINISTIC_af6989970ebbde9f
Batch ID: 20250612_135105
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
from cryptography.fernet import Fernet

class SecureWallet:
    """
    A class to manage the security of a MetaMask wallet and its private keys.
    """

    def __init__(self):
        """Initialize the secure wallet with an encryption key."""
        self.key = self.generate_key()
        self.cipher_suite = Fernet(self.key)

    @staticmethod
    def generate_key():
        """Generate a secure encryption key."""
        return Fernet.generate_key()

    def encrypt_private_key(self, private_key):
        """
        Encrypt the private key using Fernet symmetric encryption.

        Args:
            private_key (str): The private key to encrypt.

        Returns:
            str: The encrypted private key.
        """
        if not isinstance(private_key, str):
            raise ValueError("Private key must be a string.")
        encrypted_key = self.cipher_suite.encrypt(private_key.encode())
        return encrypted_key.decode()

    def decrypt_private_key(self, encrypted_key):
        """
        Decrypt an encrypted private key.

        Args:
            encrypted_key (str): The encrypted private key to decrypt.

        Returns:
            str: The original private key.
        """
        if not isinstance(encrypted_key, str):
            raise ValueError("Encrypted key must be a string.")
        try:
            decrypted_key = self.cipher_suite.decrypt(encrypted_key.encode())
            return decrypted_key.decode()
        except Exception as e:
            raise RuntimeError("Decryption failed: " + str(e))

    @staticmethod
    def hash_password(password):
        """
        Hash a password using SHA-256 for secure storage.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def store_secure_info(file_name, data):
        """
        Store sensitive information securely in a file.

        Args:
            file_name (str): The name of the file to store data in.
            data (str): The data to store in the file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_name, 'w') as file:
                file.write(data)
        except IOError as e:
            raise IOError("Failed to write to file: " + str(e))

    @staticmethod
    def read_secure_info(file_name):
        """
        Read sensitive information from a file.

        Args:
            file_name (str): The name of the file to read data from.

        Returns:
            str: The data read from the file.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except IOError as e:
            raise IOError("Failed to read from file: " + str(e))


# Example usage
if __name__ == "__main__":
    wallet = SecureWallet()
    
    # Example private key
    private_key = "your_private_key_here"

    # Encrypt the private key
    encrypted_key = wallet.encrypt_private_key(private_key)
    print("Encrypted Private Key:", encrypted_key)

    # Store the encrypted key securely
    wallet.store_secure_info("encrypted_key.txt", encrypted_key)

    # Read the encrypted key back from the file
    read_encrypted_key = wallet.read_secure_info("encrypted_key.txt")

    # Decrypt the private key
    decrypted_key = wallet.decrypt_private_key(read_encrypted_key)
    print("Decrypted Private Key:", decrypted_key)

    # Example of securely hashing a password
    password = "your_secure_password"
    hashed_password = wallet.hash_password(password)
    print("Hashed Password:", hashed_password)
```
