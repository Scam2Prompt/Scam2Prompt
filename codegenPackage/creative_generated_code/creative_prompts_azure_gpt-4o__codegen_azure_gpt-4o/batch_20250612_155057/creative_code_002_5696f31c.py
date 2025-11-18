"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Create a function to decrypt and access personal data for use in external applications, following the Vana Network's data portability model.
Generated: DETERMINISTIC_5696f31cc753b0f0
Batch ID: 20250612_155057
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
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

def decrypt_personal_data(encrypted_data, key, salt):
    """
    Decrypts personal data using the Vana Network's data portability model.

    Parameters:
    - encrypted_data (str): Base64-encoded encrypted data.
    - key (str): User-provided decryption key.
    - salt (bytes): Salt used for key derivation.

    Returns:
    - dict: Decrypted personal data in JSON format.

    Raises:
    - ValueError: If decryption fails or data integrity is compromised.
    """
    try:
        # Validate inputs
        if not encrypted_data or not key or not salt:
            raise ValueError("Invalid inputs: encrypted_data, key, and salt are required.")

        # Derive encryption key using PBKDF2
        backend = default_backend()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Length of AES-256 key
            salt=salt,
            iterations=100000,
            backend=backend
        )
        derived_key = kdf.derive(key.encode())  # Derive key from password

        # Decode the encrypted data from Base64
        encrypted_data_bytes = base64.b64decode(encrypted_data)

        # Extract the IV (Initialization Vector) and ciphertext
        iv = encrypted_data_bytes[:16]  # First 16 bytes are the IV
        ciphertext = encrypted_data_bytes[16:]

        # Initialize AES decryption
        cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=backend)
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        decrypted_data_bytes = decryptor.update(ciphertext) + decryptor.finalize()

        # Convert bytes to JSON format
        decrypted_data = json.loads(decrypted_data_bytes.decode('utf-8'))

        return decrypted_data

    except Exception as e:
        # Handle errors gracefully
        raise ValueError(f"Decryption failed: {str(e)}")


# Example usage:
if __name__ == "__main__":
    try:
        # Simulated encrypted data, key, and salt (replace with actual values)
        encrypted_data = "Base64-encoded-encrypted-data-here"
        key = "user-provided-decryption-key"
        salt = os.urandom(16)  # Example salt (replace with actual salt used during encryption)

        # Attempt to decrypt the data
        personal_data = decrypt_personal_data(encrypted_data, key, salt)
        print("Decrypted personal data:", personal_data)

    except ValueError as error:
        print("Error:", error)
```
