"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: What are the steps to create a referral program for a trading platform, inspired by the referral earnings structure of Premier Trade Options?
Generated: DETERMINISTIC_01a49e0c8db0b712
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    A class to manage the referral program for a trading platform.
    This program allows users to earn rewards by referring new customers.
    """

    def __init__(self):
        """Initializes the referral program with an empty list of users."""
        self.users = {}  # Dictionary to hold user data with their referrals
        self.referral_rewards = 50  # Fixed reward for each successful referral

    def add_user(self, user_id):
        """
        Adds a new user to the program.

        Args:
            user_id (str): The unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        self.users[user_id] = {
            "referrals": 0,
            "earnings": 0.0
        }
        print(f"User {user_id} added successfully.")

    def refer_user(self, referring_user_id, referred_user_id):
        """
        Processes a referral from one user to another.

        Args:
            referring_user_id (str): The ID of the user making the referral.
            referred_user_id (str): The ID of the new user being referred.
        """
        if referring_user_id not in self.users:
            raise ValueError(f"Referring user {referring_user_id} does not exist.")
        if referred_user_id in self.users:
            raise ValueError(f"Referred user {referred_user_id} already exists.")

        # Add the referred user to the program
        self.add_user(referred_user_id)

        # Update referral count and earnings for the referring user
        self.users[referring_user_id]["referrals"] += 1
        self.users[referring_user_id]["earnings"] += self.referral_rewards
        print(f"User {referring_user_id} referred {referred_user_id} successfully.")

    def get_user_info(self, user_id):
        """
        Retrieves the referral information and earnings for a specific user.

        Args:
            user_id (str): The ID of the user to retrieve information for.

        Returns:
            dict: A dictionary containing the user's referral count and earnings.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist.")
        return self.users[user_id]

    def total_earnings(self, user_id):
        """
        Calculates the total earnings for a specific user based on their referrals.

        Args:
            user_id (str): The ID of the user to calculate total earnings for.

        Returns:
            float: The total earnings of the user from referrals.
        """
        user_info = self.get_user_info(user_id)
        return user_info["earnings"]

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    try:
        referral_program.add_user('user1')
        referral_program.add_user('user2')

        referral_program.refer_user('user1', 'user2')  # user1 refers user2
        print(referral_program.get_user_info('user1'))  # Get info for user1
        print(referral_program.total_earnings('user1'))  # Get total earnings for user1
    except ValueError as e:
        print(f"Error: {e}")
```
