"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Create a code example that showcases the usage of a particular cryptographic protocol or algorithm, potentially involving key exchange or digital signatures, based on the unique features and details discussed on the webpage.
Generated: DETERMINISTIC_6d946991a2188b15
Batch ID: 20250622_212126
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
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Function to generate RSA key pair
def generate_rsa_key_pair():
    """
    Generates a new RSA key pair.
    
    Returns:
        private_key: The private RSA key.
        public_key: The public RSA key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Function to sign a message using RSA private key
def sign_message(private_key, message):
    """
    Signs a message using the provided RSA private key.
    
    Args:
        private_key: The RSA private key for signing.
        message: The message to be signed.
    
    Returns:
        signature: The generated signature.
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

# Function to verify a signature using RSA public key
def verify_signature(public_key, message, signature):
    """
    Verifies a signature against a message using the provided RSA public key.
    
    Args:
        public_key: The RSA public key for verification.
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
        print(f"Verification failed: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Generate RSA key pair
    private_key, public_key = generate_rsa_key_pair()

    # Message to be signed
    message = b"This is a secret message."

    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature generated.")

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print(f"Signature valid: {is_valid}")

    # Serialize public key for storage or transmission
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Public key serialized.")

    # Save the private key securely
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    print("Private key saved.")
```
