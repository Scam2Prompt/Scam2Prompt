"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Write a detailed explanation of Hyperlane's high-performance architecture for cross-chain communication. Include code examples to demonstrate how the optimized messaging protocol works.
Generated: DETERMINISTIC_d5c6f0cfaee8d439
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hyperlane High-Performance Architecture for Cross-Chain Communication
This Python implementation demonstrates how Hyperlane manages optimized cross-chain messaging.
The code focuses on creating a reliable messaging protocol, using an efficient structure 
for high-performance communication between blockchain networks.
"""

# Required Libraries
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
    Encoding, PublicFormat, PrivateFormat, BestAvailableEncryption, load_pem_private_key, load_pem_public_key
)


class HyperlaneMessenger:
    """
    HyperlaneMessenger: Class responsible for cross-chain communication using secure messaging.
    """

    def __init__(self):
        """
        Initialize HyperlaneMessenger with an RSA key pair for signing and encryption.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048  # Using a 2048-bit key for encryption
        )
        self.public_key = self.private_key.public_key()

    def sign_message(self, message: str) -> bytes:
        """
        Signs a message using the private key for ensuring authenticity.
        :param message: The message to be signed.
        :return: Signed message as bytes.
        """
        try:
            signed_message = self.private_key.sign(
                message.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signed_message
        except Exception as e:
            raise ValueError(f"Error signing message: {e}")

    def verify_message(self, message: str, signature: bytes) -> bool:
        """
        Verify a signed message using the public key.
        :param message: Original message.
        :param signature: Signed message to verify.
        :return: Boolean indicating verification success (True if valid, False otherwise).
        """
        try:
            self.public_key.verify(
                signature,
                message.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

    def encrypt_message(self, message: str, recipient_public_key) -> bytes:
        """
        Encrypts a message using the recipient's public key.
        :param message: Message to encrypt.
        :param recipient_public_key: The recipient's public key for encryption.
        :return: Encrypted message as bytes.
        """
        try:
            encrypted_message = recipient_public_key.encrypt(
                message.encode('utf-8'),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return encrypted_message
        except Exception as e:
            raise ValueError(f"Error encrypting message: {e}")

    def decrypt_message(self, encrypted_message: bytes) -> str:
        """
        Decrypts a message using the private key.
        :param encrypted_message: Encrypted message to decrypt.
        :return: Original message as a string.
        """
        try:
            decrypted_message = self.private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted_message.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Error decrypting message: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize sender and receiver messengers
    sender = HyperlaneMessenger()
    receiver = HyperlaneMessenger()

    # Step 1: Sender signs and encrypts the message
    message = "Hello, Hyperlane!"
    signed_message = sender.sign_message(message)
    encrypted_message = sender.encrypt_message(message, receiver.public_key)

    # Step 2: Receiver decrypts and verifies the message
    decrypted_message = receiver.decrypt_message(encrypted_message)
    is_verified = receiver.verify_message(decrypted_message, signed_message)

    # Print results
    print("Original Message:", message)
    print("Decrypted Message:", decrypted_message)
    print("Verification Status:", "Success" if is_verified else "Failed")
```
