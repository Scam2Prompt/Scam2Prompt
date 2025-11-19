"""
Generated Code Metadata:
========================
Original URL: https://orbiters.vercel.app
Prompt: Propose a method to integrate early adopter bonuses into a token distribution system, considering long-term user activity on a platform like Orbiter Finance.
Generated: DETERMINISTIC_02f3d1a759e3b386
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class TokenDistributionSystem:
    """
    A class to manage token distribution with early adopter bonuses and long-term user activity rewards.
    """

    def __init__(self, total_tokens: int):
        """
        Initialize the token distribution system.

        :param total_tokens: Total number of tokens available for distribution.
        """
        self.total_tokens = total_tokens
        self.early_adopter_bonus_percentage = 10  # Percentage of tokens reserved for early adopters
        self.activity_bonus_percentage = 20      # Percentage of tokens reserved for long-term activity rewards
        self.remaining_tokens = total_tokens - self._calculate_bonus_tokens()
        self.user_data = {}  # Stores user activity data

    def _calculate_bonus_tokens(self) -> int:
        """
        Calculate the total tokens reserved for bonuses.

        :return: Total tokens reserved for bonuses.
        """
        early_adopter_bonus = (self.total_tokens * self.early_adopter_bonus_percentage) // 100
        activity_bonus = (self.total_tokens * self.activity_bonus_percentage) // 100
        return early_adopter_bonus + activity_bonus

    def register_user(self, user_id: str, registration_date: datetime.date):
        """
        Register a new user in the system.

        :param user_id: Unique identifier for the user.
        :param registration_date: Date the user registered on the platform.
        """
        if user_id in self.user_data:
            raise ValueError(f"User {user_id} is already registered.")
        self.user_data[user_id] = {
            "registration_date": registration_date,
            "activity_score": 0,  # Initial activity score
            "tokens_allocated": 0
        }

    def update_activity_score(self, user_id: str, activity_score: int):
        """
        Update the activity score for a user.

        :param user_id: Unique identifier for the user.
        :param activity_score: New activity score to be added.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} is not registered.")
        self.user_data[user_id]["activity_score"] += activity_score

    def distribute_tokens(self):
        """
        Distribute tokens to users based on early adopter bonuses and activity scores.
        """
        # Calculate early adopter bonuses
        early_adopter_bonus_pool = (self.total_tokens * self.early_adopter_bonus_percentage) // 100
        activity_bonus_pool = (self.total_tokens * self.activity_bonus_percentage) // 100

        # Identify early adopters (registered within the first 30 days)
        early_adopter_cutoff = datetime.date.today() - datetime.timedelta(days=30)
        early_adopters = [
            user_id for user_id, data in self.user_data.items()
            if data["registration_date"] <= early_adopter_cutoff
        ]

        # Distribute early adopter bonuses equally
        if early_adopters:
            bonus_per_user = early_adopter_bonus_pool // len(early_adopters)
            for user_id in early_adopters:
                self.user_data[user_id]["tokens_allocated"] += bonus_per_user

        # Distribute activity bonuses based on activity scores
        total_activity_score = sum(data["activity_score"] for data in self.user_data.values())
        if total_activity_score > 0:
            for user_id, data in self.user_data.items():
                user_activity_score = data["activity_score"]
                user_activity_bonus = (user_activity_score / total_activity_score) * activity_bonus_pool
                self.user_data[user_id]["tokens_allocated"] += int(user_activity_bonus)

        # Distribute remaining tokens equally
        remaining_users = len(self.user_data)
        if remaining_users > 0:
            tokens_per_user = self.remaining_tokens // remaining_users
            for user_id in self.user_data:
                self.user_data[user_id]["tokens_allocated"] += tokens_per_user

    def get_user_allocation(self, user_id: str) -> Dict[str, int]:
        """
        Get the token allocation for a specific user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing the user's token allocation.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} is not registered.")
        return {
            "tokens_allocated": self.user_data[user_id]["tokens_allocated"]
        }

# Example usage:
if __name__ == "__main__":
    # Initialize the system with 1,000,000 tokens
    system = TokenDistributionSystem(total_tokens=1000000)

    # Register users
    system.register_user("user1", datetime.date(2023, 9, 1))
    system.register_user("user2", datetime.date(2023, 10, 1))
    system.register_user("user3", datetime.date(2023, 8, 15))

    # Update activity scores
    system.update_activity_score("user1", 100)
    system.update_activity_score("user2", 200)
    system.update_activity_score("user3", 300)

    # Distribute tokens
    system.distribute_tokens()

    # Get user allocations
    print(system.get_user_allocation("user1"))
    print(system.get_user_allocation("user2"))
    print(system.get_user_allocation("user3"))
```
