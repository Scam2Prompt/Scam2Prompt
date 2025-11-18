"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Generate code to create a referral program system that tracks user referrals and calculates referral income, as described in the Wintron referral program.
Generated: DETERMINISTIC_0635cd8af0d24d7a
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the referral program.

    Attributes:
        user_id (int): Unique identifier for the user.
        referrals (list): List of user_ids referring to this user.
        referral_income (float): Total income earned from referrals.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []
        self.referral_income = 0.0

    def add_referral(self, referral_user_id):
        """Adds a new referral to the user's list of referrals."""
        if referral_user_id not in self.referrals:
            self.referrals.append(referral_user_id)

    def update_income(self, amount):
        """Updates the referral income for the user."""
        if amount < 0:
            raise ValueError("Income amount must be non-negative.")
        self.referral_income += amount


class ReferralProgram:
    """
    Manages the referral program, tracking users and their referrals.

    Attributes:
        users (dict): Dictionary to hold User objects indexed by user_id.
        referral_rate (float): The rate at which referral income is calculated.
    """

    def __init__(self, referral_rate=0.1):
        self.users = {}
        self.referral_rate = referral_rate

    def add_user(self, user_id):
        """Adds a new user to the referral program."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def add_referral(self, user_id, referral_user_id):
        """Records a referral made by a user."""
        if user_id not in self.users or referral_user_id not in self.users:
            raise ValueError("Both users must be registered in the program.")
        
        self.users[user_id].add_referral(referral_user_id)
        self.calculate_referral_income(user_id)

    def calculate_referral_income(self, user_id):
        """Calculates and updates referral income for a user."""
        # Example scenario: Each referral earns the user $10
        referral_value = 10
        num_referrals = len(self.users[user_id].referrals)
        income = num_referrals * self.referral_rate * referral_value
        self.users[user_id].update_income(income)

    def get_user_info(self, user_id):
        """Returns the user information including referrals and income."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "referrals": user.referrals,
            "referral_income": user.referral_income,
        }


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram(referral_rate=0.1)
        
        # Adding users to the program
        referral_program.add_user(1)
        referral_program.add_user(2)
        referral_program.add_user(3)

        # User 1 refers User 2 and User 3
        referral_program.add_referral(1, 2)
        referral_program.add_referral(1, 3)

        # Fetch and print user info
        user_info = referral_program.get_user_info(1)
        print(f"User ID: {user_info['user_id']}, Referrals: {user_info['referrals']}, Income: ${user_info['referral_income']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
