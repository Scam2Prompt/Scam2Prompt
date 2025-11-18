"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourayou.sa.com
Prompt: Generate code to encrypt user data on hosting servers with advanced security measures, referencing the privacy-focused hosting described on Yourayou.sa.com.
Generated: DETERMINISTIC_045dae3325375858
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Constants for encryption
SALT_SIZE = 16  # Size of the salt in bytes
KEY_SIZE = 32   # AES-256 requires a 32-byte key
ITERATIONS = 100000  # PBKDF2 iterations for key derivation
BACKEND = default_backend()

def generate_salt():
    """
    Generate a cryptographically secure random salt.
    """
    return os.urandom(SALT_SIZE)

def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive a secure AES encryption key from a password using PBKDF2.
    Args:
        password (str): User-provided password.
        salt (bytes): Random salt to use with PBKDF2.

    Returns:
        bytes: Derived encryption key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=BACKEND
    )
    return kdf.derive(password.encode())

def encrypt_data(data: str, password: str) -> dict:
    """
    Encrypt user data using AES-256-GCM.
    Args:
        data (str): Data to encrypt.
        password (str): User-provided password for encryption.

    Returns:
        dict: Encrypted data, including cipher text, salt, IV, and authentication tag.
    """
    # Generate a random salt and derive the key
    salt = generate_salt()
    key = derive_key(password, salt)

    # Generate random IV (Initialization Vector)
    iv = os.urandom(12)  # 12 bytes for AES-GCM

    # Create the AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=BACKEND)
    encryptor = cipher.encryptor()

    # Encrypt the data
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

    # Return all necessary components for decryption
    return {
        'ciphertext': base64.b64encode(ciphertext).decode(),
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode(),
        'tag': base64.b64encode(encryptor.tag).decode()
    }

def decrypt_data(encrypted: dict, password: str) -> str:
    """
    Decrypt user data using AES-256-GCM.
    Args:
        encrypted (dict): Encrypted data dictionary with ciphertext, salt, iv, and tag.
        password (str): User-provided password for decryption.

    Returns:
        str: Decrypted plaintext data.
    """
    try:
        # Decode base64-encoded components
        ciphertext = base64.b64decode(encrypted['ciphertext'])
        salt = base64.b64decode(encrypted['salt'])
        iv = base64.b64decode(encrypted['iv'])
        tag = base64.b64decode(encrypted['tag'])

        # Derive the key using the provided password and salt
        key = derive_key(password, salt)

        # Create the AES-GCM cipher
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=BACKEND)
        decryptor = cipher.decryptor()

        # Decrypt the data
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
    except Exception as e:
        # Handle decryption errors gracefully
        raise ValueError("Decryption failed. Check the password or data integrity.") from e

# Example usage:
if __name__ == "__main__":
    password = "secure_password"
    data = "Sensitive user data."

    # Encrypt the data
    encrypted_data = encrypt_data(data, password)
    print("Encrypted Data:", encrypted_data)

    # Decrypt the data
    decrypted_data = decrypt_data(encrypted_data, password)
    print("Decrypted Data:", decrypted_data)
```
