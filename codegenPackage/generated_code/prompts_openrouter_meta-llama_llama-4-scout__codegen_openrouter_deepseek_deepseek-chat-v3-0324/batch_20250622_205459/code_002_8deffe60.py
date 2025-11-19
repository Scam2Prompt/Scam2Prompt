"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Explain how to implement a secure communication system between two parties, like QRubi's connection between the finder and the owner of a lost object.
Generated: DETERMINISTIC_8deffe6026e8f11d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import hmac
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

class SecureCommunication:
    """
    Implements secure communication between two parties using hybrid encryption.
    Combines asymmetric encryption for key exchange with symmetric encryption for data.
    """
    
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.peer_public_key = None
        self.session_key = None
        self.salt = os.urandom(16)
        
    def generate_key_pair(self):
        """Generate RSA key pair for asymmetric encryption."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        
    def serialize_public_key(self):
        """Serialize public key for transmission."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
    def load_peer_public_key(self, pem_data):
        """Load peer's public key from PEM data."""
        self.peer_public_key = serialization.load_pem_public_key(
            pem_data,
            backend=default_backend()
        )
        
    def generate_session_key(self):
        """Generate a random session key for symmetric encryption."""
        self.session_key = os.urandom(32)
        return self.session_key
        
    def encrypt_session_key(self):
        """Encrypt session key with peer's public key."""
        if not self.peer_public_key:
            raise ValueError("Peer public key not loaded")
            
        return self.peer_public_key.encrypt(
            self.session_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
    def decrypt_session_key(self, encrypted_key):
        """Decrypt session key with our private key."""
        if not self.private_key:
            raise ValueError("Private key not generated")
            
        return self.private_key.decrypt(
            encrypted_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
    def derive_key(self, password, salt=None):
        """Derive a key from a password using PBKDF2."""
        if not salt:
            salt = self.salt
            
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())
        
    def encrypt_message(self, message, key=None):
        """Encrypt a message using AES-CBC with PKCS7 padding."""
        if not key:
            if not self.session_key:
                raise ValueError("No session key available")
            key = self.session_key
            
        iv = os.urandom(16)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()
        
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        return iv + ciphertext
        
    def decrypt_message(self, encrypted_message, key=None):
        """Decrypt a message encrypted with AES-CBC."""
        if not key:
            if not self.session_key:
                raise ValueError("No session key available")
            key = self.session_key
            
        iv = encrypted_message[:16]
        ciphertext = encrypted_message[16:]
        
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        unpadder = padding.PKCS7(128).unpadder()
        message = unpadder.update(padded_data) + unpadder.finalize()
        
        return message.decode()
        
    def generate_hmac(self, message, key=None):
        """Generate HMAC for message integrity verification."""
        if not key:
            if not self.session_key:
                raise ValueError("No session key available")
            key = self.session_key
            
        return hmac.new(key, message.encode(), hashlib.sha256).digest()
        
    def verify_hmac(self, message, received_hmac, key=None):
        """Verify HMAC for message integrity."""
        if not key:
            if not self.session_key:
                raise ValueError("No session key available")
            key = self.session_key
            
        expected_hmac = hmac.new(key, message.encode(), hashlib.sha256).digest()
        return hmac.compare_digest(expected_hmac, received_hmac)
        
    def secure_send(self, message):
        """Package message with encryption and integrity checks."""
        encrypted = self.encrypt_message(message)
        message_hmac = self.generate_hmac(encrypted.hex())
        return json.dumps({
            'data': encrypted.hex(),
            'hmac': message_hmac.hex()
        })
        
    def secure_receive(self, package):
        """Unpackage and verify received message."""
        try:
            package_data = json.loads(package)
            encrypted_data = bytes.fromhex(package_data['data'])
            received_hmac = bytes.fromhex(package_data['hmac'])
            
            if not self.verify_hmac(encrypted_data.hex(), received_hmac):
                raise ValueError("HMAC verification failed")
                
            return self.decrypt_message(encrypted_data)
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            raise ValueError(f"Invalid package format: {str(e)}")
```
