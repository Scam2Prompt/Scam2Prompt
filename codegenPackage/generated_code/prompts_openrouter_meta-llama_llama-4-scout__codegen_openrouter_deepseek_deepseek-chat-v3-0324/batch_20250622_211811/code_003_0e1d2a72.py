"""
Generated Code Metadata:
========================
Original URL: https://daplatform.one
Prompt: "How would you implement data encryption for data in transit and at rest in a data platform?"
Generated: DETERMINISTIC_0e1d2a72671d16ff
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
import base64
import json
from typing import Tuple, Optional

# Constants
SALT_LENGTH = 16
IV_LENGTH = 16
ITERATIONS = 100000
KEY_LENGTH = 32
HMAC_KEY_LENGTH = 32
RSA_KEY_SIZE = 2048

class EncryptionManager:
    """
    Handles encryption and decryption for data at rest and in transit.
    Supports symmetric encryption (AES) and asymmetric encryption (RSA).
    """

    def __init__(self):
        self.backend = default_backend()

    def generate_symmetric_key(self, password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
        """
        Generate a symmetric key using PBKDF2.
        
        Args:
            password: The password to derive the key from.
            salt: Optional salt. If None, a new salt will be generated.
        
        Returns:
            Tuple of (key, salt)
        """
        if salt is None:
            salt = os.urandom(SALT_LENGTH)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=KEY_LENGTH,
            salt=salt,
            iterations=ITERATIONS,
            backend=self.backend
        )
        key = kdf.derive(password.encode())
        return key, salt

    def generate_rsa_key_pair(self) -> Tuple[bytes, bytes]:
        """
        Generate an RSA key pair.
        
        Returns:
            Tuple of (private_key, public_key) in PEM format
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=RSA_KEY_SIZE,
            backend=self.backend
        )
        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        public_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return private_pem, public_pem

    def encrypt_aes(self, data: bytes, key: bytes) -> bytes:
        """
        Encrypt data using AES-CBC with PKCS7 padding.
        
        Args:
            data: Data to encrypt.
            key: Encryption key.
        
        Returns:
            Encrypted data (IV + ciphertext)
        """
        iv = os.urandom(IV_LENGTH)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext

    def decrypt_aes(self, encrypted_data: bytes, key: bytes) -> bytes:
        """
        Decrypt data encrypted with AES-CBC.
        
        Args:
            encrypted_data: IV + ciphertext.
            key: Decryption key.
        
        Returns:
            Decrypted data.
        """
        iv = encrypted_data[:IV_LENGTH]
        ciphertext = encrypted_data[IV_LENGTH:]
        
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()

    def encrypt_rsa(self, data: bytes, public_key_pem: bytes) -> bytes:
        """
        Encrypt data using RSA-OAEP.
        
        Args:
            data: Data to encrypt.
            public_key_pem: Public key in PEM format.
        
        Returns:
            Encrypted data.
        """
        public_key = serialization.load_pem_public_key(
            public_key_pem,
            backend=self.backend
        )
        
        ciphertext = public_key.encrypt(
            data,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_rsa(self, encrypted_data: bytes, private_key_pem: bytes) -> bytes:
        """
        Decrypt data encrypted with RSA-OAEP.
        
        Args:
            encrypted_data: Encrypted data.
            private_key_pem: Private key in PEM format.
        
        Returns:
            Decrypted data.
        """
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None,
            backend=self.backend
        )
        
        return private_key.decrypt(
            encrypted_data,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def generate_hmac(self, data: bytes, hmac_key: bytes) -> bytes:
        """
        Generate HMAC for data integrity verification.
        
        Args:
            data: Data to generate HMAC for.
            hmac_key: HMAC key.
        
        Returns:
            HMAC digest.
        """
        h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=self.backend)
        h.update(data)
        return h.finalize()

    def verify_hmac(self, data: bytes, hmac_key: bytes, signature: bytes) -> bool:
        """
        Verify HMAC for data integrity.
        
        Args:
            data: Data to verify.
            hmac_key: HMAC key.
            signature: Expected HMAC.
        
        Returns:
            True if verification succeeds, False otherwise.
        """
        h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=self.backend)
        h.update(data)
        try:
            h.verify(signature)
            return True
        except:
            return False

    def encrypt_data_at_rest(self, data: dict, password: str) -> dict:
        """
        Encrypt data at rest with AES and include HMAC for integrity.
        
        Args:
            data: Data to encrypt (as dict).
            password: Password for key derivation.
        
        Returns:
            Dictionary containing encrypted data, salt, and HMAC.
        """
        json_data = json.dumps(data).encode()
        
        # Generate keys
        enc_key, salt = self.generate_symmetric_key(password)
        hmac_key = os.urandom(HMAC_KEY_LENGTH)
        
        # Encrypt data
        encrypted_data = self.encrypt_aes(json_data, enc_key)
        
        # Generate HMAC
        hmac_digest = self.generate_hmac(encrypted_data, hmac_key)
        
        return {
            'data': base64.b64encode(encrypted_data).decode(),
            'salt': base64.b64encode(salt).decode(),
            'hmac_key': base64.b64encode(hmac_key).decode(),
            'hmac': base64.b64encode(hmac_digest).decode()
        }

    def decrypt_data_at_rest(self, encrypted_package: dict, password: str) -> dict:
        """
        Decrypt data at rest and verify HMAC.
        
        Args:
            encrypted_package: Encrypted data package.
            password: Password for key derivation.
        
        Returns:
            Decrypted data as dict.
        
        Raises:
            ValueError: If HMAC verification fails.
        """
        # Decode base64 fields
        encrypted_data = base64.b64decode(encrypted_package['data'])
        salt = base64.b64decode(encrypted_package['salt'])
        hmac_key = base64.b64decode(encrypted_package['hmac_key'])
        hmac_digest = base64.b64decode(encrypted_package['hmac'])
        
        # Verify HMAC
        if not self.verify_hmac(encrypted_data, hmac_key, hmac_digest):
            raise ValueError("HMAC verification failed - data may be corrupted")
        
        # Derive key and decrypt
        enc_key, _ = self.generate_symmetric_key(password, salt)
        decrypted_data = self.decrypt_aes(encrypted_data, enc_key)
        
        return json.loads(decrypted_data.decode())

    def encrypt_data_in_transit(self,
