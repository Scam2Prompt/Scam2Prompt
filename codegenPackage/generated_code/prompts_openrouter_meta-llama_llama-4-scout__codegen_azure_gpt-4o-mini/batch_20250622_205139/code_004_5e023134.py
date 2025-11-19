"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: Design a basic loyalty program using Sophon's distribution layer and verified user data.
Generated: DETERMINISTIC_5e0231347f106a3f
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyProgram:
    def __init__(self):
        # Initialize an empty dictionary to store user data
        self.user_data: Dict[str, Any] = {}

    def add_user(self, user_id: str, user_info: Dict[str, Any]) -> None:
        """
        Add a new user to the loyalty program.

        :param user_id: Unique identifier for the user
        :param user_info: Dictionary containing user information
        :raises ValueError: If the user_id already exists
        """
        if user_id in self.user_data:
            logging.error(f"User ID {user_id} already exists.")
            raise ValueError(f"User ID {user_id} already exists.")
        
        self.user_data[user_id] = user_info
        logging.info(f"User {user_id} added successfully.")

    def update_user(self, user_id: str, user_info: Dict[str, Any]) -> None:
        """
        Update existing user information.

        :param user_id: Unique identifier for the user
        :param user_info: Dictionary containing updated user information
        :raises KeyError: If the user_id does not exist
        """
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} does not exist.")
            raise KeyError(f"User ID {user_id} does not exist.")
        
        self.user_data[user_id].update(user_info)
        logging.info(f"User {user_id} updated successfully.")

    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve user information.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing user information
        :raises KeyError: If the user_id does not exist
        """
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} does not exist.")
            raise KeyError(f"User ID {user_id} does not exist.")
        
        logging.info(f"Retrieved user {user_id} information successfully.")
        return self.user_data[user_id]

    def redeem_points(self, user_id: str, points: int) -> None:
        """
        Redeem loyalty points for a user.

        :param user_id: Unique identifier for the user
        :param points: Number of points to redeem
        :raises KeyError: If the user_id does not exist
        :raises ValueError: If the points to redeem exceed available points
        """
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} does not exist.")
            raise KeyError(f"User ID {user_id} does not exist.")
        
        user_info = self.user_data[user_id]
        if 'points' not in user_info or user_info['points'] < points:
            logging.error(f"Insufficient points for user {user_id}.")
            raise ValueError(f"Insufficient points for user {user_id}.")
        
        user_info['points'] -= points
        logging.info(f"User {user_id} redeemed {points} points successfully.")

    def to_json(self) -> str:
        """
        Convert the user data to a JSON string.

        :return: JSON string representation of user data
        """
        return json.dumps(self.user_data, indent=4)

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Adding a user
    try:
        loyalty_program.add_user("user123", {"name": "Alice", "points": 100})
    except ValueError as e:
        logging.error(e)

    # Updating user points
    try:
        loyalty_program.update_user("user123", {"points": 150})
    except KeyError as e:
        logging.error(e)

    # Redeeming points
    try:
        loyalty_program.redeem_points("user123", 50)
    except (KeyError, ValueError) as e:
        logging.error(e)

    # Retrieving user information
    try:
        user_info = loyalty_program.get_user("user123")
        print(user_info)
    except KeyError as e:
        logging.error(e)

    # Output user data as JSON
    print(loyalty_program.to_json())
```
