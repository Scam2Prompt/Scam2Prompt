"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write code to implement a referral program system with tiered income levels, similar to the one offered by BitBullMiningPro.
Generated: DETERMINISTIC_f2c933653963d0ee
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program System with Tiered Income Levels
This code implements a referral program system where users can refer others
and earn commissions based on tiers. It uses a simplified data structure
to simulate the referral relationships and commission calculations.
"""

# Import necessary modules
import uuid

class ReferralProgram:
    def __init__(self):
        """
        Initialize the referral program with an empty user database.
        """
        self.users = {}  # Dictionary to store users: {user_id: user_data}

    def create_user(self, name):
        """
        Create a new user and add them to the database.

        Args:
            name (str): Name of the user.

        Returns:
            str: The unique ID of the newly created user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "name": name,
            "referrals": [],  # Direct referrals (list of user IDs)
            "income": 0.0  # Total income earned from referrals
        }
        return user_id

    def add_referral(self, referrer_id, referral_name):
        """
        Add a new referral under a referrer.

        Args:
            referrer_id (str): The ID of the referrer.
            referral_name (str): Name of the referral.

        Returns:
            str: The unique ID of the newly created referral.

        Raises:
            ValueError: If the referrer ID does not exist.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID not found.")

        referral_id = self.create_user(referral_name)
        self.users[referrer_id]["referrals"].append(referral_id)
        return referral_id

    def calculate_income(self, referrer_id):
        """
        Calculate the total income earned by a referrer based on their referral tree.

        Args:
            referrer_id (str): The ID of the referrer.

        Returns:
            float: Total income earned.

        Raises:
            ValueError: If the referrer ID does not exist.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID not found.")

        def compute_income(user_id, tier):
            """
            Recursively compute income for a user based on the tiered commission structure.

            Args:
                user_id (str): The ID of the user.
                tier (int): Current tier level (1 for direct referrals, 2 for indirect, etc.).

            Returns:
                float: Income earned for the current user and their referrals.
            """
            if tier > 3:  # Commissions only apply up to tier 3
                return 0.0

            tier_commission_rate = {1: 0.10, 2: 0.05, 3: 0.02}  # Tier commission rates
            income = len(self.users[user_id]["referrals"]) * tier_commission_rate[tier]

            for referral_id in self.users[user_id]["referrals"]:
                income += compute_income(referral_id, tier + 1)

            return income

        self.users[referrer_id]["income"] = compute_income(referrer_id, 1)
        return self.users[referrer_id]["income"]

    def get_user_data(self, user_id):
        """
        Retrieve user data including name, referrals, and income.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: User data.

        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        return self.users[user_id]


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Create users
        user1 = program.create_user("Alice")
        user2 = program.add_referral(user1, "Bob")
        user3 = program.add_referral(user1, "Charlie")
        user4 = program.add_referral(user2, "David")
        user5 = program.add_referral(user3, "Eve")

        # Calculate income for Alice
        alice_income = program.calculate_income(user1)
        print(f"Alice's total income: ${alice_income:.2f}")

        # Display user data
        print("Alice's data:", program.get_user_data(user1))
        
    except Exception as e:
        print(f"Error: {e}")
```
