"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Create a sample code snippet for a referral program that allows users to earn commissions from deposits, inspired by MFX-Online Trade's referral system.
Generated: DETERMINISTIC_be851bb2e78fd5fd
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class User:
    """Represents a user in the referral program."""
    
    def __init__(self, user_id, referrer_id=None):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            referrer_id (int, optional): Unique identifier for the user's referrer. Defaults to None.
        """
        self.user_id = user_id
        self.referrer_id = referrer_id
        self.deposits = []
        self.referrals = []

class ReferralProgram:
    """Manages the referral program."""
    
    def __init__(self, commission_rate=0.1):
        """
        Initializes a ReferralProgram object.

        Args:
            commission_rate (float, optional): Commission rate for referrals. Defaults to 0.1 (10%).
        """
        self.users = {}
        self.commission_rate = commission_rate

    def add_user(self, user_id, referrer_id=None):
        """
        Adds a new user to the referral program.

        Args:
            user_id (int): Unique identifier for the user.
            referrer_id (int, optional): Unique identifier for the user's referrer. Defaults to None.

        Raises:
            ValueError: If the user_id already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = User(user_id, referrer_id)

    def record_deposit(self, user_id, amount):
        """
        Records a deposit for a user.

        Args:
            user_id (int): Unique identifier for the user.
            amount (float): Deposit amount.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        self.users[user_id].deposits.append(amount)
        self._award_referrer_commission(user_id, amount)

    def _award_referrer_commission(self, user_id, amount):
        """
        Awards a commission to the referrer for a deposit.

        Args:
            user_id (int): Unique identifier for the user.
            amount (float): Deposit amount.
        """
        referrer_id = self.users[user_id].referrer_id
        if referrer_id is not None:
            commission = amount * self.commission_rate
            print(f"User {referrer_id} earned a commission of {commission:.2f} for User {user_id}'s deposit of {amount:.2f}")

    def get_user_deposits(self, user_id):
        """
        Retrieves a user's deposits.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            list[float]: List of deposit amounts.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        return self.users[user_id].deposits

    def get_user_referrals(self, user_id):
        """
        Retrieves a user's referrals.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            list[int]: List of referral user IDs.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        return [user.user_id for user in self.users.values() if user.referrer_id == user_id]

def main():
    referral_program = ReferralProgram()

    # Add users
    referral_program.add_user(1)  # No referrer
    referral_program.add_user(2, 1)  # Referred by User 1
    referral_program.add_user(3, 1)  # Referred by User 1
    referral_program.add_user(4, 2)  # Referred by User 2

    # Record deposits
    referral_program.record_deposit(2, 1000.0)
    referral_program.record_deposit(3, 500.0)
    referral_program.record_deposit(4, 2000.0)

    # Retrieve user deposits and referrals
    print("User 1 deposits:", referral_program.get_user_deposits(1))
    print("User 1 referrals:", referral_program.get_user_referrals(1))
    print("User 2 deposits:", referral_program.get_user_deposits(2))
    print("User 2 referrals:", referral_program.get_user_referrals(2))

if __name__ == "__main__":
    main()
```
