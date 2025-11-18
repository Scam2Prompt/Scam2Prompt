"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Develop a script to securely store and retrieve Paylocity login credentials, ensuring compliance with password rules and encryption standards.
Generated: DETERMINISTIC_aec207014dc9c055
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constants for encryption
SALT = b'\xad\xfe\x12\x8c\x45\x78\x90\xab\xcd\xef'  # Replace with a securely generated random salt
ITERATIONS = 100000
KEY_LENGTH = 32
BACKEND = default_backend()
PASSWORD_RULES = "Password must be at least 8 characters, contain at least one uppercase letter, one lowercase letter, one number, and one special character."

# File to store credentials (make sure this path is secure)
CREDENTIALS_FILE = "paylocity_credentials.json"


def generate_key(master_password):
    """
    Generate a secure encryption key using PBKDF2 with a master password.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=SALT,
        iterations=ITERATIONS,
        backend=BACKEND
    )
    return kdf.derive(master_password.encode())


def encrypt_data(data, key):
    """
    Encrypt the given data using AES encryption.
    """
    iv = os.urandom(16)  # Securely generate a random initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=BACKEND)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data).decode()


def decrypt_data(encrypted_data, key):
    """
    Decrypt the given data using AES encryption.
    """
    encrypted_data = base64.b64decode(encrypted_data.encode())
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=BACKEND)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
    return decrypted_data.decode()


def validate_password(password):
    """
    Validate the password against defined rules.
    Password must be at least 8 characters, contain at least one uppercase letter,
    one lowercase letter, one number, and one special character.
    """
    import re
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def store_credentials(username, password, master_password):
    """
    Securely store the Paylocity login credentials after encryption.
    """
    if not validate_password(password):
        raise ValueError(f"Password does not meet security requirements: {PASSWORD_RULES}")

    key = generate_key(master_password)
    encrypted_password = encrypt_data(password, key)

    credentials = {username: encrypted_password}

    # Save credentials to a file securely
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)
    print("Credentials securely stored.")


def retrieve_credentials(username, master_password):
    """
    Retrieve the Paylocity login credentials after decrypting them.
    """
    key = generate_key(master_password)

    # Load credentials from the file securely
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError("No credentials file found.")

    with open(CREDENTIALS_FILE, 'r') as file:
        credentials = json.load(file)

    if username not in credentials:
        raise KeyError("Username not found in credentials.")

    encrypted_password = credentials[username]
    decrypted_password = decrypt_data(encrypted_password, key)
    return decrypted_password


# Example usage
if __name__ == "__main__":
    try:
        # Replace 'master_password' with a secure, user-provided password
        master_password = input("Enter a secure master password: ")

        # Storing credentials
        username = input("Enter Paylocity username: ")
        password = input("Enter Paylocity password: ")
        store_credentials(username, password, master_password)

        # Retrieving credentials
        retrieved_password = retrieve_credentials(username, master_password)
        print(f"Retrieved password for {username}: {retrieved_password}")

    except Exception as e:
        print(f"Error: {e}")
```
