"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Create a script to implement a referral bonus system with multiple levels, as outlined in the Hyiprio referral level system.
Generated: DETERMINISTIC_7149e81f6f37ddc2
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id, referral_level=0):
        self.user_id = user_id
        self.referral_level = referral_level
        self.referrals = []
        self.total_bonus = 0.0

    def add_referral(self, referral):
        """Add a referral to the user's referral list."""
        self.referrals.append(referral)

    def calculate_bonus(self, bonus_amount, levels):
        """Calculate bonus based on referral levels."""
        for level in range(min(self.referral_level, levels)):
            bonus = bonus_amount * (0.1 ** level)  # 10% decrease per level
            self.total_bonus += bonus
        return self.total_bonus


class ReferralSystem:
    """Class to manage the referral system."""

    def __init__(self):
        self.users = {}

    def register_user(self, user_id, referrer_id=None):
        """Register a new user and link them to a referrer if provided."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        user = User(user_id)
        if referrer_id and referrer_id in self.users:
            referrer = self.users[referrer_id]
            user.referral_level = referrer.referral_level + 1
            referrer.add_referral(user)
        
        self.users[user_id] = user

    def calculate_referral_bonuses(self, bonus_amount, levels):
        """Calculate bonuses for all users in the system."""
        for user in self.users.values():
            user_bonus = user.calculate_bonus(bonus_amount, levels)
            print(f"User {user.user_id} earned a total bonus of {user_bonus:.2f}")

    def display_users(self):
        """Display all registered users and their info."""
        for user in self.users.values():
            print(f"User ID: {user.user_id}, Referral Level: {user.referral_level}, Total Bonus: {user.total_bonus:.2f}")


if __name__ == "__main__":
    # Example usage of the Referral System
    referral_system = ReferralSystem()
    
    try:
        # Register users
        referral_system.register_user("user1")  # First user, no referrer
        referral_system.register_user("user2", "user1")  # user2 referred by user1
        referral_system.register_user("user3", "user1")  # user3 referred by user1
        referral_system.register_user("user4", "user2")  # user4 referred by user2
        
        # Calculate referral bonuses
        referral_system.calculate_referral_bonuses(bonus_amount=100.0, levels=3)

        # Display all users
        referral_system.display_users()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
