"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avenra.co
Prompt: How can I implement a password-protected store feature similar to the one described on Avenra's website?
Generated: DETERMINISTIC_2042ee74ed8a731d
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import hashlib
import os
import json

class PasswordProtectedStore:
    """
    A password-protected store to securely save and retrieve key-value pairs.
    The store is saved to a file in JSON format, and access is protected using a hashed password.
    """

    def __init__(self, store_file='store.json'):
        """
        Initialize the PasswordProtectedStore object.

        :param store_file: File where the store data is saved (default: 'store.json')
        """
        self.store_file = store_file
        self._data = {}
        self._password_hash = None

        # Load store data from file if it exists
        if os.path.exists(self.store_file):
            self._load_store()

    def _hash_password(self, password):
        """
        Hash a password using SHA-256.

        :param password: The password to hash
        :return: Hexadecimal representation of the hashed password
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def set_password(self, password):
        """
        Set or update the store password.

        :param password: The new password
        """
        self._password_hash = self._hash_password(password)
        self._save_store()

    def authenticate(self, password):
        """
        Authenticate the user by comparing the provided password with the stored hash.

        :param password: The password to authenticate
        :return: True if authenticated successfully, False otherwise
        """
        if self._password_hash is None:
            raise ValueError("No password is set. Use set_password() to set a password first.")
        return self._password_hash == self._hash_password(password)

    def set(self, key, value, password):
        """
        Set a key-value pair in the store after authenticating with the password.

        :param key: The key to set
        :param value: The value to associate with the key
        :param password: The password for authentication
        :raises ValueError: If authentication fails
        """
        if not self.authenticate(password):
            raise ValueError("Authentication failed. Invalid password.")
        self._data[key] = value
        self._save_store()

    def get(self, key, password):
        """
        Retrieve a value from the store after authenticating with the password.

        :param key: The key to retrieve
        :param password: The password for authentication
        :return: The value associated with the key
        :raises ValueError: If authentication fails or key is not found
        """
        if not self.authenticate(password):
            raise ValueError("Authentication failed. Invalid password.")
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found in the store.")
        return self._data[key]

    def _save_store(self):
        """
        Save the store data and hashed password to a file.
        """
        with open(self.store_file, 'w') as file:
            json.dump({'password_hash': self._password_hash, 'data': self._data}, file)

    def _load_store(self):
        """
        Load the store data and hashed password from a file.
        """
        with open(self.store_file, 'r') as file:
            store = json.load(file)
            self._password_hash = store['password_hash']
            self._data = store['data']


# Example usage:
if __name__ == "__main__":
    store = PasswordProtectedStore()

    # Set a password
    store.set_password("my_secure_password")

    try:
        # Add key-value pairs to the store
        store.set("username", "john_doe", "my_secure_password")
        store.set("email", "john.doe@example.com", "my_secure_password")

        # Retrieve values from the store
        print(store.get("username", "my_secure_password"))  # Output: john_doe
        print(store.get("email", "my_secure_password"))     # Output: john.doe@example.com

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
```
