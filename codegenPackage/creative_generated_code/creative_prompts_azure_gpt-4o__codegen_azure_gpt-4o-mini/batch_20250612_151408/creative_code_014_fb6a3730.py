"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Write code to implement TPWallet's encryption features for securing user data in a blockchain-based voting system.
Generated: DETERMINISTIC_fb6a3730df723f96
Batch ID: 20250612_151408
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
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class TPWalletEncryption:
    """
    A class to implement encryption features for securing user data in a
    blockchain-based voting system.
    """

    def __init__(self):
        """
        Initializes the TPWalletEncryption instance by generating a key if it does not exist.
        """
        self.key_filename = 'encryption_key.key'
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Loads the encryption key from a file, or generates a new one if the file does not exist.

        Returns:
            bytes: The encryption key.
        """
        if os.path.exists(self.key_filename):
            with open(self.key_filename, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_filename, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypts the provided data.

        Args:
            data (dict): The data to encrypt.

        Returns:
            str: The encrypted data as a base64 encoded string.
        """
        fernet = Fernet(self.key)
        json_data = json.dumps(data).encode()
        encrypted_data = fernet.encrypt(json_data)
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the provided encrypted data.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            dict: The decrypted data.

        Raises:
            InvalidToken: If the decryption fails, indicating the token is invalid.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return json.loads(decrypted_data)
        except InvalidToken:
            raise ValueError("Invalid encryption token. Decryption failed.")

# Example usage of TPWalletEncryption
if __name__ == "__main__":
    encryption_tool = TPWalletEncryption()

    # Sample user data to be secured
    user_data = {
        "user_id": "12345",
        "vote": "CandidateA",
        "timestamp": "2023-10-01T12:00:00Z"
    }

    # Encrypt user data
    encrypted = encryption_tool.encrypt_data(user_data)
    print("Encrypted data:", encrypted)

    # Decrypt user data
    try:
        decrypted = encryption_tool.decrypt_data(encrypted)
        print("Decrypted data:", decrypted)
    except ValueError as e:
        print(e)
```
