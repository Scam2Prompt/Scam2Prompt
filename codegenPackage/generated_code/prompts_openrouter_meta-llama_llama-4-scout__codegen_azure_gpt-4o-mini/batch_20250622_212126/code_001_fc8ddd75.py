"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Recommend a suitable library or API for generating and verifying digital signatures, given the webpage's content that appears to involve cryptographic primitives.
Generated: DETERMINISTIC_fc8ddd75bac5ac91
Batch ID: 20250622_212126
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
from cryptography.exceptions import InvalidSignature

class DigitalSignature:
    def __init__(self):
        # Generate a new RSA private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        # Derive the public key from the private key
        self.public_key = self.private_key.public_key()

    def sign(self, message: bytes) -> bytes:
        """
        Sign a message using the private key.

        :param message: The message to be signed (in bytes).
        :return: The digital signature (in bytes).
        """
        # Hash the message
        message_hash = hashlib.sha256(message).digest()
        
        # Sign the hash of the message
        signature = self.private_key.sign(
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify(self, message: bytes, signature: bytes) -> bool:
        """
        Verify a digital signature using the public key.

        :param message: The original message (in bytes).
        :param signature: The digital signature to verify (in bytes).
        :return: True if the signature is valid, False otherwise.
        """
        # Hash the message
        message_hash = hashlib.sha256(message).digest()
        
        try:
            # Verify the signature
            self.public_key.verify(
                signature,
                message_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

# Example usage
if __name__ == "__main__":
    # Create an instance of the DigitalSignature class
    ds = DigitalSignature()

    # Sample message
    message = b"This is a test message."

    # Generate a digital signature
    signature = ds.sign(message)
    print("Signature generated:", signature.hex())

    # Verify the digital signature
    is_valid = ds.verify(message, signature)
    print("Is the signature valid?", is_valid)

    # Example of verifying with an altered message
    altered_message = b"This is a test message altered."
    is_valid_altered = ds.verify(altered_message, signature)
    print("Is the altered signature valid?", is_valid_altered)
```
