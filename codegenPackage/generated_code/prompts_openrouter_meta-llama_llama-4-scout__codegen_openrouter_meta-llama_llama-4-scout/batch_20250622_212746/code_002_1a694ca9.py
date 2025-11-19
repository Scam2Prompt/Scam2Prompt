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
import hashlib
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

def generate_keypair():
    # Generate a new RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return key

def get_public_key(key):
    # Get the public key from the private key
    return key.public_key()

def sign_message(key, message):
    # Sign a message with the private key
    signature = key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    # Verify a signature with the public key
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def serialize_public_key(public_key):
    # Serialize the public key to PEM format
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def deserialize_public_key(public_key_pem):
    # Deserialize a public key from PEM format
    return serialization.load_pem_public_key(
        public_key_pem,
    )

def main():
    # Generate a new key pair
    private_key = generate_keypair()
    public_key = get_public_key(private_key)

    # Serialize the public key
    public_key_pem = serialize_public_key(public_key)

    # Deserialize the public key
    deserialized_public_key = deserialize_public_key(public_key_pem)

    # Message to sign
    message = "Hello, World!"

    # Sign the message
    signature = sign_message(private_key, message)

    # Verify the signature
    is_valid = verify_signature(deserialized_public_key, message, signature)

    print(f"Is signature valid? {is_valid}")

    # Error handling example
    try:
        invalid_signature = b"Invalid signature"
        verify_signature(deserialized_public_key, message, invalid_signature)
    except InvalidSignature:
        print("Caught InvalidSignature exception")

if __name__ == "__main__":
    main()
```
