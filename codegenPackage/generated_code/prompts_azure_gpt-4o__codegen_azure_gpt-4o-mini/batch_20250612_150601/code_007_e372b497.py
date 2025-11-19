"""
Generated Code Metadata:
========================
Original URL: https://minthidden.web.app
Prompt: Write code to implement dynamic rewards based on user activity or level status, as referenced in the "My rewards" section of the website.
Generated: DETERMINISTIC_e372b497d5b67d48
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    A class to represent a user in the rewards system.
    """

    def __init__(self, user_id, activity_level=0):
        """
        Initializes a new user with a unique ID and an activity level.

        :param user_id: Unique identifier for the user
        :param activity_level: Initial activity level of the user
        """
        self.user_id = user_id
        self.activity_level = activity_level
        self.rewards = []

    def update_activity_level(self, new_level):
        """
        Updates the user's activity level.

        :param new_level: The new activity level to set
        """
        if new_level < 0:
            raise ValueError("Activity level cannot be negative.")
        self.activity_level = new_level
        self.calculate_rewards()

    def calculate_rewards(self):
        """
        Calculates rewards based on the user's current activity level.
        Rewards are added to the user's rewards list.
        """
        # Clear existing rewards
        self.rewards.clear()

        # Define reward thresholds and corresponding rewards
        reward_thresholds = {
            1: "Bronze Badge",
            2: "Silver Badge",
            3: "Gold Badge",
            4: "Platinum Badge",
            5: "Diamond Badge"
        }

        # Assign rewards based on activity level
        for level, reward in reward_thresholds.items():
            if self.activity_level >= level:
                self.rewards.append(reward)

    def get_rewards(self):
        """
        Returns the list of rewards for the user.

        :return: List of rewards
        """
        return self.rewards


def main():
    """
    Main function to demonstrate the rewards system.
    """
    try:
        # Create a new user
        user = User(user_id=1)

        # Update activity level and display rewards
        user.update_activity_level(3)
        print(f"User ID: {user.user_id}, Activity Level: {user.activity_level}, Rewards: {user.get_rewards()}")

        # Update activity level again
        user.update_activity_level(5)
        print(f"User ID: {user.user_id}, Activity Level: {user.activity_level}, Rewards: {user.get_rewards()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
