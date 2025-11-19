"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-website.vercel.app
Prompt: How does WalletConnect ensure secure communication between mobile wallets and Dapps?
Generated: DETERMINISTIC_be9c08a961ed8b8e
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

class WalletConnect:
    """A class to handle secure communication between mobile wallets and Dapps using WalletConnect."""

    def __init__(self):
        self.session = {}
        self.private_key = None

    def generate_keys(self):
        """Generates a public/private key pair for secure communication."""
        from cryptography.hazmat.primitives.asymmetric import rsa
        
        # Generate a private key for use in the exchange
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        # Derive the public key from the private key
        public_key = self.private_key.public_key()
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def sign_message(self, message):
        """Signs a message using the private key to ensure authenticity."""
        if self.private_key is None:
            raise ValueError("Private key is not generated. Call generate_keys() first.")
        
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).digest()
        
        # Sign the hash with the private key
        signature = self.private_key.sign(
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()

    def verify_signature(self, public_key_bytes, message, signature):
        """Verifies that a signature is valid for a given message and public key."""
        public_key = serialization.load_pem_public_key(
            public_key_bytes,
            backend=default_backend()
        )
        
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).digest()
        
        try:
            public_key.verify(
                base64.b64decode(signature),
                message_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256()
            )
            return True  # Signature is valid
        except InvalidSignature:
            return False  # Signature is not valid

    def send_message(self, message, recipient_public_key):
        """Sends a securely signed message to a recipient."""
        signature = self.sign_message(message)
        payload = {
            'message': message,
            'signature': signature
        }
        # Here would be the code to actually send the payload to the recipient
        # This might involve using sockets, HTTP requests, etc.

        return payload

    def receive_message(self, payload, sender_public_key):
        """Receives a message and verifies its signature."""
        message = payload['message']
        signature = payload['signature']
        
        # Verify the signature before accepting the message
        if self.verify_signature(sender_public_key, message, signature):
            print("Message verified and accepted:", message)
        else:
            print("Invalid signature. Message rejected.")

# Example usage:
if __name__ == "__main__":
    wc = WalletConnect()
    sender_public_key = wc.generate_keys()  # Generate keys for sender
    recipient_public_key = wc.generate_keys()  # Generate keys for recipient
    
    message = "Hello from WalletConnect!"
    payload = wc.send_message(message, recipient_public_key)
    
    # Simulate receiving the message
    wc.receive_message(payload, sender_public_key)
```
