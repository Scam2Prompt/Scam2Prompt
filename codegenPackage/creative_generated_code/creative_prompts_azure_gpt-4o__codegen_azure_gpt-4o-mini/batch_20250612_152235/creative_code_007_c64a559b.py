"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawfury-token.pages.dev
Prompt: Implement a referral system for a cryptocurrency staking platform, similar to the referral info described on PawFury, that rewards users for inviting others to stake $PAW tokens.
Generated: DETERMINISTIC_c64a559b4019019d
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Optional
import uuid

class User:
    """Represents a user in the staking platform."""

    def __init__(self, username: str, wallet_address: str):
        self.username = username
        self.wallet_address = wallet_address
        self.referral_code: str = self.generate_referral_code()
        self.referrals: List[str] = []  # List of usernames referred by this user
        self.reward_balance: float = 0.0  # Rewards earned from referrals

    @staticmethod
    def generate_referral_code() -> str:
        """Generate a unique referral code for the user."""
        return str(uuid.uuid4())

    def add_referral(self, referral_username: str):
        """Adds a referral to the user's list of referrals."""
        self.referrals.append(referral_username)
        self.reward_balance += 10.0  # Reward for each successful referral
        print(f"Referral added: {referral_username}. Reward balance updated to {self.reward_balance}.")

class ReferralSystem:
    """Manages the referral system for the cryptocurrency staking platform."""

    def __init__(self):
        self.users: Dict[str, User] = {}  # Maps username to User object

    def register_user(self, username: str, wallet_address: str) -> User:
        """Register a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        new_user = User(username, wallet_address)
        self.users[username] = new_user
        print(f"User registered: {username} with wallet: {wallet_address}.")
        return new_user

    def refer_user(self, referrer_username: str, referred_username: str, wallet_address: str):
        """Processes referral of a new user by an existing user."""
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")

        if referred_username in self.users:
            raise ValueError("Referred username already exists.")

        # Register the referred user
        referred_user = self.register_user(referred_username, wallet_address)
        # Add the referral to the referrer's account
        self.users[referrer_username].add_referral(referred_username)

    def get_user_info(self, username: str) -> Optional[User]:
        """Retrieve user information by username."""
        return self.users.get(username)

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Register initial users
    user1 = referral_system.register_user("Alice", "0x12345")
    user2 = referral_system.register_user("Bob", "0x67890")

    # Alice refers Charlie
    try:
        referral_system.refer_user("Alice", "Charlie", "0xabcde")
    except ValueError as e:
        print(f"Error: {e}")

    # Display user info
    charlie_info = referral_system.get_user_info("Charlie")
    print(f"Charlie's referral code: {charlie_info.referral_code}, Referrals: {charlie_info.referrals}")
```
