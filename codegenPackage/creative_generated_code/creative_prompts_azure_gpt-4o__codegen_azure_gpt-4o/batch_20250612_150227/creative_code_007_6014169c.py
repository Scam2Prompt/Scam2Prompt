"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharecoininvestment.org
Prompt: Write code to implement a referral bonus system for new account registrations, similar to the onboarding process described on sharecoininvestment.org.
Generated: DETERMINISTIC_6014169cca138d0f
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus_system.py

import uuid
import datetime

# Database simulation (in-memory storage for this example)
users_db = {}
referral_db = {}

# Constants for referral bonus system
REFERRAL_BONUS_AMOUNT = 50.0  # $50 bonus for referrals
BONUS_EXPIRY_DAYS = 30  # Bonus expires in 30 days

# User class to represent a user in the system
class User:
    def __init__(self, username, referred_by=None):
        self.user_id = str(uuid.uuid4())  # Unique ID for each user
        self.username = username
        self.referred_by = referred_by
        self.created_at = datetime.datetime.now()
        self.bonus_earned = 0.0
        self.bonus_expiry = None

    def __str__(self):
        return f"User({self.username}, ID={self.user_id}, Bonus={self.bonus_earned}, Expiry={self.bonus_expiry})"

# Function to create a new user account
def create_account(username, referral_code=None):
    try:
        # Check if the username is already taken
        if username in [user.username for user in users_db.values()]:
            raise ValueError("Username is already taken.")

        # Create the new user
        referred_by = referral_db.get(referral_code) if referral_code else None
        new_user = User(username=username, referred_by=referred_by)

        # Save the new user to the database
        users_db[new_user.user_id] = new_user

        # Handle referral bonus if applicable
        if referred_by and referred_by in users_db:
            referrer = users_db[referred_by]
            referrer.bonus_earned += REFERRAL_BONUS_AMOUNT
            referrer.bonus_expiry = datetime.datetime.now() + datetime.timedelta(days=BONUS_EXPIRY_DAYS)

        # Generate a referral code for the new user
        referral_db[new_user.user_id] = new_user.user_id

        return new_user
    except Exception as e:
        print(f"Error creating account: {e}")
        return None

# Function to check referral bonus details
def check_bonus(user_id):
    try:
        user = users_db.get(user_id)
        if not user:
            raise ValueError("User not found.")

        if user.bonus_expiry and datetime.datetime.now() > user.bonus_expiry:
            return f"Referral bonus expired for user {user.username}."
        
        return f"User {user.username} has ${user.bonus_earned} in referral bonuses."
    except Exception as e:
        print(f"Error checking bonus: {e}")
        return None

# Example usage (uncomment to test)
# user1 = create_account("Alice")
# print(user1)
# user2 = create_account("Bob", referral_code=user1.user_id)
# print(user2)
# print(check_bonus(user1.user_id))
```
