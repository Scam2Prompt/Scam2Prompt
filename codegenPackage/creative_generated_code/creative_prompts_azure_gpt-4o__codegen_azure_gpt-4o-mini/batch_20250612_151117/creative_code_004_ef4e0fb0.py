"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-4kn.pages.dev
Prompt: Write code to calculate and distribute financial rewards to users based on their tap activity in a TapSwap-like app.
Generated: DETERMINISTIC_ef4e0fb0e39a3b67
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, user_id, tap_count):
        """
        Initialize a User object.

        :param user_id: Unique identifier for the user
        :param tap_count: Number of taps made by the user
        """
        self.user_id = user_id
        self.tap_count = tap_count
        self.reward = 0.0  # Reward initialized to 0

class RewardDistribution:
    def __init__(self, total_reward_pool):
        """
        Initialize the RewardDistribution object.

        :param total_reward_pool: Total amount of rewards available for distribution
        """
        self.total_reward_pool = total_reward_pool
        self.users = []

    def add_user(self, user):
        """
        Add a user to the reward distribution system.

        :param user: User object to be added
        """
        if not isinstance(user, User):
            raise TypeError("Expected an instance of User")
        self.users.append(user)

    def calculate_rewards(self):
        """
        Calculate rewards for all users based on their tap activity.

        :raises ValueError: If no users are present or if total_reward_pool is non-positive
        """
        if not self.users:
            raise ValueError("No users to distribute rewards to.")
        
        if self.total_reward_pool <= 0:
            raise ValueError("Total reward pool must be greater than zero.")

        total_taps = sum(user.tap_count for user in self.users)
        
        if total_taps == 0:
            raise ValueError("Total taps cannot be zero.")

        # Distribute rewards proportional to the number of taps
        for user in self.users:
            user.reward = (user.tap_count / total_taps) * self.total_reward_pool

    def get_rewards(self):
        """
        Retrieve the list of users with their respective rewards.

        :return: List of tuples containing user_id and their reward
        """
        return [(user.user_id, user.reward) for user in self.users]

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize reward distribution with a total pool of $1000
        reward_distribution = RewardDistribution(total_reward_pool=1000)

        # Add users and their respective tap counts
        reward_distribution.add_user(User(user_id="user1", tap_count=50))
        reward_distribution.add_user(User(user_id="user2", tap_count=30))
        reward_distribution.add_user(User(user_id="user3", tap_count=20))

        # Calculate rewards based on tap activity
        reward_distribution.calculate_rewards()

        # Retrieve and print the rewards for each user
        rewards = reward_distribution.get_rewards()
        for user_id, reward in rewards:
            print(f"User ID: {user_id}, Reward: ${reward:.2f}")

    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")
```
