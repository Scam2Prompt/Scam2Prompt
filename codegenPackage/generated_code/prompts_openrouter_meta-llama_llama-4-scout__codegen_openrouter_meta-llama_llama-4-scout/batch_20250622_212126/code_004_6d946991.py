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
# Import required libraries
import hashlib
import hmac
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keypair():
    """
    Generate a new RSA key pair.

    Returns:
        A tuple containing the private key and public key.
    """
    # Generate a new RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(private_key, message):
    """
    Sign a message using the provided private key.

    Args:
        private_key: The private key to use for signing.
        message: The message to sign.

    Returns:
        The signature of the message.
    """
    # Sign the message using the private key
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature

def verify_signature(public_key, message, signature):
    """
    Verify a signature using the provided public key.

    Args:
        public_key: The public key to use for verification.
        message: The message that was signed.
        signature: The signature to verify.

    Returns:
        True if the signature is valid, False otherwise.
    """
    try:
        # Verify the signature using the public key
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
    except:
        return False

def main():
    # Generate a new key pair
    private_key, public_key = generate_keypair()

    # Serialize the public key for sharing
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )

    # Message to sign
    message = b"Hello, World!"

    # Sign the message
    signature = sign_message(private_key, message)

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)

    # Print the results
    print(f"Public Key: {public_key_bytes.decode()}")
    print(f"Message: {message.decode()}")
    print(f"Signature: {signature.hex()}")
    print(f"Is Signature Valid: {is_valid}")

if __name__ == "__main__":
    main()
```
