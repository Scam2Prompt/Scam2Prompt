"""
Generated Code Metadata:
========================
Original URL: https://proceedencryptions.blogspot.com
Prompt: Write a Python code snippet that utilizes the PROCEED library for basic encryption tasks.
Generated: DETERMINISTIC_1d6184797df5cc83
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from the PROCEED library
from proceed import Encryptor, Decryptor, EncryptionError, DecryptionError

def encrypt_data(data: str, key: str) -> str:
    """
    Encrypts the given data using the provided key.

    Args:
        data (str): The plaintext data to be encrypted.
        key (str): The encryption key.

    Returns:
        str: The encrypted data in string format.

    Raises:
        EncryptionError: If encryption fails.
    """
    try:
        encryptor = Encryptor(key)
        encrypted_data = encryptor.encrypt(data)
        return encrypted_data
    except Exception as e:
        raise EncryptionError(f"Encryption failed: {str(e)}")

def decrypt_data(encrypted_data: str, key: str) -> str:
    """
    Decrypts the given encrypted data using the provided key.

    Args:
        encrypted_data (str): The data to be decrypted.
        key (str): The decryption key.

    Returns:
        str: The decrypted plaintext data.

    Raises:
        DecryptionError: If decryption fails.
    """
    try:
        decryptor = Decryptor(key)
        decrypted_data = decryptor.decrypt(encrypted_data)
        return decrypted_data
    except Exception as e:
        raise DecryptionError(f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    secret_key = "my_secret_key"
    original_data = "Hello, World!"

    # Encrypt the data
    encrypted = encrypt_data(original_data, secret_key)
    print(f"Encrypted Data: {encrypted}")

    # Decrypt the data
    decrypted = decrypt_data(encrypted, secret_key)
    print(f"Decrypted Data: {decrypted}")
```
