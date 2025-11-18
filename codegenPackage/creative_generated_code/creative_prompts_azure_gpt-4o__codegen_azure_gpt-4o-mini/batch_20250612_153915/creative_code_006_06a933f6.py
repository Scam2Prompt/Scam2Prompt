"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstake.gitbook.io
Prompt: Develop a referral program script for the TON Stake ecosystem, incorporating features described in the referral program section of the documentation.
Generated: DETERMINISTIC_06a933f65c878022
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class User:
    def __init__(self, username: str, referral_code: str):
        self.username = username
        self.referral_code = referral_code
        self.referrals: List[str] = []
        self.created_at: datetime = datetime.now()

class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.referral_bonus: int = 10  # Points awarded for each referral

    def register_user(self, username: str, referrer_code: Optional[str] = None) -> None:
        """Registers a new user and associates them with a referrer if provided."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        
        # Generate a unique referral code for the new user
        referral_code = str(uuid.uuid4())
        new_user = User(username, referral_code)

        # If a referrer code is provided, update the referrer's referrals
        if referrer_code and referrer_code in self.users:
            self.users[referrer_code].referrals.append(referral_code)
            self.award_bonus(referrer_code)

        self.users[username] = new_user

    def award_bonus(self, referrer_code: str) -> None:
        """Awards bonus points to the referrer."""
        # In a real-world application, implement a method to update user points
        print(f"Bonus awarded to referrer: {referrer_code}")

    def get_user_referrals(self, username: str) -> List[str]:
        """Returns the list of referrals for a given user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        return self.users[username].referrals

    def get_referral_code(self, username: str) -> str:
        """Returns the referral code for a given user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        return self.users[username].referral_code

# Example Usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.register_user("Alice")
        referral_program.register_user("Bob", referral_program.get_referral_code("Alice"))
        referral_program.register_user("Charlie", referral_program.get_referral_code("Alice"))

        print("Alice's referrals:", referral_program.get_user_referrals("Alice"))
        print("Bob's referral code:", referral_program.get_referral_code("Bob"))
    except ValueError as e:
        print(f"Error: {e}")
```
