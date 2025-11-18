"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Provide a code example for integrating a referral program into a crypto rewards platform, similar to the referral feature mentioned on the AVAAI Hunt site.
Generated: DETERMINISTIC_e3a316befcc26fb6
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, Optional

# Simulates a database for storing user and referral data
class MockDatabase:
    def __init__(self):
        self.users = {}
        self.referrals = {}

    def add_user(self, user_id: str, user_data: Dict):
        self.users[user_id] = user_data

    def get_user(self, user_id: str) -> Optional[Dict]:
        return self.users.get(user_id)

    def add_referral(self, referral_id: str, referrer_id: str, referred_id: str):
        self.referrals[referral_id] = {
            "referrer_id": referrer_id,
            "referred_id": referred_id
        }

    def get_referrals_by_referrer(self, referrer_id: str) -> Dict:
        return {key: val for key, val in self.referrals.items() if val["referrer_id"] == referrer_id}

# Initialize mock database
db = MockDatabase()

# Generate a unique referral code for each user
def generate_referral_code(user_id: str) -> str:
    return f"{user_id}-{uuid.uuid4().hex[:8]}"

# Register a new user in the system
def register_user(username: str, referral_code: Optional[str] = None) -> str:
    try:
        user_id = str(uuid.uuid4())
        referral_data = None
        
        # Process referral if a referral code exists
        if referral_code:
            referrer_id = referral_code.split("-")[0]
            referrer = db.get_user(referrer_id)

            if not referrer:
                raise ValueError("Invalid referral code")

            referral_data = {
                "referrer_id": referrer_id,
                "referred_id": user_id
            }
            referral_id = str(uuid.uuid4())
            db.add_referral(referral_id, referrer_id, user_id)
        
        # Add the new user to the database
        db.add_user(user_id, {
            "username": username,
            "referral_code": generate_referral_code(user_id),
            "referred_by": referral_data["referrer_id"] if referral_data else None
        })
        
        return user_id
    except Exception as e:
        print(f"Error registering user: {e}")
        return ""

# Reward the referrer based on referral actions
def reward_referrer(referrer_id: str):
    try:
        referrals = db.get_referrals_by_referrer(referrer_id)
        reward = len(referrals) * 10  # Example: 10 crypto points per referral
        print(f"Referrer {referrer_id} has been rewarded {reward} crypto points!")
    except Exception as e:
        print(f"Error rewarding referrer: {e}")

# Example usage
if __name__ == "__main__":
    # Register users
    user1 = register_user("Alice")  # Alice is the referrer
    user2 = register_user("Bob", referral_code=db.get_user(user1)["referral_code"])  # Bob uses Alice's referral code

    # Reward referrer
    reward_referrer(user1)

    # Check data in the mock database
    print("Users:", db.users)
    print("Referrals:", db.referrals)
```
