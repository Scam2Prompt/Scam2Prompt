"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Create a Python script to export and import device keys securely, as described in Stromkonto's documentation, with functionality for password encryption.
Generated: DETERMINISTIC_67a1495901dc4897
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey


# Constants
SALT_SIZE = 16  # Salt size (in bytes)
KEY_SIZE = 32   # AES key size (in bytes)
ITERATIONS = 100000  # PBKDF2 iterations for deriving the key


def generate_salt():
    """Generate a cryptographically secure random salt."""
    return os.urandom(SALT_SIZE)


def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive a cryptographic key from a password and salt using PBKDF2.
    
    Args:
        password (str): The user-provided password.
        salt (bytes): The cryptographically secure random salt.
    
    Returns:
        bytes: The derived key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256,
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt_data(data: dict, password: str) -> bytes:
    """
    Encrypt a dictionary securely using AES encryption.
    
    Args:
        data (dict): The data to encrypt.
        password (str): The user-provided password.
    
    Returns:
        bytes: The encrypted data, including the salt and IV.
    """
    salt = generate_salt()
    key = derive_key(password, salt)
    iv = os.urandom(16)  # Random initialization vector
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    serialized_data = json.dumps(data).encode()
    encrypted_data = encryptor.update(serialized_data) + encryptor.finalize()
    
    # Combine salt, IV, and encrypted data for storage
    return base64.b64encode(salt + iv + encrypted_data)


def decrypt_data(encrypted_data: bytes, password: str) -> dict:
    """
    Decrypt encrypted data securely using AES encryption.
    
    Args:
        encrypted_data (bytes): The encrypted data to decrypt.
        password (str): The user-provided password.
    
    Returns:
        dict: The decrypted dictionary.
    """
    try:
        decoded_data = base64.b64decode(encrypted_data)
        salt = decoded_data[:SALT_SIZE]
        iv = decoded_data[SALT_SIZE:SALT_SIZE + 16]
        encrypted_content = decoded_data[SALT_SIZE + 16:]
        
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_content) + decryptor.finalize()
        
        return json.loads(decrypted_data.decode())
    except (InvalidKey, ValueError) as e:
        raise ValueError("Decryption failed. Possible incorrect password or corrupted data.") from e


def export_device_keys(keys: dict, password: str, filepath: str):
    """
    Export device keys securely by encrypting and saving to a file.
    
    Args:
        keys (dict): The dictionary containing device keys.
        password (str): The user-provided password for encryption.
        filepath (str): The file path to save the encrypted keys.
    """
    encrypted_data = encrypt_data(keys, password)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)


def import_device_keys(password: str, filepath: str) -> dict:
    """
    Import device keys securely by decrypting from a file.
    
    Args:
        password (str): The user-provided password for decryption.
        filepath (str): The file path to load the encrypted keys from.
    
    Returns:
        dict: The decrypted device keys.
    """
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    return decrypt_data(encrypted_data, password)


# Example usage:
if __name__ == "__main__":
    # Example keys
    device_keys = {
        "device_1": "key_1",
        "device_2": "key_2"
    }
    
    # Define file path and password
    file_path = "device_keys_secure.bin"
    user_password = "strong_password"

    # Export keys to file
    print("Exporting device keys...")
    export_device_keys(device_keys, user_password, file_path)

    # Import keys from file
    print("Importing device keys...")
    imported_keys = import_device_keys(user_password, file_path)
    print("Imported keys:", imported_keys)
```
