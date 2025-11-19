"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the rewards system mentioned on Opteris Global's website.
Generated: DETERMINISTIC_a0b1689beb3e8f52
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

import uuid
from datetime import datetime, timedelta

# Database simulation (in production, use a proper database)
users = {}
referrals = {}

# Constants
REFERRAL_REWARD = 10  # Reward points for successful referrals
EXPIRATION_DAYS = 30  # Referral code expiration period

# User class to represent a user in the system
class User:
    def __init__(self, username, email):
        self.id = str(uuid.uuid4())  # Generate a unique user ID
        self.username = username
        self.email = email
        self.referral_code = self.generate_referral_code()
        self.reward_points = 0

    def generate_referral_code(self):
        # Generate a unique referral code based on the user's ID
        return f"REF-{self.id[:8]}"

    def add_reward_points(self, points):
        self.reward_points += points

# Function to register a new user
def register_user(username, email, referral_code=None):
    try:
        # Check if the user already exists
        if email in users:
            raise ValueError("User with this email already exists.")

        # Create a new user
        new_user = User(username, email)
        users[email] = new_user

        # Handle referral code if provided
        if referral_code:
            handle_referral(referral_code, new_user)

        return new_user
    except Exception as e:
        print(f"Error registering user: {e}")
        return None

# Function to handle referrals
def handle_referral(referral_code, new_user):
    try:
        # Check if the referral code exists and is valid
        if referral_code not in referrals:
            raise ValueError("Invalid referral code.")

        referral = referrals[referral_code]
        if referral["expiration_date"] < datetime.now():
            raise ValueError("Referral code has expired.")

        # Add reward points to the referrer
        referrer = referral["referrer"]
        referrer.add_reward_points(REFERRAL_REWARD)

        # Mark the referral as used
        referral["used"] = True
        referral["new_user"] = new_user

        print(f"Referral successful! {referrer.username} earned {REFERRAL_REWARD} points.")
    except Exception as e:
        print(f"Error handling referral: {e}")

# Function to generate a referral code for a user
def generate_referral_code(user):
    try:
        # Create a referral entry in the system
        referral_code = user.referral_code
        referrals[referral_code] = {
            "referrer": user,
            "expiration_date": datetime.now() + timedelta(days=EXPIRATION_DAYS),
            "used": False,
            "new_user": None,
        }
        return referral_code
    except Exception as e:
        print(f"Error generating referral code: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Register a new user
    user1 = register_user("Alice", "alice@example.com")
    if user1:
        print(f"User {user1.username} registered with referral code: {user1.referral_code}")

    # Generate a referral code for the user
    referral_code = generate_referral_code(user1)
    if referral_code:
        print(f"Referral code generated: {referral_code}")

    # Register another user using the referral code
    user2 = register_user("Bob", "bob@example.com", referral_code)
    if user2:
        print(f"User {user2.username} registered successfully.")

    # Print reward points for the referrer
    print(f"{user1.username} has {user1.reward_points} reward points.")
```

This code implements a basic referral program with user registration, referral code generation, and reward points allocation. It includes error handling and adheres to best practices for Python development.
