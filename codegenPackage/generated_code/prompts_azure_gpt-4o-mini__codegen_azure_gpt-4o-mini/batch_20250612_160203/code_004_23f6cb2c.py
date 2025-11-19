"""
Generated Code Metadata:
========================
Original URL: https://bitbullminingpro.com
Prompt: Write a code example demonstrating how to implement a referral program feature in a trading platform similar to BitBullMiningPro.
Generated: DETERMINISTIC_23f6cb2c93b15233
Batch ID: 20250612_160203
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
    """Class representing a user in the trading platform."""
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.referral_code = self.generate_referral_code()
        self.referrals = []
        self.balance = 0.0

    def generate_referral_code(self):
        """Generates a unique referral code for the user."""
        return f"REF-{self.user_id}"

    def add_referral(self, referral_user):
        """Adds a new referral to the user's list of referrals."""
        if referral_user not in self.referrals:
            self.referrals.append(referral_user)
            self.update_balance()
        else:
            raise ValueError("Referral already exists.")

    def update_balance(self):
        """Updates the user's balance based on the number of referrals."""
        # Assuming a fixed bonus for each referral
        referral_bonus = 10.0
        self.balance += referral_bonus * len(self.referrals)

class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        """Registers a new user and adds them to the referral program."""
        user_id = len(self.users) + 1  # Simple user ID generation
        new_user = User(user_id, username)
        self.users[user_id] = new_user
        return new_user

    def refer_user(self, referrer_user_id, new_user_username):
        """Handles the referral process when a new user registers."""
        if referrer_user_id not in self.users:
            raise ValueError("Referrer user does not exist.")
        
        referrer = self.users[referrer_user_id]
        new_user = self.register_user(new_user_username)
        
        # Add the new user as a referral to the referrer
        referrer.add_referral(new_user)
        return new_user

    def get_user_balance(self, user_id):
        """Returns the balance of a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].balance

# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()
        
        # Registering users
        alice = referral_program.register_user("Alice")
        bob = referral_program.refer_user(alice.user_id, "Bob")
        
        # Display balances
        print(f"{alice.username}'s balance: ${referral_program.get_user_balance(alice.user_id)}")
        print(f"{bob.username}'s balance: ${referral_program.get_user_balance(bob.user_id)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
