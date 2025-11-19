"""
Generated Code Metadata:
========================
Original URL: https://mymonero.co
Prompt: Explain how to implement local encryption for app data in a MyMonero-like application, ensuring user privacy and security.
Generated: DETERMINISTIC_e2d4740ad75d5f42
Batch ID: 20250612_155340
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
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import scrypt

class LocalDataEncryptor:
    """
    A class to handle local encryption and decryption of sensitive data using AES-256-GCM.
    Provides secure key derivation using scrypt and data encryption/decryption functionality.
    """
    
    def __init__(self):
        self.SALT_SIZE = 16  # bytes
        self.NONCE_SIZE = 12  # bytes for GCM
        self.TAG_SIZE = 16  # bytes for GCM
        self.SCRYPT_N = 2**14
        self.SCRYPT_R = 8
        self.SCRYPT_P = 1
        self.DERIVED_KEY_LEN = 32  # bytes for AES-256
    
    def generate_salt(self):
        """Generate a random salt for key derivation."""
        return get_random_bytes(self.SALT_SIZE)
    
    def derive_key(self, password: str, salt: bytes) -> bytes:
        """
        Derive a cryptographic key from a password using scrypt.
        
        Args:
            password: User-provided password
            salt: Random salt for key derivation
            
        Returns:
            Derived key bytes
        """
        if not password or not salt:
            raise ValueError("Password and salt must be provided")
            
        return scrypt(
            password.encode('utf-8'),
            salt,
            key_len=self.DERIVED_KEY_LEN,
            N=self.SCRYPT_N,
            r=self.SCRYPT_R,
            p=self.SCRYPT_P
        )
    
    def encrypt_data(self, plaintext: str, key: bytes) -> str:
        """
        Encrypt data using AES-256-GCM.
        
        Args:
            plaintext: Data to encrypt
            key: Encryption key (must be 32 bytes)
            
        Returns:
            Base64 encoded string containing nonce + ciphertext + tag
        """
        if not plaintext or not key:
            raise ValueError("Plaintext and key must be provided")
        if len(key) != self.DERIVED_KEY_LEN:
            raise ValueError(f"Key must be {self.DERIVED_KEY_LEN} bytes")
            
        nonce = get_random_bytes(self.NONCE_SIZE)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
        
        # Combine nonce + ciphertext + tag for storage
        encrypted_data = nonce + ciphertext + tag
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    def decrypt_data(self, encrypted_data: str, key: bytes) -> str:
        """
        Decrypt data using AES-256-GCM.
        
        Args:
            encrypted_data: Base64 encoded encrypted data (nonce + ciphertext + tag)
            key: Decryption key (must be 32 bytes)
            
        Returns:
            Decrypted plaintext string
            
        Raises:
            ValueError: If decryption fails (invalid key or tampered data)
        """
        if not encrypted_data or not key:
            raise ValueError("Encrypted data and key must be provided")
        if len(key) != self.DERIVED_KEY_LEN:
            raise ValueError(f"Key must be {self.DERIVED_KEY_LEN} bytes")
            
        try:
            encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))
            nonce = encrypted_data[:self.NONCE_SIZE]
            ciphertext = encrypted_data[self.NONCE_SIZE:-self.TAG_SIZE]
            tag = encrypted_data[-self.TAG_SIZE:]
            
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            return plaintext.decode('utf-8')
        except (ValueError, KeyError) as e:
            raise ValueError("Decryption failed - invalid key or corrupted data") from e
    
    def secure_delete(self, data: bytes):
        """
        Attempt to securely delete sensitive data from memory.
        Note: This is not guaranteed in Python due to garbage collection.
        """
        if data:
            for i in range(len(data)):
                data[i:i+1] = b'\x00'  # Overwrite with zeros


# Example usage
if __name__ == "__main__":
    encryptor = LocalDataEncryptor()
    
    # Simulate user setup
    user_password = "my_secure_password_123"
    salt = encryptor.generate_salt()
    encryption_key = encryptor.derive_key(user_password, salt)
    
    # Encrypt sensitive data
    sensitive_data = "My secret wallet data"
    encrypted = encryptor.encrypt_data(sensitive_data, encryption_key)
    print(f"Encrypted data: {encrypted}")
    
    # Decrypt data
    try:
        decrypted = encryptor.decrypt_data(encrypted, encryption_key)
        print(f"Decrypted data: {decrypted}")
    except ValueError as e:
        print(f"Decryption error: {e}")
    
    # Clean up
    encryptor.secure_delete(encryption_key)
```
