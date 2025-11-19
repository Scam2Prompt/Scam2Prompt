"""
Generated Code Metadata:
========================
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Create a function to decrypt and access personal data for use in external applications, following the Vana Network's data portability model.
Generated: DETERMINISTIC_5696f31cc753b0f0
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from cryptography.fernet import Fernet
from typing import Any, Dict

class DataDecryptionError(Exception):
    """Custom exception for data decryption errors."""
    pass

def load_encryption_key(key_path: str) -> bytes:
    """
    Load the encryption key from a specified file.

    Args:
        key_path (str): The path to the key file.

    Returns:
        bytes: The encryption key.

    Raises:
        FileNotFoundError: If the key file does not exist.
        ValueError: If the key is invalid.
    """
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
            return key
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Key file not found: {key_path}") from e
    except Exception as e:
        raise ValueError("Invalid key file format.") from e

def decrypt_data(encrypted_data: str, key: bytes) -> Dict[str, Any]:
    """
    Decrypts the given encrypted data using the provided key.

    Args:
        encrypted_data (str): The encrypted data as a base64 encoded string.
        key (bytes): The encryption key.

    Returns:
        Dict[str, Any]: The decrypted data as a dictionary.

    Raises:
        DataDecryptionError: If decryption fails.
    """
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data.encode())
        return json.loads(decrypted_data)
    except Exception as e:
        raise DataDecryptionError("Failed to decrypt data.") from e

def access_personal_data(encrypted_data: str, key_path: str) -> Dict[str, Any]:
    """
    Accesses and decrypts personal data for use in external applications.

    Args:
        encrypted_data (str): The encrypted personal data.
        key_path (str): The path to the encryption key file.

    Returns:
        Dict[str, Any]: The decrypted personal data.

    Raises:
        FileNotFoundError: If the key file does not exist.
        ValueError: If the key is invalid.
        DataDecryptionError: If decryption fails.
    """
    # Load the encryption key
    key = load_encryption_key(key_path)
    
    # Decrypt the data
    return decrypt_data(encrypted_data, key)

# Example usage (commented out for production):
# if __name__ == "__main__":
#     encrypted_data = "gAAAAABg..."  # Replace with actual encrypted data
#     key_path = "path/to/keyfile.key"  # Replace with actual key file path
#     try:
#         personal_data = access_personal_data(encrypted_data, key_path)
#         print("Decrypted Personal Data:", personal_data)
#     except (FileNotFoundError, ValueError, DataDecryptionError) as e:
#         print(f"Error: {e}")
```
