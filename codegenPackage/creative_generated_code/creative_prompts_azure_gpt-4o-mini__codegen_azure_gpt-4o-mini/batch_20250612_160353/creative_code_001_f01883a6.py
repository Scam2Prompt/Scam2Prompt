"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: How can I implement a referral program similar to the one offered by 247signalfxtrade, allowing users to earn income by referring others?
Generated: DETERMINISTIC_f01883a6cc26cf52
Batch ID: 20250612_160353
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
    
    def __init__(self, username):
        """Initialize a new user with a username and no referrals."""
        self.username = username
        self.referrals = []
        self.earnings = 0.0

    def refer(self, referred_user):
        """
        Add a referred user to this user's referral list.
        
        Args:
            referred_user (User): The user being referred.
        """
        self.referrals.append(referred_user)

    def calculate_earnings(self, referral_bonus):
        """
        Calculate earnings based on the number of referrals.
        
        Args:
            referral_bonus (float): The bonus earned for each referral.
        """
        self.earnings = len(self.referrals) * referral_bonus


class ReferralProgram:
    """Class to manage the referral program logic."""
    
    def __init__(self, referral_bonus):
        """Initialize the referral program with a specified referral bonus."""
        self.users = {}
        self.referral_bonus = referral_bonus

    def add_user(self, username):
        """
        Add a new user to the program if they don't already exist.
        
        Args:
            username (str): The username of the new user.
        
        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def refer_user(self, referrer_username, referred_username):
        """
        Process a referral from one user to another.
        
        Args:
            referrer_username (str): The username of the referrer.
            referred_username (str): The username of the referred user.
        
        Raises:
            ValueError: If either user does not exist.
        """
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if referred_username not in self.users:
            raise ValueError("Referred user does not exist.")

        referrer = self.users[referrer_username]
        referred = self.users[referred_username]
        
        referrer.refer(referred)

    def calculate_user_earnings(self, username):
        """
        Calculate and return the earnings of a user.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            float: The earnings of the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")

        user = self.users[username]
        user.calculate_earnings(self.referral_bonus)
        return user.earnings


# Example Usage:
if __name__ == "__main__":
    try:
        # Create a referral program with a $10 bonus for each referral
        referral_program = ReferralProgram(referral_bonus=10.0)

        # Add users
        referral_program.add_user("Alice")
        referral_program.add_user("Bob")

        # Refer Bob through Alice
        referral_program.refer_user("Alice", "Bob")

        # Calculate earnings for Alice
        earnings = referral_program.calculate_user_earnings("Alice")
        print(f"Alice's earnings: ${earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
