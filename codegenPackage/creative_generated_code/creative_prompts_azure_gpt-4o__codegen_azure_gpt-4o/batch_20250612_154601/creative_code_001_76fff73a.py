"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Generate a Python script that demonstrates how to securely store Bitcoin using self-custody principles, ensuring financial sovereignty as outlined by Jupiter Digital Asset.
Generated: DETERMINISTIC_76fff73a1f7a7bf0
Batch ID: 20250612_154601
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
import hmac
import secrets
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constants for PBKDF2 and encryption
SALT_LENGTH = 16  # Length of salt in bytes
ITERATIONS = 100_000  # Number of iterations for PBKDF2
KEY_LENGTH = 32  # Length of encryption key in bytes
BACKUP_FILE = "bitcoin_wallet_backup.json"  # File where encrypted private key is stored

def generate_seed_phrase():
    """
    Generate a 256-bit random seed phrase using secrets module.
    This acts as the foundation for Bitcoin self-custody.
    """
    seed_bytes = secrets.token_bytes(32)  # Generate 256-bit (32-byte) random data
    seed_phrase = hashlib.sha256(seed_bytes).hexdigest()  # Convert to hexadecimal
    return seed_phrase

def derive_private_key(seed_phrase):
    """
    Derive a Bitcoin private key from the seed phrase using HMAC-SHA256.
    """
    return hmac.new(b"Bitcoin", seed_phrase.encode(), hashlib.sha256).hexdigest()

def encrypt_private_key(private_key, password):
    """
    Encrypt the private key using AES-256-GCM with a password-derived key.
    Returns the encrypted data and the salt used for password derivation.
    """
    # Generate a random salt
    salt = secrets.token_bytes(SALT_LENGTH)
    
    # Derive encryption key using PBKDF2
    kdf = PBKDF2HMAC(algorithm=SHA256, length=KEY_LENGTH, salt=salt, iterations=ITERATIONS, backend=default_backend())
    encryption_key = kdf.derive(password.encode())
    
    # Encrypt the private key using AES-GCM
    iv = secrets.token_bytes(12)  # 12-byte random initialization vector (IV)
    cipher = Cipher(algorithms.AES(encryption_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_private_key = encryptor.update(private_key.encode()) + encryptor.finalize()
    return {
        "encrypted_private_key": encrypted_private_key.hex(),
        "salt": salt.hex(),
        "iv": iv.hex(),
        "tag": encryptor.tag.hex()  # Authentication tag for integrity
    }

def decrypt_private_key(encrypted_data, password):
    """
    Decrypt the private key using AES-256-GCM with a password-derived key.
    """
    salt = bytes.fromhex(encrypted_data["salt"])
    iv = bytes.fromhex(encrypted_data["iv"])
    tag = bytes.fromhex(encrypted_data["tag"])
    encrypted_private_key = bytes.fromhex(encrypted_data["encrypted_private_key"])
    
    # Derive decryption key using PBKDF2
    kdf = PBKDF2HMAC(algorithm=SHA256, length=KEY_LENGTH, salt=salt, iterations=ITERATIONS, backend=default_backend())
    decryption_key = kdf.derive(password.encode())
    
    # Decrypt the private key using AES-GCM
    cipher = Cipher(algorithms.AES(decryption_key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    private_key = decryptor.update(encrypted_private_key) + decryptor.finalize()
    return private_key.decode()

def backup_private_key(encrypted_data):
    """
    Save the encrypted private key and associated metadata to a local file for self-custody.
    """
    with open(BACKUP_FILE, "w") as backup_file:
        json.dump(encrypted_data, backup_file, indent=4)

def restore_private_key(password):
    """
    Restore the private key from the backup file.
    """
    if not os.path.exists(BACKUP_FILE):
        raise FileNotFoundError("Backup file not found.")
    
    with open(BACKUP_FILE, "r") as backup_file:
        encrypted_data = json.load(backup_file)
    return decrypt_private_key(encrypted_data, password)

# Main flow for demonstration
if __name__ == "__main__":
    try:
        # Step 1: Generate seed phrase
        seed_phrase = generate_seed_phrase()
        print("Generated Seed Phrase:", seed_phrase)
        
        # Step 2: Derive private key from seed phrase
        private_key = derive_private_key(seed_phrase)
        print("Derived Private Key:", private_key)
        
        # Step 3: Encrypt private key with user-defined password
        password = input("Enter a strong password for encryption: ")
        encrypted_data = encrypt_private_key(private_key, password)
        print("Encrypted Private Key:", encrypted_data)
        
        # Step 4: Backup encrypted private key locally
        backup_private_key(encrypted_data)
        print(f"Encrypted private key backed up to {BACKUP_FILE}.")
        
        # Step 5 (Optional): Restore private key from backup
        restored_private_key = restore_private_key(password)
        print("Restored Private Key:", restored_private_key)
    except Exception as e:
        print(f"An error occurred: {e}")
```
