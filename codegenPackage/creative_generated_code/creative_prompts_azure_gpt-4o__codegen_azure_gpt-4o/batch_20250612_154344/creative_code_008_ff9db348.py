"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Develop a feature using Python that connects users with like-minded members based on shared interests, as described on the Stumble! ® website.
Generated: DETERMINISTIC_ff9db3487ef61ea3
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Set


class LikeMindedConnector:
    """
    A class to connect users with like-minded members based on shared interests.
    """

    def __init__(self):
        # Initialize an empty dictionary to hold user data.
        # Format: {username: {"name": str, "interests": set}}
        self.users_data: Dict[str, Dict[str, Set[str]]] = {}

    def add_user(self, username: str, name: str, interests: List[str]) -> None:
        """
        Add a new user to the system with their interests.

        :param username: Unique username for the user.
        :param name: Full name of the user.
        :param interests: List of interests for the user.
        :raises ValueError: If the username already exists.
        """
        if username in self.users_data:
            raise ValueError(f"Username '{username}' already exists.")
        
        self.users_data[username] = {
            "name": name,
            "interests": set(interests)
        }

    def find_like_minded_users(self, username: str) -> List[str]:
        """
        Find like-minded users for a given username based on shared interests.

        :param username: The username to find matches for.
        :return: List of usernames with shared interests.
        :raises ValueError: If the username does not exist.
        """
        if username not in self.users_data:
            raise ValueError(f"Username '{username}' not found in the system.")
        
        user_interests = self.users_data[username]["interests"]
        like_minded_users = []

        for other_username, user_data in self.users_data.items():
            if other_username == username:
                continue
            if user_interests.intersection(user_data["interests"]):
                like_minded_users.append(other_username)

        return like_minded_users

    def save_users_data(self, file_path: str) -> None:
        """
        Save user data to a JSON file for persistence.

        :param file_path: Path to the JSON file.
        """
        with open(file_path, 'w') as file:
            json.dump(self.users_data, file, indent=4)

    def load_users_data(self, file_path: str) -> None:
        """
        Load user data from a JSON file.

        :param file_path: Path to the JSON file.
        :raises FileNotFoundError: If the JSON file does not exist.
        """
        try:
            with open(file_path, 'r') as file:
                self.users_data = json.load(file)
                # Convert interests lists back to sets
                for user in self.users_data.values():
                    user["interests"] = set(user["interests"])
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File '{file_path}' not found.") from e


# Example Usage:
if __name__ == "__main__":
    connector = LikeMindedConnector()

    # Add users
    connector.add_user("john_doe", "John Doe", ["music", "travel", "coding"])
    connector.add_user("jane_smith", "Jane Smith", ["travel", "photography", "coding"])
    connector.add_user("alice_jones", "Alice Jones", ["cooking", "fitness", "reading"])

    # Find like-minded users
    try:
        matches = connector.find_like_minded_users("john_doe")
        print(f"Users like-minded with 'john_doe': {matches}")
    except ValueError as e:
        print(e)

    # Save users to file
    connector.save_users_data("users_data.json")

    # Load users from file
    try:
        connector.load_users_data("users_data.json")
        print("User data loaded successfully.")
    except FileNotFoundError as e:
        print(e)
```
