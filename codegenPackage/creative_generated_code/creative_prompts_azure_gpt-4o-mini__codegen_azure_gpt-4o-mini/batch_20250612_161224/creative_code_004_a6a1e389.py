"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: How can I create a rewards system for users who participate in voting, inspired by the QnA3 credits system?
Generated: DETERMINISTIC_a6a1e3893e836975
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    A class to represent a user in the rewards system.
    
    Attributes:
    ----------
    user_id : int
        Unique identifier for the user.
    votes_cast : int
        Number of votes the user has cast.
    rewards : int
        Total rewards accumulated by the user.
    """

    def __init__(self, user_id):
        """
        Initializes a new User instance.

        Parameters:
        ----------
        user_id : int
            Unique identifier for the user.
        """
        self.user_id = user_id
        self.votes_cast = 0
        self.rewards = 0

    def cast_vote(self):
        """
        Simulates casting a vote and rewards the user.
        Each vote cast earns the user 10 reward points.
        """
        try:
            self.votes_cast += 1
            self.rewards += 10
            print(f"User {self.user_id} cast a vote. Total votes: {self.votes_cast}, Total rewards: {self.rewards}")
        except Exception as e:
            print(f"An error occurred while casting vote for user {self.user_id}: {e}")


class RewardsSystem:
    """
    A class to manage the rewards system for users.
    
    Methods:
    -------
    add_user(user_id): Adds a new user to the system.
    cast_vote(user_id): Allows the specified user to cast a vote.
    get_user_rewards(user_id): Returns the total rewards of the specified user.
    """

    def __init__(self):
        """ Initializes the rewards system with an empty user dictionary. """
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the rewards system.

        Parameters:
        ----------
        user_id : int
            Unique identifier for the user.
        
        Raises:
        ------
        ValueError: If the user already exists in the system.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        self.users[user_id] = User(user_id)
        print(f"User {user_id} added to the rewards system.")

    def cast_vote(self, user_id):
        """
        Allows the specified user to cast a vote.

        Parameters:
        ----------
        user_id : int
            Unique identifier for the user.

        Raises:
        ------
        KeyError: If the user does not exist in the system.
        """
        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found in the system.")
        self.users[user_id].cast_vote()

    def get_user_rewards(self, user_id):
        """
        Returns the total rewards of the specified user.

        Parameters:
        ----------
        user_id : int
            Unique identifier for the user.
        
        Returns:
        -------
        int: Total rewards of the user.

        Raises:
        ------
        KeyError: If the user does not exist in the system.
        """
        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found in the system.")
        return self.users[user_id].rewards


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Add users
    rewards_system.add_user(1)
    rewards_system.add_user(2)

    # Cast votes
    rewards_system.cast_vote(1)
    rewards_system.cast_vote(2)
    rewards_system.cast_vote(1)

    # Retrieve user rewards
    print(f"Total rewards for user 1: {rewards_system.get_user_rewards(1)}")
    print(f"Total rewards for user 2: {rewards_system.get_user_rewards(2)}")
```
