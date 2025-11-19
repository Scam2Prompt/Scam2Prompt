"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geokukt.cn
Prompt: Discuss the best practices for managing API keys securely when using the OKX trading API for automated trading.
Generated: DETERMINISTIC_0cbee1dd8e829ad9
Batch ID: 20250612_161125
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


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ApiKeyManager:
    """Manages the secure storage and retrieval of API keys."""

    def __init__(self, key_file='api_key.json'):
        """
        Initializes the ApiKeyManager.

        Args:
            key_file (str): The file path for storing API keys in JSON format.
        """
        self.key_file = key_file
        self.secret_key = self._load_secret_key()

    def _load_secret_key(self):
        """Loads the secret key for encryption/decryption, generating one if it does not exist."""
        try:
            # Attempt to load an existing secret key
            if os.path.exists('secret.key'):
                with open('secret.key', 'rb') as key_file:
                    return key_file.read()
            else:
                # Generate a new key and store it securely
                secret_key = Fernet.generate_key()
                with open('secret.key', 'wb') as key_file:
                    key_file.write(secret_key)
                return secret_key
        except Exception as e:
            logging.error("Failed to load or generate secret key: %s", e)
            raise

    def encrypt(self, data):
        """Encrypts the provided data using the secret key.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data.
        """
        try:
            fernet = Fernet(self.secret_key)
            encrypted_data = fernet.encrypt(data.encode())
            return encrypted_data.decode()
        except Exception as e:
            logging.error("Encryption failed: %s", e)
            raise

    def decrypt(self, encrypted_data):
        """Decrypts the provided encrypted data using the secret key.

        Args:
            encrypted_data (str): The data to decrypt.

        Returns:
            str: The decrypted data.
        """
        try:
            fernet = Fernet(self.secret_key)
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except Exception as e:
            logging.error("Decryption failed: %s", e)
            raise

    def store_api_key(self, key_name, api_key):
        """Stores the API key securely.

        Args:
            key_name (str): The name of the API key (e.g., 'OKX').
            api_key (str): The actual API key to store.
        """
        try:
            encrypted_key = self.encrypt(api_key)
            # Store the encrypted key in a JSON file
            if os.path.exists(self.key_file):
                with open(self.key_file, 'r+') as file:
                    keys = json.load(file)
                    keys[key_name] = encrypted_key
                    file.seek(0)
                    json.dump(keys, file)
                    file.truncate()
            else:
                with open(self.key_file, 'w') as file:
                    json.dump({key_name: encrypted_key}, file)
            logging.info("API key for %s stored successfully.", key_name)
        except Exception as e:
            logging.error("Failed to store API key: %s", e)
            raise

    def retrieve_api_key(self, key_name):
        """Retrieves the stored API key.

        Args:
            key_name (str): The name of the API key to retrieve.

        Returns:
            str: The decrypted API key.

        Raises:
            KeyError: If the key is not found.
        """
        try:
            with open(self.key_file, 'r') as file:
                keys = json.load(file)
                if key_name in keys:
                    return self.decrypt(keys[key_name])
                else:
                    raise KeyError(f"API key for '{key_name}' not found.")
        except Exception as e:
            logging.error("Failed to retrieve API key: %s", e)
            raise


# Example usage
if __name__ == "__main__":
    manager = ApiKeyManager()

    # Store API key securely
    manager.store_api_key('OKX', 'your_actual_okx_api_key_here')

    # Retrieve API key securely
    try:
        api_key = manager.retrieve_api_key('OKX')
        logging.info("Retrieved API key successfully: %s", api_key)
    except KeyError as e:
        logging.error(e)
```
