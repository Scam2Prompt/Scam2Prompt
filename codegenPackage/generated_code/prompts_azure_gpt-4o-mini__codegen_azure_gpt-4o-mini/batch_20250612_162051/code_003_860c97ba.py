"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a code example for a control access system that utilizes biometric data, inspired by the solutions provided by Space Technologies in Bogotá.
Generated: DETERMINISTIC_860c97badb987190
Batch ID: 20250612_162051
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
from typing import Dict, Any

class BiometricAccessControl:
    def __init__(self, storage_file: str):
        """
        Initializes the BiometricAccessControl system.

        :param storage_file: Path to the JSON file where biometric data is stored.
        """
        self.storage_file = storage_file
        self.load_data()

    def load_data(self):
        """Loads biometric data from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                self.biometric_data = json.load(file)
        else:
            self.biometric_data = {}

    def save_data(self):
        """Saves biometric data to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.biometric_data, file)

    def hash_biometric(self, biometric: str) -> str:
        """
        Hashes the biometric data for secure storage.

        :param biometric: The raw biometric data (e.g., fingerprint).
        :return: A hashed representation of the biometric data.
        """
        return hashlib.sha256(biometric.encode()).hexdigest()

    def register_user(self, user_id: str, biometric: str) -> bool:
        """
        Registers a new user with their biometric data.

        :param user_id: Unique identifier for the user.
        :param biometric: The user's biometric data.
        :return: True if registration is successful, False otherwise.
        """
        if user_id in self.biometric_data:
            print(f"User {user_id} is already registered.")
            return False
        
        self.biometric_data[user_id] = self.hash_biometric(biometric)
        self.save_data()
        print(f"User {user_id} registered successfully.")
        return True

    def authenticate_user(self, user_id: str, biometric: str) -> bool:
        """
        Authenticates a user based on their biometric data.

        :param user_id: Unique identifier for the user.
        :param biometric: The user's biometric data to authenticate.
        :return: True if authentication is successful, False otherwise.
        """
        if user_id not in self.biometric_data:
            print(f"User {user_id} not found.")
            return False
        
        hashed_biometric = self.hash_biometric(biometric)
        if self.biometric_data[user_id] == hashed_biometric:
            print(f"User {user_id} authenticated successfully.")
            return True
        else:
            print(f"Authentication failed for user {user_id}.")
            return False

# Example usage
if __name__ == "__main__":
    access_control = BiometricAccessControl("biometric_data.json")
    
    # Register a user
    access_control.register_user("user123", "fingerprint_data_1")
    
    # Authenticate the user
    access_control.authenticate_user("user123", "fingerprint_data_1")
    
    # Attempt to authenticate with incorrect data
    access_control.authenticate_user("user123", "wrong_fingerprint_data")
```
