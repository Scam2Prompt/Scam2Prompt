"""
Generated Code Metadata:
========================
Original URL: https://avenra.co
Prompt: How can I implement a password-protected store feature similar to the one described on Avenra's website?
Generated: DETERMINISTIC_2042ee74ed8a731d
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import json

class PasswordProtectedStore:
    """
    A class to implement a password-protected store feature.
    Data is encrypted using a password-derived key.
    """

    def __init__(self, store_file='store.json'):
        """
        Initialize the store with a file to save data.
        :param store_file: Path to the file where the store data will be saved.
        """
        self.store_file = store_file
        self.data = {}
        self.salt = None

    def _generate_key(self, password):
        """
        Generate a key using the provided password and a salt.
        :param password: The password to derive the key.
        :return: A key derived from the password and salt.
        """
        if not self.salt:
            # Generate a new salt if it doesn't exist
            self.salt = os.urandom(16)
        return hashlib.pbkdf2_hmac('sha256', password.encode(), self.salt, 100000)

    def set_password(self, password):
        """
        Set a password for the store. This will initialize the salt and key.
        :param password: The password to protect the store.
        """
        self.key = self._generate_key(password)

    def add_item(self, key, value):
        """
        Add an item to the store.
        :param key: The key for the item.
        :param value: The value of the item.
        """
        if not hasattr(self, 'key'):
            raise ValueError("Password must be set before adding items.")
        self.data[key] = value

    def get_item(self, key):
        """
        Retrieve an item from the store.
        :param key: The key of the item to retrieve.
        :return: The value of the item.
        """
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"Key '{key}' not found in the store.")

    def save_store(self):
        """
        Save the store data to a file, encrypting it with the password-derived key.
        """
        if not hasattr(self, 'key'):
            raise ValueError("Password must be set before saving the store.")
        encrypted_data = hashlib.pbkdf2_hmac('sha256', json.dumps(self.data).encode(), self.key, 100000)
        with open(self.store_file, 'wb') as f:
            f.write(self.salt + encrypted_data)

    def load_store(self, password):
        """
        Load the store data from a file, decrypting it with the provided password.
        :param password: The password to decrypt the store.
        """
        if not os.path.exists(self.store_file):
            raise FileNotFoundError(f"Store file '{self.store_file}' not found.")
        with open(self.store_file, 'rb') as f:
            file_content = f.read()
            self.salt = file_content[:16]
            encrypted_data = file_content[16:]
            self.key = self._generate_key(password)
            try:
                decrypted_data = hashlib.pbkdf2_hmac('sha256', encrypted_data, self.key, 100000)
                self.data = json.loads(decrypted_data.decode())
            except Exception as e:
                raise ValueError("Incorrect password or corrupted store file.") from e


# Example usage:
if __name__ == "__main__":
    store = PasswordProtectedStore()

    # Set a password for the store
    store.set_password("my_secure_password")

    # Add items to the store
    store.add_item("username", "admin")
    store.add_item("password", "12345")

    # Save the store to a file
    store.save_store()

    # Load the store from the file
    new_store = PasswordProtectedStore()
    new_store.load_store("my_secure_password")

    # Retrieve an item from the store
    print(new_store.get_item("username"))  # Output: admin
```
