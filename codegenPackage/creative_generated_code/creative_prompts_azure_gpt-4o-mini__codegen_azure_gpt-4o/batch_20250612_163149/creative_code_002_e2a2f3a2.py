"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnznc.cn
Prompt: What are the best practices for ensuring asset security in a cryptocurrency trading app like OKX, including encryption methods?
Generated: DETERMINISTIC_e2a2f3a26591a628
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7

class CryptoAssetSecurity:
    def __init__(self, encryption_key: str):
        """
        Initializes the CryptoAssetSecurity class with an encryption key.
        :param encryption_key: A user-provided secure key for encryption.
        """
        self.key = self._generate_secure_key(encryption_key)
        self.backend = default_backend()
    
    def _generate_secure_key(self, password: str, salt: bytes = None) -> bytes:
        """
        Generates a secure key using PBKDF2 with a salt.
        :param password: User-provided password.
        :param salt: Randomly generated salt. If not provided, a new one will be created.
        :return: A securely derived key.
        """
        # Generate a new random salt if not provided
        if salt is None:
            salt = os.urandom(16)
        
        # Derive the key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=self.backend
        )
        return kdf.derive(password.encode())

    def encrypt_data(self, plaintext: str) -> dict:
        """
        Encrypts plaintext data using AES encryption.
        :param plaintext: The data to be encrypted.
        :return: A dictionary containing encrypted data and the initialization vector (IV).
        """
        try:
            # Generate a random initialization vector (IV)
            iv = os.urandom(16)
            # Set up AES cipher with CBC mode and PKCS7 padding
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
            encryptor = cipher.encryptor()
            padder = PKCS7(128).padder()
            padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
            return {"ciphertext": ciphertext, "iv": iv}
        except Exception as e:
            raise ValueError(f"Encryption failed: {e}")

    def decrypt_data(self, ciphertext: bytes, iv: bytes) -> str:
        """
        Decrypts AES-encrypted data.
        :param ciphertext: The encrypted text.
        :param iv: The initialization vector used during encryption.
        :return: The decrypted plaintext.
        """
        try:
            # Set up AES cipher with CBC mode and PKCS7 padding
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
            decryptor = cipher.decryptor()
            unpadder = PKCS7(128).unpadder()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            return plaintext.decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes user passwords securely using SHA-256.
        :param password: The password to be hashed.
        :return: The hashed password as a hexadecimal string.
        """
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the security module with a user-defined key
        security_module = CryptoAssetSecurity(encryption_key="strongpassword123")

        # Encrypt sensitive data (e.g., API keys, account details)
        sensitive_data = "API_KEY_1234567890"
        encrypted = security_module.encrypt_data(sensitive_data)
        print(f"Encrypted data: {encrypted}")

        # Decrypt the data
        decrypted = security_module.decrypt_data(encrypted["ciphertext"], encrypted["iv"])
        print(f"Decrypted data: {decrypted}")

        # Hash a user password
        hashed_password = security_module.hash_password("user-secure-password")
        print(f"Hashed password: {hashed_password}")
    except Exception as error:
        print(f"Error: {error}")
```
