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
from collections import defaultdict

class ReferralProgram:
    """
    A class to manage a referral program system for a crypto casino.
    Users earn rewards for inviting friends.
    """

    def __init__(self, reward_per_referral=10):
        """
        Initializes the referral program.
        
        :param reward_per_referral: The reward (e.g., in tokens) a user earns per successful referral.
        """
        self.reward_per_referral = reward_per_referral
        self.users = {}  # Maps user_id to user details
        self.referral_tree = defaultdict(list)  # Maps referrer_id to list of referred_ids
        self.rewards = defaultdict(int)  # Maps user_id to accumulated rewards

    def register_user(self, username):
        """
        Registers a new user to the system.

        :param username: The username of the new user.
        :return: The unique user ID generated for the new user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.users[user_id] = {"username": username, "referral_code": user_id}
        self.rewards[user_id] = 0
        return user_id

    def use_referral_code(self, referred_username, referral_code):
        """
        Registers a new user using a referral code.

        :param referred_username: The username of the referred user.
        :param referral_code: The referral code of the referrer.
        :return: The unique ID for the referred user, or None if the referral code is invalid.
        """
        if referral_code not in self.users:
            print("Error: Invalid referral code.")
            return None

        referred_user_id = self.register_user(referred_username)
        self.referral_tree[referral_code].append(referred_user_id)
        self.rewards[referral_code] += self.reward_per_referral
        return referred_user_id

    def get_user_details(self, user_id):
        """
        Retrieves details for a specific user.

        :param user_id: The ID of the user.
        :return: A dictionary containing user details or None if the user doesn't exist.
        """
        return self.users.get(user_id, None)

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards for a user.

        :param user_id: The ID of the user.
        :return: The total rewards earned by the user or None if the user doesn't exist.
        """
        if user_id not in self.rewards:
            print("Error: User does not exist.")
            return None
        return self.rewards[user_id]

    def get_referral_tree(self, user_id):
        """
        Retrieves the referral tree for a specific user.

        :param user_id: The ID of the referrer.
        :return: A list of user IDs referred by the user or None if the user doesn't exist.
        """
        if user_id not in self.users:
            print("Error: User does not exist.")
            return None
        return self.referral_tree[user_id]

if __name__ == "__main__":
    # Example usage of the ReferralProgram system

    # Initialize the referral program
    referral_program = ReferralProgram(reward_per_referral=15)

    # Register main users
    alice_id = referral_program.register_user("Alice")
    print(f"Alice registered with ID: {alice_id}")

    bob_id = referral_program.register_user("Bob")
    print(f"Bob registered with ID: {bob_id}")

    # Alice refers Charlie
    charlie_id = referral_program.use_referral_code("Charlie", alice_id)
    if charlie_id:
        print(f"Charlie registered with ID: {charlie_id} using Alice's referral code.")

    # Get Alice's rewards
    alice_rewards = referral_program.get_user_rewards(alice_id)
    print(f"Alice's rewards: {alice_rewards} tokens.")

    # Get Alice's referral tree
    alice_referrals = referral_program.get_referral_tree(alice_id)
    print(f"Alice's referrals: {alice_referrals}")
```
