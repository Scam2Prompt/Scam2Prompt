"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Generate code that demonstrates how to use a specific encryption technique, potentially involving base64 encoding and decoding, as suggested by the webpage's text.
Generated: DETERMINISTIC_52e88079aed13216
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

def generate_key(password: str, salt: bytes = None) -> bytes:
    """
    Generate a cryptographic key from a password using PBKDF2HMAC.
    
    Args:
        password: The password to derive the key from.
        salt: Optional salt bytes. If None, a random salt will be generated.
    
    Returns:
        The derived key as bytes.
    """
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_message(message: str, key: bytes) -> str:
    """
    Encrypt a message using Fernet symmetric encryption.
    
    Args:
        message: The plaintext message to encrypt.
        key: The encryption key (must be URL-safe base64-encoded 32-byte key).
    
    Returns:
        The encrypted message as a base64-encoded string.
    
    Raises:
        ValueError: If the key is invalid.
    """
    try:
        f = Fernet(key)
        encrypted = f.encrypt(message.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    except Exception as e:
        raise ValueError("Encryption failed") from e

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    """
    Decrypt a message using Fernet symmetric encryption.
    
    Args:
        encrypted_message: The base64-encoded encrypted message.
        key: The decryption key (must be URL-safe base64-encoded 32-byte key).
    
    Returns:
        The decrypted plaintext message.
    
    Raises:
        ValueError: If decryption fails (invalid key or corrupted message).
    """
    try:
        f = Fernet(key)
        decoded = base64.urlsafe_b64decode(encrypted_message.encode())
        return f.decrypt(decoded).decode()
    except Exception as e:
        raise ValueError("Decryption failed") from e

# Example usage
if __name__ == "__main__":
    # Generate a key from a password
    password = "my_secure_password"
    key = generate_key(password)
    
    # Original message
    message = "This is a secret message!"
    
    # Encrypt the message
    encrypted = encrypt_message(message, key)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted: {decrypted}")
```
