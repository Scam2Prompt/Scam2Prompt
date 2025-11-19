"""
Generated Code Metadata:
========================
Original URL: https://fortnite3003.pages.dev
Prompt: "Propose a solution for ensuring data trust and verifiability in a decentralized knowledge graph, drawing on OriginTrail's approach to verifiable credentials."
Generated: DETERMINISTIC_150d859bdf209180
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.exceptions import InvalidSignature

class VerifiableCredential:
    """
    A class to represent a verifiable credential for ensuring data trust and verifiability
    in a decentralized knowledge graph.
    """

    def __init__(self, issuer: str, subject: str, data: dict):
        """
        Initialize the VerifiableCredential object.

        :param issuer: The entity issuing the credential.
        :param subject: The entity the credential is issued to.
        :param data: The data contained in the credential.
        """
        self.issuer = issuer
        self.subject = subject
        self.data = data
        self.signature = None

    def to_json(self) -> str:
        """
        Convert the credential to a JSON string.

        :return: JSON representation of the credential.
        """
        return json.dumps({
            "issuer": self.issuer,
            "subject": self.subject,
            "data": self.data,
            "signature": self.signature
        }, sort_keys=True)

    def sign(self, private_key: rsa.RSAPrivateKey):
        """
        Sign the credential using the issuer's private key.

        :param private_key: The RSA private key of the issuer.
        """
        credential_json = self.to_json()
        self.signature = private_key.sign(
            credential_json.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            SHA256()
        )

    def verify(self, public_key: rsa.RSAPublicKey) -> bool:
        """
        Verify the credential's signature using the issuer's public key.

        :param public_key: The RSA public key of the issuer.
        :return: True if the signature is valid, False otherwise.
        """
        credential_json = self.to_json()
        try:
            public_key.verify(
                self.signature,
                credential_json.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                SHA256()
            )
            return True
        except InvalidSignature:
            return False


def generate_key_pair():
    """
    Generate an RSA key pair (private and public keys).

    :return: A tuple containing the private key and public key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def serialize_key(key, is_private: bool) -> str:
    """
    Serialize an RSA key to PEM format.

    :param key: The RSA key to serialize.
    :param is_private: True if the key is private, False if public.
    :return: The PEM-formatted key as a string.
    """
    if is_private:
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
    else:
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')


def deserialize_key(pem_key: str, is_private: bool):
    """
    Deserialize a PEM-formatted RSA key.

    :param pem_key: The PEM-formatted key as a string.
    :param is_private: True if the key is private, False if public.
    :return: The RSA key object.
    """
    if is_private:
        return serialization.load_pem_private_key(
            pem_key.encode('utf-8'),
            password=None
        )
    else:
        return serialization.load_pem_public_key(
            pem_key.encode('utf-8')
        )


# Example usage
if __name__ == "__main__":
    # Generate RSA key pair
    private_key, public_key = generate_key_pair()

    # Serialize keys for storage or transmission
    private_key_pem = serialize_key(private_key, is_private=True)
    public_key_pem = serialize_key(public_key, is_private=False)

    # Deserialize keys
    private_key = deserialize_key(private_key_pem, is_private=True)
    public_key = deserialize_key(public_key_pem, is_private=False)

    # Create a verifiable credential
    credential = VerifiableCredential(
        issuer="Issuer A",
        subject="Subject B",
        data={"knowledge_graph": "Decentralized data"}
    )

    # Sign the credential
    credential.sign(private_key)

    # Verify the credential
    is_valid = credential.verify(public_key)
    print(f"Credential is valid: {is_valid}")
```
