"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxtasian.com
Prompt: Recommend best practices for securely storing API keys when interacting with the IJEX Exchange platform.
Generated: DETERMINISTIC_bcba93eecd3c620e
Batch ID: 20250612_154115
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Function to generate a new key for encryption/decryption
def generate_key():
    """Generates and returns a new encryption key."""
    return Fernet.generate_key()

# Function to encrypt sensitive data (like API keys)
def encrypt_api_key(api_key: str, key: bytes) -> bytes:
    """
    Encrypts the provided API key using the provided key.

    :param api_key: The API key to encrypt.
    :param key: The encryption key.
    :return: The encrypted API key as bytes.
    """
    f = Fernet(key)
    encrypted_key = f.encrypt(api_key.encode())
    return encrypted_key

# Function to decrypt sensitive data (like API keys)
def decrypt_api_key(encrypted_key: bytes, key: bytes) -> str:
    """
    Decrypts the provided encrypted API key using the provided key.

    :param encrypted_key: The encrypted API key to decrypt.
    :param key: The decryption key.
    :return: The decrypted API key as a string.
    """
    f = Fernet(key)
    decrypted_key = f.decrypt(encrypted_key).decode()
    return decrypted_key

# Function to save the encrypted API key to a file
def save_encrypted_key(file_path: str, encrypted_key: bytes) -> None:
    """
    Saves the encrypted API key to a specified file.

    :param file_path: The path to the file where the encrypted key will be stored.
    :param encrypted_key: The encrypted API key to save.
    """
    try:
        with open(file_path, 'wb') as file:
            file.write(encrypted_key)
    except IOError as e:
        print(f"Error saving encrypted API key: {e}")

# Function to load the encrypted API key from a file
def load_encrypted_key(file_path: str) -> bytes:
    """
    Loads the encrypted API key from a specified file.

    :param file_path: The path to the file containing the encrypted key.
    :return: The encrypted API key as bytes.
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except IOError as e:
        print(f"Error loading encrypted API key: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Example usage
    api_key = os.getenv('IJEX_API_KEY')  # Load API key from environment variable
    if not api_key:
        print("API key not found in environment variables.")
        exit(1)

    # Generate a new encryption key (store this securely)
    encryption_key = generate_key()

    # Encrypt the API key
    encrypted_api_key = encrypt_api_key(api_key, encryption_key)

    # Save the encrypted API key
    save_encrypted_key('encrypted_api_key.bin', encrypted_api_key)

    # Load the encrypted API key
    loaded_encrypted_key = load_encrypted_key('encrypted_api_key.bin')
    if loaded_encrypted_key:
        # Decrypt the API key
        decrypted_api_key = decrypt_api_key(loaded_encrypted_key, encryption_key)
        print(f"Decrypted API Key: {decrypted_api_key}")
```

Make sure to install the required packages by running:
```bash
pip install python-dotenv cryptography
```

Additionally, create a `.env` file at your project root containing your API key:
```plaintext
IJEX_API_KEY=your_actual_api_key_here
```
