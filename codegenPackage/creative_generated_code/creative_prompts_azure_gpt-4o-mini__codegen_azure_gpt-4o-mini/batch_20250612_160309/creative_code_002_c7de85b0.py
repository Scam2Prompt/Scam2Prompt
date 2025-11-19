"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaultstake.xyz
Prompt: What are the best practices for creating a referral system in a digital asset management platform like VaultStake?
Generated: DETERMINISTIC_c7de85b0601552f5
Batch ID: 20250612_160309
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
from typing import List, Dict, Optional

class Referral:
    """Class representing a referral made by a user."""
    
    def __init__(self, referrer_id: str):
        self.referral_id: str = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_id: str = referrer_id  # User ID of the referrer
        self.created_at: datetime = datetime.now()  # Timestamp when the referral was created
        self.referred_users: List[str] = []  # List of referred user IDs
        self.is_active: bool = True  # Status of the referral

    def add_referred_user(self, user_id: str) -> None:
        """Add a referred user to the referral if the referral is active."""
        if self.is_active:
            self.referred_users.append(user_id)

    def deactivate(self) -> None:
        """Deactivate the referral."""
        self.is_active = False


class User:
    """Class representing a user in the system."""
    
    def __init__(self, user_id: str, name: str):
        self.user_id: str = user_id  # Unique identifier for the user
        self.name: str = name  # Name of the user
        self.referrals: List[Referral] = []  # List of referrals made by the user

    def create_referral(self) -> Referral:
        """Create a new referral and link it to the user."""
        referral = Referral(referrer_id=self.user_id)
        self.referrals.append(referral)
        return referral

    def get_active_referrals(self) -> List[Referral]:
        """Get a list of active referrals made by the user."""
        return [referral for referral in self.referrals if referral.is_active]


class ReferralSystem:
    """Class to manage the referral system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by their user_id

    def add_user(self, user_id: str, name: str) -> User:
        """Add a new user to the system."""
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(user_id=user_id, name=name)
        self.users[user_id] = user
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by their user_id."""
        return self.users.get(user_id)

    def track_referral(self, referrer_id: str, referred_user_id: str) -> None:
        """Track a referral and add the referred user to the corresponding referral."""
        referrer = self.get_user(referrer_id)
        if referrer is None:
            raise ValueError(f"Referrer with ID {referrer_id} does not exist.")

        # Add the referred user to the referrer's active referral
        active_referrals = referrer.get_active_referrals()
        if active_referrals:
            active_referrals[0].add_referred_user(referred_user_id)  # Add to the first active referral


# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Adding users
    user1 = referral_system.add_user(user_id="user1", name="Alice")
    user2 = referral_system.add_user(user_id="user2", name="Bob")

    # Creating a referral
    referral = user1.create_referral()

    # Tracking a referral
    referral_system.track_referral(referrer_id="user1", referred_user_id="user2")

    # Output the results
    print(f"Referrer: {user1.name}, Referral ID: {referral.referral_id}, Referred Users: {referral.referred_users}")
```
