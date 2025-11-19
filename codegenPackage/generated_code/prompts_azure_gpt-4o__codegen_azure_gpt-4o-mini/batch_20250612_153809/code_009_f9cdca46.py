"""
Generated Code Metadata:
========================
Original URL: https://saitachaincoin.live
Prompt: Provide code to implement cryptographic algorithms for securing transactions and ensuring data integrity on SaitaChain.
Generated: DETERMINISTIC_f9cdca464ac78eb0
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

class CryptoUtils:
    """
    A utility class for cryptographic operations to secure transactions and ensure data integrity.
    """

    @staticmethod
    def generate_key_pair():
        """
        Generates a public/private RSA key pair.
        
        Returns:
            private_key: The private key.
            public_key: The public key.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_public_key(public_key):
        """
        Serializes the public key to PEM format.
        
        Args:
            public_key: The public key to serialize.
        
        Returns:
            str: The serialized public key in PEM format.
        """
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def sign_message(private_key, message):
        """
        Signs a message using the provided private key.
        
        Args:
            private_key: The private key to sign the message.
            message: The message to sign.
        
        Returns:
            bytes: The signature of the message.
        """
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    @staticmethod
    def verify_signature(public_key, message, signature):
        """
        Verifies the signature of a message using the provided public key.
        
        Args:
            public_key: The public key to verify the signature.
            message: The original message.
            signature: The signature to verify.
        
        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

    @staticmethod
    def hash_message(message):
        """
        Creates a SHA-256 hash of the message.
        
        Args:
            message: The message to hash.
        
        Returns:
            str: The hexadecimal representation of the hash.
        """
        return hashlib.sha256(message).hexdigest()

# Example usage
if __name__ == "__main__":
    # Generate key pair
    private_key, public_key = CryptoUtils.generate_key_pair()
    
    # Serialize public key
    public_key_pem = CryptoUtils.serialize_public_key(public_key)
    print("Public Key (PEM):")
    print(public_key_pem)

    # Message to be signed
    message = b"Secure transaction data"
    
    # Hash the message
    message_hash = CryptoUtils.hash_message(message)
    print(f"Message Hash: {message_hash}")

    # Sign the message
    signature = CryptoUtils.sign_message(private_key, message)
    print(f"Signature: {signature.hex()}")

    # Verify the signature
    is_valid = CryptoUtils.verify_signature(public_key, message, signature)
    print(f"Is the signature valid? {is_valid}")
```
