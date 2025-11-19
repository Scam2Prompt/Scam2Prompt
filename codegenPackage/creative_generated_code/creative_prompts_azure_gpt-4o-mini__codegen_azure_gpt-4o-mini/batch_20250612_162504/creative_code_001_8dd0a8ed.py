"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon5.org
Prompt: How can I implement a referral system in a crypto earning platform similar to the one described on Moon5, where users earn by inviting others?
Generated: DETERMINISTIC_8dd0a8edf12d2f10
Batch ID: 20250612_162504
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
import uuid

@dataclass
class User:
    user_id: str
    referral_code: str
    referrals: List[str] = field(default_factory=list)
    earnings: float = 0.0  # Amount earned through referrals

class ReferralSystem:
    def __init__(self):
        # Store users in a dictionary for fast access
        self.users: Dict[str, User] = {}
        
    def create_user(self) -> User:
        """Create a new user with a unique referral code."""
        user_id = str(uuid.uuid4())
        referral_code = str(uuid.uuid4())[:8]  # Shortened referral code
        new_user = User(user_id=user_id, referral_code=referral_code)
        self.users[user_id] = new_user
        return new_user

    def refer(self, referrer_id: str, invitee_id: str) -> bool:
        """Allows a user to refer another user via referral code."""
        if referrer_id not in self.users or invitee_id not in self.users:
            print("Error: One or both user IDs are invalid.")
            return False
        
        referrer = self.users[referrer_id]
        invitee = self.users[invitee_id]
        
        # Add invitee to the referrer's referrals
        if invitee_id not in referrer.referrals:
            referrer.referrals.append(invitee_id)
            self._reward_referrer(referrer)
            return True
        else:
            print(f"Error: User {invitee_id} is already referred by {referrer_id}.")
            return False

    def _reward_referrer(self, referrer: User) -> None:
        """Reward the referrer for a successful referral."""
        referral_bonus = 10.0  # Fixed bonus for each referral
        referrer.earnings += referral_bonus
        print(f"User {referrer.user_id} earned ${referral_bonus}. Total earnings: ${referrer.earnings}")

    def get_user_info(self, user_id: str) -> Optional[User]:
        """Retrieve user information based on user ID."""
        return self.users.get(user_id, None)

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Create users
    user1 = referral_system.create_user()  # Referrer
    user2 = referral_system.create_user()  # Invitee

    # User1 refers User2
    success = referral_system.refer(user1.user_id, user2.user_id)
    if success:
        print(f"User {user1.user_id} successfully referred User {user2.user_id}.")

    # Fetch and print user info
    print(referral_system.get_user_info(user1.user_id))
    print(referral_system.get_user_info(user2.user_id))
```
