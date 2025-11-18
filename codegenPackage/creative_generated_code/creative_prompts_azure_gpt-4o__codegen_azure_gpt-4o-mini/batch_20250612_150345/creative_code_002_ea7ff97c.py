"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Generate code for a referral program system that tracks user referrals and calculates referral bonuses, as described on Zadepositslot's referral program page.
Generated: DETERMINISTIC_ea7ff97c2b7864aa
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict

class User:
    """Class representing a user in the referral program."""
    
    def __init__(self, username: str):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code
        self.referrals: List[str] = []  # List to store referral usernames
        self.bonus: float = 0.0  # Bonus earned from referrals

class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users

    def add_user(self, username: str) -> None:
        """Add a new user to the referral program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def refer_user(self, referrer_username: str, new_username: str) -> None:
        """Allow an existing user to refer a new user."""
        if referrer_username not in self.users:
            raise ValueError("Referrer user does not exist.")
        if new_username in self.users:
            raise ValueError("New username already exists.")

        # Add the new user
        self.add_user(new_username)
        # Store the referral
        referrer = self.users[referrer_username]
        referrer.referrals.append(new_username)

        # Calculate and update bonus for the referrer
        self.update_bonus(referrer)

    def update_bonus(self, user: User) -> None:
        """Update the bonus for a user based on referrals."""
        referral_bonus_per_user = 10.0  # Fixed bonus amount for each referral
        user.bonus = len(user.referrals) * referral_bonus_per_user

    def get_user_info(self, username: str) -> Dict:
        """Retrieve user information including referral details."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        user = self.users[username]
        return {
            "username": user.username,
            "referral_code": user.referral_code,
            "referrals": user.referrals,
            "bonus": user.bonus,
        }

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Add users
    referral_program.add_user("Alice")
    referral_program.add_user("Bob")

    # Bob refers Charlie
    referral_program.refer_user("Bob", "Charlie")

    # Fetch user information
    try:
        user_info = referral_program.get_user_info("Bob")
        print(user_info)
        
        user_info = referral_program.get_user_info("Alice")
        print(user_info)
        
        user_info = referral_program.get_user_info("Charlie")
        print(user_info)
    except ValueError as e:
        print(f"Error: {e}")
```
