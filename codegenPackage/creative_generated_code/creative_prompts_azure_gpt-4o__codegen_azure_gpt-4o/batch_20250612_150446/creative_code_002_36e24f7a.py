"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Generate code for a referral program system that calculates referral income based on Cryptonest's referral program structure.
Generated: DETERMINISTIC_36e24f7a753306bf
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Referral Program System for Cryptonest
from typing import Dict, List


class User:
    """
    Represents a user in the referral program.
    """
    def __init__(self, user_id: str, referrer_id: str = None):
        self.user_id = user_id  # Unique identifier for the user
        self.referrer_id = referrer_id  # Referrer ID (user who referred this user)
        self.earnings = 0.0  # Total earnings from referrals


class ReferralProgram:
    """
    Manages the referral program structure and calculates referral income.
    """

    # Define referral income distribution by levels
    # Example: Level 1 (10%), Level 2 (5%), Level 3 (2%)
    REFERRAL_TIERS = [0.10, 0.05, 0.02]

    def __init__(self):
        self.users: Dict[str, User] = {}  # Stores all users by their user ID

    def add_user(self, user_id: str, referrer_id: str = None):
        """
        Adds a new user to the referral program.
        :param user_id: Unique ID of the new user.
        :param referrer_id: ID of the referrer (optional).
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        if referrer_id and referrer_id not in self.users:
            raise ValueError(f"Referrer with ID {referrer_id} does not exist.")

        # Create and add the new user
        self.users[user_id] = User(user_id, referrer_id)

    def record_transaction(self, user_id: str, transaction_amount: float):
        """
        Records a transaction and distributes referral earnings.
        :param user_id: The ID of the user making the transaction.
        :param transaction_amount: The total transaction amount.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if transaction_amount <= 0:
            raise ValueError(f"Transaction amount must be greater than zero.")

        # Apply referral earnings to referrer chain
        current_user_id = user_id
        for level, percentage in enumerate(self.REFERRAL_TIERS, start=1):
            referrer_id = self.users[current_user_id].referrer_id
            if not referrer_id:  # No more referrers in the chain
                break

            # Calculate referral income for the current level
            referral_income = transaction_amount * percentage
            self.users[referrer_id].earnings += referral_income

            # Move up the chain to the next referrer
            current_user_id = referrer_id

    def get_user_earnings(self, user_id: str) -> float:
        """
        Retrieves the total referral earnings of a user.
        :param user_id: The ID of the user.
        :return: The total earnings of the user.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return self.users[user_id].earnings

    def get_all_users(self) -> List[Dict]:
        """
        Retrieves a list of all users and their details for reporting purposes.
        :return: List of dictionaries containing user details.
        """
        return [
            {
                "user_id": user.user_id,
                "referrer_id": user.referrer_id,
                "earnings": user.earnings
            }
            for user in self.users.values()
        ]


# Example usage (can be removed in production)
if __name__ == "__main__":
    program = ReferralProgram()

    # Add users
    program.add_user("user1")  # Root user
    program.add_user("user2", "user1")
    program.add_user("user3", "user2")
    program.add_user("user4", "user3")

    # Record transactions
    program.record_transaction("user4", 100)  # User4 makes a $100 transaction

    # Display earnings
    print("User Referrals and Earnings:")
    for user in program.get_all_users():
        print(user)
```
