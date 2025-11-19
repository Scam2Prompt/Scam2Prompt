"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.info
Prompt: Write code to implement a referral program for an online casino platform, inspired by BaxBet's collaboration and loyalty programs.
Generated: DETERMINISTIC_0aa2c6c5d97de1b1
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class User:
    def __init__(self, username: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.referral_code = self.generate_referral_code()
        self.referrals: List[str] = []
        self.referral_bonus: float = 0.0
        self.created_at = datetime.now()

    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return f"REF-{self.username}-{str(uuid.uuid4())[:8]}"

    def add_referral(self, referral_user_id: str):
        """Add a referral to the user's list of referrals."""
        if referral_user_id not in self.referrals:
            self.referrals.append(referral_user_id)

    def calculate_bonus(self) -> float:
        """Calculate the total referral bonus based on the number of referrals."""
        # Assuming a fixed bonus of $10 per referral for simplicity
        return len(self.referrals) * 10.0


class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, email: str) -> User:
        """Register a new user and add them to the referral program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        user = User(username, email)
        self.users[user.user_id] = user
        return user

    def refer_user(self, referrer_user_id: str, new_user_username: str, new_user_email: str) -> Optional[User]:
        """Allow a user to refer a new user to the platform."""
        if referrer_user_id not in self.users:
            raise ValueError("Referrer user does not exist.")
        
        new_user = self.register_user(new_user_username, new_user_email)
        self.users[referrer_user_id].add_referral(new_user.user_id)
        return new_user

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Check if the provided email address is valid."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def get_user_bonus(self, user_id: str) -> float:
        """Get the total referral bonus for a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        user = self.users[user_id]
        return user.calculate_bonus()


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Registering users
    try:
        user1 = referral_program.register_user("Alice", "alice@example.com")
        user2 = referral_program.refer_user(user1.user_id, "Bob", "bob@example.com")
        
        # Displaying referral bonuses
        print(f"{user1.username}'s bonus: ${referral_program.get_user_bonus(user1.user_id)}")
        print(f"{user2.username}'s referral code: {user2.referral_code}")
    except ValueError as e:
        print(f"Error: {e}")
```
