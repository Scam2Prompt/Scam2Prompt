"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Provide an example of using StarkWare's cryptographic primitives to secure user data in a decentralized application.
Generated: DETERMINISTIC_9dc65f53dc34efb5
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from starkware.crypto.signature.signature import sign, verify
from starkware.crypto.hash.hash import pedersen_hash

class UserDataSecure:
    def __init__(self, private_key: bytes):
        """
        Initialize the UserDataSecure class with a private key.

        :param private_key: The private key used for signing data.
        """
        self.private_key = private_key

    def sign_data(self, data: dict) -> dict:
        """
        Sign the user data using the private key.

        :param data: The user data to be signed.
        :return: A dictionary containing the original data and its signature.
        """
        # Convert data to JSON string for signing
        data_str = json.dumps(data, sort_keys=True).encode('utf-8')
        
        # Generate a signature for the data
        signature = sign(data_str, self.private_key)
        
        return {
            'data': data,
            'signature': signature
        }

    def verify_data(self, signed_data: dict, public_key: bytes) -> bool:
        """
        Verify the signed user data using the public key.

        :param signed_data: The signed data containing the original data and signature.
        :param public_key: The public key corresponding to the private key used for signing.
        :return: True if the signature is valid, False otherwise.
        """
        # Convert data to JSON string for verification
        data_str = json.dumps(signed_data['data'], sort_keys=True).encode('utf-8')
        
        # Verify the signature
        return verify(data_str, signed_data['signature'], public_key)

    def hash_data(self, data: dict) -> bytes:
        """
        Hash the user data using the Pedersen hash function.

        :param data: The user data to be hashed.
        :return: The hash of the data.
        """
        # Convert data to JSON string for hashing
        data_str = json.dumps(data, sort_keys=True).encode('utf-8')
        
        # Generate a hash for the data
        return pedersen_hash(data_str)

# Example usage
if __name__ == "__main__":
    # Generate a random private key (in practice, use a secure key management system)
    private_key = os.urandom(32)
    public_key = os.urandom(32)  # In practice, derive this from the private key

    # Create an instance of UserDataSecure
    user_data_secure = UserDataSecure(private_key)

    # User data to be secured
    user_data = {
        'username': 'user123',
        'email': 'user123@example.com',
        'age': 30
    }

    # Sign the user data
    signed_data = user_data_secure.sign_data(user_data)

    # Verify the signed data
    is_valid = user_data_secure.verify_data(signed_data, public_key)
    print(f"Is the signed data valid? {is_valid}")

    # Hash the user data
    data_hash = user_data_secure.hash_data(user_data)
    print(f"Hash of the user data: {data_hash.hex()}")
```
