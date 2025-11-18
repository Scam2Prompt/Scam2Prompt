"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icrossingappxyz.com
Prompt: Recommend libraries or APIs for securely handling personal data and device IDs in a mobile application, similar to the functionality described in "Identitas Kependudukan Digital."
Generated: DETERMINISTIC_c7e68fb0f1179e16
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python example demonstrating secure handling of personal data and device IDs in a mobile application.
# This code uses appropriate libraries for encryption, environment configuration, and secure storage.

import os
import json
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants for secure handling
# Generate or store this key securely in a production environment
# Do NOT hardcode this key; use environment variables or a secure key vault.
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')

if ENCRYPTION_KEY is None:
    raise ValueError("Encryption key is not set in environment variables. Please configure ENCRYPTION_KEY.")

# Initialize the Fernet encryption instance
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_data(data: dict) -> str:
    """
    Encrypts a dictionary containing sensitive personal data or device IDs.

    Args:
        data (dict): The data to be encrypted.

    Returns:
        str: The encrypted data as a Base64-encoded string.
    """
    try:
        # Serialize the dictionary to a JSON string
        json_data = json.dumps(data)
        # Perform encryption
        encrypted_data = cipher.encrypt(json_data.encode())
        return encrypted_data.decode()  # Return as string for storage/transfer
    except Exception as e:
        raise RuntimeError(f"Failed to encrypt data: {e}")

def decrypt_data(encrypted_data: str) -> dict:
    """
    Decrypts an encrypted Base64-encoded string back into a dictionary.

    Args:
        encrypted_data (str): The encrypted data.

    Returns:
        dict: The decrypted dictionary.
    """
    try:
        # Decode the encrypted data
        decrypted_data = cipher.decrypt(encrypted_data.encode())
        # Deserialize the JSON string back into a dictionary
        return json.loads(decrypted_data.decode())
    except Exception as e:
        raise RuntimeError(f"Failed to decrypt data: {e}")

def store_secure_data(data: dict, file_path: str):
    """
    Securely stores encrypted data into a file.

    Args:
        data (dict): The data to be encrypted and stored.
        file_path (str): Path to the file where the encrypted data will be stored.
    """
    try:
        encrypted_data = encrypt_data(data)
        with open(file_path, 'w') as file:
            file.write(encrypted_data)
    except Exception as e:
        raise RuntimeError(f"Failed to store secure data: {e}")

def load_secure_data(file_path: str) -> dict:
    """
    Loads and decrypts data from a secure file.

    Args:
        file_path (str): Path to the file containing the encrypted data.

    Returns:
        dict: The decrypted data.
    """
    try:
        with open(file_path, 'r') as file:
            encrypted_data = file.read()
        return decrypt_data(encrypted_data)
    except Exception as e:
        raise RuntimeError(f"Failed to load secure data: {e}")

# Example usage
if __name__ == "__main__":
    # Example sensitive data
    sensitive_data = {
        "personal_id": "1234567890",
        "device_id": "ABCDEF123456",
        "name": "John Doe",
    }

    # Path to store encrypted data
    secure_file_path = "secure_data.txt"

    try:
        print("Encrypting and storing data securely...")
        store_secure_data(sensitive_data, secure_file_path)

        print("Loading and decrypting data securely...")
        loaded_data = load_secure_data(secure_file_path)

        print("Decrypted data:", loaded_data)
    except Exception as error:
        print(f"An error occurred: {error}")
```

### Dependencies:
1. Install `cryptography` for encryption: `pip install cryptography`
2. Install `python-dotenv` for environment variable management: `pip install python-dotenv`

### Notes:
- Ensure the `.env` file contains the `ENCRYPTION_KEY` variable with a valid key generated using `Fernet.generate_key()` (do this securely outside of the code).
- Never hardcode sensitive data or encryption keys in production code.
- Use a secure backend service for sensitive operations in large-scale applications.
