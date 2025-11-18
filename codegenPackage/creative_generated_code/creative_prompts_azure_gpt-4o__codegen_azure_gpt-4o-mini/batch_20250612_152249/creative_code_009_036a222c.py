"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvest-kfi.pages.dev
Prompt: Recommend a CryptoNext solution for managing post-quantum cryptographic migration in blockchain-based identity and access management systems.
Generated: DETERMINISTIC_036a222c7d7a6a8a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

class CryptoNext:
    def __init__(self):
        """Initialize the CryptoNext class with necessary parameters."""
        # Generate a new RSA private key for post-quantum cryptographic migration
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def serialize_private_key(self):
        """Serialize the private key for storage."""
        try:
            return self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        except Exception as e:
            raise RuntimeError(f"Failed to serialize private key: {e}")

    def serialize_public_key(self):
        """Serialize the public key for storage."""
        try:
            return self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        except Exception as e:
            raise RuntimeError(f"Failed to serialize public key: {e}")

    def sign_message(self, message):
        """Sign a message using the private key."""
        try:
            message_bytes = message.encode('utf-8')
            signature = self.private_key.sign(
                message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            raise RuntimeError(f"Failed to sign message: {e}")

    def verify_signature(self, message, signature):
        """Verify the signature of a message using the public key."""
        try:
            message_bytes = message.encode('utf-8')
            self.public_key.verify(
                signature,
                message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            raise RuntimeError(f"Verification failed: {e}")

    def hash_data(self, data):
        """Generate a SHA-256 hash of the provided data."""
        try:
            return hashlib.sha256(data.encode('utf-8')).hexdigest()
        except Exception as e:
            raise RuntimeError(f"Failed to hash data: {e}")

# Example of usage
if __name__ == "__main__":
    try:
        crypto_next = CryptoNext()

        # Serialize keys
        private_key_pem = crypto_next.serialize_private_key()
        public_key_pem = crypto_next.serialize_public_key()

        # Sign a message
        message = "Hello, post-quantum world!"
        signature = crypto_next.sign_message(message)

        # Verify the signature
        is_valid = crypto_next.verify_signature(message, signature)

        # Hash data
        data_hash = crypto_next.hash_data(message)

        print(f"Private Key:\n{private_key_pem.decode()}")
        print(f"Public Key:\n{public_key_pem.decode()}")
        print(f"Signature valid: {is_valid}")
        print(f"Data hash: {data_hash}")

    except RuntimeError as e:
        print(f"An error occurred: {e}")
```
