"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to implement basic password management recommendations for a small business, including password encryption and secure storage.
Generated: DETERMINISTIC_cc60fceee3a789df
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import getpass
import hashlib
import os
import secrets
import string
import pickle

class PasswordManager:
    def __init__(self, storage_file='passwords.dat'):
        """
        Initialize the password manager.

        :param storage_file: File to store encrypted passwords
        """
        self.storage_file = storage_file

    def _hash_password(self, password):
        """
        Hash a password for secure storage.

        :param password: Password to hash
        :return: Hashed password
        """
        # Use SHA-256 for hashing
        return hashlib.sha256(password.encode()).hexdigest()

    def _generate_password(self, length=12):
        """
        Generate a random password.

        :param length: Length of the password
        :return: Generated password
        """
        # Use a mix of characters, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and any(c in string.punctuation for c in password)):
                break
        return password

    def _encrypt_data(self, data, key):
        """
        Encrypt data using a provided key.

        :param data: Data to encrypt
        :param key: Encryption key
        :return: Encrypted data
        """
        # Simple XOR encryption
        return bytes([x ^ y for x, y in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)])])

    def _decrypt_data(self, encrypted_data, key):
        """
        Decrypt data using a provided key.

        :param encrypted_data: Data to decrypt
        :param key: Decryption key
        :return: Decrypted data
        """
        return self._encrypt_data(encrypted_data, key)

    def create_account(self, username, password):
        """
        Create a new account.

        :param username: Username for the account
        :param password: Password for the account
        """
        # Hash the password
        hashed_password = self._hash_password(password)

        try:
            # Load existing data
            with open(self.storage_file, 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            data = {}

        # Store the hashed password
        data[username] = hashed_password

        # Save the data
        with open(self.storage_file, 'wb') as f:
            pickle.dump(data, f)

    def verify_account(self, username, password):
        """
        Verify an account.

        :param username: Username for the account
        :param password: Password for the account
        :return: True if verified, False otherwise
        """
        try:
            # Load existing data
            with open(self.storage_file, 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            return False

        # Check if the username exists
        if username not in data:
            return False

        # Hash the provided password and compare
        hashed_password = self._hash_password(password)
        return data[username] == hashed_password

    def generate_and_store_password(self, username, length=12):
        """
        Generate and store a random password for an account.

        :param username: Username for the account
        :param length: Length of the password
        """
        # Generate a random password
        password = self._generate_password(length)

        # Create or update the account
        self.create_account(username, password)

        return password

def main():
    manager = PasswordManager()

    while True:
        print("1. Create Account")
        print("2. Verify Account")
        print("3. Generate and Store Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = getpass.getpass("Enter a password: ")
            manager.create_account(username, password)
            print("Account created.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            if manager.verify_account(username, password):
                print("Verified.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            username = input("Enter a username: ")
            length = int(input("Enter password length (default=12): ") or 12)
            password = manager.generate_and_store_password(username, length)
            print(f"Generated password: {password}")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
