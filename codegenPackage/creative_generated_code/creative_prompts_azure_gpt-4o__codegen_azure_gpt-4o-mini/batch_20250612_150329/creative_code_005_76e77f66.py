"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lounge.finance
Prompt: Suggest methods to securely store and manage private keys when using Lounge Finance for staking cryptocurrency.
Generated: DETERMINISTIC_76e77f6604542d5d
Batch ID: 20250612_150329
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
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

class KeyManager:
    """
    A class to handle the secure storage and management of private keys.
    """

    def __init__(self, storage_path='private_keys.json'):
        """
        Initializes the KeyManager with the specified storage path.

        :param storage_path: Path to the JSON file for storing encrypted keys.
        """
        self.storage_path = storage_path
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

        # Load existing keys if the storage path exists
        self.private_keys = self.load_keys()

    def generate_key(self):
        """
        Generates a new encryption key for encrypting and decrypting private keys.

        :return: A string representation of the generated encryption key.
        """
        return Fernet.generate_key()

    def load_keys(self):
        """
        Loads encrypted private keys from the storage file.

        :return: A dictionary of decrypted private keys.
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'rb') as file:
                encrypted_data = file.read()
            return json.loads(self.cipher.decrypt(encrypted_data).decode())
        return {}

    def save_keys(self):
        """
        Saves the encrypted private keys to the storage file.

        :raises IOError: If there's an error writing to the storage file.
        """
        try:
            with open(self.storage_path, 'wb') as file:
                encrypted_data = self.cipher.encrypt(json.dumps(self.private_keys).encode())
                file.write(encrypted_data)
        except IOError as e:
            print(f"Error saving keys: {e}")

    def add_key(self, identifier, private_key):
        """
        Adds a private key with a specific identifier to the storage.

        :param identifier: A unique identifier for the private key.
        :param private_key: The private key to be stored.
        """
        # Hash the private key for secure storage
        hashed_key = hashlib.sha256(private_key.encode()).hexdigest()
        self.private_keys[identifier] = hashed_key
        self.save_keys()

    def retrieve_key(self, identifier):
        """
        Retrieves a private key using its identifier.

        :param identifier: The unique identifier for the private key.
        :return: The hashed private key if found, otherwise None.
        """
        return self.private_keys.get(identifier, None)

    def delete_key(self, identifier):
        """
        Deletes a private key from the storage.

        :param identifier: The unique identifier for the private key to be deleted.
        """
        if identifier in self.private_keys:
            del self.private_keys[identifier]
            self.save_keys()
        else:
            print(f"Key with identifier '{identifier}' not found.")

def main():
    """
    Main function to demonstrate the KeyManager functionality.
    """
    key_manager = KeyManager()

    while True:
        print("1. Add Private Key")
        print("2. Retrieve Private Key")
        print("3. Delete Private Key")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            identifier = input("Enter a unique identifier for the key: ")
            private_key = getpass("Enter your private key: ")
            key_manager.add_key(identifier, private_key)
            print("Private key added securely.")
        elif choice == '2':
            identifier = input("Enter the identifier of the key to retrieve: ")
            retrieved_key = key_manager.retrieve_key(identifier)
            if retrieved_key:
                print(f"Retrieved key (hashed): {retrieved_key}")
            else:
                print("Key not found.")
        elif choice == '3':
            identifier = input("Enter the identifier of the key to delete: ")
            key_manager.delete_key(identifier)
            print("Key deleted if it existed.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
