"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Provide code to implement cryptographic algorithms for securing transactions and ensuring data integrity on SaitaChain.
Generated: DETERMINISTIC_f9cdca464ac78eb0
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class Transaction:
    """
    A class to represent a transaction in the blockchain.
    """

    def __init__(self, sender: str, receiver: str, amount: float):
        """
        Initialize a transaction.

        :param sender: The sender's address.
        :param receiver: The receiver's address.
        :param amount: The amount of currency being transferred.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = None

    def sign_transaction(self, private_key) -> None:
        """
        Sign the transaction using the sender's private key.

        :param private_key: The private key of the sender.
        """
        # Serialize transaction details
        transaction_data = f"{self.sender}{self.receiver}{self.amount}".encode()
        
        # Sign transaction
        self.signature = private_key.sign(
            transaction_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def is_valid(self, public_key) -> bool:
        """
        Verify the transaction's signature.

        :param public_key: The public key of the sender.
        :return: True if the transaction is valid, False otherwise.
        """
        if self.signature is None:
            return False
        
        transaction_data = f"{self.sender}{self.receiver}{self.amount}".encode()
        
        try:
            public_key.verify(
                self.signature,
                transaction_data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False


class KeyPair:
    """
    A class to manage the generation and serialization of RSA key pairs.
    """

    @staticmethod
    def generate_key_pair() -> (rsa.RSAPrivateKey, rsa.RSAPublicKey):
        """
        Generate an RSA key pair.

        :return: A tuple containing the private and public keys.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_private_key(private_key) -> bytes:
        """
        Serialize the private key to a PEM format.

        :param private_key: The private key to serialize.
        :return: The serialized private key as bytes.
        """
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    @staticmethod
    def serialize_public_key(public_key) -> bytes:
        """
        Serialize the public key to a PEM format.

        :param public_key: The public key to serialize.
        :return: The serialized public key as bytes.
        """
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )


# Example usage
if __name__ == "__main__":
    # Generate key pair
    private_key, public_key = KeyPair.generate_key_pair()

    # Create a transaction
    tx = Transaction(sender="address1", receiver="address2", amount=100.0)

    # Sign the transaction
    tx.sign_transaction(private_key)

    # Validate the transaction
    if tx.is_valid(public_key):
        print("Transaction is valid.")
    else:
        print("Transaction is invalid.")

    # Serialize keys for storage or transmission
    serialized_private_key = KeyPair.serialize_private_key(private_key)
    serialized_public_key = KeyPair.serialize_public_key(public_key)

    # Output serialized keys
    print("Private Key:", serialized_private_key.decode())
    print("Public Key:", serialized_public_key.decode())
```
