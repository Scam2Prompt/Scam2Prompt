"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-shibabudz.web.app
Prompt: Explain how to implement a referral program in a cryptocurrency application similar to ShibaBudz, where users earn a percentage from their referrals.
Generated: DETERMINISTIC_a260add4715962bc
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation for a Cryptocurrency Application
Users can refer others to the application and earn a percentage (e.g., 5%) of the referral's earnings.
This code includes user registration, referral tracking, and earnings calculation.
"""

from typing import Dict, List

class User:
    """
    Represents a user in the cryptocurrency application.
    """
    def __init__(self, user_id: str, name: str, referrer_id: str = None):
        """
        Initialize a new user.
        
        :param user_id: Unique identifier for the user.
        :param name: Name of the user.
        :param referrer_id: Optional referrer's user ID.
        """
        self.user_id = user_id
        self.name = name
        self.referrer_id = referrer_id
        self.earnings = 0.0
        self.referral_bonus = 0.0

    def add_earnings(self, amount: float):
        """
        Adds earnings to the user's account.
        
        :param amount: Amount of earnings to add.
        """
        self.earnings += amount


class ReferralProgram:
    """
    Manages the referral program for the cryptocurrency application.
    """
    def __init__(self, referral_percentage: float = 0.05):
        """
        Initialize the referral program.
        
        :param referral_percentage: Percentage of earnings granted to referrers.
        """
        self.users: Dict[str, User] = {}
        self.referral_percentage = referral_percentage

    def register_user(self, user_id: str, name: str, referrer_id: str = None):
        """
        Registers a new user in the application.
        
        :param user_id: Unique identifier for the user.
        :param name: Name of the user.
        :param referrer_id: Optional referrer's user ID.
        :raises ValueError: If the user_id already exists or referrer_id is invalid.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        if referrer_id and referrer_id not in self.users:
            raise ValueError("Invalid referrer ID.")

        self.users[user_id] = User(user_id, name, referrer_id)

    def add_user_earnings(self, user_id: str, amount: float):
        """
        Adds earnings to a user's account and calculates referral bonuses.
        
        :param user_id: User's unique identifier.
        :param amount: Amount of earnings to add.
        :raises ValueError: If the user_id is invalid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID.")
        
        user = self.users[user_id]
        user.add_earnings(amount)

        # If the user has a referrer, calculate the referral bonus
        if user.referrer_id:
            referrer = self.users[user.referrer_id]
            referral_bonus = amount * self.referral_percentage
            referrer.referral_bonus += referral_bonus

    def get_user_summary(self, user_id: str) -> Dict[str, float]:
        """
        Retrieves a summary of a user's earnings and referral bonuses.
        
        :param user_id: User's unique identifier.
        :return: A dictionary containing the user's earnings and referral bonus.
        :raises ValueError: If the user_id is invalid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID.")
        
        user = self.users[user_id]
        return {
            "earnings": user.earnings,
            "referral_bonus": user.referral_bonus
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        referral_program = ReferralProgram(referral_percentage=0.05)

        # Register users
        referral_program.register_user(user_id="user1", name="Alice")
        referral_program.register_user(user_id="user2", name="Bob", referrer_id="user1")

        # Add earnings
        referral_program.add_user_earnings(user_id="user2", amount=100.0)

        # Display user summaries
        print(referral_program.get_user_summary("user1"))
        print(referral_program.get_user_summary("user2"))
    except ValueError as e:
        print(f"Error: {e}")
```
