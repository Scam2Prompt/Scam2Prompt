"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvest-kfi.pages.dev
Prompt: Write Python code using CryptoNext's C-QSL library to implement a post-quantum secure encryption algorithm for securing IoT device communications.
Generated: DETERMINISTIC_045468e359c01b42
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import c_qsl  # Importing the CryptoNext C-QSL library for post-quantum cryptography
import os  # For generating secure random bytes
import base64  # For encoding and decoding

class PostQuantumEncryptor:
    def __init__(self):
        # Initialize the encryption algorithm
        try:
            self.algorithm = c_qsl.PQCAlgorithm()  # Replace with actual algorithm initialization
        except Exception as e:
            raise RuntimeError("Failed to initialize the post-quantum encryption algorithm.") from e

    def generate_keypair(self):
        """Generates a public/private key pair."""
        try:
            self.private_key, self.public_key = self.algorithm.generate_keypair()
            return self.public_key
        except Exception as e:
            raise RuntimeError("Key pair generation failed.") from e

    def encrypt(self, plaintext: str, public_key: bytes) -> str:
        """Encrypts the plaintext using the provided public key."""
        try:
            # Ensure the plaintext is in bytes
            plaintext_bytes = plaintext.encode('utf-8')
            ciphertext = self.algorithm.encrypt(plaintext_bytes, public_key)
            # Return the ciphertext encoded in Base64 for easier transmission
            return base64.b64encode(ciphertext).decode('utf-8')
        except Exception as e:
            raise RuntimeError("Encryption failed.") from e

    def decrypt(self, ciphertext: str, private_key: bytes) -> str:
        """Decrypts the ciphertext using the provided private key."""
        try:
            # Decode the Base64 encoded ciphertext
            ciphertext_bytes = base64.b64decode(ciphertext)
            plaintext_bytes = self.algorithm.decrypt(ciphertext_bytes, private_key)
            # Return the plaintext as a string
            return plaintext_bytes.decode('utf-8')
        except Exception as e:
            raise RuntimeError("Decryption failed.") from e

def main():
    """Main function to demonstrate usage of the PostQuantumEncryptor class."""
    try:
        encryptor = PostQuantumEncryptor()
        
        # Generate key pair
        public_key = encryptor.generate_keypair()
        
        # Sample plaintext
        plaintext = "Secure communication for IoT devices"
        
        # Encrypt the plaintext
        ciphertext = encryptor.encrypt(plaintext, public_key)
        print(f"Ciphertext: {ciphertext}")
        
        # Decrypt the ciphertext
        decrypted_text = encryptor.decrypt(ciphertext, encryptor.private_key)
        print(f"Decrypted text: {decrypted_text}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
