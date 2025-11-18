"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Create a code example demonstrating how to implement a referral program similar to Grass’s, where users can invite friends and track referral-based earnings.
Generated: DETERMINISTIC_f24ec8a414016462
Batch ID: 20250612_151246
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
    """Represents a user in the referral program."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referral_code = self.generate_referral_code()
        self.referrals = []
        self.earnings = 0.0

    def generate_referral_code(self):
        """Generates a unique referral code for the user."""
        return f"REF{self.user_id}"

    def invite_friend(self, friend):
        """Invites a friend using the user's referral code."""
        # Assume the friend is a User object
        if isinstance(friend, User):
            friend.referrals.append(self.referral_code)
            print(f"{self.name} invited {friend.name}.")
        else:
            raise ValueError("The friend must be a User instance.")


class ReferralProgram:
    """Manages the referral program, tracking earnings and user interactions."""
    
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Adds a new user to the referral program."""
        if user.user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user.user_id] = user

    def track_earnings(self, user_id, amount):
        """Tracks earnings for a specific user based on their referrals."""
        if user_id not in self.users:
            raise ValueError("User ID not found in the referral program.")
        
        user = self.users[user_id]
        user.earnings += amount
        print(f"{user.name} has earned {amount}. Total earnings: {user.earnings}.")

    def get_user_report(self, user_id):
        """Generates a report for a specific user."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")

        user = self.users[user_id]
        return {
            "name": user.name,
            "referral_code": user.referral_code,
            "referrals": user.referrals,
            "earnings": user.earnings,
        }


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Create users
        alice = User(user_id=1, name="Alice")
        bob = User(user_id=2, name="Bob")

        # Add users to the program
        program.add_user(alice)
        program.add_user(bob)

        # Alice invites Bob
        alice.invite_friend(bob)

        # Track earnings
        program.track_earnings(user_id=1, amount=50.0)  # Alice earns $50 for referral

        # Get user report
        report = program.get_user_report(user_id=1)
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
```
