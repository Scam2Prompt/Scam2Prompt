"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Provide code to implement a three-level referral system with earnings tracking, similar to the one described on the AUTOBUX platform.
Generated: DETERMINISTIC_354c8ddd7d63a0e9
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
    """
    Class to represent a user in the referral system.
    
    Attributes:
        user_id (int): Unique identifier for the user.
        referrals (list): List of User objects representing referrals.
        earnings (float): Total earnings from referrals.
        level (int): Current referral level.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []  # List to hold user referrals
        self.earnings = 0.0  # Earnings from referrals
        self.level = 0  # Level in the referral system

    def add_referral(self, referral_user):
        """
        Adds a referral to the user's list of referrals.
        
        Args:
            referral_user (User): The user being referred.
        """
        self.referrals.append(referral_user)

    def calculate_earnings(self):
        """
        Calculates the user's earnings based on their referrals.
        
        Earnings are calculated based on the levels of referrals:
        - Level 1: 10% of referral's earnings
        - Level 2: 5% of level 1 referrals' earnings
        - Level 3: 2% of level 2 referrals' earnings
        """
        level_1_earnings = sum(referral.earnings * 0.10 for referral in self.referrals)
        level_2_earnings = sum(
            referral.calculate_earnings() * 0.05 for referral in self.referrals
        )
        level_3_earnings = sum(
            sum(referral.calculate_earnings() * 0.02 for referral in referral.referrals)
            for referral in self.referrals
        )
        self.earnings = level_1_earnings + level_2_earnings + level_3_earnings

    def __str__(self):
        """
        String representation of the user for easy debugging.
        
        Returns:
            str: Information about the user including their earnings and referrals.
        """
        return f"User ID: {self.user_id}, Earnings: {self.earnings}, Referrals: {len(self.referrals)}"


def main():
    """
    Main function to test the referral system.
    
    Creates users and simulates referrals while tracking earnings.
    """
    try:
        # Create users
        user1 = User(user_id=1)
        user2 = User(user_id=2)
        user3 = User(user_id=3)
        user4 = User(user_id=4)

        # Simulate referrals
        user1.add_referral(user2)  # User 1 refers User 2
        user2.add_referral(user3)  # User 2 refers User 3
        user3.add_referral(user4)  # User 3 refers User 4

        # Set earnings for users
        user2.earnings = 100.0  # User 2 earns $100
        user3.earnings = 50.0   # User 3 earns $50
        user4.earnings = 20.0    # User 4 earns $20

        # Calculate earnings for User 1
        user1.calculate_earnings()

        # Print the results
        print(user1)
        print(user2)
        print(user3)
        print(user4)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
