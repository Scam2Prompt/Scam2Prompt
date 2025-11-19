"""
Generated Code Metadata:
========================
Original URL: https://sundusartjrny.pages.dev
Prompt: Generate a guide on how to ensure end-to-end encryption while using JRNY GALLERY for digital art transactions.
Generated: DETERMINISTIC_d9b99037cc7f0957
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# End-to-End Encryption for JRNY GALLERY Digital Art Transactions

```python
"""
This module provides end-to-end encryption utilities for secure digital art transactions
in JRNY GALLERY. It handles key generation, encryption, and decryption of art files and
transaction metadata.
"""

import os
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from typing import Tuple, Dict, Optional

class EncryptionManager:
    """
    Handles all encryption/decryption operations for JRNY GALLERY transactions.
    Uses hybrid encryption: RSA for key exchange and AES for bulk data encryption.
    """
    
    def __init__(self):
        self.backend = default_backend()
    
    def generate_key_pair(self) -> Tuple[bytes, bytes]:
        """
        Generate RSA key pair for asymmetric encryption.
        Returns (private_key, public_key) as PEM-encoded bytes.
        """
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=4096,
                backend=self.backend
            )
            public_key = private_key.public_key()
            
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
        except Exception as e:
            raise EncryptionError("Failed to generate key pair") from e
    
    def encrypt_art_file(self, file_data: bytes, public_key_pem: bytes) -> Dict[str, str]:
        """
        Encrypt digital art file using hybrid encryption.
        Returns dictionary containing encrypted data and metadata.
        """
        try:
            # Generate random symmetric key
            symmetric_key = os.urandom(32)
            iv = os.urandom(16)
            
            # Encrypt file data with AES
            cipher = Cipher(
                algorithms.AES(symmetric_key),
                modes.CBC(iv),
                backend=self.backend
            )
            encryptor = cipher.encryptor()
            
            # Pad data to AES block size
            pad_length = 16 - (len(file_data) % 16)
            padded_data = file_data + bytes([pad_length] * pad_length)
            
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            
            # Encrypt symmetric key with RSA
            public_key = serialization.load_pem_public_key(
                public_key_pem,
                backend=self.backend
            )
            
            encrypted_key = public_key.encrypt(
                symmetric_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            return {
                'encrypted_data': b64encode(encrypted_data).decode('utf-8'),
                'encrypted_key': b64encode(encrypted_key).decode('utf-8'),
                'iv': b64encode(iv).decode('utf-8'),
                'encryption_version': '1.0'
            }
        except Exception as e:
            raise EncryptionError("Failed to encrypt art file") from e
    
    def decrypt_art_file(self, encrypted_package: Dict[str, str], private_key_pem: bytes) -> bytes:
        """
        Decrypt digital art file using hybrid encryption.
        Returns original file data as bytes.
        """
        try:
            # Decode base64 fields
            encrypted_data = b64decode(encrypted_package['encrypted_data'])
            encrypted_key = b64decode(encrypted_package['encrypted_key'])
            iv = b64decode(encrypted_package['iv'])
            
            # Decrypt symmetric key with RSA
            private_key = serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=self.backend
            )
            
            symmetric_key = private_key.decrypt(
                encrypted_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            # Decrypt file data with AES
            cipher = Cipher(
                algorithms.AES(symmetric_key),
                modes.CBC(iv),
                backend=self.backend
            )
            decryptor = cipher.decryptor()
            
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
            
            # Remove padding
            pad_length = decrypted_data[-1]
            if pad_length > 16:
                raise EncryptionError("Invalid padding")
                
            return decrypted_data[:-pad_length]
        except Exception as e:
            raise EncryptionError("Failed to decrypt art file") from e
    
    def encrypt_metadata(self, metadata: dict, public_key_pem: bytes) -> str:
        """
        Encrypt transaction metadata (JSON) using RSA.
        Returns base64-encoded encrypted data.
        """
        try:
            public_key = serialization.load_pem_public_key(
                public_key_pem,
                backend=self.backend
            )
            
            json_data = json.dumps(metadata).encode('utf-8')
            
            # RSA can only encrypt data smaller than key size, so we chunk it
            chunk_size = 400  # conservative for 4096-bit key
            encrypted_chunks = []
            
            for i in range(0, len(json_data), chunk_size):
                chunk = json_data[i:i+chunk_size]
                encrypted_chunk = public_key.encrypt(
                    chunk,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                encrypted_chunks.append(encrypted_chunk)
            
            return b64encode(b''.join(encrypted_chunks)).decode('utf-8')
        except Exception as e:
            raise EncryptionError("Failed to encrypt metadata") from e
    
    def decrypt_metadata(self, encrypted_metadata: str, private_key_pem: bytes) -> dict:
        """
        Decrypt transaction metadata (JSON) using RSA.
        Returns original metadata as dictionary.
        """
        try:
            private_key = serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=self.backend
            )
            
            encrypted_data = b64decode(encrypted_metadata)
            
            # RSA decryption chunk size is key size in bytes
            chunk_size = 512  # 4096 bits = 512 bytes
            decrypted_chunks = []
            
            for i in range(0, len(encrypted_data), chunk_size):
                chunk = encrypted_data[i:i+chunk_size]
                decrypted_chunk = private_key.decrypt(
                    chunk,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                decrypted_chunks.append(decrypted_chunk)
            
            json_data = b''.join(decrypted_chunks).decode('utf-8')
            return json.loads(json_data)
        except Exception as e:
            raise EncryptionError("Failed to decrypt metadata") from e

class EncryptionError(Exception):
    """Custom exception for encryption-related errors"""
    pass

# Example usage (would be in separate module in production)
if __name__ == "__main__":
    # Initialize encryption manager
    manager = EncryptionManager()
    
    # Generate key pairs for artist and buyer
    artist_private, artist_public = manager.generate_key_pair()
    buyer_private, buyer_public = manager.generate_key_pair()
    
    # Simulate art file
    art_file = b"Digital art content goes here..."
    
    # Artist encrypts art file with buyer's public key
    encrypted_package = manager.encrypt_art_file(art_file, buyer_public)
    
    # Buyer decrypts art file
    decrypted_art = manager.decrypt_art_file(encrypted_package, buyer_private)
    
    # Verify decryption worked
    assert decrypted_art == art_file, "Decryption failed"
    
    # Encrypt transaction metadata
    metadata = {
        "artist_id": "artist123",
        "buyer_id": "buyer456",
        "art_id": "art789",
        "price": 100.00,
        "currency": "USD"
    }
    
    encrypted_metadata = manager.encrypt_metadata(metadata, buyer_public)
    decrypted_metadata = manager.decrypt_metadata(encrypted_metadata, buyer_private)
    
    # Verify metadata decryption
    assert decrypted_metadata
