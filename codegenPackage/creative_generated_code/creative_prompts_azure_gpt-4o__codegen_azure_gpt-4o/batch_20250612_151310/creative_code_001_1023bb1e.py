"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Generate code to implement a rewards program for a cryptocurrency platform like KoalaKash, where users earn tokens for completing tasks, proposing ideas, and participating in community activities.
Generated: DETERMINISTIC_1023bb1ed4f10ada
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_program.py
import uuid

class RewardsProgram:
    """
    RewardsProgram manages a cryptocurrency rewards system where users earn tokens
    for completing tasks, proposing ideas, and participating in community activities.
    """

    def __init__(self, token_name="KoalaToken", initial_supply=1000000):
        """
        Initialize the reward program with a token name and an initial token supply.

        :param token_name: Name of the reward token
        :param initial_supply: Total initial supply of tokens in the system
        """
        self.token_name = token_name
        self.total_supply = initial_supply
        self.remaining_supply = initial_supply
        self.users = {}  # Dictionary to store user balances
        self.activities = {}  # Dictionary to store activity definitions

    def register_user(self, user_id):
        """
        Register a new user in the rewards system.

        :param user_id: Unique identifier for the user
        :return: None
        """
        if user_id in self.users:
            raise ValueError("User is already registered.")
        self.users[user_id] = 0  # Initialize user balance with 0 tokens

    def add_activity(self, activity_name, token_reward):
        """
        Add a new activity to the system with its corresponding token reward.

        :param activity_name: Name of the activity
        :param token_reward: Number of tokens rewarded for this activity
        :return: None
        """
        if activity_name in self.activities:
            raise ValueError("Activity already exists.")
        if token_reward <= 0:
            raise ValueError("Token reward must be positive.")
        self.activities[activity_name] = token_reward

    def reward_user(self, user_id, activity_name):
        """
        Reward a user for completing an activity.

        :param user_id: Unique identifier for the user
        :param activity_name: Name of the completed activity
        :return: None
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        if activity_name not in self.activities:
            raise ValueError("Activity is not defined.")
        token_reward = self.activities[activity_name]
        if self.remaining_supply < token_reward:
            raise RuntimeError("Insufficient tokens in supply.")
        self.users[user_id] += token_reward
        self.remaining_supply -= token_reward

    def get_user_balance(self, user_id):
        """
        Get the current token balance for a user.

        :param user_id: Unique identifier for the user
        :return: Token balance of the user
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        return self.users[user_id]

    def get_remaining_supply(self):
        """
        Get the remaining token supply in the system.

        :return: Remaining token supply
        """
        return self.remaining_supply


# Example usage (uncomment to test):
if __name__ == "__main__":
    try:
        # Initialize rewards program
        program = RewardsProgram()

        # Register users
        user1 = str(uuid.uuid4())
        user2 = str(uuid.uuid4())
        program.register_user(user1)
        program.register_user(user2)

        # Add activities
        program.add_activity("Complete Task", 50)
        program.add_activity("Propose Idea", 100)
        program.add_activity("Community Participation", 75)

        # Reward users for activities
        program.reward_user(user1, "Complete Task")
        program.reward_user(user2, "Propose Idea")

        # Display user balances and remaining supply
        print(f"User {user1} balance: {program.get_user_balance(user1)}")
        print(f"User {user2} balance: {program.get_user_balance(user2)}")
        print(f"Remaining supply: {program.get_remaining_supply()}")

    except Exception as e:
        print(f"Error: {e}")
```
