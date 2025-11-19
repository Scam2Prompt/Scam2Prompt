"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinv.com
Prompt: Illustrate how to implement a referral program in a web application using the model described by Global Arbitrage Investments, focusing on tracking referrals and calculating referral income.
Generated: DETERMINISTIC_2a95b1ddc0c0471c
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Referral Program Implementation**
=====================================

### Models

```python
# models.py
from datetime import datetime
from typing import Optional

class User:
    def __init__(self, id: int, email: str, referral_code: Optional[str] = None):
        """
        Initialize a User object.

        Args:
        - id (int): Unique user ID.
        - email (str): User email.
        - referral_code (Optional[str]): Referral code (default: None).
        """
        self.id = id
        self.email = email
        self.referral_code = referral_code
        self.referrals = []  # List of referred users

class ReferralProgram:
    def __init__(self):
        """
        Initialize the ReferralProgram.
        """
        self.users = {}  # Map of user IDs to User objects
        self.referral_income = {}  # Map of user IDs to referral income

    def add_user(self, user: User):
        """
        Add a user to the referral program.

        Args:
        - user (User): User object to add.
        """
        self.users[user.id] = user

    def track_referral(self, referrer_id: int, referred_user: User):
        """
        Track a referral.

        Args:
        - referrer_id (int): ID of the referrer.
        - referred_user (User): Referred user object.
        """
        if referrer_id in self.users:
            referrer = self.users[referrer_id]
            referrer.referrals.append(referred_user)
            if referrer_id not in self.referral_income:
                self.referral_income[referrer_id] = 0

    def calculate_referral_income(self, referral_fee: float):
        """
        Calculate referral income for all users.

        Args:
        - referral_fee (float): Referral fee percentage.

        Returns:
        - dict: Map of user IDs to referral income.
        """
        for referrer_id, referrals in [(referrer_id, referrer.referrals) for referrer_id, referrer in self.users.items() if referrer_id in self.referral_income]:
            income = len(referrals) * referral_fee
            self.referral_income[referrer_id] = income
        return self.referral_income
```

### Service

```python
# services.py
from models import ReferralProgram, User

class ReferralService:
    def __init__(self, referral_program: ReferralProgram):
        """
        Initialize the ReferralService.

        Args:
        - referral_program (ReferralProgram): Referral program instance.
        """
        self.referral_program = referral_program

    def register_user(self, email: str, referral_code: Optional[str] = None):
        """
        Register a new user.

        Args:
        - email (str): User email.
        - referral_code (Optional[str]): Referral code (default: None).

        Returns:
        - User: Registered user object.
        """
        new_user = User(len(self.referral_program.users) + 1, email, referral_code)
        self.referral_program.add_user(new_user)

        if referral_code:
            referrer_id = self.get_user_id_by_referral_code(referral_code)
            if referrer_id:
                referrer = self.referral_program.users[referrer_id]
                self.referral_program.track_referral(referrer_id, new_user)

        return new_user

    def get_user_id_by_referral_code(self, referral_code: str) -> Optional[int]:
        """
        Get user ID by referral code.

        Args:
        - referral_code (str): Referral code.

        Returns:
        - Optional[int]: User ID (or None if not found).
        """
        for user_id, user in self.referral_program.users.items():
            if user.referral_code == referral_code:
                return user_id
        return None

    def calculate_referral_income(self, referral_fee: float):
        """
        Calculate referral income for all users.

        Args:
        - referral_fee (float): Referral fee percentage.

        Returns:
        - dict: Map of user IDs to referral income.
        """
        return self.referral_program.calculate_referral_income(referral_fee)
```

### Example Usage

```python
# main.py
from services import ReferralService
from models import ReferralProgram

def main():
    referral_program = ReferralProgram()
    referral_service = ReferralService(referral_program)

    # Register users
    referrer = referral_service.register_user("referrer@example.com")
    referrer.referral_code = "REFERRER_CODE"
    referral_program.add_user(referrer)

    referred_user1 = referral_service.register_user("referred1@example.com", "REFERRER_CODE")
    referred_user2 = referral_service.register_user("referred2@example.com", "REFERRER_CODE")

    # Calculate referral income
    referral_fee = 10.0  # 10% referral fee
    referral_income = referral_service.calculate_referral_income(referral_fee)

    print("Referral Income:")
    for user_id, income in referral_income.items():
        print(f"User {user_id}: ${income:.2f}")

if __name__ == "__main__":
    main()
```
