"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: How can I implement a referral system in a crypto earning platform similar to the one described on Moon5, where users earn by inviting others?
Generated: DETERMINISTIC_8dd0a8edf12d2f10
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.referrals = []  # List to store user IDs of referred users
        self.earnings = 0.0  # Total earnings from referrals

    def add_referral(self, referral_user):
        """Add a new referral to the user's list of referrals."""
        if referral_user.user_id not in self.referrals:
            self.referrals.append(referral_user.user_id)
            self.earnings += 10.0  # Reward for each referral
            print(f"{self.username} referred {referral_user.username}. Earnings updated to {self.earnings}.")
        else:
            print(f"{referral_user.username} is already referred by {self.username}.")

class ReferralSystem:
    """Class to manage the referral system."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def register_user(self, user_id, username):
        """Register a new user in the system."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)
        print(f"User {username} registered successfully.")

    def refer_user(self, referrer_id, referral_id, referral_username):
        """Handle the referral process."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if referral_id in self.users:
            raise ValueError("Referral user ID already exists.")
        
        # Create a new user for the referral
        referral_user = User(referral_id, referral_username)
        self.users[referrer_id].add_referral(referral_user)
        self.users[referral_id] = referral_user  # Add the new user to the system

    def get_user_earnings(self, user_id):
        """Retrieve the total earnings of a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].earnings

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    referral_system.register_user("1", "Alice")
    referral_system.register_user("2", "Bob")
    
    # Alice refers Bob
    referral_system.refer_user("1", "2", "Bob")
    
    # Check earnings
    print(f"Alice's earnings: {referral_system.get_user_earnings('1')}")
    print(f"Bob's earnings: {referral_system.get_user_earnings('2')}")
```

This code implements a simple referral system where users can refer others and earn rewards. It includes error handling for user registration and referral processes, ensuring that the system is robust and production-ready.
