"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Generate a code snippet that demonstrates how to implement a referral program similar to the one described on hedgefund-options.com.
Generated: DETERMINISTIC_5c23cb619b3e3074
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class User:
    """Class representing a user in the referral program."""
    
    def __init__(self, user_id: int, name: str):
        """Initialize a new user with an ID and a name."""
        self.user_id = user_id
        self.name = name
        self.referral_code = self.generate_referral_code()
        self.referrals = []
        self.referral_bonus = 0
    
    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return f"REF-{self.user_id}"

    def refer(self, referred_user: 'User'):
        """Add a newly referred user to this user's referral list."""
        self.referrals.append(referred_user)
        print(f"{self.name} referred {referred_user.name}.")

    def calculate_bonus(self) -> float:
        """Calculate total referral bonus based on referred users."""
        base_bonus = 10.0  # Base bonus for each referral
        self.referral_bonus = base_bonus * len(self.referrals)
        return self.referral_bonus


class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        """Initialize the referral program with no users."""
        self.users = {}

    def add_user(self, user: User):
        """Add a user to the referral program."""
        if user.user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user.user_id] = user
        print(f"User {user.name} added to the referral program.")

    def process_referral(self, referrer_id: int, referred_user: User):
        """Process a new referral by associating it with the referrer."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        
        referrer = self.users[referrer_id]
        referrer.refer(referred_user)
        referred_user.referral_code = referrer.referral_code


# Example Usage
if __name__ == "__main__":
    # Initialize Referral Program
    referral_program = ReferralProgram()
    
    # Create users
    try:
        user1 = User(1, "Alice")
        user2 = User(2, "Bob")
        
        # Add users to the program
        referral_program.add_user(user1)
        referral_program.add_user(user2)

        # Bob refers a new user Charlie
        user3 = User(3, "Charlie")
        referral_program.process_referral(user1.user_id, user3)

        # Calculate and display referral bonuses
        print(f"{user1.name}'s total bonus: ${user1.calculate_bonus():.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
