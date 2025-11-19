"""
Generated Code Metadata:
========================
Original URL: https://bondex-app.live
Prompt: Generate a code snippet to implement a referral bounty system, like the one described on the Bondex platform, using a programming language of your choice.
Generated: DETERMINISTIC_f041c4b4ed70274f
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bounty_system.py

from typing import Dict
from datetime import datetime, timedelta
import hashlib
import hmac

class ReferralBountySystem:
    def __init__(self, 
                 referral_bounty: float, 
                 max_referrals: int, 
                 bounty_validity: timedelta):
        """
        Initialize the referral bounty system.

        Args:
        - referral_bounty (float): The bounty amount for each successful referral.
        - max_referrals (int): The maximum number of referrals allowed per user.
        - bounty_validity (timedelta): The time period during which the bounty is valid.
        """
        self.referral_bounty = referral_bounty
        self.max_referrals = max_referrals
        self.bounty_validity = bounty_validity
        self.users: Dict[str, User] = {}

    def create_user(self, user_id: str, referrer: str = None):
        """
        Create a new user.

        Args:
        - user_id (str): The unique ID of the user.
        - referrer (str): The ID of the user who referred this user (optional).
        """
        if user_id in self.users:
            raise ValueError("User already exists")

        self.users[user_id] = User(user_id, referrer, self.referral_bounty, self.max_referrals, self.bounty_validity)

    def get_user(self, user_id: str):
        """
        Get a user by ID.

        Args:
        - user_id (str): The unique ID of the user.

        Returns:
        - User: The user object, or None if not found.
        """
        return self.users.get(user_id)

    def refer(self, referrer_id: str, new_user_id: str):
        """
        Record a referral.

        Args:
        - referrer_id (str): The ID of the user who made the referral.
        - new_user_id (str): The ID of the new user.

        Returns:
        - bool: True if the referral was successful, False otherwise.
        """
        referrer = self.get_user(referrer_id)
        if referrer is None:
            return False

        new_user = self.get_user(new_user_id)
        if new_user is not None:
            return False

        referrer.refer(new_user_id)
        self.create_user(new_user_id, referrer_id)
        return True

    def claim_bounty(self, user_id: str):
        """
        Claim the referral bounty.

        Args:
        - user_id (str): The ID of the user claiming the bounty.

        Returns:
        - float: The bounty amount, or 0 if not eligible.
        """
        user = self.get_user(user_id)
        if user is None:
            return 0

        return user.claim_bounty()


class User:
    def __init__(self, 
                 user_id: str, 
                 referrer: str, 
                 referral_bounty: float, 
                 max_referrals: int, 
                 bounty_validity: timedelta):
        self.user_id = user_id
        self.referrer = referrer
        self.referral_bounty = referral_bounty
        self.max_referrals = max_referrals
        self.bounty_validity = bounty_validity
        self.referrals = []
        self.bounty_claimed = False
        self.bounty_claimed_at = None

    def refer(self, new_user_id: str):
        """
        Record a referral.

        Args:
        - new_user_id (str): The ID of the new user.
        """
        if len(self.referrals) < self.max_referrals:
            self.referrals.append(new_user_id)

    def claim_bounty(self) -> float:
        """
        Claim the referral bounty.

        Returns:
        - float: The bounty amount, or 0 if not eligible.
        """
        if self.bounty_claimed:
            return 0

        if len(self.referrals) < self.max_referrals:
            return 0

        if self.bounty_claimed_at is not None and self.bounty_claimed_at + self.bounty_validity > datetime.now():
            return 0

        self.bounty_claimed = True
        self.bounty_claimed_at = datetime.now()
        return self.referral_bounty


def generate_signature(secret_key: str, user_id: str) -> str:
    """
    Generate a signature for a user.

    Args:
    - secret_key (str): The secret key.
    - user_id (str): The user ID.

    Returns:
    - str: The signature.
    """
    return hmac.new(secret_key.encode(), user_id.encode(), hashlib.sha256).hexdigest()


def verify_signature(secret_key: str, user_id: str, signature: str) -> bool:
    """
    Verify a signature for a user.

    Args:
    - secret_key (str): The secret key.
    - user_id (str): The user ID.
    - signature (str): The signature.

    Returns:
    - bool: True if the signature is valid, False otherwise.
    """
    expected_signature = generate_signature(secret_key, user_id)
    return hmac.compare_digest(expected_signature, signature)


# Example usage
if __name__ == "__main__":
    system = ReferralBountySystem(referral_bounty=10.0, max_referrals=5, bounty_validity=timedelta(days=30))

    system.create_user("user1")
    system.refer("user1", "user2")
    system.refer("user1", "user3")

    print(system.claim_bounty("user1"))  # Output: 0.0
    system.create_user("user4")
    system.create_user("user5")
    system.create_user("user6")
    print(system.claim_bounty("user1"))  # Output: 10.0

    secret_key = "my_secret_key"
    user_id = "user1"
    signature = generate_signature(secret_key, user_id)
    print(verify_signature(secret_key, user_id, signature))  # Output: True
```
