"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of how to decrypt and access personal data for use in applications with Vana's data portability features.
Generated: DETERMINISTIC_aa5507ef0f2d829d
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import base64
import cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


class VanaDataDecryptor:
    def __init__(self, encryption_key: bytes, iv: bytes):
        """
        Initialize the decryptor with the encryption key and initialization vector (IV).
        :param encryption_key: Symmetric encryption key (32 bytes for AES-256).
        :param iv: Initialization vector (16 bytes for AES).
        """
        if len(encryption_key) != 32:
            raise ValueError("Encryption key must be 32 bytes for AES-256.")
        if len(iv) != 16:
            raise ValueError("Initialization vector (IV) must be 16 bytes.")

        self.encryption_key = encryption_key
        self.iv = iv
        self.backend = default_backend()

    def decrypt_data(self, encrypted_data: str) -> dict:
        """
        Decrypt the encrypted data and return it as a dictionary.
        :param encrypted_data: Base64-encoded string of the encrypted data.
        :return: Decrypted data as a Python dictionary.
        """
        try:
            # Decode the base64-encoded encrypted data
            encrypted_bytes = base64.b64decode(encrypted_data)

            # Initialize the AES cipher in CBC mode
            cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(self.iv), backend=self.backend)
            decryptor = cipher.decryptor()

            # Decrypt the data
            padded_plaintext = decryptor.update(encrypted_bytes) + decryptor.finalize()

            # Unpad the decrypted data
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            plaintext_bytes = unpadder.update(padded_plaintext) + unpadder.finalize()

            # Convert the plaintext bytes to a JSON string and then parse it as a Python dictionary
            plaintext = plaintext_bytes.decode('utf-8')
            decrypted_data = json.loads(plaintext)

            return decrypted_data
        except (ValueError, cryptography.exceptions.InvalidKey, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to decrypt data: {str(e)}") from e


# Example Usage
if __name__ == "__main__":
    # Example key and IV (DO NOT use hardcoded keys in production!)
    encryption_key = b"0123456789abcdef0123456789abcdef"  # 32 bytes for AES-256
    iv = b"0123456789abcdef"                             # 16 bytes for AES

    # Example encrypted data (Base64-encoded string)
    # Note: Replace this with actual encrypted data from Vana's data portability feature.
    encrypted_data = "c29tZWVuY3J5cHRlZGRhdGE="

    try:
        decryptor = VanaDataDecryptor(encryption_key, iv)
        decrypted_data = decryptor.decrypt_data(encrypted_data)

        print("Decrypted Data:", decrypted_data)
    except RuntimeError as e:
        print(f"Error: {e}")
```
