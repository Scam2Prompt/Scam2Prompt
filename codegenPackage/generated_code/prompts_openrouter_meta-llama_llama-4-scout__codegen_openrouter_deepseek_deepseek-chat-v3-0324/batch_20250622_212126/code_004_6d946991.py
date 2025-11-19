"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Create a code example that showcases the usage of a particular cryptographic protocol or algorithm, potentially involving key exchange or digital signatures, based on the unique features and details discussed on the webpage.
Generated: DETERMINISTIC_6d946991a2188b15
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

def generate_ec_keys():
    """
    Generate ECDSA key pair for signing and verification.
    Returns private and public keys.
    """
    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    """
    Sign a message using ECDSA.
    Returns the signature.
    """
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    """
    Verify a message signature using ECDSA.
    Raises InvalidSignature if verification fails.
    """
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False

def derive_shared_key(private_key, peer_public_key):
    """
    Perform ECDH key exchange and derive shared key using HKDF.
    Returns the derived key.
    """
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ecdh key derivation',
        backend=default_backend()
    ).derive(shared_key)
    return derived_key

def serialize_public_key(public_key):
    """
    Serialize public key to PEM format.
    """
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def deserialize_public_key(pem_data):
    """
    Deserialize public key from PEM format.
    """
    return serialization.load_pem_public_key(
        pem_data,
        backend=default_backend()
    )

def main():
    # Alice generates her key pair
    alice_private, alice_public = generate_ec_keys()
    
    # Bob generates his key pair
    bob_private, bob_public = generate_ec_keys()
    
    # Alice and Bob exchange public keys (simulated here)
    alice_public_pem = serialize_public_key(alice_public)
    bob_public_pem = serialize_public_key(bob_public)
    
    # Deserialize received public keys
    alice_received_public = deserialize_public_key(bob_public_pem)
    bob_received_public = deserialize_public_key(alice_public_pem)
    
    # Derive shared secret
    alice_shared_key = derive_shared_key(alice_private, alice_received_public)
    bob_shared_key = derive_shared_key(bob_private, bob_received_public)
    
    # Verify both parties derived the same key
    assert alice_shared_key == bob_shared_key, "Key derivation failed"
    
    # Alice signs a message
    message = b"Important message for Bob"
    signature = sign_message(alice_private, message)
    
    # Bob verifies the signature
    is_valid = verify_signature(bob_received_public, message, signature)
    print(f"Signature valid: {is_valid}")

if __name__ == "__main__":
    main()
```
