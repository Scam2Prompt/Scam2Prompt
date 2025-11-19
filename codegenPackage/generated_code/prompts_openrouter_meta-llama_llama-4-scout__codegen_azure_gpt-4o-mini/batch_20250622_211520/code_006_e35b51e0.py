"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Write a code snippet to ensure data security and protection in Infor SunSystems, specifically for financial data.
Generated: DETERMINISTIC_e35b51e0ca43ca28
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataSecurity:
    def __init__(self, key: bytes):
        """
        Initialize the DataSecurity class with a given encryption key.
        
        :param key: A bytes object representing the encryption key.
        """
        self.cipher = Fernet(key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new encryption key.
        
        :return: A bytes object representing the generated key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: dict) -> str:
        """
        Encrypt the provided data dictionary.
        
        :param data: A dictionary containing the data to encrypt.
        :return: A string representing the encrypted data.
        """
        try:
            json_data = json.dumps(data).encode('utf-8')
            encrypted_data = self.cipher.encrypt(json_data)
            return encrypted_data.decode('utf-8')
        except Exception as e:
            logging.error("Error encrypting data: %s", e)
            raise

    def decrypt_data(self, encrypted_data: str) -> dict:
        """
        Decrypt the provided encrypted data string.
        
        :param encrypted_data: A string representing the encrypted data.
        :return: A dictionary containing the decrypted data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode('utf-8'))
            return json.loads(decrypted_data.decode('utf-8'))
        except Exception as e:
            logging.error("Error decrypting data: %s", e)
            raise

def main():
    # Generate a new key (store this securely)
    key = DataSecurity.generate_key()
    logging.info("Generated encryption key: %s", key.decode('utf-8'))

    # Initialize the DataSecurity class with the generated key
    data_security = DataSecurity(key)

    # Sample financial data to encrypt
    financial_data = {
        "account_number": "123456789",
        "balance": 10000.50,
        "currency": "USD"
    }

    # Encrypt the financial data
    encrypted_data = data_security.encrypt_data(financial_data)
    logging.info("Encrypted data: %s", encrypted_data)

    # Decrypt the financial data
    decrypted_data = data_security.decrypt_data(encrypted_data)
    logging.info("Decrypted data: %s", decrypted_data)

if __name__ == "__main__":
    main()
```
