"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Develop a referral program system in Python for a crypto casino, where users earn rewards for inviting friends, as described on Coin Rush.
Generated: DETERMINISTIC_9a5d5dbb2fba324a
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class User:
    def __init__(self, username):
        """
        Initialize a new user with a unique ID, username and referral information.

        Args:
            username (str): The username of the user.
        """
        self.id = uuid.uuid4()
        self.username = username
        self.referrals = []
        self.rewards = 0

    def add_referral(self, referral_user):
        """
        Add a referral user and update rewards.

        Args:
            referral_user (User): The new user being referred.
        """
        self.referrals.append(referral_user)
        self.rewards += 10  # Fixed reward for each referral
        print(f"{self.username} has referred {referral_user.username}. Total rewards: {self.rewards}")


class ReferralProgram:
    def __init__(self):
        """
        Initialize the referral program with an empty list of users.
        """
        self.users = {}

    def register_user(self, username):
        """
        Register a new user in the referral program.

        Args:
            username (str): The username of the new user.

        Returns:
            User: The newly created User object.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' already exists.")
        
        new_user = User(username)
        self.users[username] = new_user
        print(f"User '{username}' registered successfully.")
        return new_user

    def refer_user(self, referrer_username, referral_username):
        """
        Process user referral.

        Args:
            referrer_username (str): The username of the user making the referral.
            referral_username (str): The username of the referred user.

        Raises:
            ValueError: If either user is not found.
        """
        if referrer_username not in self.users:
            raise ValueError(f"Referrer '{referrer_username}' not found.")
        
        if referral_username in self.users:
            raise ValueError(f"Referral '{referral_username}' already exists.")
        
        referrer = self.users[referrer_username]
        referral_user = self.register_user(referral_username)
        referrer.add_referral(referral_user)


def main():
    """
    Main function to run the referral program simulation.
    """
    referral_program = ReferralProgram()

    # Register users
    try:
        user1 = referral_program.register_user("Alice")
        user2 = referral_program.register_user("Bob")

        # User1 refers User2
        referral_program.refer_user("Alice", "Charlie")
        
        # Display rewards
        print(f"{user1.username} has rewards: {user1.rewards}")
        print(f"{user2.username} has rewards: {user2.rewards}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
