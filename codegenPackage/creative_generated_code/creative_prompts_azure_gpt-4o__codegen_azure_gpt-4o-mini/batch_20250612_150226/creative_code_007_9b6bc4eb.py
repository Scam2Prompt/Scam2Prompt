"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website2-70z.pages.dev
Prompt: Write code to integrate a decentralized identity system into a crypto network, focusing on redefining ownership as described by Innodapter ApS.
Generated: DETERMINISTIC_9b6bc4ebdd0c2d33
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature


class DecentralizedIdentity:
    def __init__(self):
        """Initialize the Decentralized Identity system with a new key pair."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.identity = {}

    def create_identity(self, identity_data):
        """
        Create a decentralized identity.

        :param identity_data: A dictionary containing identity information
        :return: A JSON representation of the identity
        """
        try:
            identity_hash = self._hash_data(identity_data)
            self.identity = {
                'data': identity_data,
                'hash': identity_hash,
                'owner': self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ).decode()
            }
            return json.dumps(self.identity)
        except Exception as e:
            print(f"Error creating identity: {e}")

    def sign_identity(self):
        """
        Sign the identity with the private key to ensure ownership.

        :return: The signature of the identity
        """
        try:
            identity_bytes = json.dumps(self.identity).encode()
            signature = self.private_key.sign(
                identity_bytes,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            print(f"Error signing identity: {e}")

    @staticmethod
    def _hash_data(data):
        """
        Generate a SHA-256 hash of the given data.

        :param data: The data to be hashed
        :return: The SHA-256 hash of the data
        """
        data_string = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(data_string).hexdigest()

    def verify_identity(self, signature):
        """
        Verify the identity signature.

        :param signature: The signature to verify
        :return: Boolean indicating validity of the signature
        """
        try:
            identity_bytes = json.dumps(self.identity).encode()
            public_key = self.public_key

            # Verify the signature
            public_key.verify(
                signature,
                identity_bytes,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            print("Invalid signature.")
            return False
        except Exception as e:
            print(f"Error verifying identity: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    identity_system = DecentralizedIdentity()
    
    # Define identity data
    identity_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    
    # Create identity
    identity_json = identity_system.create_identity(identity_info)
    print("Created Identity:", identity_json)

    # Sign the identity
    signature = identity_system.sign_identity()
    print("Signature:", signature.hex())

    # Verify the identity
    is_valid = identity_system.verify_identity(signature)
    print("Is signature valid?", is_valid)
```
