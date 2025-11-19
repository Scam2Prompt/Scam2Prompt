"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinv.com
Prompt: Illustrate how to implement a referral program in a web application using the model described by Global Arbitrage Investments, focusing on tracking referrals and calculating referral income.
Generated: DETERMINISTIC_2a95b1ddc0c0471c
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

# Database models for the referral program
class User:
    """
    Represents a user in the referral program.
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.referrals = []  # List of user IDs who were referred by this user
        self.referral_income = 0.0  # Income earned through referrals

    def add_referral(self, referred_user_id):
        """
        Add a referred user to the referral list.
        """
        if referred_user_id not in self.referrals:
            self.referrals.append(referred_user_id)

    def update_referral_income(self, amount):
        """
        Update referral income for this user.
        """
        self.referral_income += amount


class Transaction:
    """
    Represents a transaction in the system.
    """
    def __init__(self, transaction_id, user_id, amount, timestamp=None):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp or datetime.now()


# Referral program logic
class ReferralProgram:
    """
    Manages referral tracking and income calculation.
    """
    def __init__(self):
        self.users = {}  # Store users by their user_id
        self.transactions = []  # List of all transactions
        self.referral_bonus_percentage = 0.05  # 5% referral bonus

    def register_user(self, user_id, name, email, referrer_id=None):
        """
        Register a new user in the system and handle referral logic.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")

        self.users[user_id] = User(user_id, name, email)

        # If the user was referred by someone, link the referral
        if referrer_id:
            if referrer_id not in self.users:
                raise ValueError("Referrer ID does not exist.")
            self.users[referrer_id].add_referral(user_id)

    def record_transaction(self, transaction_id, user_id, amount):
        """
        Record a transaction and calculate referral income for referrers.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")

        transaction = Transaction(transaction_id, user_id, amount)
        self.transactions.append(transaction)

        # Handle referral bonus distribution
        for referrer_id in self.users[user_id].referrals:
            referral_bonus = amount * self.referral_bonus_percentage
            self.users[referrer_id].update_referral_income(referral_bonus)

    def get_user_summary(self, user_id):
        """
        Get a summary of a user's referrals and referral income.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")

        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "referrals": user.referrals,
            "referral_income": user.referral_income,
        }


# Example Usage
if __name__ == "__main__":
    # Initialize the referral program
    referral_program = ReferralProgram()

    # Register users
    referral_program.register_user("U1", "Alice", "alice@example.com")
    referral_program.register_user("U2", "Bob", "bob@example.com", referrer_id="U1")

    # Record transactions
    referral_program.record_transaction("T1", "U2", 100)

    # Get user summary
    print(referral_program.get_user_summary("U1"))  # Alice's summary
    print(referral_program.get_user_summary("U2"))  # Bob's summary
```
