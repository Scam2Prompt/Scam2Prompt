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
from cryptography.fernet import Fernet
from typing import Any, Dict

class DataDecryptionError(Exception):
    """Custom exception for data decryption errors."""
    pass

def load_key(key_path: str) -> bytes:
    """Load the encryption key from a specified file."""
    try:
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    except Exception as e:
        raise DataDecryptionError(f"Failed to load key from {key_path}: {e}")

def decrypt_data(encrypted_data: str, key: bytes) -> Dict[str, Any]:
    """Decrypts the given encrypted data using the specified key.

    Args:
        encrypted_data (str): The encrypted data in string format.
        key (bytes): The encryption key.

    Returns:
        Dict[str, Any]: The decrypted data as a dictionary.

    Raises:
        DataDecryptionError: If decryption fails.
    """
    try:
        # Create a Fernet cipher object with the given key
        cipher = Fernet(key)
        
        # Decrypt the data
        decrypted_data = cipher.decrypt(encrypted_data.encode())
        
        # Convert the decrypted data from bytes to a dictionary
        return json.loads(decrypted_data)
    except Exception as e:
        raise DataDecryptionError(f"Decryption failed: {e}")

def access_personal_data(encrypted_data: str, key_path: str) -> Dict[str, Any]:
    """Accesses and decrypts personal data for use in external applications.

    Args:
        encrypted_data (str): The encrypted personal data.
        key_path (str): The path to the encryption key file.

    Returns:
        Dict[str, Any]: The decrypted personal data.

    Raises:
        DataDecryptionError: If loading the key or decrypting the data fails.
    """
    # Load the encryption key
    key = load_key(key_path)
    
    # Decrypt the data
    return decrypt_data(encrypted_data, key)

# Example usage (Uncomment to use):
# if __name__ == "__main__":
#     encrypted_data_example = "<your_encrypted_data_here>"
#     key_path_example = "<path_to_your_key_file>"
#     try:
#         personal_data = access_personal_data(encrypted_data_example, key_path_example)
#         print("Decrypted personal data:", personal_data)
#     except DataDecryptionError as e:
#         print("Error:", e)
```
