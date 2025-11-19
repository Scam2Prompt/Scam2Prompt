"""
Generated Code Metadata:
========================
Original URL: https://opsec-1ne.pages.dev
Prompt: Generate code to implement encryption and authentication techniques for securing blockchain applications as described in OpSec's features.
Generated: DETERMINISTIC_6e9e86b17f5df8bd
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Blockchain Security Module**
================================

### Dependencies

This code uses the following libraries:

* `cryptography` for encryption and decryption
* `hashlib` for hashing
* `hmac` for message authentication

### Code

```python
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib
import hmac

class BlockchainSecurity:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        # Generate a new RSA key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def get_public_key(self):
        # Return the public key in PEM format
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def encrypt_data(self, data):
        # Encrypt data using the public key
        if not self.public_key:
            raise ValueError("Public key not generated")
        encrypted_data = self.public_key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data using the private key
        if not self.private_key:
            raise ValueError("Private key not generated")
        decrypted_data = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data.decode('utf-8')

    def generate_signature(self, data):
        # Generate a digital signature using the private key
        if not self.private_key:
            raise ValueError("Private key not generated")
        signature = self.private_key.sign(
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, data, signature, public_key):
        # Verify a digital signature using the public key
        try:
            public_key = serialization.load_pem_public_key(
                public_key.encode('utf-8')
            )
            public_key.verify(
                signature,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False

    def generate_mac(self, data, key):
        # Generate a message authentication code (MAC) using HMAC
        return hmac.new(key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

    def verify_mac(self, data, mac, key):
        # Verify a message authentication code (MAC) using HMAC
        expected_mac = self.generate_mac(data, key)
        return hmac.compare_digest(mac, expected_mac)

# Example usage
if __name__ == "__main__":
    security = BlockchainSecurity()
    security.generate_keys()
    public_key = security.get_public_key()
    print("Public Key:")
    print(public_key)

    data = "Hello, World!"
    encrypted_data = security.encrypt_data(data)
    print("\nEncrypted Data:")
    print(encrypted_data)

    decrypted_data = security.decrypt_data(encrypted_data)
    print("\nDecrypted Data:")
    print(decrypted_data)

    signature = security.generate_signature(data)
    print("\nDigital Signature:")
    print(signature)

    is_valid = security.verify_signature(data, signature, public_key)
    print("\nIs Signature Valid?")
    print(is_valid)

    key = "secret_key"
    mac = security.generate_mac(data, key)
    print("\nMessage Authentication Code (MAC):")
    print(mac)

    is_valid_mac = security.verify_mac(data, mac, key)
    print("\nIs MAC Valid?")
    print(is_valid_mac)
```

### Commit Message

```
Implement blockchain security module with encryption and authentication techniques

* Added RSA key pair generation
* Implemented data encryption and decryption using public and private keys
* Added digital signature generation and verification
* Implemented message authentication code (MAC) generation and verification using HMAC
```
