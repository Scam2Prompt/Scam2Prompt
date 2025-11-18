"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Write a script to simulate the referral commission system described on the Coinmining website. Include functionality to calculate the 20% commission based on active deposits from referrals.
Generated: DETERMINISTIC_3d4faa2b42b73997
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    A class to represent a user in the referral system.

    Attributes:
    ----------
    user_id : int
        Unique identifier for the user.
    active_deposit : float
        The amount of the user's active deposit.
    referrals : list
        A list of User instances that have referred to this user.
    """

    def __init__(self, user_id, active_deposit=0.0):
        self.user_id = user_id
        self.active_deposit = active_deposit
        self.referrals = []

    def add_referral(self, referral):
        """
        Adds a user to the list of referrals.

        Parameters:
        ----------
        referral : User
            The user instance that is a referral.
        """
        self.referrals.append(referral)

    def calculate_commission(self):
        """
        Calculates the total commission earned from referrals.

        Returns:
        -------
        float
            Total commission based on the active deposits of referrals.
        """
        total_commission = 0.0
        for referral in self.referrals:
            commission = referral.active_deposit * 0.20  # 20% commission
            total_commission += commission
        return total_commission


def main():
    # Example usage of the User class to simulate the referral system.
    try:
        # Create users
        user1 = User(user_id=1, active_deposit=500.0)
        user2 = User(user_id=2, active_deposit=300.0)
        user3 = User(user_id=3, active_deposit=700.0)

        # User 1 refers User 2 and User 3
        user1.add_referral(user2)
        user1.add_referral(user3)

        # Calculate commissions
        commission_earned = user1.calculate_commission()

        # Display the results
        print(f"User ID: {user1.user_id} has earned a total commission of: ${commission_earned:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
