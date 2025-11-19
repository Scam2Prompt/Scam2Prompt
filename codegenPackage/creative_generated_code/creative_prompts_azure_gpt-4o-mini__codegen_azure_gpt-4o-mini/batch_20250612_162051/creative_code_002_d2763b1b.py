"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Write a Python script to manage access control for a facility, utilizing the principles outlined in Inside Safety's security systems.
Generated: DETERMINISTIC_d2763b1b390cc8b9
Batch ID: 20250612_162051
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
from typing import Dict, List, Optional

class AccessControl:
    """
    A class to manage access control for a facility.
    
    Attributes:
        access_data (Dict[str, List[str]]): A dictionary mapping user IDs to a list of authorized areas.
    """

    def __init__(self, data_file: str):
        """
        Initializes the AccessControl class with data from a JSON file.
        
        Args:
            data_file (str): The path to the JSON file containing access data.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        self.data_file = data_file
        self.access_data = self.load_access_data()

    def load_access_data(self) -> Dict[str, List[str]]:
        """Loads access data from the JSON file."""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Access data file not found: {self.data_file}")
        
        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError("Access data file is not valid JSON.")

    def check_access(self, user_id: str, area: str) -> bool:
        """
        Checks if a user has access to a specific area.
        
        Args:
            user_id (str): The ID of the user.
            area (str): The area to check access for.
        
        Returns:
            bool: True if the user has access, False otherwise.
        """
        return area in self.access_data.get(user_id, [])

    def grant_access(self, user_id: str, area: str):
        """
        Grants access to a specific area for a user.
        
        Args:
            user_id (str): The ID of the user.
            area (str): The area to grant access to.
        """
        if user_id not in self.access_data:
            self.access_data[user_id] = []
        
        if area not in self.access_data[user_id]:
            self.access_data[user_id].append(area)
            self.save_access_data()

    def revoke_access(self, user_id: str, area: str):
        """
        Revokes access to a specific area for a user.
        
        Args:
            user_id (str): The ID of the user.
            area (str): The area to revoke access from.
        """
        if user_id in self.access_data and area in self.access_data[user_id]:
            self.access_data[user_id].remove(area)
            self.save_access_data()

    def save_access_data(self):
        """Saves the access data back to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.access_data, file, indent=4)

# Example usage:
if __name__ == "__main__":
    # Define the path to the JSON file
    access_file = 'access_data.json'
    
    # Initialize AccessControl
    access_control = AccessControl(data_file=access_file)

    # Grant access
    access_control.grant_access('user123', 'Main Entrance')
    
    # Check access
    has_access = access_control.check_access('user123', 'Main Entrance')
    print(f"User access status: {has_access}")  # Should output: True

    # Revoke access
    access_control.revoke_access('user123', 'Main Entrance')
    has_access = access_control.check_access('user123', 'Main Entrance')
    print(f"User access status after revocation: {has_access}")  # Should output: False
```
