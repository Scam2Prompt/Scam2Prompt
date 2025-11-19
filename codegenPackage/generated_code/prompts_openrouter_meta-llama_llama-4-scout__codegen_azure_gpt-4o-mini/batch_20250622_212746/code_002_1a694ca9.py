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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

class DigitalSignatureAuth:
    def __init__(self):
        # Generate a new RSA private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        # Derive the public key from the private key
        self.public_key = self.private_key.public_key()

    def sign_message(self, message: str) -> str:
        """
        Sign a message using the private key.

        :param message: The message to be signed.
        :return: Base64 encoded signature.
        """
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).digest()
        
        # Sign the hash with the private key
        signature = self.private_key.sign(
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # Return the base64 encoded signature
        return base64.b64encode(signature).decode()

    def verify_signature(self, message: str, signature: str) -> bool:
        """
        Verify a message signature using the public key.

        :param message: The original message.
        :param signature: The base64 encoded signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
        # Decode the base64 signature
        decoded_signature = base64.b64decode(signature)
        
        # Hash the original message
        message_hash = hashlib.sha256(message.encode()).digest()
        
        try:
            # Verify the signature
            self.public_key.verify(
                decoded_signature,
                message_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            # Log the error (in production, use a logging framework)
            print(f"Signature verification failed: {e}")
            return False

    def export_keys(self) -> dict:
        """
        Export the private and public keys.

        :return: A dictionary containing the PEM encoded private and public keys.
        """
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL
        )
        
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return {
            'private_key': private_pem.decode(),
            'public_key': public_pem.decode()
        }

# Example usage
if __name__ == "__main__":
    auth = DigitalSignatureAuth()
    
    # Export keys for storage or transmission
    keys = auth.export_keys()
    print("Private Key:\n", keys['private_key'])
    print("Public Key:\n", keys['public_key'])
    
    # Sign a message
    message = "This is a secure message."
    signature = auth.sign_message(message)
    print("Signature:\n", signature)
    
    # Verify the signature
    is_valid = auth.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)
```
