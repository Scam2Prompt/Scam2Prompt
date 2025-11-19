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
import base64
from cryptography.fernet import Fernet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Decryptor:
    def __init__(self, key: str):
        """
        Initialize the Decryptor with a given key.

        :param key: A base64 encoded key for Fernet encryption.
        """
        self.key = key.encode()  # Encode the key to bytes
        self.cipher = Fernet(self.key)

    def decrypt(self, encrypted_message: str) -> str:
        """
        Decrypts an encrypted message using the Fernet cipher.

        :param encrypted_message: The encrypted message as a base64 encoded string.
        :return: The decrypted message as a string.
        """
        try:
            # Decode the encrypted message from base64
            encrypted_message_bytes = base64.urlsafe_b64decode(encrypted_message)
            # Decrypt the message
            decrypted_message = self.cipher.decrypt(encrypted_message_bytes)
            return decrypted_message.decode()  # Return as string
        except Exception as e:
            logging.error("Decryption failed: %s", e)
            raise ValueError("Decryption failed. Please check the encrypted message and key.") from e

def main():
    # Example usage
    # Replace with your actual key and encrypted message
    key = "YOUR_BASE64_ENCODED_KEY_HERE"
    encrypted_message = "YOUR_ENCRYPTED_MESSAGE_HERE"

    decryptor = Decryptor(key)

    try:
        decrypted_message = decryptor.decrypt(encrypted_message)
        logging.info("Decrypted message: %s", decrypted_message)
    except ValueError as e:
        logging.error("Error during decryption: %s", e)

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_BASE64_ENCODED_KEY_HERE` and `YOUR_ENCRYPTED_MESSAGE_HERE` with the actual key and encrypted message you wish to decrypt. Ensure that the key is a valid base64 encoded string used for Fernet encryption.
