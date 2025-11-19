"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shitcoinwallet.co
Prompt: Explain how to securely store the private key for my Shitcoin Wallet and why it's important for transaction authorization.
Generated: DETERMINISTIC_6a614fe0866e8c02
Batch ID: 20250612_160703
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
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Constants
PRIVATE_KEY_FILE = "private_key.json"  # File to securely store the encrypted private key
SALT_FILE = "salt.bin"                # Salt file for key derivation
ITERATIONS = 100_000                  # Number of iterations for PBKDF2

def generate_salt() -> bytes:
    """
    Generates a random salt and saves it to a file.
    If the salt file already exists, it loads the existing salt.
    Returns:
        bytes: The generated or loaded salt.
    """
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as file:
            return file.read()
    else:
        salt = os.urandom(16)  # 16 bytes of random salt
        with open(SALT_FILE, "wb") as file:
            file.write(salt)
        return salt

def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derives a secure key using the PBKDF2 key derivation function.
    Args:
        password (str): The user-provided password.
        salt (bytes): The salt used for key derivation.
    Returns:
        bytes: The derived encryption key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), 
        length=32, 
        salt=salt, 
        iterations=ITERATIONS, 
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_private_key(private_key: str, password: str) -> None:
    """
    Encrypts the private key using AES encryption and saves it to a file.
    Args:
        private_key (str): The private key to encrypt.
        password (str): The user-provided password to derive the encryption key.
    """
    salt = generate_salt()
    key = derive_key(password, salt)

    # AES encryption using AES-GCM mode
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 12-byte nonce for AES-GCM
    encrypted_key = aesgcm.encrypt(nonce, private_key.encode(), None)

    # Save encrypted data and nonce as JSON
    with open(PRIVATE_KEY_FILE, "w") as file:
        json.dump({"nonce": nonce.hex(), "encrypted_key": encrypted_key.hex()}, file)

def decrypt_private_key(password: str) -> str:
    """
    Decrypts the private key from the file using the specified password.
    Args:
        password (str): The user-provided password to derive the decryption key.
    Returns:
        str: The decrypted private key.
    """
    if not os.path.exists(PRIVATE_KEY_FILE):
        raise FileNotFoundError("Private key file not found.")
    if not os.path.exists(SALT_FILE):
        raise FileNotFoundError("Salt file not found.")

    # Load salt, nonce, and encrypted key from files
    with open(SALT_FILE, "rb") as file:
        salt = file.read()
    with open(PRIVATE_KEY_FILE, "r") as file:
        data = json.load(file)
        nonce = bytes.fromhex(data["nonce"])
        encrypted_key = bytes.fromhex(data["encrypted_key"])

    key = derive_key(password, salt)

    # AES decryption using AES-GCM mode
    aesgcm = AESGCM(key)
    try:
        decrypted_key = aesgcm.decrypt(nonce, encrypted_key, None)
        return decrypted_key.decode()
    except Exception as e:
        raise ValueError(f"Failed to decrypt private key: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Prompt user for private key and password
        action = input("Would you like to (e)ncrypt or (d)ecrypt your private key? ").lower()
        if action == "e":
            private_key = input("Enter your private key: ").strip()
            password = input("Enter a strong password: ").strip()
            encrypt_private_key(private_key, password)
            print("Private key encrypted and securely stored.")
        elif action == "d":
            password = input("Enter your password: ").strip()
            private_key = decrypt_private_key(password)
            print(f"Decrypted private key: {private_key}")
        else:
            print("Invalid option selected.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
