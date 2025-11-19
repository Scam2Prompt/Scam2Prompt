"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerspluslimited.com
Prompt: Outline a strategy for implementing a referral program in a web application, similar to the 3-level commission structure offered by MINERS PLUS.
Generated: DETERMINISTIC_1ac1bc97e85923d9
Batch ID: 20250612_160404
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
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.referrals = []  # List to store referred users
        self.commissions = 0  # Total commissions earned

    def refer_user(self, user):
        """
        Refer a new user and add to the referrals list.
        """
        self.referrals.append(user)

    def calculate_commissions(self):
        """
        Calculate total commissions based on referral levels.
        Each referral earns a commission for the user and their referrer.
        """
        level_commission = [0.1, 0.05, 0.02]  # Commissions for levels 1, 2, 3
        
        # Iterate through referrals to calculate commissions
        for level in range(min(3, len(self.referrals))):
            self.commissions += self.referrals[level].earned_amount * level_commission[level]
        
        return self.commissions


class ReferralProgram:
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def add_user(self, user):
        """
        Add a new user to the referral program.
        """
        if user.user_id in self.users:
            raise ValueError("User with this ID already exists.")
        self.users[user.user_id] = user

    def refer(self, referrer_id, referred_user):
        """
        Handle the referral process when a user refers a new user.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer not found.")

        referrer = self.users[referrer_id]
        referrer.refer_user(referred_user)
        
        # Calculate commissions for the referrer
        referrer_commissions = referrer.calculate_commissions()
        return referrer_commissions


# Example usage:
if __name__ == "__main__":
    # Create the referral program
    referral_program = ReferralProgram()
    
    # Create users
    user1 = User(user_id=1, name="Alice", email="alice@example.com")
    user2 = User(user_id=2, name="Bob", email="bob@example.com")

    # Add users to the program
    referral_program.add_user(user1)
    referral_program.add_user(user2)

    # Assuming user 1 refers user 2
    user2.earned_amount = 100  # Simulate some earnings for the referred user
    commissions_earned = referral_program.refer(referrer_id=1, referred_user=user2)

    print(f"User {user1.name} earned commissions: {commissions_earned}")
```
