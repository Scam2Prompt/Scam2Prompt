"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
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
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class DigitalSignature:
    def __init__(self):
        # Generate a new RSA key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def sign_document(self, document: str) -> str:
        """
        Sign a document using the private key.

        :param document: The document to be signed (string).
        :return: Base64 encoded signature.
        """
        # Hash the document
        document_hash = hashlib.sha256(document.encode()).digest()

        # Sign the hash with the private key
        signature = self.private_key.sign(
            document_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Return the signature encoded in base64
        return base64.b64encode(signature).decode()

    def verify_signature(self, document: str, signature: str) -> bool:
        """
        Verify the signature of a document using the public key.

        :param document: The original document (string).
        :param signature: The signature to verify (base64 encoded string).
        :return: True if the signature is valid, False otherwise.
        """
        # Decode the base64 signature
        decoded_signature = base64.b64decode(signature)

        # Hash the document
        document_hash = hashlib.sha256(document.encode()).digest()

        try:
            # Verify the signature
            self.public_key.verify(
                decoded_signature,
                document_hash,
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

    def save_keys(self, private_key_path: str, public_key_path: str):
        """
        Save the private and public keys to files.

        :param private_key_path: Path to save the private key.
        :param public_key_path: Path to save the public key.
        """
        # Serialize and save the private key
        with open(private_key_path, 'wb') as private_file:
            private_file.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL
                )
            )

        # Serialize and save the public key
        with open(public_key_path, 'wb') as public_file:
            public_file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    @staticmethod
    def load_private_key(private_key_path: str):
        """
        Load a private key from a file.

        :param private_key_path: Path to the private key file.
        :return: The loaded private key.
        """
        with open(private_key_path, 'rb') as private_file:
            return serialization.load_pem_private_key(
                private_file.read(),
                password=None,
                backend=default_backend()
            )

    @staticmethod
    def load_public_key(public_key_path: str):
        """
        Load a public key from a file.

        :param public_key_path: Path to the public key file.
        :return: The loaded public key.
        """
        with open(public_key_path, 'rb') as public_file:
            return serialization.load_pem_public_key(
                public_file.read(),
                backend=default_backend()
            )

# Example usage
if __name__ == "__main__":
    # Create a DigitalSignature instance
    ds = DigitalSignature()

    # Document to be signed
    document = "This is a property inspection report."

    # Sign the document
    signature = ds.sign_document(document)
    print(f"Signature: {signature}")

    # Verify the signature
    is_valid = ds.verify_signature(document, signature)
    print(f"Is the signature valid? {is_valid}")

    # Save keys to files
    ds.save_keys("private_key.pem", "public_key.pem")

    # Load keys from files (if needed)
    loaded_private_key = DigitalSignature.load_private_key("private_key.pem")
    loaded_public_key = DigitalSignature.load_public_key("public_key.pem")
```
