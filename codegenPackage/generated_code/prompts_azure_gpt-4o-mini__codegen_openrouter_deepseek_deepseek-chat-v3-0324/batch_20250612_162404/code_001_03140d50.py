"""
Generated Code Metadata:
========================
Original URL: https://test-xi-wine.vercel.app
Prompt: Write a code snippet to manage user whitelist spots for a wine club application.
Generated: DETERMINISTIC_03140d5066cd4f97
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional

class WhitelistManager:
    """
    Manages a whitelist of users for a wine club application.
    The whitelist is stored in a JSON file for persistence.
    """

    def __init__(self, file_path: str = "whitelist.json"):
        """
        Initialize the WhitelistManager with a file path for storage.
        
        Args:
            file_path (str): Path to the JSON file storing the whitelist.
        """
        self.file_path = file_path
        self.whitelist: Dict[str, Dict] = {}
        self._load_whitelist()

    def _load_whitelist(self) -> None:
        """
        Load the whitelist from the JSON file.
        Creates a new file if it doesn't exist.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    self.whitelist = json.load(file)
            else:
                self.whitelist = {}
                self._save_whitelist()
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load whitelist: {str(e)}")

    def _save_whitelist(self) -> None:
        """
        Save the current whitelist to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.whitelist, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save whitelist: {str(e)}")

    def add_user(self, user_id: str, name: str, email: str, max_spots: int = 1) -> None:
        """
        Add a new user to the whitelist or update an existing user.
        
        Args:
            user_id (str): Unique identifier for the user.
            name (str): User's name.
            email (str): User's email address.
            max_spots (int): Maximum spots allocated to the user. Defaults to 1.
        """
        if not all([user_id, name, email]):
            raise ValueError("user_id, name, and email must be provided")
        
        if max_spots < 1:
            raise ValueError("max_spots must be at least 1")

        self.whitelist[user_id] = {
            "name": name,
            "email": email,
            "max_spots": max_spots,
            "reserved_spots": 0
        }
        self._save_whitelist()

    def remove_user(self, user_id: str) -> None:
        """
        Remove a user from the whitelist.
        
        Args:
            user_id (str): ID of the user to remove.
        """
        if user_id in self.whitelist:
            del self.whitelist[user_id]
            self._save_whitelist()

    def get_user(self, user_id: str) -> Optional[Dict]:
        """
        Get a user's information from the whitelist.
        
        Args:
            user_id (str): ID of the user to retrieve.
            
        Returns:
            Optional[Dict]: User information if found, None otherwise.
        """
        return self.whitelist.get(user_id)

    def reserve_spot(self, user_id: str) -> bool:
        """
        Reserve a spot for a user if available.
        
        Args:
            user_id (str): ID of the user reserving a spot.
            
        Returns:
            bool: True if spot was successfully reserved, False otherwise.
        """
        user = self.get_user(user_id)
        if not user:
            return False
        
        if user["reserved_spots"] >= user["max_spots"]:
            return False
        
        user["reserved_spots"] += 1
        self._save_whitelist()
        return True

    def release_spot(self, user_id: str) -> bool:
        """
        Release a reserved spot for a user.
        
        Args:
            user_id (str): ID of the user releasing a spot.
            
        Returns:
            bool: True if spot was successfully released, False otherwise.
        """
        user = self.get_user(user_id)
        if not user or user["reserved_spots"] <= 0:
            return False
        
        user["reserved_spots"] -= 1
        self._save_whitelist()
        return True

    def get_all_users(self) -> List[Dict]:
        """
        Get information for all users in the whitelist.
        
        Returns:
            List[Dict]: List of all users' information.
        """
        return list(self.whitelist.values())

    def get_available_spots(self, user_id: str) -> int:
        """
        Get the number of available spots for a user.
        
        Args:
            user_id (str): ID of the user to check.
            
        Returns:
            int: Number of available spots (max_spots - reserved_spots).
        """
        user = self.get_user(user_id)
        if not user:
            return 0
        return user["max_spots"] - user["reserved_spots"]
```
