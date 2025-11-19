"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import base64
import json
import os
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

    def sign_data(self, data):
        """
        Sign the provided data using the private key.

        Parameters:
            data (str): The data to be signed.

        Returns:
            str: The base64 encoded signature.
        """
        # Hash the data
        data_bytes = data.encode('utf-8')
        hash_value = hashlib.sha256(data_bytes).digest()

        # Sign the hash with the private key
        signature = self.private_key.sign(
            hash_value,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('utf-8')

    def verify_signature(self, data, signature):
        """
        Verify the provided signature using the public key.

        Parameters:
            data (str): The data that needs to be verified.
            signature (str): The base64 encoded signature.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        # Hash the data
        data_bytes = data.encode('utf-8')
        hash_value = hashlib.sha256(data_bytes).digest()

        # Decode the signature from base64
        decoded_signature = base64.b64decode(signature)

        try:
            # Verify the signature with the public key
            self.public_key.verify(
                decoded_signature,
                hash_value,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            # If verification fails, print the error and return False
            print(f"Signature verification failed: {e}")
            return False

    def save_keys(self, private_key_path='private_key.pem', public_key_path='public_key.pem'):
        """
        Save the RSA keys to the specified file paths.

        Parameters:
            private_key_path (str): The file path to save the private key.
            public_key_path (str): The file path to save the public key.
        """
        # Serialize and save the private key
        with open(private_key_path, 'wb') as private_file:
            private_file.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                )
            )

        # Serialize and save the public key
        with open(public_key_path, 'wb') as public_file:
            public_file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

    @staticmethod
    def load_private_key(private_key_path):
        """
        Load a private key from a specified file path.

        Parameters:
            private_key_path (str): The file path to the private key.

        Returns:
            PrivateKey: The loaded private key.
        """
        with open(private_key_path, 'rb') as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key

    @staticmethod
    def load_public_key(public_key_path):
        """
        Load a public key from a specified file path.

        Parameters:
            public_key_path (str): The file path to the public key.

        Returns:
            PublicKey: The loaded public key.
        """
        with open(public_key_path, 'rb') as public_file:
            public_key = serialization.load_pem_public_key(
                public_file.read(),
                backend=default_backend()
            )
        return public_key

# Example usage
if __name__ == "__main__":
    # Initialize digital signature
    ds = DigitalSignature()

    # Sample data
    data_to_sign = json.dumps({"property_id": 123, "inspector": "John Doe", "timestamp": "2023-10-01"})

    # Sign data
    signature = ds.sign_data(data_to_sign)
    print(f"Signature: {signature}")

    # Verify signature
    is_valid = ds.verify_signature(data_to_sign, signature)
    print(f"Is signature valid? {is_valid}")

    # Save the keys
    ds.save_keys()
```
