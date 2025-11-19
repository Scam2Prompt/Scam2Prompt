"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.creatorlink.net
Prompt: Explain the role of end-to-end encryption in Wallet Connect and how it ensures secure transactions and data transfer between wallets and dApps.
Generated: DETERMINISTIC_45da9d381e561674
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import json

class WalletConnectEncryption:
    """
    Implements end-to-end encryption for Wallet Connect protocol.
    Handles key generation, encryption, and decryption of messages.
    """
    
    def __init__(self):
        """
        Initialize with default parameters for ECDH key exchange and AES encryption.
        """
        self.curve = ec.SECP256K1()
        self.aes_key_length = 32
        self.iv_length = 16
        
    def generate_key_pair(self):
        """
        Generate a new ECDH key pair for the session.
        
        Returns:
            tuple: (private_key, public_key) in bytes format
        """
        private_key = ec.generate_private_key(self.curve, default_backend())
        public_key = private_key.public_key()
        
        priv_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        pub_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return priv_bytes, pub_bytes
    
    def derive_shared_secret(self, private_key_bytes, peer_public_key_bytes):
        """
        Derive shared secret using ECDH key exchange.
        
        Args:
            private_key_bytes: Local private key in bytes
            peer_public_key_bytes: Peer's public key in bytes
            
        Returns:
            bytes: Shared secret derived from ECDH
        """
        try:
            private_key = serialization.load_pem_private_key(
                private_key_bytes,
                password=None,
                backend=default_backend()
            )
            
            peer_public_key = serialization.load_pem_public_key(
                peer_public_key_bytes,
                backend=default_backend()
            )
            
            shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
            
            # Derive encryption key using HKDF
            derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=self.aes_key_length,
                salt=None,
                info=b'walletconnect',
                backend=default_backend()
            ).derive(shared_secret)
            
            return derived_key
        except Exception as e:
            raise ValueError(f"Key derivation failed: {str(e)}")
    
    def encrypt_message(self, key, message):
        """
        Encrypt message using AES-256-GCM.
        
        Args:
            key: Encryption key derived from shared secret
            message: Message to encrypt (string or bytes)
            
        Returns:
            dict: Dictionary containing iv, ciphertext, and tag
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
            
        iv = os.urandom(self.iv_length)
        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        
        return {
            'iv': iv.hex(),
            'ciphertext': ciphertext.hex(),
            'tag': encryptor.tag.hex()
        }
    
    def decrypt_message(self, key, encrypted_data):
        """
        Decrypt message using AES-256-GCM.
        
        Args:
            key: Encryption key derived from shared secret
            encrypted_data: Dictionary containing iv, ciphertext, and tag
            
        Returns:
            bytes: Decrypted message
        """
        try:
            iv = bytes.fromhex(encrypted_data['iv'])
            ciphertext = bytes.fromhex(encrypted_data['ciphertext'])
            tag = bytes.fromhex(encrypted_data['tag'])
            
            cipher = Cipher(
                algorithms.AES(key),
                modes.GCM(iv, tag),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            return plaintext
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
    
    def secure_transaction(self, private_key, peer_public_key, transaction_data):
        """
        Complete secure transaction flow: derive key, encrypt, and return encrypted payload.
        
        Args:
            private_key: Local private key
            peer_public_key: Peer's public key
            transaction_data: Transaction data to encrypt
            
        Returns:
            dict: Encrypted transaction payload
        """
        try:
            shared_key = self.derive_shared_secret(private_key, peer_public_key)
            encrypted = self.encrypt_message(shared_key, json.dumps(transaction_data))
            return encrypted
        except Exception as e:
            raise ValueError(f"Secure transaction failed: {str(e)}")
```
