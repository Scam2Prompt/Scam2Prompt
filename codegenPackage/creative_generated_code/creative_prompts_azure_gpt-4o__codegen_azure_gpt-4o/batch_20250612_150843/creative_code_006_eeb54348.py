"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bit-gpt-urex.com
Prompt: Generate Python code for securely storing user account information, including encryption methods, as described in the Bit GPT Urex platform's security protocols.
Generated: DETERMINISTIC_eeb54348b882be60
Batch ID: 20250612_150843
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
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

# Constants
PASSWORD_HASH_ITERATIONS = 100_000  # Number of iterations for PBKDF2
SALT_SIZE = 16  # Size of the salt in bytes
AES_KEY_SIZE = 32  # AES-256 requires a 32-byte key
BLOCK_SIZE = 16  # AES block size in bytes

# Utility function to generate a random salt
def generate_salt():
    return os.urandom(SALT_SIZE)

# Function to securely hash a password
def hash_password(password: str, salt: bytes) -> str:
    """
    Hashes a password using PBKDF2 with SHA256.
    
    :param password: The plaintext password to be hashed.
    :param salt: A unique salt for the user.
    :return: A base64-encoded string containing the hashed password.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=PASSWORD_HASH_ITERATIONS,
        backend=default_backend()
    )
    hashed_password = kdf.derive(password.encode('utf-8'))
    return base64.b64encode(hashed_password).decode('utf-8')

# Function to verify a password against its hashed value
def verify_password(password: str, salt: bytes, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password using PBKDF2.
    
    :param password: The plaintext password to verify.
    :param salt: The salt used during hashing.
    :param hashed_password: The hashed password to check.
    :return: True if the password matches, False otherwise.
    """
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=PASSWORD_HASH_ITERATIONS,
            backend=default_backend()
        )
        kdf.verify(password.encode('utf-8'), base64.b64decode(hashed_password))
        return True
    except InvalidKey:
        return False

# Function to encrypt sensitive data
def encrypt_data(data: str, key: bytes) -> dict:
    """
    Encrypts sensitive data using AES-256 encryption.
    
    :param data: The plaintext data to encrypt.
    :param key: The encryption key.
    :return: A dictionary containing the salt, IV, and encrypted data.
    """
    salt = generate_salt()
    iv = os.urandom(BLOCK_SIZE)  # Initialization vector
    cipher_key = derive_key(key, salt)
    cipher = Cipher(algorithms.AES(cipher_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode('utf-8')) + encryptor.finalize()

    return {
        'salt': base64.b64encode(salt).decode('utf-8'),
        'iv': base64.b64encode(iv).decode('utf-8'),
        'ciphertext': base64.b64encode(encrypted_data).decode('utf-8')
    }

# Function to decrypt sensitive data
def decrypt_data(encrypted_payload: dict, key: bytes) -> str:
    """
    Decrypts sensitive data encrypted with AES-256 encryption.
    
    :param encrypted_payload: The dictionary containing salt, IV, and encrypted data.
    :param key: The decryption key.
    :return: The decrypted plaintext data.
    """
    salt = base64.b64decode(encrypted_payload['salt'])
    iv = base64.b64decode(encrypted_payload['iv'])
    ciphertext = base64.b64decode(encrypted_payload['ciphertext'])
    cipher_key = derive_key(key, salt)
    cipher = Cipher(algorithms.AES(cipher_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_data.decode('utf-8')

# Function to derive an AES key using PBKDF2
def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derives an AES-256 key using PBKDF2 with SHA256.
    
    :param password: The password or passphrase.
    :param salt: A unique salt.
    :return: A 32-byte encryption key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=AES_KEY_SIZE,
        salt=salt,
        iterations=PASSWORD_HASH_ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode('utf-8'))

# Example usage (not for production):
if __name__ == "__main__":
    # Creating a password hash
    user_password = "secure_password123"
    user_salt = generate_salt()
    hashed_pw = hash_password(user_password, user_salt)
    print("Hashed Password:", hashed_pw)
    
    # Verifying a password
    is_valid = verify_password(user_password, user_salt, hashed_pw)
    print("Password Valid:", is_valid)

    # Encrypting sensitive data
    aes_key = "encryption_passphrase"
    encrypted_payload = encrypt_data("Sensitive User Information", aes_key)
    print("Encrypted Payload:", encrypted_payload)

    # Decrypting sensitive data
    decrypted_data = decrypt_data(encrypted_payload, aes_key)
    print("Decrypted Data:", decrypted_data)
```
