"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icrossingappxyz.com
Prompt: Provide a Python implementation for encrypting data during transmission, as described in the "Identitas Kependudukan Digital" app's security practices.
Generated: DETERMINISTIC_49e4d6ee876ccba9
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

class EncryptionService:
    def __init__(self):
        # Generate a private-public key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def encrypt_data(self, plaintext: str) -> str:
        """Encrypts plaintext using the public key."""
        try:
            ciphertext = self.public_key.encrypt(
                plaintext.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            # Encode ciphertext to base64 for transmission
            return base64.b64encode(ciphertext).decode()
        except Exception as e:
            raise RuntimeError("Encryption failed") from e

    def decrypt_data(self, ciphertext_b64: str) -> str:
        """Decrypts base64 encoded ciphertext using the private key."""
        try:
            # Decode the base64 encoded ciphertext
            ciphertext = base64.b64decode(ciphertext_b64.encode())
            plaintext = self.private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return plaintext.decode()
        except (ValueError, InvalidSignature) as e:
            raise RuntimeError("Decryption failed") from e

    def get_public_key(self) -> str:
        """Returns the public key in PEM format."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

# Example usage
if __name__ == "__main__":
    encryption_service = EncryptionService()
    
    # Get public key for sharing
    public_key = encryption_service.get_public_key()
    print("Public Key:\n", public_key)

    # Example data to encrypt
    data_to_encrypt = "Sensitive information"
    
    # Encrypt the data
    encrypted_data = encryption_service.encrypt_data(data_to_encrypt)
    print("Encrypted Data:\n", encrypted_data)

    # Decrypt the data
    decrypted_data = encryption_service.decrypt_data(encrypted_data)
    print("Decrypted Data:\n", decrypted_data)
```
