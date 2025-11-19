"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a referral program for an online casino platform, including tracking referrals and calculating rewards, inspired by BaxBet's collaboration programs.
Generated: DETERMINISTIC_ad5a55ac3bd08b21
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
    def __init__(self, username: str):
        self.username = username
        self.referral_code: str = self.generate_referral_code()
        self.referrals: List[str] = []
        self.reward_points: int = 0

    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return str(uuid.uuid4())

    def add_referral(self, referral_code: str) -> None:
        """Add a referral to the user's list of referrals."""
        self.referrals.append(referral_code)

    def calculate_rewards(self) -> int:
        """Calculate rewards based on the number of referrals."""
        # Assuming a reward of 10 points per referral
        self.reward_points = len(self.referrals) * 10
        return self.reward_points


class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str) -> User:
        """Register a new user in the referral program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def refer_user(self, referrer_username: str, new_username: str) -> Optional[User]:
        """Allow a user to refer a new user."""
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if new_username in self.users:
            raise ValueError("New username already exists.")

        new_user = self.register_user(new_username)
        referrer = self.users[referrer_username]
        referrer.add_referral(new_user.referral_code)
        return new_user

    def get_user_rewards(self, username: str) -> int:
        """Get the total reward points for a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].calculate_rewards()


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Register users
    user1 = referral_program.register_user("Alice")
    user2 = referral_program.refer_user("Alice", "Bob")

    # Calculate rewards
    alice_rewards = referral_program.get_user_rewards("Alice")
    print(f"Alice's reward points: {alice_rewards}")

    # Attempt to refer an existing user
    try:
        referral_program.refer_user("Alice", "Bob")
    except ValueError as e:
        print(e)  # Output: New username already exists.
```
