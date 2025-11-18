"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danielasteinsapir.com
Prompt: Generate a script to encrypt and decrypt sensitive files on Windows and Mac systems, referencing the Tornado Cash privacy principles.
Generated: DETERMINISTIC_faa76300936ecb20
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
from base64 import b64encode, b64decode

# Constants
SALT_SIZE = 16  # Salt size in bytes
KEY_SIZE = 32   # AES key size (256 bits)
ITERATIONS = 100000  # PBKDF2 iterations for key derivation

def generate_key(password: str, salt: bytes) -> bytes:
    """
    Generate a symmetric key using PBKDF2 and the provided password and salt.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_file: str, output_file: str, password: str):
    """
    Encrypt a file using AES-256 encryption and save the encrypted content.
    """
    try:
        # Generate a random salt
        salt = os.urandom(SALT_SIZE)
        
        # Generate the encryption key
        key = generate_key(password, salt)
        
        # Initialize cipher
        iv = os.urandom(16)  # AES block size is 16 bytes
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Read file content
        with open(input_file, 'rb') as f:
            data = f.read()
        
        # Pad data to AES block size
        padder = PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        # Encrypt data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Save salt, IV, and encrypted data to output file
        with open(output_file, 'wb') as f:
            f.write(salt + iv + encrypted_data)
        
        print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(input_file: str, output_file: str, password: str):
    """
    Decrypt an encrypted file using AES-256 decryption and save the original content.
    """
    try:
        # Read salt, IV, and encrypted data from input file
        with open(input_file, 'rb') as f:
            salt = f.read(SALT_SIZE)
            iv = f.read(16)  # AES block size
            encrypted_data = f.read()
        
        # Generate the decryption key
        key = generate_key(password, salt)
        
        # Initialize cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Decrypt data
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # Remove padding
        unpadder = PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        
        # Save the original file content
        with open(output_file, 'wb') as f:
            f.write(data)
        
        print(f"File '{input_file}' decrypted successfully to '{output_file}'.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def main():
    """
    Main function for handling command-line arguments and performing encryption/decryption.
    """
    parser = argparse.ArgumentParser(description="Encrypt and decrypt files using AES-256.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("password", help="Encryption/Decryption password")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_file(args.input_file, args.output_file, args.password)
    elif args.mode == "decrypt":
        decrypt_file(args.input_file, args.output_file, args.password)

if __name__ == "__main__":
    main()
```
