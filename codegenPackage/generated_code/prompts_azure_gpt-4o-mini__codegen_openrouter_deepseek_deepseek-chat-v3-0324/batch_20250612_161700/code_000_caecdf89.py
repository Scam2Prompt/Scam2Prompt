"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
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
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from datetime import datetime
import base64
import json
from typing import Dict, Tuple, Optional

class DigitalSignatureManager:
    """
    A class to handle digital signature generation and verification for property inspection reports.
    """
    
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self._generate_key_pair()
    
    def _generate_key_pair(self) -> None:
        """
        Generate RSA key pair for signing and verification.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def sign_document(self, document_data: Dict) -> Tuple[str, str]:
        """
        Sign a document (property inspection report) with digital signature.
        
        Args:
            document_data: Dictionary containing the document data to be signed
            
        Returns:
            Tuple of (signature, public_key) in base64 encoded strings
        """
        try:
            # Convert document to JSON string and encode to bytes
            document_json = json.dumps(document_data, sort_keys=True).encode('utf-8')
            
            # Generate hash of the document
            document_hash = hashlib.sha256(document_json).digest()
            
            # Add timestamp to the signature
            timestamp = datetime.utcnow().isoformat().encode('utf-8')
            
            # Sign the document hash + timestamp
            signature = self.private_key.sign(
                document_hash + timestamp,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            # Serialize public key
            public_key_bytes = self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            
            return (
                base64.b64encode(signature).decode('utf-8'),
                base64.b64encode(public_key_bytes).decode('utf-8'),
                timestamp.decode('utf-8')
            )
        except Exception as e:
            raise Exception(f"Error signing document: {str(e)}")
    
    @staticmethod
    def verify_signature(
        document_data: Dict,
        signature: str,
        public_key: str,
        timestamp: str
    ) -> bool:
        """
        Verify a document's digital signature.
        
        Args:
            document_data: Original document data that was signed
            signature: Base64 encoded signature string
            public_key: Base64 encoded public key string
            timestamp: ISO format timestamp string
            
        Returns:
            Boolean indicating whether verification was successful
        """
        try:
            # Load public key
            public_key_bytes = base64.b64decode(public_key.encode('utf-8'))
            pub_key = serialization.load_pem_public_key(
                public_key_bytes,
                backend=default_backend()
            )
            
            # Recreate document hash
            document_json = json.dumps(document_data, sort_keys=True).encode('utf-8')
            document_hash = hashlib.sha256(document_json).digest()
            
            # Decode signature
            signature_bytes = base64.b64decode(signature.encode('utf-8'))
            
            # Verify signature
            pub_key.verify(
                signature_bytes,
                document_hash + timestamp.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def save_key_pair(self, private_key_path: str, public_key_path: str) -> None:
        """
        Save key pair to files.
        
        Args:
            private_key_path: Path to save private key
            public_key_path: Path to save public key
        """
        try:
            # Save private key
            with open(private_key_path, 'wb') as f:
                f.write(self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))
            
            # Save public key
            with open(public_key_path, 'wb') as f:
                f.write(self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
        except Exception as e:
            raise Exception(f"Error saving key pair: {str(e)}")
    
    @staticmethod
    def load_key_pair(private_key_path: str, public_key_path: str) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Load key pair from files.
        
        Args:
            private_key_path: Path to private key file
            public_key_path: Path to public key file
            
        Returns:
            Tuple of (private_key, public_key)
        """
        try:
            # Load private key
            with open(private_key_path, 'rb') as f:
                private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=default_backend()
                )
            
            # Load public key
            with open(public_key_path, 'rb') as f:
                public_key = serialization.load_pem_public_key(
                    f.read(),
                    backend=default_backend()
                )
            
            return private_key, public_key
        except Exception as e:
            raise Exception(f"Error loading key pair: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Sample property inspection data
    inspection_data = {
        "property_id": "12345",
        "inspector": "John Doe",
        "date": "2023-11-15",
        "findings": {
            "roof": "Good condition",
            "plumbing": "Minor leaks",
            "electrical": "Up to code"
        }
    }
    
    # Initialize signature manager
    signature_manager = DigitalSignatureManager()
    
    # Sign the inspection report
    try:
        signature, public_key, timestamp = signature_manager.sign_document(inspection_data)
        print("Document signed successfully!")
        print(f"Signature: {signature[:50]}...")
        print(f"Public Key: {public_key[:50]}...")
        print(f"Timestamp: {timestamp}")
        
        # Verify the signature
        is_valid = DigitalSignatureManager.verify_signature(
            inspection_data,
            signature,
            public_key,
            timestamp
        )
        print(f"Signature valid: {is_valid}")
        
        # Save keys for later use
        signature_manager.save_key_pair("private_key.pem", "public_key.pem")
    except Exception as e:
        print(f"Error: {str(e)}")
```
