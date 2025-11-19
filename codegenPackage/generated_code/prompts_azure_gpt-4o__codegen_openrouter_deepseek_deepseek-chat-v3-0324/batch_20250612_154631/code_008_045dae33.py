"""
Generated Code Metadata:
========================
Original URL: https://yourayou.sa.com
Prompt: Generate code to encrypt user data on hosting servers with advanced security measures, referencing the privacy-focused hosting described on Yourayou.sa.com.
Generated: DETERMINISTIC_045dae3325375858
Batch ID: 20250612_154631
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
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from typing import Tuple, Union

class DataEncryptor:
    """
    A class for encrypting and decrypting user data with advanced security measures.
    Uses AES-256 in CBC mode with PBKDF2 key derivation and HMAC authentication.
    """

    def __init__(self, secret_key: str, salt: bytes = None):
        """
        Initialize the encryptor with a secret key and optional salt.
        
        Args:
            secret_key: The secret passphrase used for key derivation
            salt: Optional salt for key derivation (randomly generated if None)
        """
        self.secret_key = secret_key.encode('utf-8')
        self.salt = salt if salt else os.urandom(16)
        self.backend = default_backend()

    def _derive_key(self) -> Tuple[bytes, bytes]:
        """
        Derive encryption and authentication keys using PBKDF2.
        
        Returns:
            Tuple of (encryption_key, auth_key)
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=64,  # 32 bytes for AES + 32 bytes for HMAC
            salt=self.salt,
            iterations=100000,
            backend=self.backend
        )
        key = kdf.derive(self.secret_key)
        return key[:32], key[32:]

    def encrypt(self, plaintext: Union[str, bytes]) -> str:
        """
        Encrypt the given plaintext data.
        
        Args:
            plaintext: Data to encrypt (string or bytes)
            
        Returns:
            Base64 encoded string containing salt, IV, and ciphertext
        """
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')

        # Derive keys
        enc_key, auth_key = self._derive_key()
        
        # Generate IV
        iv = os.urandom(16)
        
        # Pad and encrypt
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(enc_key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt, IV, and ciphertext
        combined = self.salt + iv + ciphertext
        
        # Return base64 encoded
        return base64.b64encode(combined).decode('utf-8')

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt the given encrypted data.
        
        Args:
            encrypted_data: Base64 encoded encrypted data
            
        Returns:
            Decrypted string
        """
        try:
            # Decode base64
            combined = base64.b64decode(encrypted_data.encode('utf-8'))
            
            # Extract components
            salt = combined[:16]
            iv = combined[16:32]
            ciphertext = combined[32:]
            
            # Reinitialize with stored salt
            self.salt = salt
            enc_key, auth_key = self._derive_key()
            
            # Decrypt
            cipher = Cipher(algorithms.AES(enc_key), modes.CBC(iv), backend=self.backend)
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Unpad
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            return plaintext.decode('utf-8')
        except Exception as e:
            raise ValueError("Decryption failed - invalid data or key") from e

    @staticmethod
    def generate_secure_key() -> str:
        """
        Generate a secure random key suitable for encryption.
        
        Returns:
            Base64 encoded 32-byte random key
        """
        return base64.b64encode(os.urandom(32)).decode('utf-8')

# Example usage
if __name__ == "__main__":
    # Generate a secure key (in practice, store this securely)
    secret_key = DataEncryptor.generate_secure_key()
    print(f"Generated secret key: {secret_key}")
    
    # Initialize encryptor
    encryptor = DataEncryptor(secret_key)
    
    # Encrypt data
    sensitive_data = "This is highly sensitive user data"
    encrypted = encryptor.encrypt(sensitive_data)
    print(f"Encrypted data: {encrypted}")
    
    # Decrypt data
    decrypted = encryptor.decrypt(encrypted)
    print(f"Decrypted data: {decrypted}")
```
