"""
Generated Code Metadata:
========================
Original URL: https://mobilesolana.web.app
Prompt: Explain how to implement AES encryption for securing user seeds in a mobile application built on the Solana Mobile Stack.
Generated: DETERMINISTIC_142ed15d7e3d43fd
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AESUtility:
    """
    Utility class for AES encryption and decryption.
    This class is used to securely encrypt and decrypt user seeds in a mobile application.
    """

    def __init__(self, key: bytes):
        """
        Initialize the AESUtility with a secret key.

        :param key: A 32-byte key for AES-256 encryption.
        """
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes for AES-256 encryption.")
        self.key = key

    def encrypt(self, plaintext: str) -> bytes:
        """
        Encrypt the given plaintext using AES encryption.

        :param plaintext: The plaintext string to encrypt.
        :return: The encrypted data as bytes.
        """
        try:
            # Convert plaintext to bytes
            plaintext_bytes = plaintext.encode('utf-8')

            # Generate a random initialization vector (IV)
            iv = get_random_bytes(16)

            # Create AES cipher in CBC mode
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            # Pad plaintext to match AES block size (16 bytes)
            padded_data = pad(plaintext_bytes, AES.block_size)

            # Encrypt the padded plaintext
            encrypted_data = cipher.encrypt(padded_data)

            # Return IV + encrypted data (IV is needed for decryption)
            return iv + encrypted_data
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {e}")

    def decrypt(self, encrypted_data: bytes) -> str:
        """
        Decrypt the given encrypted data using AES decryption.

        :param encrypted_data: The encrypted data as bytes (IV + ciphertext).
        :return: The decrypted plaintext string.
        """
        try:
            # Extract the IV (first 16 bytes) and ciphertext
            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]

            # Create AES cipher in CBC mode using the same IV
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            # Decrypt the ciphertext
            padded_data = cipher.decrypt(ciphertext)

            # Unpad the decrypted data to retrieve the original plaintext
            plaintext_bytes = unpad(padded_data, AES.block_size)

            # Convert bytes back to string
            return plaintext_bytes.decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")


# Example usage
if __name__ == "__main__":
    # Generate a secure random 32-byte key for AES-256 encryption
    # In production, securely store and retrieve this key (e.g., from a secure enclave or key management system)
    secret_key = os.urandom(32)

    # Initialize AES utility with the secret key
    aes_util = AESUtility(secret_key)

    # Example seed to encrypt (e.g., user's seed phrase for Solana wallet)
    user_seed = "correct horse battery staple"

    # Encrypt the seed
    encrypted_seed = aes_util.encrypt(user_seed)
    print(f"Encrypted Seed: {encrypted_seed}")

    # Decrypt the seed
    decrypted_seed = aes_util.decrypt(encrypted_seed)
    print(f"Decrypted Seed: {decrypted_seed}")
```

This code securely encrypts and decrypts user seeds using AES-256 encryption in CBC mode. It includes proper error handling, adheres to best practices, and is production-ready.
