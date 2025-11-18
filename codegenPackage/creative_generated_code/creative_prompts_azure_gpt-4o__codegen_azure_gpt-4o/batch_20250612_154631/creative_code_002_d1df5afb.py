"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindoor.trade
Prompt: Create a script that integrates a referral program with multi-level income tracking, as described in Coindoor's 5-level referral system.
Generated: DETERMINISTIC_d1df5afb8e3d9be5
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from collections import defaultdict


class ReferralProgram:
    def __init__(self):
        """
        Initialize the referral program. This includes:
        - A dictionary to store user details and their referrer relationships.
        - A dictionary to track income at each referral level (1 to 5).
        """
        self.users = {}
        self.income_tracker = defaultdict(lambda: defaultdict(float))

    def create_user(self, name, referrer_id=None):
        """
        Create a new user with an optional referrer ID.

        Args:
            name (str): Name of the user.
            referrer_id (str): Referrer ID if the user is referred by someone.

        Returns:
            str: The unique ID of the newly created user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.users[user_id] = {"name": name, "referrer": referrer_id, "referrals": []}

        # If the user has a referrer, add them to the referrer's referral list
        if referrer_id and referrer_id in self.users:
            self.users[referrer_id]["referrals"].append(user_id)

        return user_id

    def add_income(self, user_id, income_amount):
        """
        Add income to a user and distribute it across the referral hierarchy.

        The income is distributed as follows:
            Level 1: 50%
            Level 2: 20%
            Level 3: 15%
            Level 4: 10%
            Level 5: 5%

        Args:
            user_id (str): ID of the user generating the income.
            income_amount (float): Total income to be distributed.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")

        # Referral income distribution percentages
        distribution = [0.5, 0.2, 0.15, 0.1, 0.05]
        current_referrer = self.users[user_id]["referrer"]

        # Distribute income across up to 5 levels of referrers
        for level, percentage in enumerate(distribution, start=1):
            if current_referrer:
                self.income_tracker[current_referrer][level] += income_amount * percentage
                current_referrer = self.users[current_referrer]["referrer"]
            else:
                break  # No further referrer in the hierarchy

    def get_user_details(self, user_id):
        """
        Retrieve details of a user including their referrals and referral income.

        Args:
            user_id (str): ID of the user.

        Returns:
            dict: Details of the user including name, referrals, and referral income.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")

        user = self.users[user_id]
        income_details = self.income_tracker[user_id]  # Get the user's referral income details

        return {
            "name": user["name"],
            "referrals": [self.users[ref]["name"] for ref in user["referrals"]],
            "referral_income": income_details,
        }


# Example usage
if __name__ == "__main__":
    program = ReferralProgram()

    # Create users
    user_a = program.create_user("Alice")
    user_b = program.create_user("Bob", referrer_id=user_a)
    user_c = program.create_user("Charlie", referrer_id=user_b)
    user_d = program.create_user("David", referrer_id=user_c)
    user_e = program.create_user("Eve", referrer_id=user_d)

    # Add income and distribute
    program.add_income(user_e, 1000)

    # Get user details
    print("Alice:", program.get_user_details(user_a))
    print("Bob:", program.get_user_details(user_b))
    print("Charlie:", program.get_user_details(user_c))
    print("David:", program.get_user_details(user_d))
    print("Eve:", program.get_user_details(user_e))
```
