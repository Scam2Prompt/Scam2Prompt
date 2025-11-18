"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amf-verification.org
Prompt: Recommend libraries or APIs to implement cryptographic authentication using asymmetric cryptography and digital signatures, as described in the AMF wallet validation system.
Generated: DETERMINISTIC_c4f2bb49a465ab93
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code demonstrating cryptographic authentication using asymmetric cryptography and digital signatures. This implementation uses the `cryptography` library, which is a widely recommended library for cryptographic operations in Python.

```python
"""
Cryptographic Authentication using Asymmetric Cryptography and Digital Signatures.

This example demonstrates:
1. Key generation (private/public keys).
2. Signing a message with the private key.
3. Verifying the signature using the public key.

Requirements:
Install `cryptography` library:
    pip install cryptography
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    PrivateFormat,
    NoEncryption
)
from cryptography.exceptions import InvalidSignature


class CryptographicAuthentication:
    """A class to manage asymmetric cryptography and digital signatures."""

    def __init__(self):
        """
        Initialize the class by generating a new RSA key pair.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def sign_message(self, message: bytes) -> bytes:
        """
        Sign a message using the private key.

        Args:
            message (bytes): The message to be signed.

        Returns:
            bytes: The signature of the message.
        """
        # Generate the digital signature
        signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, message: bytes, signature: bytes) -> bool:
        """
        Verify the digital signature of a message using the public key.

        Args:
            message (bytes): The original message.
            signature (bytes): The signature to be verified.

        Returns:
            bool: True if the signature is valid; False otherwise.
        """
        try:
            self.public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def export_keys(self) -> tuple[str, str]:
        """
        Export the private and public keys as PEM-encoded strings.

        Returns:
            tuple[str, str]: PEM-encoded private key and public key.
        """
        private_key_pem = self.private_key.private_bytes(
            Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
        ).decode()
        public_key_pem = self.public_key.public_bytes(
            Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
        ).decode()
        return private_key_pem, public_key_pem


# Example Usage
def main():
    """Demonstration of cryptographic authentication."""
    # Create the CryptographicAuthentication instance
    crypto_auth = CryptographicAuthentication()

    # Export the keys (optional)
    private_key, public_key = crypto_auth.export_keys()
    print("Private Key (PEM):\n", private_key)
    print("Public Key (PEM):\n", public_key)

    # Message to be signed
    message = b"This is the message to sign."

    # Sign the message
    signature = crypto_auth.sign_message(message)
    print("Signature:", signature.hex())

    # Verify the signature
    is_valid = crypto_auth.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)

    # Test with an invalid signature
    is_invalid = crypto_auth.verify_signature(message, b"invalid_signature")
    print("Is the signature valid (with tampered data)?", is_invalid)


if __name__ == "__main__":
    main()
```

### Notes:
- Install the `cryptography` library via `pip install cryptography`.
- Ensure the code is run in a secure environment, especially when handling private keys.
