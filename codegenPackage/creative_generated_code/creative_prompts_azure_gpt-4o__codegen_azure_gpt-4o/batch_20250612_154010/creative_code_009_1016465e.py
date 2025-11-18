"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Develop a referral system that tracks referred users and rewards points accordingly, as described in the VEMP Hunt campaign features.
Generated: DETERMINISTIC_1016465e353d7038
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List


class ReferralSystem:
    """
    A referral system to track referred users and reward points based on referrals.
    """

    def __init__(self):
        # Initialize storage for users and their referral data
        self.users: Dict[str, Dict] = {}  # Structure: {user_id: {referrals: [referred_user_ids], points: int}}

    def create_user(self) -> str:
        """
        Registers a new user in the system and returns their unique ID.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {'referrals': [], 'points': 0}  # Initialize user data
        print(f"User created with ID: {user_id}")
        return user_id

    def refer_user(self, referrer_id: str) -> str:
        """
        Allows a user to refer another user.
        :param referrer_id: ID of the user who is referring someone.
        :return: ID of the referred user.
        """
        # Ensure referrer exists
        if referrer_id not in self.users:
            raise ValueError("Referrer ID does not exist in the system.")

        # Create a new user for the referred friend
        referred_id = self.create_user()

        # Associate the referred user with the referrer
        self.users[referrer_id]['referrals'].append(referred_id)

        # Reward points to the referrer
        self.reward_points(referrer_id, 10)  # Example reward: 10 points per referral
        return referred_id

    def reward_points(self, user_id: str, points: int):
        """
        Rewards points to a user.
        :param user_id: ID of the user to receive points.
        :param points: Number of points to add.
        """
        # Ensure user exists
        if user_id not in self.users:
            raise ValueError("User ID does not exist in the system.")

        # Add points to the user's total
        self.users[user_id]['points'] += points
        print(f"User {user_id} rewarded with {points} points. Total points: {self.users[user_id]['points']}")

    def get_user_data(self, user_id: str) -> Dict:
        """
        Retrieves the data for a specific user.
        :param user_id: ID of the user whose data to retrieve.
        :return: User data dictionary.
        """
        # Ensure user exists
        if user_id not in self.users:
            raise ValueError("User ID does not exist in the system.")

        return self.users[user_id]


if __name__ == "__main__":
    # Example usage of the referral system
    system = ReferralSystem()

    # Create initial users
    user1 = system.create_user()
    user2 = system.create_user()

    # User1 refers a friend
    referred_user = system.refer_user(user1)

    # Print user data
    print("User1 Data:", system.get_user_data(user1))
    print("User2 Data:", system.get_user_data(user2))
    print("Referred User Data:", system.get_user_data(referred_user))
```
