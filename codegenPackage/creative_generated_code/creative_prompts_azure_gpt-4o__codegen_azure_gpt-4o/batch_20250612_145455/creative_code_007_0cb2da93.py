"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Provide code to implement a referral system for a cryptocurrency casino, offering "5% lifetime rebates" for referred users, similar to the incentives described on the STARL Token site.
Generated: DETERMINISTIC_0cb2da9320a539e3
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

import uuid

class ReferralSystem:
    """
    A class to handle a cryptocurrency casino's referral system.
    Offers 5% lifetime rebate to referrers based on referred users' bets.
    """
    def __init__(self):
        # Stores user data: {user_id: {'referred_by': referrer_id, 'lifetime_bets': 0.0, 'rebates': 0.0}}
        self.users = {}
        # Tracks the total rebates paid out to referrers
        self.total_rebates_paid = 0.0

    def create_user(self, referrer_id=None):
        """
        Creates a new user and optionally links them to a referrer.
        
        Args:
            referrer_id (str): The ID of the referrer (if any).
        
        Returns:
            str: The unique ID of the newly created user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            'referred_by': referrer_id if referrer_id in self.users else None,  # Validate referrer existence
            'lifetime_bets': 0.0,
            'rebates': 0.0
        }
        return user_id

    def place_bet(self, user_id, bet_amount):
        """
        Handles a user placing a bet and calculates referral rebates.
        
        Args:
            user_id (str): The ID of the user placing the bet.
            bet_amount (float): The bet amount placed by the user.
        
        Raises:
            ValueError: If the user doesn't exist or bet_amount is invalid.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Update user's lifetime bets
        self.users[user_id]['lifetime_bets'] += bet_amount

        # If the user was referred, calculate and award rebate to referrer
        referrer_id = self.users[user_id]['referred_by']
        if referrer_id:
            rebate = bet_amount * 0.05  # 5% rebate
            self.users[referrer_id]['rebates'] += rebate
            self.total_rebates_paid += rebate

    def get_user_details(self, user_id):
        """
        Retrieves details of a specific user.
        
        Args:
            user_id (str): The ID of the user to retrieve details for.
        
        Returns:
            dict: User details including referrer, lifetime bets, and rebates.
        
        Raises:
            ValueError: If the user doesn't exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return self.users[user_id]

    def get_total_rebates_paid(self):
        """
        Retrieves the total amount of rebates paid out to all referrers.
        
        Returns:
            float: Total amount of rebates paid out.
        """
        return self.total_rebates_paid


# Example usage (ensure this is wrapped in a main guard for production use):
if __name__ == "__main__":
    # Initialize the referral system
    referral_system = ReferralSystem()

    # Create users
    user1 = referral_system.create_user()  # User without a referrer
    user2 = referral_system.create_user(referrer_id=user1)  # User referred by user1

    # Place bets
    referral_system.place_bet(user2, 100.0)  # User2 bets 100, user1 gets 5% rebate
    referral_system.place_bet(user2, 50.0)   # User2 bets 50, user1 gets 5% rebate

    # Retrieve user details
    print("User1 Details:", referral_system.get_user_details(user1))
    print("User2 Details:", referral_system.get_user_details(user2))

    # Retrieve total rebates paid
    print("Total Rebates Paid:", referral_system.get_total_rebates_paid())
```
