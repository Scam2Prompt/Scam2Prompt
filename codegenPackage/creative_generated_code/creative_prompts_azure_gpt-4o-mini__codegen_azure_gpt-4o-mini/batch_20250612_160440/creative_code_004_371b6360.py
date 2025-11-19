"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindoor.trade
Prompt: Illustrate how to implement a referral program in a trading application, inspired by Coindoor's five-level referral income structure.
Generated: DETERMINISTIC_371b63606d7b6b28
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the trading application."""
    
    def __init__(self, user_id, referral_code=None):
        self.user_id = user_id
        self.referral_code = referral_code
        self.referrals = []
        self.referral_income = 0.0

    def add_referral(self, referral_user):
        """Add a referral to the user's list of referrals."""
        self.referrals.append(referral_user)

    def calculate_income(self):
        """Calculate total referral income based on the hierarchy."""
        income_levels = [0.10, 0.05, 0.03, 0.02, 0.01]  # Income percentages for each referral level
        total_income = 0.0
        
        # Process referrals by levels
        for level in range(len(income_levels)):
            for referral in self.get_referrals_at_level(level):
                total_income += referral.last_trade_amount * income_levels[level]
        
        self.referral_income = total_income
        return total_income

    def get_referrals_at_level(self, level):
        """Get referrals at a specific level."""
        if level == 0:
            return self.referrals
        else:
            referrals_at_level = []
            for referral in self.referrals:
                referrals_at_level.extend(referral.get_referrals_at_level(level - 1))
            return referrals_at_level


class Trade:
    """Class representing a trade conducted by a user."""
    
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount
        user.last_trade_amount = amount  # Store the last trade amount for income calculations


class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, referral_code=None):
        """Register a new user and set up referral tracking."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        new_user = User(user_id, referral_code)
        
        if referral_code and referral_code in self.users:
            referrer = self.users[referral_code]
            referrer.add_referral(new_user)  # Add this user to the referrer's referral list
        
        self.users[user_id] = new_user

    def record_trade(self, user_id, amount):
        """Record a trade for a user and update their referral income."""
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        
        user = self.users[user_id]
        trade = Trade(user, amount)
        user.calculate_income()  # Update the referral income after the trade


# Example usage of the referral program
if __name__ == "__main__":
    # Create a referral program instance
    referral_program = ReferralProgram()
    
    # Register users
    referral_program.register_user("user1")  # No referrer
    referral_program.register_user("user2", "user1")  # user1 refers user2
    referral_program.register_user("user3", "user1")  # user1 refers user3
    referral_program.register_user("user4", "user2")  # user2 refers user4

    # Record trades for users
    referral_program.record_trade("user1", 1000)
    referral_program.record_trade("user2", 800)
    referral_program.record_trade("user3", 500)
    referral_program.record_trade("user4", 300)

    # Display referral income for user1
    user1 = referral_program.users["user1"]
    print(f"Referral Income for {user1.user_id}: {user1.calculate_income()}")

    # Handle potential errors in a production setting
    try:
        referral_program.register_user("user1")  # Attempt to re-register existing user
    except ValueError as e:
        print(f"Error: {e}")
```
