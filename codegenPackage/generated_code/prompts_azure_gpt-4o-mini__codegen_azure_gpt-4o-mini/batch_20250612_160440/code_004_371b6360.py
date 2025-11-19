"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: Illustrate how to implement a referral program in a trading application, inspired by Coindoor's five-level referral income structure.
Generated: DETERMINISTIC_371b63606d7b6b28
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the trading application."""
    
    def __init__(self, user_id, name, referral_code=None):
        """
        Initialize a new user.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param referral_code: Code of the user who referred this user
        """
        self.user_id = user_id
        self.name = name
        self.referral_code = referral_code
        self.referrals = []  # List to store referred users
        self.level_income = [0] * 5  # Income from each referral level

    def add_referral(self, referral_user):
        """Add a referred user to the user's referral list."""
        self.referrals.append(referral_user)

    def calculate_income(self):
        """Calculate total income from referrals based on levels."""
        for level in range(5):
            self.level_income[level] = len(self.referrals) * (level + 1) * 10  # Example income calculation
        return self.level_income


class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        """Initialize the referral program with an empty user list."""
        self.users = {}

    def register_user(self, user_id, name, referral_code=None):
        """
        Register a new user in the referral program.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param referral_code: Code of the user who referred this user
        :raises ValueError: If the user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        new_user = User(user_id, name, referral_code)
        self.users[user_id] = new_user
        
        # If there's a referral code, add this user to the referrer's list
        if referral_code and referral_code in self.users:
            referrer = self.users[referral_code]
            referrer.add_referral(new_user)

    def calculate_all_incomes(self):
        """Calculate and return the income for all users in the program."""
        incomes = {}
        for user_id, user in self.users.items():
            incomes[user_id] = user.calculate_income()
        return incomes


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Register users
    try:
        referral_program.register_user("user1", "Alice")
        referral_program.register_user("user2", "Bob", "user1")
        referral_program.register_user("user3", "Charlie", "user1")
        referral_program.register_user("user4", "David", "user2")
        referral_program.register_user("user5", "Eve", "user3")
    except ValueError as e:
        print(f"Error: {e}")

    # Calculate and print incomes
    incomes = referral_program.calculate_all_incomes()
    for user_id, income in incomes.items():
        print(f"User ID: {user_id}, Income Levels: {income}")
```
