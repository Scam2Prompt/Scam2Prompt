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

```python
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

class DigitalSignatureHandler:
    """
    A class for generating and verifying digital signatures using RSA.
    Uses cryptography library which is a popular choice for cryptographic operations.
    """
    
    def __init__(self, key_size=2048):
        """
        Initialize with RSA key pair generation.
        
        Args:
            key_size (int): Size of RSA key, default is 2048 bits
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def sign_data(self, data):
        """
        Sign the given data using the private key.
        
        Args:
            data (bytes): Data to be signed
            
        Returns:
            bytes: The signature
        """
        if not isinstance(data, bytes):
            raise TypeError("Data must be in bytes format")
            
        signature = self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def verify_signature(self, data, signature):
        """
        Verify the signature against the given data using the public key.
        
        Args:
            data (bytes): Original data that was signed
            signature (bytes): Signature to verify
            
        Returns:
            bool: True if verification succeeds, False otherwise
        """
        if not isinstance(data, bytes) or not isinstance(signature, bytes):
            raise TypeError("Both data and signature must be in bytes format")
            
        try:
            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
    
    def get_public_key_pem(self):
        """
        Get the public key in PEM format.
        
        Returns:
            bytes: Public key in PEM format
        """
        return self.public_key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo
        )
    
    def get_private_key_pem(self):
        """
        Get the private key in PEM format.
        
        Returns:
            bytes: Private key in PEM format
        """
        return self.private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption()
        )

# Example usage
if __name__ == "__main__":
    handler = DigitalSignatureHandler()
    data = b"Important message to sign"
    
    # Sign the data
    signature = handler.sign_data(data)
    print(f"Signature: {signature.hex()}")
    
    # Verify the signature
    is_valid = handler.verify_signature(data, signature)
    print(f"Signature valid: {is_valid}")
    
    # Try with tampered data
    tampered_data = b"Tampered message"
    is_valid = handler.verify_signature(tampered_data, signature)
    print(f"Tampered signature valid: {is_valid}")
```
