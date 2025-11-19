"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Generate code that demonstrates how to use a specific encryption technique, potentially involving base64 encoding and decoding, as suggested by the webpage's text.
Generated: DETERMINISTIC_52e88079aed13216
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import base64
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a symmetric encryption key using Fernet.
    Returns:
        key (bytes): A base64-encoded encryption key.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Encrypt a message using the provided key.
    Args:
        message (str): The plaintext message to encrypt.
        key (bytes): The base64-encoded encryption key.
    Returns:
        encrypted_message (str): The encrypted message, base64-encoded.
    """
    try:
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        return base64.b64encode(encrypted_message).decode()
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

def decrypt_message(encrypted_message, key):
    """
    Decrypt an encrypted message using the provided key.
    Args:
        encrypted_message (str): The base64-encoded encrypted message.
        key (bytes): The base64-encoded encryption key.
    Returns:
        decrypted_message (str): The decrypted plaintext message.
    """
    try:
        fernet = Fernet(key)
        encrypted_message_bytes = base64.b64decode(encrypted_message)
        decrypted_message = fernet.decrypt(encrypted_message_bytes).decode()
        return decrypted_message
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Generate a new encryption key
        key = generate_key()
        print(f"Generated Key: {key.decode()}")

        # Original message
        original_message = "This is a secret message."
        print(f"Original Message: {original_message}")

        # Encrypt the message
        encrypted_message = encrypt_message(original_message, key)
        print(f"Encrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Decrypted Message: {decrypted_message}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
