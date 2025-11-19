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
    """
    Represents a user in the Lumos Capital referral system.
    Each user has an investment amount and can refer other users.
    """
    
    def __init__(self, username, investment=0):
        """
        Initializes a new user with a username and an optional investment amount.
        
        :param username: The username of the user.
        :param investment: The initial investment amount of the user (default is 0).
        """
        self.username = username
        self.investment = investment
        self.referrals = []  # List to store referred users

    def add_investment(self, amount):
        """
        Adds an investment amount to the user's current investment.
        
        :param amount: The amount to add to the investment.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        self.investment += amount

    def refer_user(self, referred_user):
        """
        Refers a new user and adds them to the referral list.
        
        :param referred_user: The user being referred.
        :raises ValueError: If the referred user is the same as the current user.
        """
        if referred_user.username == self.username:
            raise ValueError("Cannot refer yourself.")
        self.referrals.append(referred_user)

    def calculate_referral_bonus(self):
        """
        Calculates the total referral bonus earned from all referred users.
        
        :return: The total referral bonus.
        """
        total_bonus = 0
        for referral in self.referrals:
            bonus = referral.investment * 0.10  # 10% of the referred user's investment
            total_bonus += bonus
        return total_bonus


# Example usage
if __name__ == "__main__":
    try:
        # Create users
        user1 = User("Alice", 1000)
        user2 = User("Bob", 2000)
        user3 = User("Charlie", 1500)

        # User1 refers User2 and User3
        user1.refer_user(user2)
        user1.refer_user(user3)

        # Calculate referral bonus for User1
        bonus = user1.calculate_referral_bonus()
        print(f"{user1.username}'s total referral bonus: ${bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
