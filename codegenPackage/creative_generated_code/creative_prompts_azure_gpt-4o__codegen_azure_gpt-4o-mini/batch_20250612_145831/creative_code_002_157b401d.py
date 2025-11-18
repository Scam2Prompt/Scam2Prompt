"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Generate code to implement an affiliate program system similar to Smarts-invests, where users earn commissions based on referral deposits.
Generated: DETERMINISTIC_157b401d865b3e65
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# affiliate_program.py

class User:
    """A class representing a user in the affiliate program."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []
        self.commission_earned = 0.0

    def add_referral(self, referral):
        """Add a referral to the user's list of referrals."""
        self.referrals.append(referral)

    def earn_commission(self, amount):
        """Increase the user's commission earned by a specified amount."""
        if amount < 0:
            raise ValueError("Commission amount must be non-negative.")
        self.commission_earned += amount


class AffiliateProgram:
    """A class to manage the affiliate program and calculate commissions."""
    
    def __init__(self, commission_rate=0.1):
        self.users = {}
        self.commission_rate = commission_rate

    def register_user(self, user_id, name):
        """Register a new user in the affiliate program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def refer_user(self, referrer_id, referred_user_id, name):
        """Allow a user to refer another user and register them."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        self.register_user(referred_user_id, name)
        self.users[referrer_id].add_referral(referred_user_id)

    def deposit(self, user_id, amount):
        """Simulate a deposit made by a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.pay_commission(user_id, amount)

    def pay_commission(self, user_id, amount):
        """Calculate and pay commission to the referrer based on the deposit."""
        referrer = self.get_referrer(user_id)
        if referrer:
            commission = amount * self.commission_rate
            self.users[referrer].earn_commission(commission)

    def get_referrer(self, user_id):
        """Retrieve the referrer of the specified user."""
        for user in self.users.values():
            if user_id in user.referrals:
                return user.user_id
        return None

    def get_user_commissions(self, user_id):
        """Return the total commissions earned by a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].commission_earned


# Example Usage
if __name__ == "__main__":
    try:
        program = AffiliateProgram()

        # Register users
        program.register_user("1", "Alice")
        program.register_user("2", "Bob")

        # Alice refers Bob
        program.refer_user("1", "3", "Charlie")

        # Bob makes a deposit
        program.deposit("2", 1000)

        # Get commissions earned by Alice
        print(f"Alice's total commissions: ${program.get_user_commissions('1'):.2f}")

        # Get commissions earned by Bob
        print(f"Bob's total commissions: ${program.get_user_commissions('2'):.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
