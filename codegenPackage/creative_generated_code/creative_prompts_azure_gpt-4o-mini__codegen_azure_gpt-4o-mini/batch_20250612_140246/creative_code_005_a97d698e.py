"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-stores.web.app
Prompt: Generate a sample code for a rewards program that incentivizes user engagement in a decentralized marketplace using Pushd tokens.
Generated: DETERMINISTIC_a97d698e0db3e312
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_program.py

class User:
    """
    Class representing a user in the rewards program.
    Attributes:
        user_id (str): Unique identifier for the user.
        engagement_score (int): Points based on user engagement.
        pushd_tokens (int): Current balance of Pushd tokens.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.engagement_score = 0
        self.pushd_tokens = 0

    def add_engagement(self, score):
        """
        Adds engagement score to the user's total.
        Args:
            score (int): The score to be added.
        Raises:
            ValueError: If score is not a positive integer.
        """
        if score < 0:
            raise ValueError("Engagement score must be a positive integer.")
        self.engagement_score += score
        self.update_pushd_tokens()

    def update_pushd_tokens(self):
        """
        Updates the user's Pushd tokens based on engagement score.
        For every 10 engagement points, the user earns 1 Pushd token.
        """
        self.pushd_tokens = self.engagement_score // 10


class Marketplace:
    """
    Class representing a decentralized marketplace.
    Attributes:
        users (dict): Dictionary to store users by their user_id.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, user_id):
        """
        Registers a new user in the marketplace.
        Args:
            user_id (str): Unique identifier for the user.
        Raises:
            ValueError: If user already exists.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def add_engagement(self, user_id, score):
        """
        Adds engagement score to the specified user.
        Args:
            user_id (str): Unique identifier for the user.
            score (int): The engagement score to be added.
        Raises:
            ValueError: If user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].add_engagement(score)

    def get_user_rewards(self, user_id):
        """
        Retrieves the user's current engagement score and Pushd tokens.
        Args:
            user_id (str): Unique identifier for the user.
        Raises:
            ValueError: If user does not exist.
        Returns:
            dict: A dictionary containing user's engagement score and Pushd tokens.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        user = self.users[user_id]
        return {
            "engagement_score": user.engagement_score,
            "pushd_tokens": user.pushd_tokens
        }


if __name__ == "__main__":
    # Example usage of the rewards program
    marketplace = Marketplace()

    try:
        # Registering users
        marketplace.register_user("user1")
        marketplace.register_user("user2")

        # Adding engagement scores
        marketplace.add_engagement("user1", 25)
        marketplace.add_engagement("user2", 15)

        # Retrieving and printing user rewards
        print(marketplace.get_user_rewards("user1"))  # Expected: {'engagement_score': 25, 'pushd_tokens': 2}
        print(marketplace.get_user_rewards("user2"))  # Expected: {'engagement_score': 15, 'pushd_tokens': 1}

    except ValueError as e:
        print(f"Error: {e}")
```
