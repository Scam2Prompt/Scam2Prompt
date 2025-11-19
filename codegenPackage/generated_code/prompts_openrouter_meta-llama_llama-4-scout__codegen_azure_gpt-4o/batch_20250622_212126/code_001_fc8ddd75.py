"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Recommend a suitable library or API for generating and verifying digital signatures, given the webpage's content that appears to involve cryptographic primitives.
Generated: DETERMINISTIC_fc8ddd75bac5ac91
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is Python code using the `cryptography` library, which is a widely used and robust library for cryptographic operations, including generating and verifying digital signatures.

```python
# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
)

# Function to generate RSA key pair
def generate_key_pair():
    """
    Generates an RSA private and public key pair.

    Returns:
        private_key: RSA private key object
        public_key: RSA public key object
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Commonly used public exponent
        key_size=2048,         # Key size in bits (2048 is secure and widely used)
    )
    public_key = private_key.public_key()
    return private_key, public_key


# Function to sign data using the private key
def sign_data(private_key, data):
    """
    Signs the given data using the provided RSA private key.

    Args:
        private_key: RSA private key object
        data (bytes): Data to be signed

    Returns:
        signature (bytes): Digital signature of the data
    """
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),  # Mask generation function
            salt_length=padding.PSS.MAX_LENGTH,  # Maximum salt length
        ),
        hashes.SHA256(),  # Hashing algorithm
    )
    return signature


# Function to verify the signature using the public key
def verify_signature(public_key, data, signature):
    """
    Verifies the digital signature of the given data using the provided RSA public key.

    Args:
        public_key: RSA public key object
        data (bytes): Original data
        signature (bytes): Digital signature to verify

    Returns:
        bool: True if the signature is valid, False otherwise
    """
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),  # Mask generation function
                salt_length=padding.PSS.MAX_LENGTH,  # Maximum salt length
            ),
            hashes.SHA256(),  # Hashing algorithm
        )
        return True  # Signature is valid
    except Exception as e:
        # Handle verification failure
        print(f"Signature verification failed: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Generate RSA key pair
    private_key, public_key = generate_key_pair()

    # Serialize keys for storage or transmission (optional)
    private_key_bytes = private_key.private_bytes(
        Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
    )
    public_key_bytes = public_key.public_bytes(
        Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
    )

    # Print serialized keys (optional)
    print("Private Key:")
    print(private_key_bytes.decode())
    print("Public Key:")
    print(public_key_bytes.decode())

    # Data to be signed
    data = b"Important message to be signed"

    # Generate digital signature
    signature = sign_data(private_key, data)
    print(f"Signature: {signature.hex()}")

    # Verify the signature
    is_valid = verify_signature(public_key, data, signature)
    print(f"Is the signature valid? {is_valid}")
```

This code demonstrates how to generate RSA keys, sign data, and verify digital signatures using the `cryptography` library. It includes error handling, comments, and follows best practices for production-ready code.
