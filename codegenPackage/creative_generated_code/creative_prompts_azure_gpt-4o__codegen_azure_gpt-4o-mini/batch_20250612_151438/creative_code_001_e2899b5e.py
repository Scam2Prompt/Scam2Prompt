"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-crypto.online
Prompt: Generate a script that simulates the referral bonus system for OctaFx VIP plans, ensuring it adheres to the zero-level referral bonus structure mentioned on the webpage.
Generated: DETERMINISTIC_e2899b5ef169c58b
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    def __init__(self):
        """Initialize the referral system with an empty list of users."""
        self.users = {}
        self.referral_bonuses = {}

    def add_user(self, user_id, referred_by=None):
        """
        Add a user to the referral system.
        
        :param user_id: Unique identifier for the user.
        :param referred_by: User ID of the referring user (if any).
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        self.users[user_id] = {
            'referred_by': referred_by,
            'bonus': 0
        }
        
        if referred_by:
            self._update_referral_bonus(referred_by)

    def _update_referral_bonus(self, user_id):
        """
        Update the referral bonus for the referring user.
        
        :param user_id: User ID of the referring user.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        # Ensure the bonus structure is followed (zero-level bonus)
        self.referral_bonuses.setdefault(user_id, 0)
        self.referral_bonuses[user_id] += 0  # Assuming zero-level means no bonus is given

    def get_user_bonus(self, user_id):
        """
        Get the current bonus for a specific user.
        
        :param user_id: Unique identifier for the user.
        :return: The bonus amount for the user.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.referral_bonuses.get(user_id, 0)

    def display_users(self):
        """Display all users and their referral information."""
        for user_id, info in self.users.items():
            bonus = self.get_user_bonus(user_id)
            print(f"User ID: {user_id}, Referred By: {info['referred_by']}, Bonus: {bonus}")


# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        referral_system.add_user("user1")
        referral_system.add_user("user2", referred_by="user1")
        referral_system.add_user("user3", referred_by="user1")
        
        # Attempting to add an existing user to see error handling
        # referral_system.add_user("user1")  # Uncomment to test error handling
        
        referral_system.display_users()
        
    except ValueError as e:
        print(f"Error: {e}")
```
