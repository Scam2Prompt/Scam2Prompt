"""
Generated Code Metadata:
========================
Original URL: https://prsivnote.com
Prompt: Implement a secure note storage system using a cryptographic library like OpenSSL, with features like note expiration and password-based encryption.
Generated: DETERMINISTIC_fda5c7f8b561a5f4
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import base64
import hashlib
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Constants
SALT_SIZE = 16  # Size of the salt in bytes
KEY_SIZE = 32   # AES-256 requires a 32-byte key
ITERATIONS = 100000  # Number of iterations for PBKDF2
EXPIRATION_FORMAT = "%Y-%m-%d %H:%M:%S"  # Format for expiration timestamps

# Helper function to generate a random salt
def generate_salt():
    return os.urandom(SALT_SIZE)

# Helper function to derive a key from a password and salt
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256,
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encrypt a note with AES-256
def encrypt_note(note, password, expiration_minutes):
    # Generate a random salt
    salt = generate_salt()
    
    # Derive the encryption key from the password and salt
    key = derive_key(password, salt)
    
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create the cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the note
    encrypted_note = encryptor.update(note.encode()) + encryptor.finalize()
    
    # Calculate expiration timestamp
    expiration_time = (datetime.now() + timedelta(minutes=expiration_minutes)).strftime(EXPIRATION_FORMAT)
    
    # Return the encrypted note, salt, IV, and expiration timestamp
    return {
        "encrypted_note": base64.b64encode(encrypted_note).decode(),
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(iv).decode(),
        "expiration_time": expiration_time
    }

# Decrypt a note with AES-256
def decrypt_note(encrypted_data, password):
    try:
        # Extract components from the encrypted data
        encrypted_note = base64.b64decode(encrypted_data["encrypted_note"])
        salt = base64.b64decode(encrypted_data["salt"])
        iv = base64.b64decode(encrypted_data["iv"])
        expiration_time = encrypted_data["expiration_time"]
        
        # Check if the note has expired
        if datetime.now() > datetime.strptime(expiration_time, EXPIRATION_FORMAT):
            raise ValueError("The note has expired.")
        
        # Derive the decryption key from the password and salt
        key = derive_key(password, salt)
        
        # Create the cipher object
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Decrypt the note
        decrypted_note = decryptor.update(encrypted_note) + decryptor.finalize()
        
        return decrypted_note.decode()
    except Exception as e:
        # Handle decryption errors
        raise ValueError(f"Failed to decrypt the note: {str(e)}")

# Example usage
if __name__ == "__main__":
    # User inputs
    note = "This is a secret note."
    password = "strongpassword123"
    expiration_minutes = 5  # Note expires in 5 minutes
    
    # Encrypt the note
    encrypted_data = encrypt_note(note, password, expiration_minutes)
    print("Encrypted Data:", encrypted_data)
    
    # Decrypt the note
    try:
        decrypted_note = decrypt_note(encrypted_data, password)
        print("Decrypted Note:", decrypted_note)
    except ValueError as e:
        print(e)
```
