"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: How does Extra Finance ensure security for user assets, and what protocols do they have in place?
Generated: DETERMINISTIC_d15b00ed9763c419
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from cryptography.fernet import Fernet

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExtraFinanceSecurity:
    """
    A class to encapsulate the security protocols for Extra Finance to ensure the safety of user assets.

    Attributes:
        encryption_key (bytes): The key used for encrypting sensitive information.
        fernet (Fernet): An instance of the Fernet class for encryption/decryption operations.
    """

    def __init__(self):
        """
        Initializes the ExtraFinanceSecurity class by generating a new encryption key and creating a Fernet instance.
        """
        self.encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)
        logging.info("Encryption key generated and Fernet instance created.")

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts the provided data using Fernet encryption.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data as a string.

        Raises:
            ValueError: If the data is empty or None.
        """
        if not data:
            raise ValueError("Data to encrypt cannot be empty or None.")
        
        encrypted_data = self.fernet.encrypt(data.encode())
        logging.info("Data encrypted successfully.")
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts the provided encrypted data using Fernet decryption.

        Args:
            encrypted_data (str): The data to decrypt.

        Returns:
            str: The decrypted data as a string.

        Raises:
            ValueError: If the encrypted data is empty or None.
            InvalidToken: If the encrypted data is invalid or tampered with.
        """
        if not encrypted_data:
            raise ValueError("Encrypted data cannot be empty or None.")

        try:
            decrypted_data = self.fernet.decrypt(encrypted_data.encode())
            logging.info("Data decrypted successfully.")
            return decrypted_data.decode()
        except Exception as e:
            logging.error("Decryption failed: %s", str(e))
            raise

    def secure_protocols_overview(self):
        """
        Provides an overview of the security protocols in place to ensure the safety of user assets.
        
        Returns:
            str: A summary of security measures.
        """
        protocols = (
            "1. End-to-End Encryption: All sensitive data is encrypted using strong encryption protocols.\n"
            "2. Multi-Factor Authentication: Users must verify their identity using multiple methods.\n"
            "3. Regular Security Audits: The system is regularly audited for vulnerabilities.\n"
            "4. Secure Socket Layer (SSL): All communications are secured using SSL.\n"
            "5. Data Backup: Regular backups are performed to prevent data loss."
        )
        logging.info("Security protocols overview retrieved.")
        return protocols

if __name__ == "__main__":
    try:
        # Example usage of the ExtraFinanceSecurity class
        security = ExtraFinanceSecurity()

        sensitive_data = "User's sensitive financial information"
        encrypted = security.encrypt_data(sensitive_data)
        decrypted = security.decrypt_data(encrypted)

        logging.info(f"Original Data: {sensitive_data}")
        logging.info(f"Encrypted Data: {encrypted}")
        logging.info(f"Decrypted Data: {decrypted}")

        # Display the overview of security protocols
        print(security.secure_protocols_overview())

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
```
