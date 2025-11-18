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

class User:
    """
    A class to represent a user in the cryptocurrency casino.
    
    Attributes:
        user_id (str): Unique identifier for the user.
        referrals (list): List of users referred by this user.
        total_bets (float): Total amount bet by this user.
        lifetime_rebate (float): Total lifetime rebate accrued by this user.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []
        self.total_bets = 0.0
        self.lifetime_rebate = 0.0

    def refer_user(self, referred_user):
        """
        Refer a new user and add them to the referrals list.
        
        Parameters:
            referred_user (User): The user being referred.
        """
        self.referrals.append(referred_user)

    def place_bet(self, amount):
        """
        Place a bet and update total bets and lifetime rebate.
        
        Parameters:
            amount (float): The amount of the bet placed.
        
        Raises:
            ValueError: If the bet amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        self.total_bets += amount
        self.lifetime_rebate += amount * 0.05  # 5% rebate on the bet amount


class ReferralSystem:
    """
    A class to manage the referral system within the cryptocurrency casino.
    
    Attributes:
        users (dict): Dictionary mapping user_ids to User objects.
    """

    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        """
        Add a new user to the referral system.
        
        Parameters:
            user_id (str): Unique identifier for the new user.
        
        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        self.users[user_id] = User(user_id)

    def refer(self, referrer_id, referred_id):
        """
        Link a referrer with a referred user.
        
        Parameters:
            referrer_id (str): User ID of the referrer.
            referred_id (str): User ID of the referred user.
        
        Raises:
            KeyError: If either user ID does not exist.
        """
        if referrer_id not in self.users or referred_id not in self.users:
            raise KeyError("Both referrer and referred user must exist.")
        
        self.users[referrer_id].refer_user(self.users[referred_id])

    def place_bet(self, user_id, amount):
        """
        Place a bet for a user and update their total bets and rebates.
        
        Parameters:
            user_id (str): User ID of the user placing the bet.
            amount (float): The amount of the bet placed.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID {user_id} does not exist.")
        
        self.users[user_id].place_bet(amount)

    def get_user_rebate(self, user_id):
        """
        Retrieve the lifetime rebate of a user.
        
        Parameters:
            user_id (str): User ID to retrieve the rebate for.
        
        Returns:
            float: The lifetime rebate accrued by the user.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id].lifetime_rebate


# Example usage of the ReferralSystem
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Add users
    referral_system.add_user("user1")
    referral_system.add_user("user2")
    referral_system.add_user("user3")

    # User1 refers User2
    referral_system.refer("user1", "user2")

    # User2 places a bet
    referral_system.place_bet("user2", 100)

    # Check User1's lifetime rebate from User2's bet
    rebate = referral_system.get_user_rebate("user1")
    print(f"User1's lifetime rebate: {rebate:.2f}")  # Output: User1's lifetime rebate: 5.00
```
