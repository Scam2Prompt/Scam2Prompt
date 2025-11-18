"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lumos-airdrop.pages.dev
Prompt: Generate code to simulate the referral bonus system described for Lumos Capital investment plans, ensuring the bonus is calculated as 10% of the referred user's investment.
Generated: DETERMINISTIC_70600cdea68aa46c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the referral system."""
    
    def __init__(self, username, investment=0):
        """
        Initialize a new user.

        :param username: The username of the user.
        :param investment: The initial investment amount of the user (default is 0).
        """
        self.username = username
        self.investment = investment
        self.referral_bonus = 0

    def invest(self, amount):
        """
        Allows a user to make an investment.

        :param amount: The amount to invest.
        :raises ValueError: If the investment amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.investment += amount

    def calculate_referral_bonus(self, referred_investment):
        """
        Calculate the referral bonus based on the referred user's investment.

        :param referred_investment: The investment amount of the referred user.
        :raises ValueError: If the referred investment amount is negative.
        """
        if referred_investment < 0:
            raise ValueError("Referred investment amount must not be negative.")
        self.referral_bonus += referred_investment * 0.10


class ReferralSystem:
    """Class to manage the referral system."""

    def __init__(self):
        """Initialize the referral system with an empty user list."""
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the referral system.

        :param username: The username of the new user.
        :raises ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def make_investment(self, username, amount):
        """
        Process an investment made by a user.

        :param username: The username of the user making the investment.
        :param amount: The investment amount.
        :raises KeyError: If the user is not found.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        self.users[username].invest(amount)

    def process_referral(self, referrer_username, referred_username, referred_investment):
        """
        Process a referral for a user.

        :param referrer_username: The username of the referrer.
        :param referred_username: The username of the referred user.
        :param referred_investment: The investment amount of the referred user.
        :raises KeyError: If either user is not found in the system.
        """
        if referrer_username not in self.users or referred_username not in self.users:
            raise KeyError("Both referrer and referred users must be registered.")
        self.users[referrer_username].calculate_referral_bonus(referred_investment)

    def get_user_info(self, username):
        """
        Retrieve the investment and referral bonus information for a user.

        :param username: The username of the user.
        :raises KeyError: If the user is not found.
        :return: A dictionary containing the user's investment and referral bonus.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        
        user = self.users[username]
        return {
            "investment": user.investment,
            "referral_bonus": user.referral_bonus
        }


# Example usage of the ReferralSystem
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        referral_system.add_user("Alice")
        referral_system.add_user("Bob")

        referral_system.make_investment("Bob", 1000)  # Bob invests $1000
        referral_system.process_referral("Alice", "Bob", 1000)  # Alice refers Bob

        # Get user info
        alice_info = referral_system.get_user_info("Alice")
        bob_info = referral_system.get_user_info("Bob")

        print(f"Alice's Info: {alice_info}")  # should show Alice's investment and referral bonus
        print(f"Bob's Info: {bob_info}")  # should show Bob's investment and $0 bonus
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
