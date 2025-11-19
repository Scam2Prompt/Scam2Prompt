"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Provide an example of how to implement a referral program in a trading application similar to Finance Impact Pro's offering.
Generated: DETERMINISTIC_acdeec7269b6845e
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import Dict, Optional, List

class User:
    def __init__(self, username: str):
        self.username = username
        self.referral_code: str = self.generate_referral_code()
        self.referred_users: List['User'] = []
        self.referral_rewards: float = 0.0
        self.registration_date: datetime = datetime.now()

    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return str(uuid.uuid4())

    def add_referred_user(self, user: 'User'):
        """Add a referred user to the list."""
        self.referred_users.append(user)

    def calculate_rewards(self) -> None:
        """Calculate rewards based on referred users."""
        self.referral_rewards = len(self.referred_users) * 10.0  # Example: $10 reward per referral

class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, referral_code: Optional[str] = None) -> User:
        """Register a new user, applying referral rewards if applicable."""
        new_user = User(username)
        
        if referral_code and referral_code in self.users:
            referrer = self.users[referral_code]
            referrer.add_referred_user(new_user)

            # Update referrer's rewards
            referrer.calculate_rewards()

        self.users[new_user.referral_code] = new_user
        return new_user

    def get_user_rewards(self, referral_code: str) -> float:
        """Retrieve the total rewards for a given user by their referral code."""
        user = self.users.get(referral_code)
        if not user:
            raise ValueError("User not found with the given referral code.")
        return user.referral_rewards

# Example usage:
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()
        
        # Registering users with referrals
        user1 = referral_program.register_user("Alice")
        print(f"User {user1.username} registered with referral code: {user1.referral_code}")

        user2 = referral_program.register_user("Bob", referral_code=user1.referral_code)
        print(f"User {user2.username} registered with referral code: {user2.referral_code}")

        user3 = referral_program.register_user("Charlie", referral_code=user1.referral_code)
        print(f"User {user3.username} registered with referral code: {user3.referral_code}")

        # Checking rewards
        rewards = referral_program.get_user_rewards(user1.referral_code)
        print(f"{user1.username} has earned ${rewards} in referral rewards.")

    except ValueError as e:
        print(f"Error: {e}")
```
