"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tswap.exchange
Prompt: What are the steps to implement a referral system in a crypto exchange app based on the TeleSwap model?
Generated: DETERMINISTIC_16dbcc60d9bdb6b7
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral System Implementation for a Crypto Exchange App
Based on the TeleSwap Model
"""

from typing import Dict, Optional
import uuid


# ================================
# Database Mock (Replace with actual DB in production)
# ================================

class MockDatabase:
    users = {}  # Stores user data
    referrals = {}  # Stores referral relationships

db = MockDatabase()


# ================================
# User Model
# ================================

class User:
    def __init__(self, username: str, referral_code: Optional[str] = None):
        self.id = str(uuid.uuid4())  # Generate a unique user ID
        self.username = username
        self.referral_code = self.generate_referral_code()
        self.referred_by = referral_code  # The referral code used during registration

    def generate_referral_code(self) -> str:
        """ Generate a unique referral code for the user. """
        return self.username + "_" + self.id[:8]  # Example format: username_UUID

    def to_dict(self) -> Dict:
        """ Convert user data to dictionary format for storage. """
        return {
            "id": self.id,
            "username": self.username,
            "referral_code": self.referral_code,
            "referred_by": self.referred_by,
        }


# ================================
# Referral System
# ================================

class ReferralSystem:
    @staticmethod
    def register_user(username: str, referral_code: Optional[str] = None) -> Dict:
        """
        Register a new user. If a referral code is provided, link the referral relationship.
        
        Args:
            username (str): Username of the new user.
            referral_code (Optional[str]): Referral code used during registration.

        Returns:
            Dict: Registered user data.
        """

        # Validate inputs
        if not username:
            raise ValueError("Username cannot be empty.")
        if referral_code and referral_code not in db.referrals:
            raise ValueError("Invalid referral code.")

        # Create new user instance
        user = User(username, referral_code)
        db.users[user.id] = user.to_dict()

        # If referred by someone, establish the referral relationship
        if referral_code:
            if referral_code not in db.referrals:
                db.referrals[referral_code] = []
            db.referrals[referral_code].append(user.id)

        return user.to_dict()

    @staticmethod
    def get_referrals(referral_code: str) -> Optional[Dict]:
        """
        Get all users referred by a user using their referral code.

        Args:
            referral_code (str): Referral code of the user.

        Returns:
            Optional[Dict]: List of referred users. None if no referrals found.
        """
        if referral_code not in db.referrals:
            return None

        referred_users = [
            db.users[user_id] for user_id in db.referrals[referral_code]
        ]
        return referred_users


# ================================
# Example Usage
# ================================

def main():
    try:
        # Register users
        user1 = ReferralSystem.register_user("Alice")
        print("User Registered:", user1)

        user2 = ReferralSystem.register_user("Bob", referral_code=user1["referral_code"])
        print("User Registered:", user2)

        # Get referrals for Alice
        alice_referrals = ReferralSystem.get_referrals(user1["referral_code"])
        print("Alice's referrals:", alice_referrals)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
