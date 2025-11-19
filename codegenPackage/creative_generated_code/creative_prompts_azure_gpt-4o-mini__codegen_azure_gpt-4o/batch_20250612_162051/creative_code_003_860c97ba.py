"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a code example for a control access system that utilizes biometric data, inspired by the solutions provided by Space Technologies in Bogotá.
Generated: DETERMINISTIC_860c97badb987190
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib  # For hashing biometric data
import json  # For simulating a database
import os  # For file handling
from typing import Optional

class BiometricAccessControl:
    """
    A control access system utilizing biometric data for authentication.
    This code example is inspired by solutions provided by Space Technologies in Bogotá.
    """

    def __init__(self, database_file: str = "biometric_data.json"):
        """
        Initializes the access control system.

        :param database_file: Path to the JSON file acting as the database for storing user data.
        """
        self.database_file = database_file
        self._initialize_database()

    def _initialize_database(self):
        """
        Ensures the database file exists. Creates a new file if it does not exist.
        """
        if not os.path.exists(self.database_file):
            with open(self.database_file, 'w') as db_file:
                json.dump({}, db_file)  # Initialize an empty dictionary in the file

    def _load_database(self) -> dict:
        """
        Loads the database content from the file.

        :return: The content of the database as a dictionary.
        """
        try:
            with open(self.database_file, 'r') as db_file:
                return json.load(db_file)
        except json.JSONDecodeError:
            # Handle case where JSON file is corrupted
            return {}

    def _save_database(self, data: dict):
        """
        Saves the given data into the database file.

        :param data: Dictionary to be saved into the database.
        """
        with open(self.database_file, 'w') as db_file:
            json.dump(data, db_file)

    def register_user(self, user_id: str, biometric_data: str) -> bool:
        """
        Registers a new user with their biometric data.

        :param user_id: Unique identifier for the user.
        :param biometric_data: Raw biometric data (e.g., fingerprint string or encoded image).
        :return: True if registration is successful, False if the user already exists.
        """
        database = self._load_database()

        if user_id in database:
            # User already exists
            return False

        # Hash the biometric data for storage
        biometric_hash = hashlib.sha256(biometric_data.encode()).hexdigest()
        database[user_id] = biometric_hash
        self._save_database(database)
        return True

    def authenticate_user(self, user_id: str, biometric_data: str) -> bool:
        """
        Authenticates a user based on their biometric data.

        :param user_id: Unique identifier for the user.
        :param biometric_data: Raw biometric data provided for authentication.
        :return: True if authentication is successful, False otherwise.
        """
        database = self._load_database()

        if user_id not in database:
            # User not found
            return False

        # Hash the input biometric data for comparison
        biometric_hash = hashlib.sha256(biometric_data.encode()).hexdigest()

        # Compare the provided hash with the stored hash
        return database[user_id] == biometric_hash

    def remove_user(self, user_id: str) -> bool:
        """
        Removes a user from the database.

        :param user_id: Unique identifier for the user to be removed.
        :return: True if removal is successful, False if the user does not exist.
        """
        database = self._load_database()

        if user_id not in database:
            # User not found
            return False

        # Remove user from database
        del database[user_id]
        self._save_database(database)
        return True


# Example usage
if __name__ == "__main__":
    system = BiometricAccessControl()

    # Register users
    print(system.register_user("user123", "fingerprint_data_123"))  # True
    print(system.register_user("user123", "fingerprint_data_123"))  # False (already exists)

    # Authenticate users
    print(system.authenticate_user("user123", "fingerprint_data_123"))  # True
    print(system.authenticate_user("user123", "wrong_data"))           # False

    # Remove users
    print(system.remove_user("user123"))  # True
    print(system.remove_user("user123"))  # False (already removed)
```
