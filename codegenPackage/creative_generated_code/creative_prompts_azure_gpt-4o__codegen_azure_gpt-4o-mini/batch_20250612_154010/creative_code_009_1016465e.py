"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Develop a referral system that tracks referred users and rewards points accordingly, as described in the VEMP Hunt campaign features.
Generated: DETERMINISTIC_1016465e353d7038
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to track referred users
        self.points = 0  # Points earned through referrals

    def refer(self, referred_user):
        """Add a referred user and reward points."""
        self.referrals.append(referred_user)
        self.points += 10  # Reward points for each referral
        print(f"{self.name} referred {referred_user.name}. Total points: {self.points}")

class ReferralSystem:
    """Class to manage the referral system."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def add_user(self, user_id, name):
        """Add a new user to the referral system."""
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = User(user_id, name)
        print(f"User {name} added with ID {user_id}.")

    def refer_user(self, referrer_id, referred_user_id, referred_user_name):
        """Handle the referral of a new user by an existing user."""
        if referrer_id not in self.users:
            raise ValueError(f"Referrer ID {referrer_id} does not exist.")
        if referred_user_id in self.users:
            raise ValueError(f"Referred user ID {referred_user_id} already exists.")
        
        # Create a new user for the referred user
        referred_user = User(referred_user_id, referred_user_name)
        self.users[referred_user_id] = referred_user
        self.users[referrer_id].refer(referred_user)

    def get_user_points(self, user_id):
        """Retrieve total points for a user."""
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        return self.users[user_id].points

    def list_referrals(self, user_id):
        """List all referrals made by a user."""
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        return [referral.name for referral in self.users[user_id].referrals]

# Sample usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_system.add_user("1", "Alice")
    referral_system.add_user("2", "Bob")
    
    # Refer users
    referral_system.refer_user("1", "3", "Charlie")
    referral_system.refer_user("1", "4", "Daisy")
    
    # Display points
    print(f"Alice's points: {referral_system.get_user_points('1')}")
    
    # List referrals
    print(f"Alice's referrals: {referral_system.list_referrals('1')}")
```

Note: This code is designed to be clean, efficient, and ready for production use while including error handling and comments for clarity.
