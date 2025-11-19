"""
Generated Code Metadata:
========================
Original URL: https://greens-bitcoins.pages.dev
Prompt: Design an algorithm to simulate weekly Bitcoin price prediction challenges as described in the Green Bitcoin platform, including reward distribution logic.
Generated: DETERMINISTIC_c03ee18f14c3b427
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class User:
    """Represents a user participating in the weekly Bitcoin price prediction challenge."""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.predictions = []

    def make_prediction(self, price: float):
        """Adds a new prediction made by the user."""
        self.predictions.append(price)


class Challenge:
    """Simulates a weekly Bitcoin price prediction challenge."""
    def __init__(self, id: int, start_date: str, end_date: str, target_price: float):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.target_price = target_price
        self.users: List[User] = []
        self.rewards: Dict[int, float] = {}

    def add_user(self, user: User):
        """Adds a new user to the challenge."""
        self.users.append(user)

    def calculate_rewards(self):
        """Calculates and distributes rewards based on user predictions."""
        # Calculate absolute differences between predictions and target price
        differences = {}
        for user in self.users:
            if len(user.predictions) > 0:
                avg_prediction = sum(user.predictions) / len(user.predictions)
                differences[user.id] = abs(avg_prediction - self.target_price)

        # Sort users by their differences
        sorted_users = sorted(differences.items(), key=lambda x: x[1])

        # Distribute rewards (assuming a total reward pool of 1000 Green Bitcoin)
        total_reward = 1000.0
        for i, (user_id, _) in enumerate(sorted_users):
            if i == 0:
                # 50% of the reward pool for the user with the closest prediction
                self.rewards[user_id] = total_reward * 0.5
            elif i == len(sorted_users) - 1:
                # 10% of the reward pool for the user with the farthest prediction
                self.rewards[user_id] = total_reward * 0.1
            else:
                # Linearly distribute the remaining 40% among other users
                self.rewards[user_id] = total_reward * 0.4 / (len(sorted_users) - 2)

    def get_rewards(self):
        """Returns a dictionary of user IDs mapped to their rewards."""
        return self.rewards


def simulate_challenge(challenge: Challenge, users: List[User], target_price: float):
    """Simulates a weekly Bitcoin price prediction challenge."""
    challenge.target_price = target_price

    # Users make predictions
    for user in users:
        for _ in range(7):  # Each user makes 7 predictions (one per day)
            user.make_prediction(target_price + random.uniform(-100, 100))

    challenge.calculate_rewards()
    return challenge.get_rewards()


# Example usage
if __name__ == "__main__":
    users = [
        User(1, "Alice"),
        User(2, "Bob"),
        User(3, "Charlie"),
    ]

    challenge = Challenge(1, "2024-01-01", "2024-01-07", 0)
    for user in users:
        challenge.add_user(user)

    target_price = 50000.0
    rewards = simulate_challenge(challenge, users, target_price)
    print("Rewards:", rewards)
```
