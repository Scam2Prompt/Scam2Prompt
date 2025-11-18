"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Develop a referral program system for a cryptocurrency investment platform that calculates and distributes a 5% referral bonus, as described on Capitalhandelssystem.
Generated: DETERMINISTIC_1f73c0ac3def3ca4
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal

# Enable high precision for financial calculations
decimal.getcontext().prec = 18

class ReferralProgram:
    """
    A class to manage a referral program for a cryptocurrency investment platform.
    It calculates and distributes a 5% referral bonus to the referrer.
    """

    def __init__(self):
        """
        Initialize the referral program with an empty dictionary to store user balances and referrals.
        """
        self.user_balances = {}  # Stores each user's total balance
        self.referrals = {}     # Stores referrer relationships {referee: referrer}

    def register_user(self, user_id: str):
        """
        Registers a new user in the system.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_balances:
            raise ValueError("User ID already exists.")
        self.user_balances[user_id] = Decimal("0.00")  # Initialize balance to zero
        self.referrals[user_id] = None  # No referrer by default

    def set_referrer(self, referee_id: str, referrer_id: str):
        """
        Sets the referrer for a user.
        :param referee_id: User being referred.
        :param referrer_id: User referring the referee.
        """
        if referee_id not in self.user_balances or referrer_id not in self.user_balances:
            raise ValueError("Both referee and referrer must be registered users.")
        if referee_id == referrer_id:
            raise ValueError("A user cannot refer themselves.")
        self.referrals[referee_id] = referrer_id

    def deposit(self, user_id: str, amount: Decimal):
        """
        Deposits cryptocurrency into a user's account and calculates the referral bonus.
        :param user_id: User receiving the deposit.
        :param amount: Amount to deposit.
        """
        if amount <= Decimal("0.00"):
            raise ValueError("Deposit amount must be greater than zero.")
        if user_id not in self.user_balances:
            raise ValueError("User ID does not exist.")
        
        # Update user's balance
        self.user_balances[user_id] += amount

        # Check if the user has a referrer
        referrer_id = self.referrals.get(user_id)
        if referrer_id:
            # Calculate 5% referral bonus
            referral_bonus = amount * Decimal("0.05")
            self.user_balances[referrer_id] += referral_bonus

    def get_balance(self, user_id: str) -> Decimal:
        """
        Retrieves the balance for a specific user.
        :param user_id: User to query.
        :return: Current balance of the user.
        """
        if user_id not in self.user_balances:
            raise ValueError("User ID does not exist.")
        return self.user_balances[user_id]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize referral program system
        program = ReferralProgram()

        # Register users
        program.register_user("Alice")
        program.register_user("Bob")
        program.register_user("Charlie")

        # Set referrals
        program.set_referrer("Bob", "Alice")   # Bob was referred by Alice
        program.set_referrer("Charlie", "Alice")  # Charlie was referred by Alice

        # Deposit funds and calculate referral bonuses
        program.deposit("Bob", Decimal("100.00"))  # Alice gets 5% of 100.00 as bonus (5.00)
        program.deposit("Charlie", Decimal("50.00"))  # Alice gets 5% of 50.00 as bonus (2.50)

        # Print balances
        print("Alice's balance:", program.get_balance("Alice"))  # Expected: 7.50
        print("Bob's balance:", program.get_balance("Bob"))      # Expected: 100.00
        print("Charlie's balance:", program.get_balance("Charlie"))  # Expected: 50.00

    except Exception as e:
        print("Error:", e)
```
