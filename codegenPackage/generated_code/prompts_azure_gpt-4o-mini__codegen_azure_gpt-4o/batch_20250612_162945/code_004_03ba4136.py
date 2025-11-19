"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: What are the steps to ensure the security and immutability of code stored as blobs in a decentralized Git service?
Generated: DETERMINISTIC_03ba41366fc6bf40
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script that demonstrates steps to ensure the security and immutability of code stored as blobs in a decentralized Git service. It includes hashing, signing, and verification mechanisms.

```python
import hashlib
import os
import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import PSS, MGF1
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.exceptions import InvalidSignature

# Step 1: Generate RSA key pair for signing and verification
def generate_key_pair():
    """
    Generates an RSA key pair for signing and verification.
    Returns the private and public keys.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Step 2: Hash the code blob
def hash_blob(blob_content):
    """
    Computes a SHA-256 hash of the given blob content.
    Args:
        blob_content (str): The content of the code blob.
    Returns:
        str: The hexadecimal representation of the hash.
    """
    sha256 = hashlib.sha256()
    sha256.update(blob_content.encode('utf-8'))
    return sha256.hexdigest()

# Step 3: Sign the hash using the private key
def sign_blob_hash(private_key, blob_hash):
    """
    Signs the hash of the blob using the private key.
    Args:
        private_key: RSA private key for signing.
        blob_hash (str): The hash of the blob to be signed.
    Returns:
        bytes: The signature.
    """
    signature = private_key.sign(
        blob_hash.encode('utf-8'),
        PSS(
            mgf=MGF1(SHA256()),
            salt_length=PSS.MAX_LENGTH
        ),
        Prehashed(SHA256())
    )
    return signature

# Step 4: Verify the signature using the public key
def verify_blob_signature(public_key, blob_hash, signature):
    """
    Verifies the signature of the blob hash using the public key.
    Args:
        public_key: RSA public key for verification.
        blob_hash (str): The hash of the blob.
        signature (bytes): The signature to verify.
    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    try:
        public_key.verify(
            signature,
            blob_hash.encode('utf-8'),
            PSS(
                mgf=MGF1(SHA256()),
                salt_length=PSS.MAX_LENGTH
            ),
            Prehashed(SHA256())
        )
        return True
    except InvalidSignature:
        return False

# Step 5: Save keys and metadata securely
def save_keys_and_metadata(private_key, public_key, blob_hash, signature, file_path):
    """
    Saves the keys and metadata (hash and signature) to a JSON file.
    Args:
        private_key: RSA private key.
        public_key: RSA public key.
        blob_hash (str): The hash of the blob.
        signature (bytes): The signature of the blob hash.
        file_path (str): Path to save the metadata file.
    """
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    metadata = {
        "private_key": private_key_pem,
        "public_key": public_key_pem,
        "blob_hash": blob_hash,
        "signature": signature.hex()
    }

    with open(file_path, 'w') as f:
        json.dump(metadata, f, indent=4)

# Step 6: Main function to demonstrate the process
def main():
    """
    Main function to demonstrate the security and immutability process.
    """
    # Example code blob content
    blob_content = "print('Hello, secure world!')"

    # Generate RSA key pair
    private_key, public_key = generate_key_pair()

    # Compute hash of the blob
    blob_hash = hash_blob(blob_content)

    # Sign the hash
    signature = sign_blob_hash(private_key, blob_hash)

    # Verify the signature
    is_valid = verify_blob_signature(public_key, blob_hash, signature)
    print(f"Signature valid: {is_valid}")

    # Save keys and metadata securely
    save_keys_and_metadata(private_key, public_key, blob_hash, signature, "metadata.json")
    print("Keys and metadata saved to 'metadata.json'.")

if __name__ == "__main__":
    main()
```
