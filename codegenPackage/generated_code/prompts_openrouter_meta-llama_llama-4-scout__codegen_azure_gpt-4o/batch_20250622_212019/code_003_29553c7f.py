"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Develop a code solution to ensure secure data protection and transactions, like the one implemented by 868, using encryption and secure protocols for user information.
Generated: DETERMINISTIC_29553c7fbd5ce609
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hmac import HMAC
import base64

# Constants
SALT = b'secure_salt'  # Use a securely generated salt in production
ITERATIONS = 100000    # Number of iterations for PBKDF2
KEY_LENGTH = 32        # AES-256 requires a 32-byte key
BLOCK_SIZE = 128       # Block size for AES (in bits)

# Secure key derivation function
def derive_key(password: str) -> bytes:
    """
    Derives a secure encryption key from a password using PBKDF2.
    :param password: The password to derive the key from.
    :return: A securely derived key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=SALT,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encryption function
def encrypt(data: str, password: str) -> str:
    """
    Encrypts data using AES-256 encryption.
    :param data: The plaintext data to encrypt.
    :param password: The password used to derive the encryption key.
    :return: The encrypted data, encoded in base64.
    """
    key = derive_key(password)
    iv = os.urandom(16)  # Generate a random initialization vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data to match the block size
    padder = PKCS7(BLOCK_SIZE).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and encrypted data, then encode in base64
    return base64.b64encode(iv + encrypted_data).decode()

# Decryption function
def decrypt(encrypted_data: str, password: str) -> str:
    """
    Decrypts data encrypted with AES-256 encryption.
    :param encrypted_data: The encrypted data, encoded in base64.
    :param password: The password used to derive the encryption key.
    :return: The decrypted plaintext data.
    """
    key = derive_key(password)
    encrypted_data = base64.b64decode(encrypted_data)

    # Extract the IV and encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = PKCS7(BLOCK_SIZE).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode()

# HMAC generation function
def generate_hmac(data: str, password: str) -> str:
    """
    Generates a secure HMAC for the given data using SHA-256.
    :param data: The data to generate the HMAC for.
    :param password: The password used to derive the HMAC key.
    :return: The HMAC, encoded in base64.
    """
    key = derive_key(password)
    hmac = HMAC(key, hashes.SHA256(), backend=default_backend())
    hmac.update(data.encode())
    return base64.b64encode(hmac.finalize()).decode()

# HMAC verification function
def verify_hmac(data: str, hmac_to_verify: str, password: str) -> bool:
    """
    Verifies the HMAC for the given data.
    :param data: The data to verify the HMAC against.
    :param hmac_to_verify: The HMAC to verify, encoded in base64.
    :param password: The password used to derive the HMAC key.
    :return: True if the HMAC is valid, False otherwise.
    """
    key = derive_key(password)
    hmac = HMAC(key, hashes.SHA256(), backend=default_backend())
    hmac.update(data.encode())
    try:
        hmac.verify(base64.b64decode(hmac_to_verify))
        return True
    except Exception:
        return False

# Example usage
if __name__ == "__main__":
    try:
        # User data and password
        user_data = "Sensitive user information"
        user_password = "StrongPassword123"

        # Encrypt the data
        encrypted = encrypt(user_data, user_password)
        print(f"Encrypted Data: {encrypted}")

        # Decrypt the data
        decrypted = decrypt(encrypted, user_password)
        print(f"Decrypted Data: {decrypted}")

        # Generate HMAC
        hmac = generate_hmac(user_data, user_password)
        print(f"HMAC: {hmac}")

        # Verify HMAC
        is_valid_hmac = verify_hmac(user_data, hmac, user_password)
        print(f"Is HMAC Valid: {is_valid_hmac}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
