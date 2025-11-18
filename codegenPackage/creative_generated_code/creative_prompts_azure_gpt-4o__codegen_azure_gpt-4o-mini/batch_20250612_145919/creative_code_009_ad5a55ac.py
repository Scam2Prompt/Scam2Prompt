"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a referral program for an online casino platform, including tracking referrals and calculating rewards, inspired by BaxBet's collaboration programs.
Generated: DETERMINISTIC_ad5a55ac3bd08b21
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class User:
    """Class to represent a user in the referral program."""
    user_id: str
    referrals: List[str] = field(default_factory=list)
    rewards: float = 0.0  # Store rewards in a float format for monetary values

class ReferralProgram:
    """Class to manage the referral program."""

    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user_id

    def add_user(self, user_id: str) -> None:
        """Add a new user to the referral program."""
        if user_id in self.users:
            raise ValueError(f"User with id {user_id} already exists.")
        self.users[user_id] = User(user_id=user_id)

    def refer_user(self, referrer_id: str, referee_id: str) -> None:
        """Process a referral from a referrer to a referee."""
        if referrer_id not in self.users:
            raise ValueError(f"Referrer {referrer_id} does not exist.")
        if referee_id in self.users:
            raise ValueError(f"User {referee_id} already exists.")
        
        # Add the referee to the referral program
        self.add_user(referee_id)
        # Track the referral
        self.users[referrer_id].referrals.append(referee_id)

    def calculate_rewards(self, user_id: str, reward_per_referral: float) -> None:
        """Calculate and assign rewards to a user based on their referrals."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist.")
        
        user = self.users[user_id]
        referral_count = len(user.referrals)
        total_rewards = referral_count * reward_per_referral
        user.rewards += total_rewards  # Update user's total rewards

    def get_user_info(self, user_id: str) -> Optional[User]:
        """Retrieve user information."""
        return self.users.get(user_id, None)

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    try:
        # Add users
        referral_program.add_user("user1")
        referral_program.add_user("user2")

        # User1 refers User2
        referral_program.refer_user("user1", "user2")

        # Calculate rewards for User1
        referral_program.calculate_rewards("user1", reward_per_referral=10.0)

        # Fetch and display user information
        user1_info = referral_program.get_user_info("user1")
        user2_info = referral_program.get_user_info("user2")

        print(f"User1 Info: {user1_info}")
        print(f"User2 Info: {user2_info}")

    except ValueError as e:
        print(f"Error: {e}")
```
