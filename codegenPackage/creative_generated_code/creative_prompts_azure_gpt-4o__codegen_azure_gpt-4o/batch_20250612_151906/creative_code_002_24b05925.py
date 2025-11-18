"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Generate code for creating a digital pass system that tracks user profiles, rewards, and career opportunities, inspired by Metacade's platform functionality.
Generated: DETERMINISTIC_24b059259edaf866
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Exception classes for error handling
class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

# Class to represent a user profile
class UserProfile:
    def __init__(self, user_id, name, email):
        """
        Initializes a user profile.
        :param user_id: Unique ID for the user
        :param name: Name of the user
        :param email: Email of the user
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.rewards = 0  # Number of rewards earned
        self.career_opportunities = []  # List of career opportunities

    def to_dict(self):
        """
        Converts user profile to dictionary for serialization.
        :return: Dictionary representation of the user profile
        """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "rewards": self.rewards,
            "career_opportunities": self.career_opportunities,
        }

# Class to manage the digital pass system
class DigitalPassSystem:
    def __init__(self):
        """
        Initializes the digital pass system with an empty user database.
        """
        self.users = {}  # Dictionary to store user profiles keyed by user_id
    
    def add_user(self, user_id, name, email):
        """
        Adds a new user to the system.
        :param user_id: Unique ID for the user
        :param name: Name of the user
        :param email: Email of the user
        :raises UserAlreadyExistsError: If user_id already exists
        """
        if user_id in self.users:
            raise UserAlreadyExistsError(f"User with ID {user_id} already exists.")
        self.users[user_id] = UserProfile(user_id, name, email)

    def get_user(self, user_id):
        """
        Retrieves a user profile by user_id.
        :param user_id: Unique ID for the user
        :return: UserProfile object
        :raises UserNotFoundError: If user_id does not exist
        """
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        return self.users[user_id]
    
    def reward_user(self, user_id, reward_points):
        """
        Rewards a user with points.
        :param user_id: Unique ID for the user
        :param reward_points: Number of reward points to add
        :raises UserNotFoundError: If user_id does not exist
        """
        user = self.get_user(user_id)
        user.rewards += reward_points

    def add_career_opportunity(self, user_id, opportunity):
        """
        Adds a career opportunity to a user's profile.
        :param user_id: Unique ID for the user
        :param opportunity: Description of the career opportunity
        :raises UserNotFoundError: If user_id does not exist
        """
        user = self.get_user(user_id)
        user.career_opportunities.append({
            "description": opportunity,
            "date_added": datetime.now().isoformat(),
        })

    def serialize_users(self, file_path):
        """
        Serializes all user profiles to a JSON file.
        :param file_path: Path to the JSON file
        """
        with open(file_path, 'w') as file:
            json.dump({user_id: user.to_dict() for user_id, user in self.users.items()}, file, indent=4)

    def load_users(self, file_path):
        """
        Loads user profiles from a JSON file.
        :param file_path: Path to the JSON file
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            for user_id, user_data in data.items():
                profile = UserProfile(
                    user_id=user_id, 
                    name=user_data["name"], 
                    email=user_data["email"]
                )
                profile.rewards = user_data["rewards"]
                profile.career_opportunities = user_data["career_opportunities"]
                self.users[user_id] = profile

# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = DigitalPassSystem()
    try:
        # Add users
        system.add_user("user001", "Alice", "alice@example.com")
        system.add_user("user002", "Bob", "bob@example.com")

        # Reward users
        system.reward_user("user001", 10)
        system.reward_user("user002", 20)

        # Add career opportunities
        system.add_career_opportunity("user001", "Software Engineer Position")
        system.add_career_opportunity("user002", "Data Analyst Job Opening")

        # Serialize to file
        system.serialize_users("users.json")

        # Load users from file
        new_system = DigitalPassSystem()
        new_system.load_users("users.json")
        print("Loaded users:", new_system.users)

    except Exception as e:
        print(f"Error: {e}")
```
