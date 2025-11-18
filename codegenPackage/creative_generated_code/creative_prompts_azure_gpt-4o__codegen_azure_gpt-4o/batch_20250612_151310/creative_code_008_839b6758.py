"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-a30.pages.dev
Prompt: Generate a script to invite users to Ethena via a referral system and calculate the additional 10% shard rewards earned through referrals.
Generated: DETERMINISTIC_839b6758c32cb816
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class User:
    def __init__(self, user_id, username):
        """
        Initialize a User object.

        :param user_id: Unique identifier for the user
        :param username: Username of the user
        """
        self.user_id = user_id
        self.username = username
        self.shards = 0
        self.referrals = []

    def add_shards(self, amount):
        """
        Add shards to the user's account.

        :param amount: Number of shards to be added
        """
        self.shards += amount

    def add_referral(self, referral_user):
        """
        Add a referral user.

        :param referral_user: User object of the referred user
        """
        self.referrals.append(referral_user)

class ReferralSystem:
    def __init__(self):
        """
        Initialize the ReferralSystem object.
        Manages users and referrals.
        """
        self.users = {}

    def create_user(self, username):
        """
        Create a new user and add them to the system.

        :param username: Username of the new user
        :return: Created User object
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        new_user = User(user_id, username)
        self.users[user_id] = new_user
        return new_user

    def invite_user(self, referrer_id, referred_username):
        """
        Invite a user via a referral system.

        :param referrer_id: User ID of the referrer
        :param referred_username: Username of the referred user
        :return: Created User object for the referred user
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID does not exist.")

        referrer = self.users[referrer_id]
        referred_user = self.create_user(referred_username)

        # Add referral relationship
        referrer.add_referral(referred_user)

        # Calculate and add shard reward
        referral_reward = self.calculate_referral_reward(referrer)
        referrer.add_shards(referral_reward)

        return referred_user

    def calculate_referral_reward(self, referrer):
        """
        Calculate the referral reward (10% of referrer's current shard balance).

        :param referrer: Referrer User object
        :return: Amount of shards rewarded
        """
        return int(referrer.shards * 0.1)  # 10% reward

    def print_user_details(self, user_id):
        """
        Print details about a user.

        :param user_id: User ID
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")

        user = self.users[user_id]
        print(f"User: {user.username} (ID: {user.user_id})")
        print(f"Shards: {user.shards}")
        print(f"Referrals: {[ref.username for ref in user.referrals]}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the referral system
        system = ReferralSystem()

        # Create a referrer user
        referrer = system.create_user("Alice")

        # Add shards to the referrer for testing
        referrer.add_shards(100)

        # Invite a new user via referral
        referred = system.invite_user(referrer.user_id, "Bob")

        # Print user details
        system.print_user_details(referrer.user_id)
        system.print_user_details(referred.user_id)

    except Exception as e:
        print(f"An error occurred: {e}")
```
