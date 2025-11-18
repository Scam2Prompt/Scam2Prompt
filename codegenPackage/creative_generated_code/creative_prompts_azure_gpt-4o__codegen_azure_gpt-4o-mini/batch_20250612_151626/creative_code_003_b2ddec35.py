"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue.fin.live
Prompt: Create a script to comply with 152-ФЗ РФ (Russian personal data legislation) when handling user data for a financial platform like ФинПлатформа.
Generated: DETERMINISTIC_b2ddec358ad576da
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime
from typing import Optional


class UserDataHandler:
    """
    Class to manage user data in compliance with 152-ФЗ РФ legislation.
    This class provides functionality for storing, retrieving,
    and deleting user personal data securely.
    """

    def __init__(self, storage_path: str):
        """
        Initialize the UserDataHandler with the specified storage path.
        
        :param storage_path: Directory where user data files will be stored.
        """
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def _get_file_path(self, user_id: str) -> str:
        """
        Get the file path for a user's data based on their user ID.
        
        :param user_id: Unique identifier for the user.
        :return: Full path to the user's data file.
        """
        return os.path.join(self.storage_path, f"{user_id}.json")

    def save_user_data(self, user_id: str, user_data: dict) -> None:
        """
        Save user personal data to a file in JSON format.
        
        :param user_id: Unique identifier for the user.
        :param user_data: Dictionary containing user personal data.
        :raises ValueError: If user_id or user_data are invalid.
        """
        if not user_id or not isinstance(user_data, dict):
            raise ValueError("Invalid user ID or user data.")

        file_path = self._get_file_path(user_id)
        user_data['created_at'] = datetime.now().isoformat()  # Record the creation timestamp

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(user_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write user data to file: {e}")

    def load_user_data(self, user_id: str) -> Optional[dict]:
        """
        Load user personal data from a file.
        
        :param user_id: Unique identifier for the user.
        :return: Dictionary containing user personal data, or None if not found.
        :raises ValueError: If user_id is invalid.
        """
        if not user_id:
            raise ValueError("Invalid user ID.")

        file_path = self._get_file_path(user_id)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"No data found for user ID: {user_id}")
            return None
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to decode user data: {e}")

    def delete_user_data(self, user_id: str) -> None:
        """
        Delete the user personal data file.
        
        :param user_id: Unique identifier for the user.
        :raises ValueError: If user_id is invalid.
        """
        if not user_id:
            raise ValueError("Invalid user ID.")

        file_path = self._get_file_path(user_id)

        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print(f"No data found to delete for user ID: {user_id}")
        except OSError as e:
            raise RuntimeError(f"Failed to delete user data file: {e}")


# Example of usage
if __name__ == "__main__":
    user_data_handler = UserDataHandler(storage_path='user_data')

    # Example user data
    user_id = "123456"
    user_data = {
        "name": "Ivan Ivanov",
        "email": "ivan@example.com",
        "phone": "+7 123 456 78 90",
    }

    try:
        # Save user data
        user_data_handler.save_user_data(user_id, user_data)

        # Load user data
        loaded_data = user_data_handler.load_user_data(user_id)
        print("Loaded user data:", loaded_data)

        # Delete user data
        user_data_handler.delete_user_data(user_id)

    except Exception as e:
        print(f"An error occurred: {e}")
```
