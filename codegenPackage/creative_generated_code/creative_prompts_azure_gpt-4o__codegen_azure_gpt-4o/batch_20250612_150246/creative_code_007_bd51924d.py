"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kings-tradefx.com
Prompt: Provide a Python implementation for a referral bonus system in a forex trading platform, similar to the one offered by KINGSTRADE FX during account registration.
Generated: DETERMINISTIC_bd51924d1f78409c
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class ReferralBonusSystem:
    def __init__(self, bonus_amount=50):
        """
        Initialize the referral bonus system.
        :param bonus_amount: The fixed bonus amount for a referral. Default is $50.
        """
        self.bonus_amount = bonus_amount
        self.users = {}  # Dictionary to store user accounts
        self.referrals = {}  # Dictionary to track referrals

    def register_user(self, username, referral_code=None):
        """
        Register a new user to the system.
        :param username: The username of the new user.
        :param referral_code: (Optional) Referral code of the user who referred this user.
        :return: User details including the generated account ID and referral code.
        """
        if username in self.users:
            raise ValueError("Username already taken. Please choose a different username.")
        
        # Generate unique account ID and referral code
        account_id = str(uuid.uuid4())
        user_referral_code = str(uuid.uuid4())[:8]  # Generate a short referral code
        
        # Create user account
        self.users[username] = {
            "account_id": account_id,
            "username": username,
            "referral_code": user_referral_code,
            "balance": 0.0
        }

        # Process referral bonus if a valid referral code is provided
        if referral_code:
            self._process_referral_bonus(referral_code, username)

        return self.users[username]

    def _process_referral_bonus(self, referral_code, new_user):
        """
        Process referral bonus for the user who referred the new user.
        :param referral_code: Referral code provided by the new user during registration.
        :param new_user: Username of the newly registered user.
        """
        # Check if the referral code exists
        referrer = next((user for user in self.users.values()
                        if user["referral_code"] == referral_code), None)
        if referrer:
            # Add bonus to the referrer's account balance
            referrer["balance"] += self.bonus_amount
            
            # Record the referral relationship
            self.referrals.setdefault(referrer["username"], []).append(new_user)
        else:
            raise ValueError("Invalid referral code. Referral bonus not applied.")

    def get_user_details(self, username):
        """
        Retrieve details of a user account.
        :param username: Username of the user.
        :return: User account details.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username]

    def get_referrals(self, username):
        """
        Get a list of referrals made by a user.
        :param username: Username of the referring user.
        :return: List of referred users.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        return self.referrals.get(username, [])

    def get_user_balance(self, username):
        """
        Retrieve the current balance of a user.
        :param username: Username of the user.
        :return: User's account balance.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username]["balance"]


if __name__ == "__main__":
    # Example usage
    system = ReferralBonusSystem(bonus_amount=50)

    try:
        # Register users
        user1 = system.register_user("Alice")
        user2 = system.register_user("Bob", referral_code=user1["referral_code"])
        user3 = system.register_user("Charlie", referral_code=user1["referral_code"])

        # Display user details
        print("User 1 details:", system.get_user_details("Alice"))
        print("User 2 details:", system.get_user_details("Bob"))
        print("User 3 details:", system.get_user_details("Charlie"))

        # Display referral information
        print("Alice's referrals:", system.get_referrals("Alice"))

        # Display user balances
        print("Alice's balance:", system.get_user_balance("Alice"))
        print("Bob's balance:", system.get_user_balance("Bob"))
        print("Charlie's balance:", system.get_user_balance("Charlie"))

    except ValueError as e:
        print("Error:", str(e))
```
