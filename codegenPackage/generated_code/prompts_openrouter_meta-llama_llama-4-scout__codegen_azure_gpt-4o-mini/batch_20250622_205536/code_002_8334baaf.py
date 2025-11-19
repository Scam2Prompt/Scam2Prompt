"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: "Generate a tutorial on how to create a digital pass for a gaming platform like Metacade, including code snippets for profile creation and reward unlocking."
Generated: DETERMINISTIC_8334baaf6fdb70f5
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_pass.py

class UserProfile:
    """
    A class to represent a user profile on the gaming platform.
    """

    def __init__(self, username, email):
        """
        Initializes a new user profile.

        :param username: str - The username of the user.
        :param email: str - The email address of the user.
        """
        self.username = username
        self.email = email
        self.rewards = []
        self.is_active = True

    def deactivate(self):
        """Deactivates the user profile."""
        self.is_active = False

    def add_reward(self, reward):
        """
        Adds a reward to the user's profile.

        :param reward: str - The reward to be added.
        """
        if self.is_active:
            self.rewards.append(reward)
        else:
            raise ValueError("Cannot add reward to an inactive profile.")

    def __str__(self):
        """Returns a string representation of the user profile."""
        return f"UserProfile(username={self.username}, email={self.email}, rewards={self.rewards})"


class RewardSystem:
    """
    A class to manage rewards for users on the gaming platform.
    """

    def __init__(self):
        """Initializes the reward system with an empty rewards list."""
        self.available_rewards = ["10% Discount", "Free Game", "Exclusive Access"]

    def unlock_reward(self, user_profile, reward):
        """
        Unlocks a reward for a user profile if it is available.

        :param user_profile: UserProfile - The user profile to unlock the reward for.
        :param reward: str - The reward to unlock.
        :raises ValueError: If the reward is not available.
        """
        if reward not in self.available_rewards:
            raise ValueError(f"Reward '{reward}' is not available.")
        
        user_profile.add_reward(reward)
        print(f"Reward '{reward}' unlocked for {user_profile.username}!")


def main():
    """Main function to demonstrate profile creation and reward unlocking."""
    try:
        # Create a new user profile
        user1 = UserProfile(username="Gamer123", email="gamer123@example.com")
        print(user1)

        # Create a reward system instance
        reward_system = RewardSystem()

        # Unlock a reward for the user
        reward_system.unlock_reward(user1, "10% Discount")
        print(user1)

        # Attempt to unlock an unavailable reward
        reward_system.unlock_reward(user1, "Nonexistent Reward")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
