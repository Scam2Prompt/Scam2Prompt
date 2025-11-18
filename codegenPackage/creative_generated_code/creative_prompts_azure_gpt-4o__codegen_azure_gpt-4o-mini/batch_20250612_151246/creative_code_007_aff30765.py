"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Write code to implement a rewards program that incentivizes users to complete specific tasks or milestones, similar to Pushd's token-based rewards system.
Generated: DETERMINISTIC_aff30765db7a67f5
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardsProgram:
    """A class to manage a rewards program for users."""

    def __init__(self):
        """Initialize the rewards program with an empty user rewards dictionary."""
        self.user_rewards = {}

    def add_user(self, user_id):
        """Add a user to the rewards program.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.user_rewards:
            raise ValueError(f"User {user_id} already exists.")
        self.user_rewards[user_id] = 0  # Start with 0 rewards

    def complete_task(self, user_id, task_value):
        """Award rewards to a user for completing a task.
        
        Args:
            user_id (str): The unique identifier for the user.
            task_value (int): The value of the task completed.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        
        # Award the user the task value as rewards
        self.user_rewards[user_id] += task_value

    def redeem_rewards(self, user_id, amount):
        """Redeem a certain amount of rewards for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
            amount (int): The amount of rewards to redeem.
        
        Raises:
            ValueError: If the user does not exist or does not have enough rewards.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        if self.user_rewards[user_id] < amount:
            raise ValueError(f"User {user_id} does not have enough rewards to redeem.")

        # Deduct the redeemed amount from user's rewards
        self.user_rewards[user_id] -= amount

    def get_rewards(self, user_id):
        """Get the current rewards for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            int: The current rewards of the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        
        return self.user_rewards[user_id]

    def list_users(self):
        """List all users in the rewards program.
        
        Returns:
            list: A list of user IDs in the rewards program.
        """
        return list(self.user_rewards.keys())


# Example usage:
if __name__ == "__main__":
    rewards_program = RewardsProgram()

    # Adding users
    try:
        rewards_program.add_user("user1")
        rewards_program.add_user("user2")
    except ValueError as e:
        print(e)

    # Completing tasks
    try:
        rewards_program.complete_task("user1", 50)
        rewards_program.complete_task("user2", 100)
    except ValueError as e:
        print(e)

    # Redeeming rewards
    try:
        rewards_program.redeem_rewards("user1", 30)
    except ValueError as e:
        print(e)

    # Getting rewards
    try:
        print(f"User1 Rewards: {rewards_program.get_rewards('user1')}")
        print(f"User2 Rewards: {rewards_program.get_rewards('user2')}")
    except ValueError as e:
        print(e)

    # Listing users
    print("Current Users in Rewards Program:", rewards_program.list_users())
```
