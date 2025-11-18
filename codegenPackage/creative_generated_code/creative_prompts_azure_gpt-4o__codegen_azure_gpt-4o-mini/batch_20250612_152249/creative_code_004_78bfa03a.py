"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Suggest tools or libraries to securely store sensitive client data for a law firm handling cases like domestic violence and immigration, as outlined on juridiskklinik.se.
Generated: DETERMINISTIC_78bfa03a329997ae
Batch ID: 20250612_152249
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
import base64
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

# Define a class to handle secure storage of sensitive client data
class SecureDataStore:
    def __init__(self, key_file='secret.key'):
        """
        Initialize the SecureDataStore with a key for encryption/decryption.
        If the key file does not exist, generate a new key.
        """
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.generate_key()
        self.load_key()

    def generate_key(self):
        """Generate a new Fernet key and save it to a file."""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        """Load the Fernet key from the specified key file."""
        with open(self.key_file, 'rb') as key_file:
            self.key = key_file.read()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        """
        Encrypt the given data.

        Parameters:
        data (dict): Dictionary containing sensitive client data.

        Returns:
        str: Base64 encoded string of the encrypted data.
        """
        json_data = json.dumps(data).encode('utf-8')
        encrypted_data = self.cipher.encrypt(json_data)
        return base64.urlsafe_b64encode(encrypted_data).decode('utf-8')

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the given encrypted data.

        Parameters:
        encrypted_data (str): Base64 encoded string of the encrypted data.

        Returns:
        dict: Decrypted dictionary containing sensitive client data.
        
        Raises:
        InvalidToken: If the decryption fails due to an invalid token.
        """
        try:
            decrypted_data = self.cipher.decrypt(base64.urlsafe_b64decode(encrypted_data))
            return json.loads(decrypted_data.decode('utf-8'))
        except InvalidToken:
            raise ValueError("Invalid token. Decryption failed.")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of SecureDataStore
        store = SecureDataStore()

        # Example client data to be stored securely
        client_data = {
            'name': 'John Doe',
            'sensitive_info': 'This is sensitive data',
            'case_type': 'Domestic Violence'
        }

        # Encrypt the client data
        encrypted_data = store.encrypt_data(client_data)
        print("Encrypted Data:", encrypted_data)

        # Decrypt the data back to its original form
        decrypted_data = store.decrypt_data(encrypted_data)
        print("Decrypted Data:", decrypted_data)

    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
```
