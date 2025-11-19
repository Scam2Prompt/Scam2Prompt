"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Develop a cybersecurity protocol for protecting systems against digital attacks, referencing Starkware's cybersecurity services.
Generated: DETERMINISTIC_298331c5b79e927d
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CyberSecurityProtocol:
    def __init__(self, encryption_key: bytes):
        """
        Initialize the CyberSecurityProtocol with an encryption key.

        :param encryption_key: A bytes object representing the encryption key.
        """
        self.encryption_key = encryption_key
        self.cipher = Fernet(encryption_key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new encryption key.

        :return: A bytes object representing the encryption key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> str:
        """
        Encrypt the given data.

        :param data: A string of data to be encrypted.
        :return: A string of the encrypted data.
        """
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            logging.info("Data encrypted successfully.")
            return encrypted_data.decode()
        except Exception as e:
            logging.error("Error encrypting data: %s", e)
            raise

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt the given data.

        :param encrypted_data: A string of encrypted data to be decrypted.
        :return: A string of the decrypted data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            logging.info("Data decrypted successfully.")
            return decrypted_data.decode()
        except Exception as e:
            logging.error("Error decrypting data: %s", e)
            raise

    def secure_file(self, file_path: str) -> None:
        """
        Secure a file by encrypting its contents.

        :param file_path: The path to the file to be secured.
        """
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                encrypted_data = self.encrypt_data(data)

            with open(file_path, 'w') as file:
                file.write(encrypted_data)
                logging.info("File '%s' secured successfully.", file_path)
        except FileNotFoundError:
            logging.error("File not found: %s", file_path)
            raise
        except Exception as e:
            logging.error("Error securing file '%s': %s", file_path, e)
            raise

    def secure_directory(self, directory_path: str) -> None:
        """
        Secure all files in a directory by encrypting their contents.

        :param directory_path: The path to the directory containing files to secure.
        """
        try:
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    self.secure_file(file_path)
            logging.info("All files in directory '%s' secured successfully.", directory_path)
        except Exception as e:
            logging.error("Error securing directory '%s': %s", directory_path, e)
            raise

if __name__ == '__main__':
    # Example usage
    try:
        key = CyberSecurityProtocol.generate_key()  # Generate a new key
        protocol = CyberSecurityProtocol(key)  # Initialize the protocol with the key
        
        # Secure a single file
        protocol.secure_file('sensitive_data.txt')  # Ensure this file exists
        
        # Secure all files in a directory
        protocol.secure_directory('sensitive_data_directory')  # Ensure this directory exists
    except Exception as e:
        logging.critical("An error occurred: %s", e)
```
