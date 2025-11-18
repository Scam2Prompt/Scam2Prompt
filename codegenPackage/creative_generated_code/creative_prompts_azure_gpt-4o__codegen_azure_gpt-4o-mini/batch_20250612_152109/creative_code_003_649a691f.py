"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Generate code to implement a referral bonus system for the God Candle project, where users can earn rewards for referring others to purchase NFTs or claim tokens.
Generated: DETERMINISTIC_649a691f32e26068
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus.py

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.referrals = []  # List to store referred users
        self.bonus_points = 0  # Initial bonus points

    def add_referral(self, referred_user):
        """Add a new referral and update bonus points."""
        self.referrals.append(referred_user)
        self.bonus_points += 10  # Assume 10 points for each referral
        print(f"Referral added: {referred_user.username}. Total bonus points: {self.bonus_points}")

class ReferralSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def register_user(self, user_id, username):
        """Register a new user."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        new_user = User(user_id, username)
        self.users[user_id] = new_user
        print(f"User registered: {username}")

    def refer_user(self, referrer_id, referred_user_id, referred_username):
        """Allow a user to refer another user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer not found.")
        
        # Register the referred user
        self.register_user(referred_user_id, referred_username)
        
        # Add the referral to the referrer
        referrer = self.users[referrer_id]
        referrer.add_referral(self.users[referred_user_id])

    def get_user_bonus(self, user_id):
        """Get total bonus points for a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id].bonus_points

if __name__ == "__main__":
    # Example usage of the ReferralSystem
    try:
        referral_system = ReferralSystem()
        
        # Register users
        referral_system.register_user(1, "Alice")
        referral_system.register_user(2, "Bob")

        # Alice refers Bob
        referral_system.refer_user(1, 3, "Charlie")  # Alice refers Charlie
        
        # Checking bonus points
        print(f"Alice's bonus points: {referral_system.get_user_bonus(1)}")
        print(f"Bob's bonus points: {referral_system.get_user_bonus(2)}")
        print(f"Charlie's bonus points: {referral_system.get_user_bonus(3)}")

    except ValueError as e:
        print(f"Error: {e}")
```
