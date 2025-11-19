"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Provide an example of how to implement a referral program in a trading application similar to Finance Impact Pro's offering.
Generated: DETERMINISTIC_acdeec7269b6845e
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class User:
    """Class representing a user in the trading application."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referral_code = self.generate_referral_code()
        self.referrals = []
        self.balance = 0.0

    def generate_referral_code(self):
        """Generate a unique referral code for the user."""
        return f"REF-{self.user_id}"

    def add_referral(self, referral_user):
        """Add a new referral to the user's list of referrals."""
        if referral_user not in self.referrals:
            self.referrals.append(referral_user)
            return True
        return False

    def reward_referral(self, amount):
        """Reward the user for a successful referral."""
        if amount > 0:
            self.balance += amount
            return True
        return False


class ReferralProgram:
    """Class to manage the referral program logic."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, name):
        """Register a new user in the referral program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def refer_user(self, referrer_id, new_user_id, new_user_name):
        """Handle the referral of a new user by an existing user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        
        new_user = self.register_user(new_user_id, new_user_name)
        referrer = self.users[referrer_id]

        # Add the new user as a referral to the referrer
        if referrer.add_referral(new_user):
            # Reward the referrer for the successful referral
            referrer.reward_referral(10.0)  # Reward amount can be adjusted
            return True
        return False

    def get_user_balance(self, user_id):
        """Get the current balance of a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].balance


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Register users
    referral_program.register_user("001", "Alice")
    referral_program.register_user("002", "Bob")

    # Bob refers a new user Charlie
    try:
        referral_program.refer_user("001", "003", "Charlie")
        print(f"Alice's balance after referral: {referral_program.get_user_balance('001')}")
    except ValueError as e:
        print(f"Error: {e}")

    # Check balances
    print(f"Alice's balance: {referral_program.get_user_balance('001')}")
    print(f"Bob's balance: {referral_program.get_user_balance('002')}")
```
