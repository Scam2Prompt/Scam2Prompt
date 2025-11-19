"""
Generated Code Metadata:
========================
Original URL: https://slnportal-launchpad.vercel.app
Prompt: Write a program to calculate and display user rewards based on passes and points in the Smart Layer Launchpad system.
Generated: DETERMINISTIC_cd43a5516eda1ab9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_calculator.py

class User:
    """Represents a user in the Smart Layer Launchpad system."""

    def __init__(self, user_id, passes, points):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            passes (int): Number of passes the user has.
            points (int): Number of points the user has.
        """
        self.user_id = user_id
        self.passes = passes
        self.points = points


class RewardsCalculator:
    """Calculates and displays user rewards based on passes and points."""

    def __init__(self, rewards_config):
        """
        Initializes a RewardsCalculator object.

        Args:
            rewards_config (dict): Configuration dictionary for rewards.
                Expected format:
                    {
                        'pass_thresholds': [
                            {'passes': int, 'reward': int},
                            ...
                        ],
                        'point_thresholds': [
                            {'points': int, 'reward': int},
                            ...
                        ]
                    }
        """
        self.rewards_config = rewards_config

    def calculate_rewards(self, user):
        """
        Calculates rewards for a given user.

        Args:
            user (User): User object.

        Returns:
            dict: Rewards for the user.
        """
        rewards = {'passes': 0, 'points': 0}

        # Calculate pass-based rewards
        for threshold in self.rewards_config['pass_thresholds']:
            if user.passes >= threshold['passes']:
                rewards['passes'] = max(rewards['passes'], threshold['reward'])

        # Calculate point-based rewards
        for threshold in self.rewards_config['point_thresholds']:
            if user.points >= threshold['points']:
                rewards['points'] = max(rewards['points'], threshold['reward'])

        return rewards

    def display_rewards(self, user, rewards):
        """
        Displays rewards for a given user.

        Args:
            user (User): User object.
            rewards (dict): Rewards for the user.
        """
        print(f"User ID: {user.user_id}")
        print(f"Passes: {user.passes}")
        print(f"Points: {user.points}")
        print(f"Rewards:")
        print(f"  Passes: {rewards['passes']}")
        print(f"  Points: {rewards['points']}")


def main():
    # Example rewards configuration
    rewards_config = {
        'pass_thresholds': [
            {'passes': 10, 'reward': 100},
            {'passes': 50, 'reward': 500},
            {'passes': 100, 'reward': 1000}
        ],
        'point_thresholds': [
            {'points': 100, 'reward': 50},
            {'points': 500, 'reward': 200},
            {'points': 1000, 'reward': 500}
        ]
    }

    calculator = RewardsCalculator(rewards_config)

    try:
        user_id = int(input("Enter user ID: "))
        passes = int(input("Enter number of passes: "))
        points = int(input("Enter number of points: "))

        user = User(user_id, passes, points)
        rewards = calculator.calculate_rewards(user)
        calculator.display_rewards(user, rewards)

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
