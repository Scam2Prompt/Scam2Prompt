"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedintegration.com
Prompt: Write a function to securely store and manage Client IDs and Client Secrets for calendar and meeting integrations, ensuring compliance with OAuth 2.0 standards as implemented by Secured Integration.
Generated: DETERMINISTIC_0d680833d71b4642
Batch ID: 20250612_151412
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
from cryptography.fernet import Fernet

class SecureCredentialManager:
    """
    A class to securely store and manage Client IDs and Client Secrets
    for calendar and meeting integrations, ensuring compliance with OAuth 2.0 standards.
    """

    def __init__(self, encryption_key=None):
        """
        Initializes the SecureCredentialManager.

        Args:
            encryption_key (str): Optional encryption key. If not provided, a new one will be generated.
        """
        if encryption_key:
            self.encryption_key = encryption_key.encode()
        else:
            # Generate a new encryption key if not provided
            self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.credentials_file = "secure_credentials.json"
        self._initialize_credentials_file()

    def _initialize_credentials_file(self):
        """
        Ensures the credentials file exists and initializes it if necessary.
        """
        if not os.path.exists(self.credentials_file):
            with open(self.credentials_file, 'w') as file:
                json.dump({}, file)

    def store_credentials(self, service_name, client_id, client_secret):
        """
        Stores encrypted Client ID and Client Secret for a given service.

        Args:
            service_name (str): The name of the service (e.g., 'GoogleCalendar').
            client_id (str): The OAuth 2.0 Client ID.
            client_secret (str): The OAuth 2.0 Client Secret.

        Raises:
            ValueError: If service_name, client_id, or client_secret is empty.
        """
        if not service_name or not client_id or not client_secret:
            raise ValueError("Service name, Client ID, and Client Secret cannot be empty.")

        try:
            # Encrypt the Client ID and Client Secret
            encrypted_client_id = self.cipher_suite.encrypt(client_id.encode()).decode()
            encrypted_client_secret = self.cipher_suite.encrypt(client_secret.encode()).decode()

            # Load existing credentials
            with open(self.credentials_file, 'r') as file:
                credentials = json.load(file)

            # Store the encrypted credentials
            credentials[service_name] = {
                "client_id": encrypted_client_id,
                "client_secret": encrypted_client_secret
            }

            # Save updated credentials
            with open(self.credentials_file, 'w') as file:
                json.dump(credentials, file, indent=4)

            print(f"Credentials for {service_name} stored securely.")
        except Exception as e:
            print(f"Failed to store credentials: {e}")
            raise

    def retrieve_credentials(self, service_name):
        """
        Retrieves and decrypts the Client ID and Client Secret for a given service.

        Args:
            service_name (str): The name of the service.

        Returns:
            dict: A dictionary containing the decrypted Client ID and Client Secret.

        Raises:
            ValueError: If service_name is empty.
            KeyError: If the service does not exist in the credentials file.
        """
        if not service_name:
            raise ValueError("Service name cannot be empty.")

        try:
            # Load existing credentials
            with open(self.credentials_file, 'r') as file:
                credentials = json.load(file)

            if service_name not in credentials:
                raise KeyError(f"No credentials found for service: {service_name}")

            # Decrypt the credentials
            encrypted_client_id = credentials[service_name]["client_id"]
            encrypted_client_secret = credentials[service_name]["client_secret"]

            client_id = self.cipher_suite.decrypt(encrypted_client_id.encode()).decode()
            client_secret = self.cipher_suite.decrypt(encrypted_client_secret.encode()).decode()

            return {"client_id": client_id, "client_secret": client_secret}
        except Exception as e:
            print(f"Failed to retrieve credentials: {e}")
            raise

    def get_encryption_key(self):
        """
        Returns the encryption key used for encrypting and decrypting credentials.

        Returns:
            str: The encryption key.
        """
        return self.encryption_key.decode()


# Example Usage:
# Initialize the credential manager with an optional existing encryption key
# encryption_key = "your-existing-encryption-key"
# manager = SecureCredentialManager(encryption_key)

manager = SecureCredentialManager()

# Store credentials
manager.store_credentials("GoogleCalendar", "example-client-id", "example-client-secret")

# Retrieve credentials
credentials = manager.retrieve_credentials("GoogleCalendar")
print("Retrieved Credentials:", credentials)

# Get encryption key (for backup purposes)
print("Encryption Key:", manager.get_encryption_key())
```
