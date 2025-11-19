"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Generate a code snippet for data encryption that small businesses can use to safeguard customer data, based on the cybersecurity measures detailed by CyberConnect.
Generated: DETERMINISTIC_5474ed105ca7f257
Batch ID: 20250612_155253
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

# Function to generate a secure encryption key using a password and salt
def generate_key(password: str, salt: bytes) -> bytes:
    """
    Generate a secure encryption key using PBKDF2 (Password-Based Key Derivation Function 2).
    
    Args:
        password (str): The password to derive the key.
        salt (bytes): A cryptographically secure random salt.
    
    Returns:
        bytes: The derived encryption key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 32-byte key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt data
def encrypt_data(data: str, key: bytes) -> dict:
    """
    Encrypt data using AES encryption in CBC mode with PKCS7 padding.
    
    Args:
        data (str): The plaintext data to encrypt.
        key (bytes): The encryption key.
    
    Returns:
        dict: A dictionary containing the ciphertext and the initialization vector (IV).
    """
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)  # AES block size is 16 bytes
    
    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Apply PKCS7 padding to the plaintext data
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    
    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    return {"ciphertext": ciphertext, "iv": iv}

# Function to decrypt data
def decrypt_data(encrypted_data: dict, key: bytes) -> str:
    """
    Decrypt data using AES encryption in CBC mode with PKCS7 padding.
    
    Args:
        encrypted_data (dict): A dictionary containing the ciphertext and the initialization vector (IV).
        key (bytes): The encryption key.
    
    Returns:
        str: The decrypted plaintext data.
    """
    ciphertext = encrypted_data["ciphertext"]
    iv = encrypted_data["iv"]
    
    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove PKCS7 padding from the decrypted data
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    try:
        # User-provided password
        password = "securepassword123"
        
        # Generate a random salt
        salt = os.urandom(16)
        
        # Derive encryption key
        key = generate_key(password, salt)
        
        # Data to encrypt
        customer_data = "Customer Name: John Doe, Email: john.doe@example.com"
        
        # Encrypt the data
        encrypted = encrypt_data(customer_data, key)
        print("Encrypted Data:", encrypted)
        
        # Decrypt the data
        decrypted = decrypt_data(encrypted, key)
        print("Decrypted Data:", decrypted)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
