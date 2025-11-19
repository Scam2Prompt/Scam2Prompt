"""
Generated Code Metadata:
========================
Original URL: https://kayen.pages.dev
Prompt: Generate code to facilitate a referral mission system that rewards users for inviting others, inspired by KAYEN's community engagement strategies.
Generated: DETERMINISTIC_ee0bfef9efd6ed15
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_mission_system.py

from datetime import datetime, timedelta
import uuid
import hashlib

class ReferralMissionSystem:
    def __init__(self):
        # Initialize an in-memory data store for demonstration purposes.
        # In a production environment, use a database.
        self.users = {}
        self.referrals = {}

    def create_user(self, user_id, email):
        """Create a new user."""
        if user_id in self.users:
            raise ValueError("User already exists")

        # Generate a unique referral code for the user
        referral_code = self.generate_referral_code(user_id)

        self.users[user_id] = {
            "email": email,
            "referral_code": referral_code,
            "referrals": [],
            "reward_balance": 0
        }

        return self.users[user_id]

    def generate_referral_code(self, user_id):
        """Generate a unique referral code for a user."""
        # Combine user ID and a random UUID to create a unique referral code
        referral_code = hashlib.sha256((str(user_id) + str(uuid.uuid4())).encode()).hexdigest()[:8]
        return referral_code

    def refer_user(self, referrer_id, referral_code, new_user_email):
        """Refer a new user to the system."""
        if referrer_id not in self.users:
            raise ValueError("Referrer not found")

        if referral_code not in [user["referral_code"] for user in self.users.values()]:
            raise ValueError("Invalid referral code")

        # Find the user who owns the referral code
        referred_user_id = [user_id for user_id, user in self.users.items() if user["referral_code"] == referral_code][0]

        if referred_user_id != referrer_id:
            raise ValueError("Referral code does not belong to the referrer")

        # Create the new user
        new_user_id = str(uuid.uuid4())
        self.create_user(new_user_id, new_user_email)

        # Add the new user to the referrer's referrals
        self.users[referrer_id]["referrals"].append(new_user_id)

        # Reward the referrer
        self.reward_referrer(referrer_id)

    def reward_referrer(self, referrer_id):
        """Reward the referrer for a successful referral."""
        # For demonstration purposes, reward 10 points for each referral
        self.users[referrer_id]["reward_balance"] += 10

    def get_user_info(self, user_id):
        """Get a user's information."""
        if user_id not in self.users:
            raise ValueError("User not found")

        return self.users[user_id]

    def get_referral_code(self, user_id):
        """Get a user's referral code."""
        if user_id not in self.users:
            raise ValueError("User not found")

        return self.users[user_id]["referral_code"]

def main():
    referral_system = ReferralMissionSystem()

    # Create users
    user1 = referral_system.create_user("user1", "user1@example.com")
    user2 = referral_system.create_user("user2", "user2@example.com")

    # Get referral codes
    user1_referral_code = referral_system.get_referral_code("user1")
    print(f"User 1 referral code: {user1_referral_code}")

    # Refer a new user
    referral_system.refer_user("user1", user1_referral_code, "new_user@example.com")

    # Get user info
    user1_info = referral_system.get_user_info("user1")
    print(f"User 1 info: {user1_info}")

if __name__ == "__main__":
    main()
```
