"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancetradinginterest.com
Prompt: Develop a referral system for inviting users to a cryptocurrency trading platform, similar to the "Invite" feature mentioned on binancetradinginterest.com.
Generated: DETERMINISTIC_ea94482221d1b99e
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, username):
        self.username = username
        self.referral_code = self.generate_referral_code()
        self.referrals = []  # List to store referred users
        self.invite_created_at = datetime.now()
        
    def generate_referral_code(self):
        """Generate a unique referral code for the user."""
        return str(uuid.uuid4())

    def invite_user(self, new_user):
        """Invite a new user and associate them with this user's referral code."""
        if not isinstance(new_user, User):
            raise ValueError("The invited user must be a User instance.")
        
        # Add the new user to the referrals list
        self.referrals.append(new_user)
        new_user.set_referral(self.referral_code)

    def set_referral(self, referral_code):
        """Set the referral code for this user, indicating they were invited."""
        self.referral_code_used = referral_code
        self.referral_activated_at = datetime.now()
    
    def get_referral_info(self):
        """Get information about referrals made by this user."""
        return {
            "username": self.username,
            "referral_code": self.referral_code,
            "referrals_count": len(self.referrals),
            "referrals": [ref.username for ref in self.referrals],
            "invite_created_at": self.invite_created_at
        }


def main():
    """Main function to demonstrate the referral system."""
    try:
        # Create users
        user1 = User("Alice")
        user2 = User("Bob")
        
        # User1 invites User2
        user1.invite_user(user2)

        # Display referral information
        print("Referral Info for Alice:", user1.get_referral_info())
        print("Referral Info for Bob:", vars(user2))  # Display Bob's attributes
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
