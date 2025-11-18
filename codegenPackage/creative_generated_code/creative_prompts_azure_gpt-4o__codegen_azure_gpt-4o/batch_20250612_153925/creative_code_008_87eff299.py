"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-startowers.com
Prompt: Create a script to enable secure storage and local generation of private keys for a crypto wallet, similar to StarTower's approach.
Generated: DETERMINISTIC_87eff299a97fa801
Batch ID: 20250612_153925
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
import hashlib
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend

# Constants for secure key storage
KEY_STORAGE_FILE = 'crypto_wallet_keys.json'
SALT_SIZE = 16  # Size of the salt in bytes
KEY_ITERATIONS = 100_000  # Number of iterations for key derivation
PASSWORD_PROTECTION_ENABLED = True  # Toggle password protection for private keys

def generate_private_key():
    """
    Generate a new RSA private key.
    Returns:
        private_key: An RSA private key object.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def serialize_private_key(private_key, password=None):
    """
    Serialize the private key securely, optionally encrypting it with a password.
    Args:
        private_key: RSA private key object.
        password (str): Password for encryption. If None, the key is stored without encryption.
    Returns:
        serialized_key (bytes): The serialized private key.
    """
    encryption_algorithm = (
        serialization.BestAvailableEncryption(password.encode()) if password else serialization.NoEncryption()
    )
    serialized_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )
    return serialized_key

def store_key(identifier, private_key_bytes, salt=None):
    """
    Store the private key in a JSON file securely.
    Args:
        identifier (str): A unique identifier for the key (e.g., wallet name).
        private_key_bytes (bytes): Serialized private key bytes.
        salt (bytes): Salt used for encryption, if applicable.
    """
    if not os.path.exists(KEY_STORAGE_FILE):
        keys_data = {}
    else:
        with open(KEY_STORAGE_FILE, 'r') as file:
            keys_data = json.load(file)

    keys_data[identifier] = {
        "private_key": base64.b64encode(private_key_bytes).decode(),
        "salt": base64.b64encode(salt).decode() if salt else None
    }

    with open(KEY_STORAGE_FILE, 'w') as file:
        json.dump(keys_data, file, indent=4)

def derive_key(password, salt):
    """
    Derive a cryptographic key using a password and a salt.
    Args:
        password (str): The password to use.
        salt (bytes): The salt value.
    Returns:
        derived_key (bytes): The derived key.
    """
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=KEY_ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def create_wallet(identifier, password=None):
    """
    Create a new wallet by generating and securely storing a private key.
    Args:
        identifier (str): A unique name for the wallet.
        password (str): Optional password for protecting the key. If None, no password is used.
    """
    # Generate a private key
    private_key = generate_private_key()

    if PASSWORD_PROTECTION_ENABLED and password:
        # Generate a salt for key derivation
        salt = os.urandom(SALT_SIZE)
        derived_key = derive_key(password, salt)
        encrypted_private_key = serialize_private_key(private_key, password=base64.b64encode(derived_key).decode())
        store_key(identifier, encrypted_private_key, salt)
    else:
        # Serialize the key without password protection
        serialized_key = serialize_private_key(private_key)
        store_key(identifier, serialized_key)

def load_wallet(identifier, password=None):
    """
    Load a wallet's private key securely.
    Args:
        identifier (str): The unique wallet name.
        password (str): Password to decrypt the private key (if applicable).
    Returns:
        private_key: The RSA private key object.
    """
    # Load stored keys from file
    if not os.path.exists(KEY_STORAGE_FILE):
        raise FileNotFoundError("Key storage file not found.")

    with open(KEY_STORAGE_FILE, 'r') as file:
        keys_data = json.load(file)

    if identifier not in keys_data:
        raise ValueError(f"Wallet with identifier '{identifier}' not found.")

    key_entry = keys_data[identifier]
    private_key_bytes = base64.b64decode(key_entry["private_key"])
    salt = base64.b64decode(key_entry["salt"]) if key_entry["salt"] else None

    if PASSWORD_PROTECTION_ENABLED and password and salt:
        derived_key = derive_key(password, salt)
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=base64.b64encode(derived_key).decode(),
            backend=default_backend()
        )
    else:
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )
    return private_key

# Usage Example:
if __name__ == "__main__":
    try:
        wallet_name = input("Enter wallet name: ")
        wallet_password = input("Enter wallet password (optional): ")

        create_wallet(wallet_name, wallet_password)
        print(f"Wallet '{wallet_name}' created successfully.")

        loaded_key = load_wallet(wallet_name, wallet_password)
        print(f"Wallet '{wallet_name}' loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
