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
"""
This script demonstrates the use of the Elliptic Curve Digital Signature Algorithm (ECDSA) for signing and verifying messages.
It uses the `cryptography` library, which is a widely-used library for cryptographic operations in Python.
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

def generate_key_pair():
    """
    Generate an ECDSA private-public key pair using the SECP256R1 curve.
    Returns:
        private_key: The private key object.
        public_key: The corresponding public key object.
    """
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    """
    Sign a message using the provided private key.
    Args:
        private_key: The ECDSA private key object.
        message: The message to be signed (bytes).
    Returns:
        signature: The generated signature (bytes).
    """
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature

def verify_signature(public_key, message, signature):
    """
    Verify a signature using the provided public key.
    Args:
        public_key: The ECDSA public key object.
        message: The original message (bytes).
        signature: The signature to be verified (bytes).
    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False

if __name__ == "__main__":
    # Example usage
    try:
        # Generate key pair
        private_key, public_key = generate_key_pair()

        # Message to be signed
        message = b"Secure message using ECDSA"

        # Sign the message
        signature = sign_message(private_key, message)
        print("Signature generated successfully.")

        # Verify the signature
        is_valid = verify_signature(public_key, message, signature)
        if is_valid:
            print("Signature verification succeeded.")
        else:
            print("Signature verification failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
