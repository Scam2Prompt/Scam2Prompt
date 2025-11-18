"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Generate code to implement advanced security measures for confidential data processing in outsourcing models, as highlighted on Vital Corporate Solutions' website.
Generated: DETERMINISTIC_3a06466c4f4809a2
Batch ID: 20250612_153225
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
import logging
from cryptography.fernet import Fernet
from typing import Any, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecureDataProcessor:
    def __init__(self, encryption_key: bytes):
        """
        Initialize the SecureDataProcessor with an encryption key.
        
        :param encryption_key: A bytes object representing the encryption key.
        """
        self.fernet = Fernet(encryption_key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new encryption key.
        
        :return: A bytes object representing the new encryption key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: Dict[str, Any]) -> str:
        """
        Encrypt the provided data.
        
        :param data: A dictionary containing data to encrypt.
        :return: An encrypted string representation of the data.
        """
        try:
            json_data = json.dumps(data).encode('utf-8')  # Convert data to JSON string
            encrypted_data = self.fernet.encrypt(json_data)  # Encrypt the JSON string
            return encrypted_data.decode('utf-8')  # Return as a UTF-8 string
        except Exception as e:
            logging.error("Error encrypting data: %s", e)
            raise

    def decrypt_data(self, encrypted_data: str) -> Dict[str, Any]:
        """
        Decrypt the provided encrypted data.
        
        :param encrypted_data: The encrypted string to decrypt.
        :return: A dictionary containing the decrypted data.
        """
        try:
            decrypted_data = self.fernet.decrypt(encrypted_data.encode('utf-8'))  # Decrypt the data
            return json.loads(decrypted_data.decode('utf-8'))  # Convert back to dictionary
        except Exception as e:
            logging.error("Error decrypting data: %s", e)
            raise

def main():
    # Example usage
    try:
        # Generate a secure key for encryption
        key = SecureDataProcessor.generate_key()
        logging.info("Generated Key: %s", key)

        processor = SecureDataProcessor(key)

        # Sample confidential data
        confidential_data = {
            "client_id": "12345",
            "project_details": "Data analysis for Q1 revenues",
            "access_level": "high"
        }

        # Encrypt the confidential data
        encrypted_data = processor.encrypt_data(confidential_data)
        logging.info("Encrypted Data: %s", encrypted_data)

        # Decrypt the data for processing
        decrypted_data = processor.decrypt_data(encrypted_data)
        logging.info("Decrypted Data: %s", decrypted_data)

    except Exception as e:
        logging.error("An error occurred in main: %s", e)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have the `cryptography` library installed before running the code. You can install it using pip:
```bash
pip install cryptography
```
