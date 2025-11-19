"""
Generated Code Metadata:
========================
Original URL: https://on1force.web.app
Prompt: Write a Python script to decrypt lore elements like the "Voice of M0R1A" using cryptographic techniques, as part of the 0N1 Force storytelling experience.
Generated: DETERMINISTIC_f23298f0aea3861e
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import base64
from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generate a secret key for encryption and decryption.

    Returns:
        bytes: A URL-safe base64-encoded key.
    """
    # Generate a secret key
    key = Fernet.generate_key()
    return key

def load_key(key_file):
    """
    Load a secret key from a file.

    Args:
        key_file (str): The path to the key file.

    Returns:
        bytes: The loaded key.

    Raises:
        FileNotFoundError: If the key file does not exist.
    """
    try:
        with open(key_file, 'rb') as f:
            key = f.read()
        return key
    except FileNotFoundError:
        print(f"Error: Key file '{key_file}' not found.")
        return None

def decrypt_message(key, encrypted_message):
    """
    Decrypt a message using the provided key.

    Args:
        key (bytes): The secret key.
        encrypted_message (str): The encrypted message.

    Returns:
        str: The decrypted message.

    Raises:
        Exception: If decryption fails.
    """
    try:
        # Create a Fernet instance with the key
        fernet = Fernet(key)
        # Decode the encrypted message from base64
        encrypted_message_bytes = base64.urlsafe_b64decode(encrypted_message)
        # Decrypt the message
        decrypted_message_bytes = fernet.decrypt(encrypted_message_bytes)
        # Return the decrypted message as a string
        return decrypted_message_bytes.decode('utf-8')
    except Exception as e:
        print(f"Error: Decryption failed - {e}")
        return None

def main():
    # Specify the key file and encrypted message
    key_file = 'secret.key'
    encrypted_message = 'encrypted_message_here'

    # Generate a key if needed
    # key = generate_key()
    # with open(key_file, 'wb') as f:
    #     f.write(key)

    # Load the key
    key = load_key(key_file)
    if key is None:
        return

    # Decrypt the message
    decrypted_message = decrypt_message(key, encrypted_message)

    if decrypted_message is not None:
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
```
