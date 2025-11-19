"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Design a referral program similar to MFX-Online Trade's, allowing users to earn commissions from deposits made by referred friends, and describe its benefits and potential drawbacks.
Generated: DETERMINISTIC_684cc1b5aa2408af
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from datetime import datetime, timedelta
from typing import Dict

class ReferralProgram:
    def __init__(self):
        # Initialize referral program settings
        self.referral_link_expiration_days = 30  # days
        self.commission_rate = 0.1  # 10% commission
        self.min_deposit_requirement = 100  # minimum deposit required

        # Initialize in-memory storage for demonstration purposes
        # In a real application, use a database to store user and referral data
        self.users: Dict[str, User] = {}
        self.referrals: Dict[str, Referral] = {}

    def create_user(self, user_id: str) -> User:
        """Create a new user."""
        if user_id in self.users:
            raise ValueError("User already exists")

        user = User(user_id)
        self.users[user_id] = user
        return user

    def generate_referral_link(self, user_id: str) -> str:
        """Generate a referral link for a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist")

        user = self.users[user_id]
        referral_link = f"referral-{user_id}-{datetime.now().timestamp()}"
        expiration_date = datetime.now() + timedelta(days=self.referral_link_expiration_days)

        referral = Referral(referral_link, user_id, expiration_date)
        self.referrals[referral_link] = referral

        return referral_link

    def process_deposit(self, referral_link: str, deposit_amount: float) -> float:
        """Process a deposit made by a referred user."""
        if referral_link not in self.referrals:
            raise ValueError("Invalid referral link")

        referral = self.referrals[referral_link]
        if referral.expiration_date < datetime.now():
            raise ValueError("Referral link has expired")

        if deposit_amount < self.min_deposit_requirement:
            raise ValueError("Deposit amount does not meet the minimum requirement")

        referrer_user_id = referral.referrer_user_id
        referrer_user = self.users[referrer_user_id]

        commission = deposit_amount * self.commission_rate
        referrer_user.earned_commissions += commission

        return commission

class User:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.earned_commissions = 0.0

class Referral:
    def __init__(self, referral_link: str, referrer_user_id: str, expiration_date: datetime):
        self.referral_link = referral_link
        self.referrer_user_id = referrer_user_id
        self.expiration_date = expiration_date

def main():
    referral_program = ReferralProgram()

    # Create users
    user1 = referral_program.create_user("user1")
    user2 = referral_program.create_user("user2")

    # Generate referral link
    referral_link = referral_program.generate_referral_link("user1")
    print(f"Referral link: {referral_link}")

    # Process deposit
    try:
        commission = referral_program.process_deposit(referral_link, 1000.0)
        print(f"Commission earned: {commission}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
