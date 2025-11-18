"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointrusts-mining.com
Prompt: Develop a secure system for offline storage of cryptocurrency wallet details, as emphasized in Cointrust-mining's security measures.
Generated: DETERMINISTIC_e465854fbfa39111
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class OfflineCryptoWalletStorage:
    def __init__(self, password: str):
        """
        Initialize the storage system with an encryption key derived from the user password.
        """
        self.backend = default_backend()
        self.salt = os.urandom(16)  # Random salt for PBKDF2 key derivation
        self.key = self._derive_key(password)

    def _derive_key(self, password: str):
        """
        Derive a secure encryption key using PBKDF2 with the provided password and a random salt.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100_000,
            backend=self.backend
        )
        return kdf.derive(password.encode())

    def encrypt_data(self, data: dict) -> bytes:
        """
        Encrypt the given data using AES with the derived key in GCM mode for security.
        """
        iv = os.urandom(12)  # 12-byte IV for GCM mode
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        json_data = json.dumps(data).encode('utf-8')  # Convert dictionary to JSON string
        encrypted_data = encryptor.update(json_data) + encryptor.finalize()
        return base64.b64encode(iv + encryptor.tag + encrypted_data)

    def decrypt_data(self, encrypted_data: bytes) -> dict:
        """
        Decrypt the encrypted data and return the original dictionary.
        """
        decoded_data = base64.b64decode(encrypted_data)
        iv = decoded_data[:12]
        tag = decoded_data[12:28]
        encrypted_payload = decoded_data[28:]
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=self.backend)
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_payload) + decryptor.finalize()
        return json.loads(decrypted_data.decode('utf-8'))

    def store_wallet_details(self, filepath: str, wallet_details: dict):
        """
        Securely store wallet details in an encrypted file.
        """
        encrypted_data = self.encrypt_data(wallet_details)
        with open(filepath, 'wb') as file:
            file.write(self.salt + encrypted_data)  # Save salt along with the encrypted data

    def load_wallet_details(self, filepath: str) -> dict:
        """
        Load and decrypt wallet details from a file.
        """
        with open(filepath, 'rb') as file:
            file_data = file.read()
        self.salt = file_data[:16]  # Extract salt from the file
        encrypted_data = file_data[16:]  # Extract encrypted data
        self.key = self._derive_key(password)  # Derive the key again using the extracted salt
        return self.decrypt_data(encrypted_data)

# Example usage:
# wallet_storage = OfflineCryptoWalletStorage(password="secure_password")
# wallet_storage.store_wallet_details("wallet.dat", {"address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "private_key": "L5BmH1sdQ..."})
# loaded_details = wallet_storage.load_wallet_details("wallet.dat")
# print(loaded_details)
```
