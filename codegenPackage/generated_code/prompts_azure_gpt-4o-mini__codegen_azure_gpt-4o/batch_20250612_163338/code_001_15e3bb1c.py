"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a code snippet that demonstrates how to implement a system for inviting friends to earn $BIGTIME rewards in a game like Big Time.
Generated: DETERMINISTIC_15e3bb1c149baf1b
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import random

class BigTimeRewardsSystem:
    """
    A system for inviting friends to earn $BIGTIME rewards in a game.
    """

    def __init__(self):
        # Dictionary to store user data: {user_id: {"invited_friends": [], "reward_balance": 0}}
        self.users = {}

    def create_user(self, username):
        """
        Creates a new user in the system.
        :param username: str - The username of the new user.
        :return: str - The unique user ID.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {"username": username, "invited_friends": [], "reward_balance": 0}
        return user_id

    def invite_friend(self, inviter_id, friend_username):
        """
        Invites a friend to the system and rewards the inviter.
        :param inviter_id: str - The ID of the user inviting the friend.
        :param friend_username: str - The username of the friend being invited.
        :return: str - The unique user ID of the invited friend.
        """
        if inviter_id not in self.users:
            raise ValueError("Inviter ID does not exist.")

        # Create the invited friend as a new user
        friend_id = self.create_user(friend_username)

        # Add the friend to the inviter's list of invited friends
        self.users[inviter_id]["invited_friends"].append(friend_id)

        # Reward the inviter with $BIGTIME points
        reward_points = self._calculate_reward_points()
        self.users[inviter_id]["reward_balance"] += reward_points

        return friend_id

    def _calculate_reward_points(self):
        """
        Calculates the reward points for inviting a friend.
        :return: int - The number of reward points.
        """
        # For simplicity, reward points are randomly generated between 10 and 100
        return random.randint(10, 100)

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.
        :param user_id: str - The ID of the user.
        :return: dict - The user's information.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id]

    def get_reward_balance(self, user_id):
        """
        Retrieves the reward balance of a user.
        :param user_id: str - The ID of the user.
        :return: int - The reward balance.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id]["reward_balance"]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rewards system
        rewards_system = BigTimeRewardsSystem()

        # Create a user
        user_id = rewards_system.create_user("Player1")
        print(f"User created: {user_id}")

        # Invite a friend
        friend_id = rewards_system.invite_friend(user_id, "Player2")
        print(f"Friend invited: {friend_id}")

        # Get user info
        user_info = rewards_system.get_user_info(user_id)
        print(f"User info: {user_info}")

        # Get reward balance
        reward_balance = rewards_system.get_reward_balance(user_id)
        print(f"Reward balance: {reward_balance} $BIGTIME")
    except Exception as e:
        print(f"Error: {e}")
```
