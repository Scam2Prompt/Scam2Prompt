"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on1force.web.app
Prompt: Write a Python script to decrypt lore elements like the "Voice of M0R1A" using cryptographic techniques, as part of the 0N1 Force storytelling experience.
Generated: DETERMINISTIC_f23298f0aea3861e
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.fernet import Fernet
import base64
import hashlib
from typing import Optional

def generate_key() -> bytes:
    """
    Generate a Fernet key for encryption and decryption.

    Returns:
        bytes: A base64 encoded 32-byte key for Fernet.
    """
    return Fernet.generate_key()

def load_key(key_path: str) -> bytes:
    """
    Load a pre-existing key from a file.

    Args:
        key_path (str): The file path to the key.

    Returns:
        bytes: The loaded key.

    Raises:
        FileNotFoundError: If the key file does not exist.
        Exception: For any other errors that may occur during reading.
    """
    try:
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The key file '{key_path}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the key: {e}")

def decrypt_message(encrypted_message: bytes, key: bytes) -> Optional[str]:
    """
    Decrypt an encrypted message using Fernet symmetric encryption.

    Args:
        encrypted_message (bytes): The message to decrypt.
        key (bytes): The Fernet key used for decryption.

    Returns:
        Optional[str]: The decrypted message or None if decryption fails.
    """
    try:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message)
        return decrypted_message.decode('utf-8')
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

def main():
    """
    Main function to run the decryption process for lore elements.
    """
    # Path to the key file (ensure you have the correct path)
    key_path = "secret.key"
    
    # Load the key
    try:
        key = load_key(key_path)
    except Exception as e:
        print(e)
        return

    # Example encrypted message (base64 encoded)
    encrypted_message_base64 = input("Enter the encrypted message (base64): ")
    
    try:
        # Decode the base64 message
        encrypted_message = base64.b64decode(encrypted_message_base64)
    except Exception as e:
        print(f"Error decoding base64 message: {e}")
        return

    # Attempt to decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    
    if decrypted_message is not None:
        print("Decrypted message:", decrypted_message)
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()
```

Make sure to install the required `cryptography` library before running the script:

```bash
pip install cryptography
```
