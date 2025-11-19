"""
Generated Code Metadata:
========================
Original URL: https://mycrypto-wallet.com
Prompt: Write code to encrypt and decrypt cryptocurrency wallet data using AES encryption in Python.
Generated: DETERMINISTIC_2af5f18e2a3b70e8
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import secrets
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import json

def generate_key(size=256):
    """
    Generate a random AES key.

    Args:
        size (int): Key size in bits. Defaults to 256.

    Returns:
        bytes: The generated key.
    """
    return secrets.token_bytes(size // 8)

def encrypt_data(data: dict, key: bytes) -> str:
    """
    Encrypt wallet data using AES encryption.

    Args:
        data (dict): The wallet data to encrypt.
        key (bytes): The AES key.

    Returns:
        str: The encrypted data as a base64-encoded string.

    Raises:
        ValueError: If the key is not a bytes object.
    """
    if not isinstance(key, bytes):
        raise ValueError("Key must be a bytes object")

    # Generate a random 128-bit IV
    iv = secrets.token_bytes(16)

    # Create a new AES-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Convert data to bytes
    data_bytes = json.dumps(data).encode('utf-8')

    # Pad the data to a multiple of the block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data_bytes) + padder.finalize()

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Return the IV and encrypted data as a base64-encoded string
    return base64.b64encode(iv + encrypted_data).decode('utf-8')

def decrypt_data(encrypted_data: str, key: bytes) -> dict:
    """
    Decrypt wallet data using AES decryption.

    Args:
        encrypted_data (str): The encrypted data as a base64-encoded string.
        key (bytes): The AES key.

    Returns:
        dict: The decrypted wallet data.

    Raises:
        ValueError: If the key is not a bytes object or if the encrypted data is invalid.
    """
    if not isinstance(key, bytes):
        raise ValueError("Key must be a bytes object")

    try:
        # Decode the base64-encoded string
        encrypted_data_bytes = base64.b64decode(encrypted_data)
    except Exception as e:
        raise ValueError("Invalid encrypted data") from e

    # Extract the IV and encrypted data
    if len(encrypted_data_bytes) < 16:
        raise ValueError("Invalid encrypted data")
    iv = encrypted_data_bytes[:16]
    encrypted_data_bytes = encrypted_data_bytes[16:]

    # Create a new AES-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the encrypted data
    try:
        decrypted_padded_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()
    except Exception as e:
        raise ValueError("Invalid encrypted data") from e

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    data_bytes = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Return the decrypted data as a dictionary
    return json.loads(data_bytes.decode('utf-8'))

# Example usage
if __name__ == "__main__":
    key = generate_key()
    wallet_data = {
        "address": "0x1234567890",
        "private_key": "0x9876543210"
    }

    encrypted_data = encrypt_data(wallet_data, key)
    print(f"Encrypted data: {encrypted_data}")

    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Decrypted data: {decrypted_data}")
```
