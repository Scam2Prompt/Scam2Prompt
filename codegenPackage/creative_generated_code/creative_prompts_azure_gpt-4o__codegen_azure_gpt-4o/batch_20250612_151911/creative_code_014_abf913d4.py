"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to encrypt sensitive data for a growing business, following CyberConnect's cybersecurity guidelines.
Generated: DETERMINISTIC_abf913d4640980c5
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

# Constants
SALT_SIZE = 16  # Size of the salt in bytes
KEY_SIZE = 32  # AES requires a key size of 16, 24, or 32 bytes
ITERATIONS = 100000  # Number of iterations for key derivation
BLOCK_SIZE = 128  # Block size for PKCS7 padding

def generate_key(password: str, salt: bytes) -> bytes:
    """
    Derives a symmetric encryption key using PBKDF2.
    
    :param password: User-provided password for key generation.
    :param salt: Random salt for key derivation.
    :return: Derived symmetric key.
    """
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt(data: str, password: str) -> str:
    """
    Encrypts the provided data using AES encryption.

    :param data: Data to be encrypted, as a string.
    :param password: User-provided password for encryption.
    :return: Encrypted data, encoded as a Base64 string.
    """
    # Generate a random salt
    salt = os.urandom(SALT_SIZE)
    
    # Generate encryption key
    key = generate_key(password, salt)
    
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Apply PKCS7 padding to plaintext
    padder = PKCS7(BLOCK_SIZE).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    
    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Concatenate salt, IV, and encrypted data, then encode as Base64
    result = b64encode(salt + iv + encrypted_data).decode()
    return result

def decrypt(encrypted_data: str, password: str) -> str:
    """
    Decrypts the provided encrypted data using AES decryption.

    :param encrypted_data: Encrypted data, as a Base64-encoded string.
    :param password: User-provided password for decryption.
    :return: Decrypted plaintext data, as a string.
    """
    # Decode Base64-encoded input
    encrypted_data_bytes = b64decode(encrypted_data)
    
    # Extract salt, IV, and encrypted content
    salt = encrypted_data_bytes[:SALT_SIZE]
    iv = encrypted_data_bytes[SALT_SIZE:SALT_SIZE + 16]
    encrypted_content = encrypted_data_bytes[SALT_SIZE + 16:]
    
    # Generate decryption key
    key = generate_key(password, salt)
    
    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the encrypted content
    padded_data = decryptor.update(encrypted_content) + decryptor.finalize()
    
    # Remove PKCS7 padding from plaintext
    unpadder = PKCS7(BLOCK_SIZE).unpadder()
    plaintext_data = unpadder.update(padded_data) + unpadder.finalize()
    
    return plaintext_data.decode()

if __name__ == "__main__":
    # Example usage
    try:
        # User-provided sensitive data and password
        sensitive_data = "This is confidential information."
        password = "secure_password"
        
        # Encrypt the data
        encrypted = encrypt(sensitive_data, password)
        print("Encrypted Data:", encrypted)
        
        # Decrypt the data
        decrypted = decrypt(encrypted, password)
        print("Decrypted Data:", decrypted)
    except Exception as e:
        # Handle unexpected errors gracefully
        print("An error occurred:", str(e))
```
