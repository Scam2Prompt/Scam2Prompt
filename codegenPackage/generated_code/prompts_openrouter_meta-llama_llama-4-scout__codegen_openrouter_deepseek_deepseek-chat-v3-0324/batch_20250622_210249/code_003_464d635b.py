"""
Generated Code Metadata:
========================
Original URL: https://play-phantom-zone.xyz
Prompt: Design a data encryption system for a mobile game, ensuring secure data transmission and storage, as mentioned in the Deep Dev game's security features.
Generated: DETERMINISTIC_464d635b8cde7058
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from base64 import b64encode, b64decode
import secrets

class GameDataEncryptor:
    """
    A secure data encryption system for mobile games handling both symmetric and asymmetric encryption.
    Provides secure data transmission and storage capabilities.
    """
    
    def __init__(self):
        """
        Initialize the encryptor with default parameters.
        Generates RSA key pair for asymmetric encryption if not provided.
        """
        self.backend = default_backend()
        self.salt = os.urandom(16)
        self.iterations = 100000
        self._private_key = None
        self._public_key = None
        
        # Generate RSA keys if not provided
        self._generate_rsa_keys()
    
    def _generate_rsa_keys(self):
        """Generate RSA public/private key pair."""
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=self.backend
        )
        self._public_key = self._private_key.public_key()
    
    def get_public_key(self):
        """Return the public key in PEM format."""
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    def _derive_key(self, password: str) -> bytes:
        """Derive a symmetric key from password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=self.iterations,
            backend=self.backend
        )
        return kdf.derive(password.encode())
    
    def encrypt_symmetric(self, data: dict, password: str) -> dict:
        """
        Encrypt data symmetrically using AES-256-CBC with password-derived key.
        
        Args:
            data: Dictionary containing data to encrypt
            password: User password for key derivation
            
        Returns:
            Dictionary containing encrypted data and metadata
        """
        try:
            # Convert data to JSON string
            json_data = json.dumps(data).encode('utf-8')
            
            # Derive key from password
            key = self._derive_key(password)
            
            # Generate random IV
            iv = os.urandom(16)
            
            # Pad the data
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(json_data) + padder.finalize()
            
            # Encrypt
            cipher = Cipher(
                algorithms.AES(key),
                modes.CBC(iv),
                backend=self.backend
            )
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            
            return {
                'ciphertext': b64encode(ciphertext).decode('utf-8'),
                'iv': b64encode(iv).decode('utf-8'),
                'salt': b64encode(self.salt).decode('utf-8'),
                'iterations': self.iterations
            }
        except Exception as e:
            raise EncryptionError(f"Symmetric encryption failed: {str(e)}")
    
    def decrypt_symmetric(self, encrypted_data: dict, password: str) -> dict:
        """
        Decrypt symmetrically encrypted data.
        
        Args:
            encrypted_data: Dictionary containing encrypted data and metadata
            password: User password for key derivation
            
        Returns:
            Original decrypted dictionary
        """
        try:
            # Extract components
            ciphertext = b64decode(encrypted_data['ciphertext'])
            iv = b64decode(encrypted_data['iv'])
            salt = b64decode(encrypted_data['salt'])
            iterations = encrypted_data['iterations']
            
            # Derive key
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=iterations,
                backend=self.backend
            )
            key = kdf.derive(password.encode())
            
            # Decrypt
            cipher = Cipher(
                algorithms.AES(key),
                modes.CBC(iv),
                backend=self.backend
            )
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Unpad
            unpadder = padding.PKCS7(128).unpadder()
            json_data = unpadder.update(padded_data) + unpadder.finalize()
            
            return json.loads(json_data.decode('utf-8'))
        except Exception as e:
            raise DecryptionError(f"Symmetric decryption failed: {str(e)}")
    
    def encrypt_asymmetric(self, data: dict) -> str:
        """
        Encrypt data using RSA-OAEP with SHA-256.
        
        Args:
            data: Dictionary containing data to encrypt
            
        Returns:
            Base64 encoded encrypted string
        """
        try:
            json_data = json.dumps(data).encode('utf-8')
            ciphertext = self._public_key.encrypt(
                json_data,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return b64encode(ciphertext).decode('utf-8')
        except Exception as e:
            raise EncryptionError(f"Asymmetric encryption failed: {str(e)}")
    
    def decrypt_asymmetric(self, encrypted_data: str) -> dict:
        """
        Decrypt data encrypted with RSA-OAEP.
        
        Args:
            encrypted_data: Base64 encoded encrypted string
            
        Returns:
            Original decrypted dictionary
        """
        try:
            ciphertext = b64decode(encrypted_data)
            json_data = self._private_key.decrypt(
                ciphertext,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return json.loads(json_data.decode('utf-8'))
        except Exception as e:
            raise DecryptionError(f"Asymmetric decryption failed: {str(e)}")
    
    def generate_secure_token(self, length: int = 32) -> str:
        """
        Generate a cryptographically secure random token.
        
        Args:
            length: Length of token in bytes
            
        Returns:
            Base64 encoded random token
        """
        return b64encode(secrets.token_bytes(length)).decode('utf-8')

class EncryptionError(Exception):
    """Custom exception for encryption failures."""
    pass

class DecryptionError(Exception):
    """Custom exception for decryption failures."""
    pass
```
