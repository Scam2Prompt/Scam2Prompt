"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Construct a code example that integrates a referral program for hot tub purchases, similar to the one offered by Country Leisure, into an existing e-commerce platform.
Generated: DETERMINISTIC_18830af9fcc907be
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py
# This module integrates a referral program for hot tub purchases into an e-commerce platform.

import uuid
from datetime import datetime, timedelta
from typing import Dict, List


# Database simulation (replace with a proper database in production)
users_db: Dict[str, Dict] = {}  # Stores user details
referrals_db: Dict[str, Dict] = {}  # Stores referral details


class ReferralProgram:
    """
    A class to manage the referral program for hot tub purchases.
    """

    def __init__(self, reward_amount: float, referral_validity_days: int):
        """
        Initializes the Referral Program.
        :param reward_amount: Amount rewarded for successful referrals.
        :param referral_validity_days: Number of days a referral link remains valid.
        """
        self.reward_amount = reward_amount
        self.referral_validity_days = referral_validity_days

    def generate_referral_code(self, user_id: str) -> str:
        """
        Generates a unique referral code for a user.
        :param user_id: ID of the user generating the referral code.
        :return: Referral code as a string.
        """
        if user_id not in users_db:
            raise ValueError("User not found.")

        referral_code = str(uuid.uuid4())
        expiration_date = datetime.now() + timedelta(days=self.referral_validity_days)

        referrals_db[referral_code] = {
            "user_id": user_id,
            "created_at": datetime.now(),
            "expires_at": expiration_date,
            "successful_referrals": 0
        }

        return referral_code

    def validate_referral_code(self, referral_code: str) -> bool:
        """
        Validates a referral code by checking its existence and expiration.
        :param referral_code: Referral code to be validated.
        :return: True if the code is valid, False otherwise.
        """
        referral = referrals_db.get(referral_code)

        if not referral:
            return False

        if datetime.now() > referral["expires_at"]:
            return False

        return True

    def apply_referral_code(self, referral_code: str, purchaser_id: str) -> None:
        """
        Applies a referral code to a purchase and rewards the referrer.
        :param referral_code: The referral code used during purchase.
        :param purchaser_id: ID of the purchaser using the referral code.
        """
        if not self.validate_referral_code(referral_code):
            raise ValueError("Invalid or expired referral code.")

        referral = referrals_db[referral_code]
        referrer_id = referral["user_id"]

        if referrer_id == purchaser_id:
            raise ValueError("Users cannot refer themselves.")

        # Reward the referrer
        users_db[referrer_id]["balance"] += self.reward_amount
        referral["successful_referrals"] += 1


# Example usage of the referral program
if __name__ == "__main__":
    # Initialize users database with dummy data
    users_db["user1"] = {"name": "Alice", "balance": 0.0}
    users_db["user2"] = {"name": "Bob", "balance": 0.0}

    # Initialize the referral program
    referral_program = ReferralProgram(reward_amount=50.0, referral_validity_days=30)

    try:
        # Generate a referral code for Alice
        alice_referral_code = referral_program.generate_referral_code("user1")
        print(f"Alice's referral code: {alice_referral_code}")

        # Apply the referral code during Bob's purchase
        referral_program.apply_referral_code(alice_referral_code, "user2")
        print(f"Referral code applied successfully.")

        # Verify updated balances
        print(f"Alice's balance: {users_db['user1']['balance']}")
        print(f"Bob's balance: {users_db['user2']['balance']}")
    except ValueError as e:
        print(f"Error: {e}")
```
