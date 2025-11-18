"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wildhorse-llc.com
Prompt: Provide code to implement end-to-end encryption for user data on Wildhorse LLC's platform, leveraging hybrid encryption algorithms.
Generated: DETERMINISTIC_02a5b8e3bdb2a590
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import constant_time
from base64 import b64encode, b64decode

class HybridEncryption:
    def __init__(self):
        # Generate RSA key pair for asymmetric encryption
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self._public_key = self._private_key.public_key()
    
    def get_public_key(self):
        """
        Serialize and return the public key for distribution.
        """
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    def encrypt(self, plaintext: str, recipient_public_key: bytes) -> dict:
        """
        Encrypts the given plaintext using hybrid encryption (AES + RSA).
        
        Args:
            plaintext (str): The data to encrypt.
            recipient_public_key (bytes): The public key of the recipient.

        Returns:
            dict: Encrypted data containing the AES encrypted message, IV, and RSA-encrypted AES key.
        """
        try:
            # Convert plaintext to bytes
            plaintext_bytes = plaintext.encode('utf-8')

            # Generate a symmetric key for AES encryption
            aes_key = os.urandom(32)  # 256-bit AES key

            # Generate IV for AES (16 bytes for AES block size)
            iv = os.urandom(16)

            # Encrypt the plaintext using AES
            cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext_bytes) + encryptor.finalize()

            # Load recipient's public key
            recipient_key = serialization.load_pem_public_key(recipient_public_key)

            # Encrypt the AES key using RSA
            encrypted_aes_key = recipient_key.encrypt(
                aes_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            return {
                'ciphertext': b64encode(ciphertext).decode('utf-8'),
                'iv': b64encode(iv).decode('utf-8'),
                'rsa_encrypted_key': b64encode(encrypted_aes_key).decode('utf-8')
            }
        except Exception as e:
            # Handle encryption errors gracefully
            raise ValueError(f"Encryption error: {e}")
    
    def decrypt(self, encrypted_data: dict) -> str:
        """
        Decrypts the given encrypted data using hybrid encryption (AES + RSA).
        
        Args:
            encrypted_data (dict): The encrypted data containing:
                - ciphertext: AES encrypted data
                - iv: Initialization vector for AES
                - rsa_encrypted_key: RSA-encrypted AES key

        Returns:
            str: Decrypted plaintext.
        """
        try:
            # Decode base64-encoded components
            ciphertext = b64decode(encrypted_data['ciphertext'])
            iv = b64decode(encrypted_data['iv'])
            rsa_encrypted_key = b64decode(encrypted_data['rsa_encrypted_key'])

            # Decrypt the AES key using RSA
            aes_key = self._private_key.decrypt(
                rsa_encrypted_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Decrypt the ciphertext using AES
            cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
            decryptor = cipher.decryptor()
            plaintext_bytes = decryptor.update(ciphertext) + decryptor.finalize()

            return plaintext_bytes.decode('utf-8')
        except Exception as e:
            # Handle decryption errors gracefully
            raise ValueError(f"Decryption error: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize hybrid encryption system
    encryption_system = HybridEncryption()

    # Generate and share the public key
    public_key = encryption_system.get_public_key()

    # Encrypt data
    plaintext = "Sensitive user data for Wildhorse LLC"
    encrypted_data = encryption_system.encrypt(plaintext, public_key)

    print("Encrypted Data:", encrypted_data)

    # Decrypt data
    decrypted_data = encryption_system.decrypt(encrypted_data)

    print("Decrypted Data:", decrypted_data)

```
