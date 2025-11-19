"""
Generated Code Metadata:
========================
Original URL: https://amf-verification.org
Prompt: Generate a code example for a cryptographically secure authentication protocol using digital signatures and asymmetric cryptography for certifying unique control over private keys, as described in the AMF validation system.
Generated: DETERMINISTIC_1a694ca9b4b5bf21
Batch ID: 20250622_212746
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
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate RSA key pair
def generate_key_pair():
    """
    Generates a new RSA key pair (private and public keys).
    Returns:
        private_key: RSA private key object
        public_key: RSA public key object
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Serialize keys for storage or transmission
def serialize_keys(private_key, public_key):
    """
    Serializes the private and public keys to PEM format.
    Args:
        private_key: RSA private key object
        public_key: RSA public key object
    Returns:
        private_pem: Serialized private key in PEM format
        public_pem: Serialized public key in PEM format
    """
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

# Sign a message using the private key
def sign_message(private_key, message):
    """
    Signs a message using the RSA private key.
    Args:
        private_key: RSA private key object
        message: Message to be signed (bytes)
    Returns:
        signature: Digital signature of the message
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

# Verify a signature using the public key
def verify_signature(public_key, message, signature):
    """
    Verifies a digital signature using the RSA public key.
    Args:
        public_key: RSA public key object
        message: Original message (bytes)
        signature: Digital signature to verify
    Returns:
        is_valid: Boolean indicating whether the signature is valid
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
        # Signature verification failed
        return False

# Example usage
if __name__ == "__main__":
    # Generate key pair
    private_key, public_key = generate_key_pair()

    # Serialize keys
    private_pem, public_pem = serialize_keys(private_key, public_key)
    print("Private Key (PEM):\n", private_pem.decode())
    print("Public Key (PEM):\n", public_pem.decode())

    # Message to be signed
    message = b"Authenticate this message securely."

    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature (Base64):", base64.b64encode(signature).decode())

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("Is the signature valid?", is_valid)
```
