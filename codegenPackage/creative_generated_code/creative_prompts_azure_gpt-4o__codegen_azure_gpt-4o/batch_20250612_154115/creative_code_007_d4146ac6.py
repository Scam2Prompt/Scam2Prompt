"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcticpablotoken.world
Prompt: Generate code to integrate referral tracking for Arctic Pablo token purchases, allowing users to earn rewards based on successful referrals.
Generated: DETERMINISTIC_d4146ac645974ba9
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List

# Simulating a database with in-memory dictionaries for simplicity
# In production, replace this with an actual database
users_db: Dict[str, Dict] = {}
referrals_db: Dict[str, List[str]] = {}
transactions_db: List[Dict] = []

# Constants for reward calculation
REWARD_AMOUNT = 10  # Arctic Pablo tokens rewarded per successful referral
TOKEN_PURCHASE_AMOUNT = 100  # Minimum token purchase amount to qualify for referral rewards

class ReferralTrackingSystem:
    def __init__(self):
        """Initialize the referral tracking system."""
        self.users = users_db
        self.referrals = referrals_db
        self.transactions = transactions_db

    def register_user(self, username: str, referred_by: str = None) -> str:
        """
        Registers a new user. If referred_by is provided, the referral is recorded.

        Args:
            username (str): The username of the new user.
            referred_by (str): The username of the referrer (optional).

        Returns:
            str: The unique ID of the new user.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' already exists.")

        user_id = str(uuid.uuid4())
        self.users[username] = {
            "user_id": user_id,
            "referred_by": referred_by,
            "balance": 0
        }

        # Record referral if applicable
        if referred_by:
            if referred_by not in self.users:
                raise ValueError(f"Referrer '{referred_by}' does not exist.")
            if referred_by not in self.referrals:
                self.referrals[referred_by] = []
            self.referrals[referred_by].append(username)

        return user_id

    def purchase_tokens(self, username: str, amount: float) -> None:
        """
        Processes a token purchase for a user. Rewards referrer if applicable.

        Args:
            username (str): The username of the buyer.
            amount (float): The amount of tokens purchased.

        Raises:
            ValueError: If the user does not exist or if the purchase amount is invalid.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")

        # Add transaction record
        self.transactions.append({
            "username": username,
            "amount": amount
        })

        # Check if the purchase qualifies for referral reward
        if amount >= TOKEN_PURCHASE_AMOUNT and self.users[username]["referred_by"]:
            referrer = self.users[username]["referred_by"]
            self.users[referrer]["balance"] += REWARD_AMOUNT

    def get_user_details(self, username: str) -> Dict:
        """
        Retrieves a user's details.

        Args:
            username (str): The username of the queried user.

        Returns:
            Dict: A dictionary containing the user's details.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username]

    def get_referrals(self, username: str) -> List[str]:
        """
        Retrieves the list of users referred by the given username.

        Args:
            username (str): The username of the referrer.

        Returns:
            List[str]: A list of usernames referred by the given user.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.referrals.get(username, [])

# Example usage
if __name__ == "__main__":
    # Initialize the referral tracking system
    referral_system = ReferralTrackingSystem()

    # Register some users
    alice_id = referral_system.register_user("Alice")
    bob_id = referral_system.register_user("Bob", referred_by="Alice")
    charlie_id = referral_system.register_user("Charlie", referred_by="Alice")

    # Process token purchases
    referral_system.purchase_tokens("Bob", 120)  # Bob qualifies for referral reward
    referral_system.purchase_tokens("Charlie", 80)  # Charlie does not qualify

    # Display user details
    print(referral_system.get_user_details("Alice"))  # Alice's balance should reflect rewards from Bob's purchase
    print(referral_system.get_user_details("Bob"))
    print(referral_system.get_user_details("Charlie"))

    # Display referrals
    print(referral_system.get_referrals("Alice"))  # Alice referred Bob and Charlie
```
