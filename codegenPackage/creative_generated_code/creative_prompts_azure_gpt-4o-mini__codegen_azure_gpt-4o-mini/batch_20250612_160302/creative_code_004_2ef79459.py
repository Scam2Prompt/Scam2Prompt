"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: How can I implement a referral program in my investment platform like the one described on Zadepositslot?
Generated: DETERMINISTIC_2ef79459453c4200
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class User:
    """Class representing a user in the investment platform."""

    def __init__(self, user_id, referral_code=None):
        """
        Initializes a new user with a unique ID and an optional referral code.

        Args:
            user_id (str): Unique identifier for the user.
            referral_code (str, optional): Code of the user who referred this user.
        """
        self.user_id = user_id
        self.referral_code = referral_code
        self.referrals = []  # List to store referrals made by this user

    def add_referral(self, referral):
        """Adds a new referral to the user's list of referrals.

        Args:
            referral (User): The user that was referred.
        """
        self.referrals.append(referral)

class ReferralProgram:
    """Class representing the referral program logic."""

    def __init__(self):
        """Initializes the referral program with an empty user database."""
        self.users = {}  # Dictionary to hold user_id and User object

    def register_user(self, user_id, referral_code=None):
        """Registers a new user and links them to a referrer if applicable.

        Args:
            user_id (str): Unique identifier for the new user.
            referral_code (str, optional): Code of the referring user.

        Raises:
            ValueError: If the user_id already exists or if the referral_code is invalid.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        # If a referral code is provided, check if it exists
        if referral_code and referral_code not in self.users:
            raise ValueError("Invalid referral code.")

        new_user = User(user_id, referral_code)
        self.users[user_id] = new_user
        
        # Add this user to the referrer's list of referrals if a referral code was provided
        if referral_code:
            referrer = self.users[referral_code]
            referrer.add_referral(new_user)

    def get_referrals(self, user_id):
        """Returns a list of referrals for a given user.

        Args:
            user_id (str): Unique identifier of the user.

        Returns:
            list: List of User objects that the user has referred.

        Raises:
            ValueError: If the user_id is not found.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        return self.users[user_id].referrals

# Example usage of the ReferralProgram
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Register a user without a referral
    referral_program.register_user("user1")
    
    # Register a user with a referral code
    referral_program.register_user("user2", "user1")

    # Get referrals for user1
    try:
        referrals = referral_program.get_referrals("user1")
        print(f"User1 has referred: {[user.user_id for user in referrals]}")
    except ValueError as e:
        print(e)
```
