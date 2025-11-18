"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Recommend libraries for implementing a secure and GDPR-compliant data-sharing system, similar to Immediate Migna's approach to handling personal data.
Generated: DETERMINISTIC_f78134faab526f5b
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python code demonstrates a secure and GDPR-compliant data-sharing system by leveraging recommended libraries.
It ensures compliance with GDPR practices, including encryption, anonymization, and secure transfer of personal data.
"""

import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import json
import hashlib
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Constants for encryption
AES_KEY_SIZE = 32  # 256-bit AES encryption
IV_SIZE = 16  # Initialization Vector size
ITERATIONS = 100000  # Iterations for PBKDF2

def generate_rsa_key_pair():
    """
    Generate an RSA key pair for secure communication.
    Returns the private and public keys in PEM format.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    # Serialize keys to PEM format
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

def encrypt_data(data, password):
    """
    Encrypt personal data using AES encryption with PBKDF2 key derivation.
    
    Args:
        data (str): The data to be encrypted.
        password (str): The password for key derivation.
        
    Returns:
        dict: Contains encrypted data, salt, and IV.
    """
    # Generate a random salt
    salt = os.urandom(16)
    
    # Key derivation using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )
    key = kdf.derive(password.encode())
    
    # Generate a random IV
    iv = os.urandom(IV_SIZE)
    
    # Encrypt the data using AES CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    
    # Pad data to match block size (16 bytes for AES)
    padded_data = data + (AES_KEY_SIZE - len(data) % AES_KEY_SIZE) * ' '
    encrypted_data = encryptor.update(padded_data.encode()) + encryptor.finalize()
    
    # Encode the encrypted data, salt, and IV using Base64 for safe storage/transmission
    return {
        'encrypted_data': base64.b64encode(encrypted_data).decode(),
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode(),
    }

def decrypt_data(encrypted_dict, password):
    """
    Decrypt personal data encrypted using AES encryption and PBKDF2 key derivation.
    
    Args:
        encrypted_dict (dict): Contains encrypted data, salt, and IV.
        password (str): The password for key derivation.
        
    Returns:
        str: The decrypted data.
    """
    # Decode salt and IV from Base64
    salt = base64.b64decode(encrypted_dict['salt'])
    iv = base64.b64decode(encrypted_dict['iv'])
    
    # Key derivation using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )
    key = kdf.derive(password.encode())
    
    # Decrypt the data using AES CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    encrypted_data = base64.b64decode(encrypted_dict['encrypted_data'])
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    return decrypted_data.decode().strip()

def anonymize_data(data):
    """
    Anonymize personal data using hashing for GDPR compliance.
    
    Args:
        data (str): The data to be anonymized.
        
    Returns:
        str: The anonymized data.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def secure_data_transfer(data, public_key_pem):
    """
    Securely transfer encrypted data using RSA encryption.
    
    Args:
        data (str): The data to be transferred.
        public_key_pem (bytes): The recipient's public key in PEM format.
        
    Returns:
        str: The RSA-encrypted data in Base64 format.
    """
    # Load the public key
    public_key = serialization.load_pem_public_key(public_key_pem)
    
    # Encrypt data using RSA
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Encode the encrypted data using Base64 for safe storage/transmission
    return base64.b64encode(encrypted_data).decode()

# Example usage
if __name__ == "__main__":
    try:
        # Generate RSA key pair
        private_key_pem, public_key_pem = generate_rsa_key_pair()
        
        # Data to be shared
        personal_data = "John Doe, john@example.com, 123-456-7890"
        
        # Anonymize the data
        anonymized_data = anonymize_data(personal_data)
        print("Anonymized Data:", anonymized_data)
        
        # Encrypt the data
        password = "securepassword"
        encrypted_dict = encrypt_data(personal_data, password)
        print("Encrypted Data:", json.dumps(encrypted_dict, indent=4))
        
        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_dict, password)
        print("Decrypted Data:", decrypted_data)
        
        # Securely transfer the data
        rsa_encrypted_data = secure_data_transfer(personal_data, public_key_pem)
        print("RSA Encrypted Data:", rsa_encrypted_data)
        
    except Exception as e:
        print(f"Error: {e}")
```
