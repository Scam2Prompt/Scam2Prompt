"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica-auth.vercel.app
Prompt: Recommend best practices for implementing secure blockchain authentication across multiple networks, as seen in Matrica.
Generated: DETERMINISTIC_bff05da3e0466828
Batch ID: 20250612_152358
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
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature

class BlockchainAuthenticator:
    """
    A class to implement secure blockchain authentication across multiple networks.
    """

    def __init__(self):
        """
        Initializes a new instance with a generated RSA key pair.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def sign_message(self, message: str) -> bytes:
        """
        Signs a message using the private key.

        Args:
            message (str): The message to sign.

        Returns:
            bytes: The signed message.
        """
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).digest()
        # Sign the hash
        signature = self.private_key.sign(
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, message: str, signature: bytes) -> bool:
        """
        Verifies the signature of a message.

        Args:
            message (str): The original message.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            message_hash = hashlib.sha256(message.encode()).digest()
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

    def serialize_keys(self) -> dict:
        """
        Serializes the public and private keys to a dictionary.

        Returns:
            dict: A dictionary containing serialized keys.
        """
        return {
            "private_key": self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL
            ).decode(),
            "public_key": self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()
        }

    @staticmethod
    def deserialize_private_key(private_key_pem: str):
        """
        Deserializes a private key from PEM format.

        Args:
            private_key_pem (str): The PEM formatted private key.

        Returns:
            PrivateKey: The deserialized RSA private key.
        """
        return serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None
        )

    @staticmethod
    def deserialize_public_key(public_key_pem: str):
        """
        Deserializes a public key from PEM format.

        Args:
            public_key_pem (str): The PEM formatted public key.

        Returns:
            PublicKey: The deserialized RSA public key.
        """
        return serialization.load_pem_public_key(
            public_key_pem.encode()
        )

# Example usage
if __name__ == "__main__":
    authenticator = BlockchainAuthenticator()
    message = "This is a secure message."

    # Sign the message
    signature = authenticator.sign_message(message)
    print("Signature:", signature)

    # Verify the signature
    is_valid = authenticator.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)

    # Serialize keys
    keys = authenticator.serialize_keys()
    print("Serialized Keys:", keys)

    # Deserialize example (not typically done in the same run)
    private_key = authenticator.deserialize_private_key(keys['private_key'])
    public_key = authenticator.deserialize_public_key(keys['public_key'])

    # Confirm deserialization was successful by verifying the signature again with the new keys
    new_authenticator = BlockchainAuthenticator()
    new_authenticator.private_key = private_key
    new_authenticator.public_key = public_key
    is_valid_new = new_authenticator.verify_signature(message, signature)
    print("Is the signature valid with deserialized keys?", is_valid_new)
```
