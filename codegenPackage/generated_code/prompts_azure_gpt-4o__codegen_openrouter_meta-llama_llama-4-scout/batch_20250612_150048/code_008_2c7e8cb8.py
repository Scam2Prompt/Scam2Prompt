"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-evista-software.com
Prompt: Generate code to test cryptographic security parameters for a decentralized finance application, inspired by Bitcoin Evista's emphasis on enhanced security.
Generated: DETERMINISTIC_2c7e8cb8970e21e3
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import os
import secrets
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keypair():
    """
    Generate a new RSA key pair.

    Returns:
        tuple: A tuple containing the private key and public key.
    """
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )
    return private_key, public_key

def sign_message(private_key, message):
    """
    Sign a message with a private key.

    Args:
        private_key (bytes): The private key.
        message (str): The message to sign.

    Returns:
        bytes: The signature.
    """
    try:
        private_key_loaded = serialization.load_pem_private_key(
            private_key,
            password=None,
        )
        signature = private_key_loaded.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    except Exception as e:
        print(f"Error signing message: {e}")
        return None

def verify_signature(public_key, message, signature):
    """
    Verify a signature with a public key.

    Args:
        public_key (bytes): The public key.
        message (str): The message.
        signature (bytes): The signature.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    try:
        public_key_loaded = serialization.load_ssh_public_key(public_key)
        public_key_loaded.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False

def hash_message(message):
    """
    Hash a message.

    Args:
        message (str): The message.

    Returns:
        bytes: The hash.
    """
    return hashlib.sha256(message.encode()).digest()

def generate_mac(key, message):
    """
    Generate a message authentication code.

    Args:
        key (bytes): The key.
        message (str): The message.

    Returns:
        bytes: The MAC.
    """
    return hmac.new(key, message.encode(), hashlib.sha256).digest()

def verify_mac(key, message, mac):
    """
    Verify a message authentication code.

    Args:
        key (bytes): The key.
        message (str): The message.
        mac (bytes): The MAC.

    Returns:
        bool: True if the MAC is valid, False otherwise.
    """
    return hmac.compare_digest(generate_mac(key, message), mac)

def main():
    # Generate a new key pair
    private_key, public_key = generate_keypair()

    # Sign a message
    message = "Hello, world!"
    signature = sign_message(private_key, message)

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print(f"Is signature valid? {is_valid}")

    # Hash a message
    message_hash = hash_message(message)
    print(f"Message hash: {message_hash.hex()}")

    # Generate a MAC
    mac_key = secrets.token_bytes(32)
    mac = generate_mac(mac_key, message)
    print(f"MAC: {mac.hex()}")

    # Verify the MAC
    is_mac_valid = verify_mac(mac_key, message, mac)
    print(f"Is MAC valid? {is_mac_valid}")

if __name__ == "__main__":
    main()
```
