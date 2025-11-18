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
import uuid


class ReferralProgram:
    """
    A class that manages a referral program, allowing users to refer others and calculate referral income.
    """

    def __init__(self):
        """
        Initialize the referral program with empty user and referral data structures.
        """
        self.users = {}  # Dictionary to store user information
        self.referrals = {}  # Dictionary to store referral relationships

    def create_user(self, username):
        """
        Create a new user in the referral program.
        :param username: Name of the user
        :return: User ID of the created user
        """
        if username in [user['username'] for user in self.users.values()]:
            raise ValueError("Username already exists. Please choose a different username.")
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {"username": username, "referral_income": 0}
        return user_id

    def add_referral(self, referrer_id, referee_username):
        """
        Add a referral relationship between an existing user (referrer) and a new user (referee).
        :param referrer_id: User ID of the referrer (existing user)
        :param referee_username: Name of the referee (new user)
        :return: User ID of the referee
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID is invalid. User does not exist.")
        referee_id = self.create_user(referee_username)
        self.referrals[referee_id] = referrer_id
        self.update_referral_income(referrer_id)  # Update the referral income for the referrer
        return referee_id

    def update_referral_income(self, user_id, income_per_referral=10):
        """
        Update the referral income for a given user.
        :param user_id: ID of the user whose referral income will be updated
        :param income_per_referral: Income amount credited for a single referral (default: $10)
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID for updating referral income.")
        self.users[user_id]["referral_income"] += income_per_referral

    def get_user_info(self, user_id):
        """
        Retrieve information about a user.
        :param user_id: ID of the user
        :return: User information dictionary
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        return self.users[user_id]

    def get_referral_tree(self):
        """
        Retrieve the entire referral tree showing relationships between users.
        :return: Dictionary of referral relationships
        """
        return self.referrals


# Example Usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Create initial users
        user1_id = program.create_user("Alice")
        user2_id = program.create_user("Bob")

        # Alice refers Charlie
        charlie_id = program.add_referral(user1_id, "Charlie")

        # Bob refers Dave
        dave_id = program.add_referral(user2_id, "Dave")

        # Retrieve user info
        print("User Info:", program.get_user_info(user1_id))
        print("Referral Tree:", program.get_referral_tree())

    except Exception as e:
        print(f"Error: {e}")
```
