"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: Generate code to implement a referral program for a tax document generation service, similar to the $36-per-referral system described on https://polymarket.tax.
Generated: DETERMINISTIC_9baa0dfb30d3916a
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class ReferralProgram:
    """
    A class to manage a referral program.
    """

    def __init__(self, referral_bonus=36.0):
        """
        Initialize the referral program with a default referral bonus.

        :param referral_bonus: Amount rewarded per valid referral (default is $36.00).
        """
        self.referral_bonus = referral_bonus
        self.users = {}  # Dictionary to store user info (user_id -> user data)
        self.referrals = {}  # Dictionary to track referrals (referrer_id -> list of referred_ids)

    def create_user(self, name, email):
        """
        Create a new user in the system.

        :param name: The user's name.
        :param email: The user's email address.
        :return: The generated user ID.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "name": name,
            "email": email,
            "referral_balance": 0.0
        }
        return user_id

    def refer_user(self, referrer_id, name, email):
        """
        Allow an existing user to refer a new user.

        :param referrer_id: The ID of the user referring someone.
        :param name: The referred user's name.
        :param email: The referred user's email address.
        :return: The new user's ID if successful.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID not found.")

        # Create the referred user
        referred_user_id = self.create_user(name, email)

        # Track the referral
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_user_id)

        # Update the referrer's balance
        self.users[referrer_id]["referral_balance"] += self.referral_bonus

        return referred_user_id

    def get_user_info(self, user_id):
        """
        Retrieve information for a specific user.

        :param user_id: The user ID.
        :return: A dictionary containing user information.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        return self.users[user_id]

    def get_referral_info(self, referrer_id):
        """
        Retrieve referral information for a specific user.

        :param referrer_id: The referrer's user ID.
        :return: A dictionary containing the referrer's referral data.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID not found.")
        
        referred_users = self.referrals.get(referrer_id, [])
        referral_data = {
            "referrer_name": self.users[referrer_id]["name"],
            "referral_balance": self.users[referrer_id]["referral_balance"],
            "referred_users": [self.users[uid]["name"] for uid in referred_users]
        }
        return referral_data


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Create a referrer user
        referrer_id = program.create_user(name="Alice", email="alice@example.com")
        print("Referrer created:", program.get_user_info(referrer_id))

        # Referrer refers a new user
        referred_id = program.refer_user(referrer_id, name="Bob", email="bob@example.com")
        print("Referred user created:", program.get_user_info(referred_id))

        # Get referrer's referral info
        referral_info = program.get_referral_info(referrer_id)
        print("Referral info:", referral_info)

    except Exception as e:
        print("Error:", str(e))
```
