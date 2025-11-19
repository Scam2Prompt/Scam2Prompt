"""
Generated Code Metadata:
========================
Original URL: https://lumos-airdrop.pages.dev
Prompt: Generate code to simulate the referral bonus system described for Lumos Capital investment plans, ensuring the bonus is calculated as 10% of the referred user's investment.
Generated: DETERMINISTIC_70600cdea68aa46c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Represents a user with an investment amount and referral information."""

    def __init__(self, user_id, investment_amount):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            investment_amount (float): The amount invested by the user.
        """
        self.user_id = user_id
        self.investment_amount = investment_amount
        self.referred_by = None  # User ID of the user who referred this user


class ReferralBonusSystem:
    """Simulates the referral bonus system for Lumos Capital investment plans."""

    def __init__(self):
        """Initializes the referral bonus system."""
        self.users = {}  # Maps user IDs to User objects

    def add_user(self, user_id, investment_amount, referred_by=None):
        """
        Adds a new user to the system.

        Args:
            user_id (int): Unique identifier for the user.
            investment_amount (float): The amount invested by the user.
            referred_by (int, optional): User ID of the user who referred this user. Defaults to None.

        Raises:
            ValueError: If the investment amount is negative.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount cannot be negative")

        user = User(user_id, investment_amount)
        user.referred_by = referred_by
        self.users[user_id] = user

    def calculate_referral_bonus(self, user_id):
        """
        Calculates the referral bonus for a given user.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            float: The referral bonus amount.

        Raises:
            ValueError: If the user ID is not found in the system.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found in the system")

        user = self.users[user_id]
        if user.referred_by is None:
            return 0.0  # No referral bonus if the user was not referred by anyone

        referred_by_user = self.users.get(user.referred_by)
        if referred_by_user is None:
            return 0.0  # No referral bonus if the referrer is not found

        bonus = user.investment_amount * 0.10  # 10% of the referred user's investment
        return bonus

    def get_user_investment(self, user_id):
        """
        Gets the investment amount for a given user.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            float: The investment amount.

        Raises:
            ValueError: If the user ID is not found in the system.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found in the system")

        return self.users[user_id].investment_amount


def main():
    # Example usage:
    referral_system = ReferralBonusSystem()

    # Add users
    referral_system.add_user(1, 1000.0)  # User 1 invests $1000
    referral_system.add_user(2, 500.0, referred_by=1)  # User 2 invests $500, referred by User 1

    # Calculate referral bonus
    bonus = referral_system.calculate_referral_bonus(1)
    print(f"Referral bonus for User 1: ${bonus:.2f}")

    try:
        # Test error handling
        referral_system.add_user(3, -200.0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
