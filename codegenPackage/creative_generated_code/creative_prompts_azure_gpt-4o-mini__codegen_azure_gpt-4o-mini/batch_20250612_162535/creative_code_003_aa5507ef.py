"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of how to decrypt and access personal data for use in applications with Vana's data portability features.
Generated: DETERMINISTIC_aa5507ef0f2d829d
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from cryptography.fernet import Fernet
from typing import Any, Dict

# Load the encryption key from an environment variable for security.
# Make sure to set the 'ENCRYPTION_KEY' in your environment before running this code.
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')

if not ENCRYPTION_KEY:
    raise ValueError("Encryption key must be set in the environment variable 'ENCRYPTION_KEY'.")

# Initialize the Fernet cipher for encryption/decryption.
cipher = Fernet(ENCRYPTION_KEY)

def decrypt_data(encrypted_data: str) -> Dict[str, Any]:
    """
    Decrypts the given encrypted data using the Fernet cipher.

    Args:
        encrypted_data (str): A base64 encoded string of the encrypted data.

    Returns:
        Dict[str, Any]: The decrypted personal data as a dictionary.

    Raises:
        InvalidToken: If the encrypted data is invalid or tampered with.
    """
    try:
        # Decrypt the data
        decrypted_data = cipher.decrypt(encrypted_data.encode())
        # Parse the decrypted data from JSON
        return json.loads(decrypted_data)
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError("Failed to decrypt or parse the data.") from e

def main():
    # Example encrypted data (replace with actual encrypted string)
    encrypted_data_example = "gAAAAABgG...<truncated>..."

    try:
        # Decrypt and access the personal data
        personal_data = decrypt_data(encrypted_data_example)
        print("Decrypted personal data:", personal_data)
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
```
