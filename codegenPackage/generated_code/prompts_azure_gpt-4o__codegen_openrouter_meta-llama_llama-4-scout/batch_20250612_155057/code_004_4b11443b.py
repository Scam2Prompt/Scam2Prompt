"""
Generated Code Metadata:
========================
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of integrating a crypto wallet to secure personal data and enable querying, based on the Vana Network demo.
Generated: DETERMINISTIC_4b11443b1071b615
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass

# Vana Network Demo: Secure Personal Data with Crypto Wallet

class SecureDataWallet:
    def __init__(self, password, salt=None):
        """
        Initialize the secure data wallet.

        :param password: The password to use for encryption.
        :param salt: The salt to use for key derivation. If None, a random salt will be generated.
        """
        if salt is None:
            self.salt = os.urandom(16)
        else:
            self.salt = salt

        self.password = password
        self.key = self.derive_key(password, self.salt)
        self.cipher_suite = Fernet(self.key)

    def derive_key(self, password, salt):
        """
        Derive a key from a password and salt using PBKDF2HMAC.

        :param password: The password to use for key derivation.
        :param salt: The salt to use for key derivation.
        :return: The derived key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def encrypt_data(self, data):
        """
        Encrypt data using the cipher suite.

        :param data: The data to encrypt.
        :return: The encrypted data.
        """
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """
        Decrypt data using the cipher suite.

        :param encrypted_data: The encrypted data to decrypt.
        :return: The decrypted data.
        """
        return self.cipher_suite.decrypt(encrypted_data).decode()

    def save_wallet(self, filename):
        """
        Save the wallet to a file.

        :param filename: The filename to save the wallet to.
        """
        with open(filename, 'wb') as f:
            f.write(self.salt + self.key)

    def load_wallet(self, filename):
        """
        Load a wallet from a file.

        :param filename: The filename to load the wallet from.
        :return: The loaded wallet.
        """
        with open(filename, 'rb') as f:
            data = f.read()
            self.salt = data[:16]
            self.key = data[16:]
            return SecureDataWallet(getpass.getpass("Enter password: "), self.salt)

def main():
    password = getpass.getpass("Enter password: ")
    wallet = SecureDataWallet(password)

    while True:
        print("1. Encrypt data")
        print("2. Decrypt data")
        print("3. Save wallet")
        print("4. Load wallet")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            data = input("Enter data to encrypt: ")
            encrypted_data = wallet.encrypt_data(data)
            print("Encrypted data:", encrypted_data)
        elif choice == "2":
            encrypted_data = input("Enter encrypted data: ").encode()
            try:
                decrypted_data = wallet.decrypt_data(encrypted_data)
                print("Decrypted data:", decrypted_data)
            except Exception as e:
                print("Error decrypting data:", str(e))
        elif choice == "3":
            filename = input("Enter filename to save wallet: ")
            wallet.save_wallet(filename)
        elif choice == "4":
            filename = input("Enter filename to load wallet: ")
            loaded_wallet = wallet.load_wallet(filename)
            # Use loaded_wallet for further operations
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
