"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Implement a "refer a friend" feature for a crypto casino platform, similar to the affiliate program mentioned on Jups.io.
Generated: DETERMINISTIC_a8ae6bde02c3539d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class ReferralProgram:
    """
    A class to manage the 'Refer a Friend' feature for a crypto casino platform.
    """

    def __init__(self):
        # Store referral mappings and statistics
        self.referrals = {}  # {referrer_id: {"referral_code": code, "referred_users": [id, ...], "rewards": amount}}
        self.users = {}  # {user_id: {"name": name, "balance": balance, "referred_by": referrer_id}}
        self.reward_per_referral = 10  # Reward in crypto for each successfully referred user

    def generate_referral_code(self, referrer_id):
        """
        Generate a unique referral code for a user.
        """
        if referrer_id not in self.referrals:
            referral_code = str(uuid.uuid4())[:8]  # Generate a short unique code
            self.referrals[referrer_id] = {"referral_code": referral_code, "referred_users": [], "rewards": 0}
            return referral_code
        else:
            return self.referrals[referrer_id]["referral_code"]

    def register_user(self, user_id, name, referral_code=None):
        """
        Register a new user. If a referral code is provided, associate the user with the referrer.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} is already registered.")

        # Check if referral code is valid
        referrer_id = None
        if referral_code:
            referrer_id = self.find_referrer(referral_code)
            if not referrer_id:
                raise ValueError("Invalid referral code provided.")

        # Register the user
        self.users[user_id] = {"name": name, "balance": 0, "referred_by": referrer_id}

        # Update referrer's referral statistics
        if referrer_id:
            self.referrals[referrer_id]["referred_users"].append(user_id)
            self.referrals[referrer_id]["rewards"] += self.reward_per_referral
            self.users[referrer_id]["balance"] += self.reward_per_referral  # Add reward to referrer's balance

    def find_referrer(self, referral_code):
        """
        Find the referrer ID using the referral code. Returns None if not found.
        """
        for referrer_id, data in self.referrals.items():
            if data["referral_code"] == referral_code:
                return referrer_id
        return None

    def get_referral_statistics(self, referrer_id):
        """
        Retrieve referral statistics for a specific referrer.
        """
        if referrer_id not in self.referrals:
            raise ValueError(f"No referral data found for referrer ID {referrer_id}.")
        return self.referrals[referrer_id]

    def display_user(self, user_id):
        """
        Display details of a specific user.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        return self.users[user_id]


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()

        # Create users and referral codes
        referrer_id = "user123"
        referral_program.register_user(referrer_id, "Alice")
        referral_code = referral_program.generate_referral_code(referrer_id)
        print(f"Alice's referral code: {referral_code}")

        # New user registers with referral code
        new_user_id = "user456"
        referral_program.register_user(new_user_id, "Bob", referral_code)
        print("Bob registered successfully!")

        # Fetch statistics
        stats = referral_program.get_referral_statistics(referrer_id)
        print(f"Alice's referral statistics: {stats}")

        # Display user details
        user_details = referral_program.display_user(new_user_id)
        print(f"Bob's details: {user_details}")

    except Exception as e:
        print(f"Error: {e}")
```
