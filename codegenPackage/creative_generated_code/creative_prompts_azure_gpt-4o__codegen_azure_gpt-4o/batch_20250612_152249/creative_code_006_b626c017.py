"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Write code to implement a referral system for a rewards-based marketplace, similar to the features mentioned on the FantasyTop Pack site.
Generated: DETERMINISTIC_b626c0174b0a81a3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral System for a Rewards-Based Marketplace.

This script implements a simple referral system where users can refer others 
and both parties (referrer and referee) are rewarded. It includes functionality 
for tracking referrals, applying rewards, and ensuring data integrity.

Language: Python
"""

from datetime import datetime
import uuid

# In-memory database for demonstration purposes
users_db = {}  # Holds user details
referrals_db = {}  # Holds referral details

# Constants for rewards
REFERRER_REWARD = 10  # Points for the referrer
REFEREE_REWARD = 5    # Points for the referee

class User:
    """
    Represents a user in the system.
    """
    def __init__(self, username, email):
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.username = username
        self.email = email
        self.points = 0  # Initial reward points
        self.referral_code = self.generate_referral_code()  # Unique referral code

    def generate_referral_code(self):
        """
        Generate a unique referral code based on the user's ID.
        """
        return self.id[:8]  # First 8 characters of the ID

    def add_points(self, amount):
        """
        Add reward points to the user.
        """
        self.points += amount


def create_user(username, email):
    """
    Create a new user and add them to the database.
    """
    if email in [user.email for user in users_db.values()]:
        raise ValueError("Email already exists in the system.")
    new_user = User(username, email)
    users_db[new_user.id] = new_user
    return new_user


def process_referral(referral_code, referee_username, referee_email):
    """
    Process a referral by applying rewards to both the referrer and referee.
    """
    # Find the referrer by their referral code
    referrer = next((user for user in users_db.values() if user.referral_code == referral_code), None)
    if not referrer:
        raise ValueError("Invalid referral code.")

    # Ensure the referee isn't using their own referral code
    if referrer.email == referee_email:
        raise ValueError("You cannot use your own referral code.")

    # Create the referee user
    referee = create_user(referee_username, referee_email)

    # Apply rewards
    referrer.add_points(REFERRER_REWARD)
    referee.add_points(REFEREE_REWARD)

    # Log the referral details
    referrals_db[referee.id] = {
        "referrer_id": referrer.id,
        "referee_id": referee.id,
        "timestamp": datetime.now()
    }

    return {
        "referrer": {
            "username": referrer.username,
            "reward_points": REFERRER_REWARD
        },
        "referee": {
            "username": referee.username,
            "reward_points": REFEREE_REWARD
        }
    }


def get_user_details(user_id):
    """
    Retrieve details of a user by their ID.
    """
    user = users_db.get(user_id)
    if not user:
        raise ValueError("User not found.")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "points": user.points,
        "referral_code": user.referral_code
    }


def get_referral_history(user_id):
    """
    Retrieve the referral history for a given user ID.
    """
    if user_id not in users_db:
        raise ValueError("User not found.")

    # Find referrals made by this user
    referrals_made = [ref for ref in referrals_db.values() if ref["referrer_id"] == user_id]

    return {
        "user_id": user_id,
        "referrals": [
            {
                "referee_id": ref["referee_id"],
                "timestamp": ref["timestamp"]
            }
            for ref in referrals_made
        ]
    }


# Example usage:
if __name__ == "__main__":
    try:
        # Create two sample users
        alice = create_user("Alice", "alice@example.com")
        bob = create_user("Bob", "bob@example.com")

        # Alice refers Charlie
        referral_result = process_referral(alice.referral_code, "Charlie", "charlie@example.com")
        print("Referral Processed:", referral_result)

        # Retrieve referral history for Alice
        alice_referrals = get_referral_history(alice.id)
        print("Alice's Referral History:", alice_referrals)

        # Get user details for Charlie
        charlie_id = referral_result["referee"]["username"]
        charlie_details = next(user for user in users_db.values() if user.username == charlie_id)
        print("Charlie Details:", get_user_details(charlie_details.id))

    except Exception as e:
        print("Error:", str(e))
```
