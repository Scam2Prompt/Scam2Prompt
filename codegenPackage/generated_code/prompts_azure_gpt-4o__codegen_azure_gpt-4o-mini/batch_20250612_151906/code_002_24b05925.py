"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: Generate code for creating a digital pass system that tracks user profiles, rewards, and career opportunities, inspired by Metacade's platform functionality.
Generated: DETERMINISTIC_24b059259edaf866
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_pass_system.py

class UserProfile:
    """
    Class to represent a user profile in the digital pass system.
    """

    def __init__(self, user_id, name, email):
        """
        Initialize a new user profile.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param email: Email address of the user
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.rewards = 0
        self.career_opportunities = []

    def add_rewards(self, points):
        """
        Add rewards points to the user's profile.

        :param points: Number of points to add
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.rewards += points

    def add_career_opportunity(self, opportunity):
        """
        Add a career opportunity to the user's profile.

        :param opportunity: Career opportunity to add
        """
        self.career_opportunities.append(opportunity)

    def __str__(self):
        return f"UserProfile(user_id={self.user_id}, name={self.name}, email={self.email}, rewards={self.rewards}, career_opportunities={self.career_opportunities})"


class DigitalPassSystem:
    """
    Class to manage the digital pass system, including user profiles.
    """

    def __init__(self):
        """
        Initialize the digital pass system with an empty user database.
        """
        self.users = {}

    def create_user(self, user_id, name, email):
        """
        Create a new user profile.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param email: Email address of the user
        :raises ValueError: If the user ID already exists
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = UserProfile(user_id, name, email)

    def get_user(self, user_id):
        """
        Retrieve a user profile by user ID.

        :param user_id: Unique identifier for the user
        :return: UserProfile object
        :raises KeyError: If the user ID does not exist
        """
        if user_id not in self.users:
            raise KeyError("User ID not found.")
        return self.users[user_id]

    def add_rewards_to_user(self, user_id, points):
        """
        Add rewards points to a user's profile.

        :param user_id: Unique identifier for the user
        :param points: Number of points to add
        :raises KeyError: If the user ID does not exist
        """
        user = self.get_user(user_id)
        user.add_rewards(points)

    def add_career_opportunity_to_user(self, user_id, opportunity):
        """
        Add a career opportunity to a user's profile.

        :param user_id: Unique identifier for the user
        :param opportunity: Career opportunity to add
        :raises KeyError: If the user ID does not exist
        """
        user = self.get_user(user_id)
        user.add_career_opportunity(opportunity)

    def __str__(self):
        return f"DigitalPassSystem(users={self.users})"


# Example usage
if __name__ == "__main__":
    try:
        dps = DigitalPassSystem()
        dps.create_user("001", "Alice Smith", "alice@example.com")
        dps.add_rewards_to_user("001", 100)
        dps.add_career_opportunity_to_user("001", "Software Engineer at TechCorp")

        user_profile = dps.get_user("001")
        print(user_profile)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
