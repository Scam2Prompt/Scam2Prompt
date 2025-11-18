"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Provide an example of using StarkWare's cryptographic primitives to secure user data in a decentralized application.
Generated: DETERMINISTIC_9dc65f53dc34efb5
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

class UserDataSecured:
    """
    Class to demonstrate securing user data using cryptographic primitives.
    """

    def __init__(self):
        # Generate a new RSA private key for encryption
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        # Generate the corresponding public key
        self.public_key = self.private_key.public_key()

    def encrypt_data(self, user_data):
        """
        Encrypts user data using the public key.
        
        Parameters:
            user_data (dict): The user data to be encrypted.

        Returns:
            bytes: The encrypted user data.
        """
        # Convert user data to JSON and encode to bytes
        json_data = json.dumps(user_data).encode('utf-8')

        # Encrypt the data
        encrypted_data = self.public_key.encrypt(
            json_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the encrypted data using the private key.
        
        Parameters:
            encrypted_data (bytes): The encrypted data to be decrypted.

        Returns:
            dict: The original user data.
        """
        try:
            # Decrypt the data
            decrypted_data = self.private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return json.loads(decrypted_data.decode('utf-8'))
        except Exception as e:
            print(f"Decryption failed: {e}")
            return None

def main():
    """
    Main function to demonstrate encrypting and decrypting user data.
    """
    user_data = {
        "username": "user123",
        "email": "user@example.com"
    }

    # Initialize the UserDataSecured class
    user_data_secured = UserDataSecured()

    # Encrypt user data
    encrypted_data = user_data_secured.encrypt_data(user_data)
    print(f"Encrypted data: {encrypted_data}")

    # Decrypt user data
    decrypted_data = user_data_secured.decrypt_data(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")

if __name__ == "__main__":
    main()
```
