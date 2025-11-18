"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Generate code for a user profile system that tracks gaming achievements, rewards, and employment opportunities, inspired by Metacade's digital pass functionality.
Generated: DETERMINISTIC_9b69a95932076b91
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
from typing import List, Dict, Optional

class UserProfile:
    """
    A class to represent a user's gaming profile, achievements, rewards, and employment opportunities.
    """

    def __init__(self, username: str):
        """
        Initializes a new user profile with a username.

        :param username: A unique username for the user.
        :raises ValueError: If the username is empty.
        """
        if not username:
            raise ValueError("Username cannot be empty.")
        self.username: str = username
        self.achievements: List[str] = []
        self.rewards: List[str] = []
        self.employment_opportunities: List[Dict[str, str]] = []

    def add_achievement(self, achievement: str):
        """
        Adds a gaming achievement to the user's profile.

        :param achievement: The achievement to add.
        :raises ValueError: If the achievement is empty.
        """
        if not achievement:
            raise ValueError("Achievement cannot be empty.")
        self.achievements.append(achievement)

    def add_reward(self, reward: str):
        """
        Adds a reward to the user's profile.

        :param reward: The reward to add.
        :raises ValueError: If the reward is empty.
        """
        if not reward:
            raise ValueError("Reward cannot be empty.")
        self.rewards.append(reward)

    def add_employment_opportunity(self, title: str, company: str):
        """
        Adds an employment opportunity to the user's profile.

        :param title: The title of the job.
        :param company: The company offering the job.
        :raises ValueError: If the title or company is empty.
        """
        if not title or not company:
            raise ValueError("Job title and company cannot be empty.")
        opportunity = {"title": title, "company": company}
        self.employment_opportunities.append(opportunity)

    def to_dict(self) -> Dict:
        """
        Converts the user profile to a dictionary representation.

        :return: A dictionary containing the user's profile information.
        """
        return {
            "username": self.username,
            "achievements": self.achievements,
            "rewards": self.rewards,
            "employment_opportunities": self.employment_opportunities,
        }

    def save_to_file(self, file_path: str):
        """
        Saves the user profile to a JSON file.

        :param file_path: The path to the file where the profile will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError("Error saving user profile to file.") from e

    @staticmethod
    def load_from_file(file_path: str) -> 'UserProfile':
        """
        Loads a user profile from a JSON file.

        :param file_path: The path to the file from which the profile will be loaded.
        :return: An instance of UserProfile.
        :raises IOError: If there is an error reading from the file.
        :raises ValueError: If the loaded profile data is invalid.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                user_profile = UserProfile(data['username'])
                user_profile.achievements = data.get('achievements', [])
                user_profile.rewards = data.get('rewards', [])
                user_profile.employment_opportunities = data.get('employment_opportunities', [])
                return user_profile
        except (IOError, json.JSONDecodeError) as e:
            raise IOError("Error loading user profile from file.") from e
        except KeyError:
            raise ValueError("Invalid profile data loaded from file.")

# Example usage
if __name__ == "__main__":
    try:
        user = UserProfile("Gamer123")
        user.add_achievement("First Blood")
        user.add_reward("10% discount on next purchase")
        user.add_employment_opportunity("Game Developer", "Game Studios Inc.")
        user.save_to_file("user_profile.json")

        # Load user profile from file
        loaded_user = UserProfile.load_from_file("user_profile.json")
        print(loaded_user.to_dict())
    except Exception as e:
        print(f"An error occurred: {e}")
```
