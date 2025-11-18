"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Create a script that simulates the scanning of a QR code and establishes a secure communication channel between the finder and the owner, as described in QRubi's functionality.
Generated: DETERMINISTIC_a5b98d62e6b8e2bd
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import json
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7

# Simulate QR Code Scanning and Secure Communication
class QRubi:
    def __init__(self):
        self.secret_key = None  # Shared key for secure communication

    def generate_qr_data(self):
        """
        Generates QR code data with simulated owner information.
        """
        owner_data = {
            "owner_id": "12345",
            "owner_public_key": base64.b64encode(os.urandom(32)).decode('utf-8'),
        }
        qr_data = json.dumps(owner_data)
        return qr_data

    def scan_qr_code(self, qr_data):
        """
        Simulates scanning a QR code and extracting the owner's information.
        """
        try:
            # Parse QR data
            owner_info = json.loads(qr_data)
            if "owner_id" in owner_info and "owner_public_key" in owner_info:
                return owner_info
            else:
                raise ValueError("Invalid QR Code data.")
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error scanning QR Code: {e}")
            return None

    def establish_secure_channel(self, owner_info):
        """
        Establishes a secure communication channel using a shared secret.
        """
        try:
            # Generate shared secret key using owner's public key (simulated)
            salt = os.urandom(16)  # Random salt for key derivation
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            self.secret_key = kdf.derive(owner_info["owner_public_key"].encode('utf-8'))
            print("Secure communication channel established.")
        except Exception as e:
            print(f"Error establishing secure channel: {e}")
            self.secret_key = None

    def encrypt_message(self, message):
        """
        Encrypts a message using the established secret key.
        """
        try:
            if not self.secret_key:
                raise ValueError("Secret key not established.")
            
            # Encrypt message
            iv = os.urandom(16)  # Initialization vector
            cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            padder = PKCS7(128).padder()
            padded_message = padder.update(message.encode('utf-8')) + padder.finalize()
            encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
            
            # Return IV and encrypted message
            return base64.b64encode(iv).decode('utf-8'), base64.b64encode(encrypted_message).decode('utf-8')
        except Exception as e:
            print(f"Error encrypting message: {e}")
            return None, None

    def decrypt_message(self, iv, encrypted_message):
        """
        Decrypts an encrypted message using the established secret key.
        """
        try:
            if not self.secret_key:
                raise ValueError("Secret key not established.")
            
            # Decrypt message
            iv = base64.b64decode(iv)
            encrypted_message = base64.b64decode(encrypted_message)
            cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
            unpadder = PKCS7(128).unpadder()
            message = unpadder.update(padded_message) + unpadder.finalize()
            
            return message.decode('utf-8')
        except Exception as e:
            print(f"Error decrypting message: {e}")
            return None


# Example usage
if __name__ == "__main__":
    qrubi = QRubi()

    # Step 1: Generate QR code data
    qr_data = qrubi.generate_qr_data()
    print("Generated QR Code Data:", qr_data)

    # Step 2: Scan QR code
    owner_info = qrubi.scan_qr_code(qr_data)
    if owner_info:
        print("Scanned Owner Info:", owner_info)

        # Step 3: Establish Secure Channel
        qrubi.establish_secure_channel(owner_info)

        # Step 4: Encrypt and Decrypt Messages
        message = "Hello, secure world!"
        iv, encrypted_message = qrubi.encrypt_message(message)
        if iv and encrypted_message:
            print("Encrypted Message:", encrypted_message)
            print("Decrypted Message:", qrubi.decrypt_message(iv, encrypted_message))
```
